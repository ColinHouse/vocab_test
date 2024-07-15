from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QHeaderView, QScrollArea, QHBoxLayout, QPushButton, \
    QMessageBox, QCheckBox, QTableWidgetItem


class StatsUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.stats_layout = QVBoxLayout()

        self.stats_table = QTableWidget()
        self.stats_table.setColumnCount(5)
        self.stats_table.setHorizontalHeaderLabels(["", "中文词组", "尝试次数", "错误次数", "错误率"])
        self.stats_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.stats_layout.addWidget(self.stats_table)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area_content = QWidget()
        scroll_area_content.setLayout(self.stats_layout)
        scroll_area.setWidget(scroll_area_content)

        button_layout = QHBoxLayout()

        back_button = QPushButton("返回")
        back_button.clicked.connect(self.parent.back_to_main_ui)
        button_layout.addWidget(back_button)

        delete_button = QPushButton("删除")
        delete_button.clicked.connect(self.delete_selected_words)
        button_layout.addWidget(delete_button)

        self.stats_layout.addLayout(button_layout)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(scroll_area)
        self.setLayout(self.layout)

    def update_stats_table(self):
        self.stats_table.setRowCount(0)  # 清空现有表格内容

        for row, (word, data) in enumerate(self.parent.stats.items()):
            attempts = data['attempts']
            errors = data['errors']
            error_rate = (errors / attempts * 100) if attempts > 0 else 0
            self.stats_table.insertRow(row)
            checkbox = QCheckBox()
            checkbox.setStyleSheet("margin-left:50%; margin-right:50%;")
            self.stats_table.setCellWidget(row, 0, checkbox)
            self.stats_table.setItem(row, 1, QTableWidgetItem(word))
            self.stats_table.setItem(row, 2, QTableWidgetItem(str(attempts)))
            self.stats_table.setItem(row, 3, QTableWidgetItem(str(errors)))
            error_rate_item = QTableWidgetItem(f"{error_rate:.2f}%")
            error_rate_item.setData(Qt.EditRole, error_rate)  # 设置数据为错误率的数值形式
            self.stats_table.setItem(row, 4, error_rate_item)

        self.stats_table.sortItems(4, Qt.DescendingOrder)  # 按照错误率降序排序

    def delete_selected_words(self):
        """Mark selected words for deletion."""
        self.words_to_delete = []
        for row in range(self.stats_table.rowCount()):
            if self.stats_table.cellWidget(row, 0).isChecked():
                word_item = self.stats_table.item(row, 1)
                if word_item:
                    self.words_to_delete.append(word_item.text())

        if not self.words_to_delete:
            QMessageBox.information(self, "提示", "请选择要删除的词汇。")
            return  # No words selected

        # Confirm deletion
        reply = QMessageBox.question(
            self, '确认删除', "确定删除选中的词汇？",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.confirm_delete()

    def confirm_delete(self):
        """Delete the marked words from the vocabulary and stats."""
        if hasattr(self, 'words_to_delete'):
            for word in self.words_to_delete:
                if word in self.parent.vocab:
                    del self.parent.vocab[word]
                if word in self.parent.stats:
                    del self.parent.stats[word]
            self.words_to_delete = []
            self.parent.write_vocab(self.parent.vocab)
            self.parent.write_stats(self.parent.stats)
            self.update_stats_table()
