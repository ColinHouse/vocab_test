from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QScrollArea


class StatsUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.stats_layout = QVBoxLayout()

        self.stats_table = QTableWidget()
        self.stats_table.setColumnCount(4)
        self.stats_table.setHorizontalHeaderLabels(["中文词组", "尝试次数", "错误次数", "错误率"])

        self.stats_layout.addWidget(self.stats_table)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area_content = QWidget()
        scroll_area_content.setLayout(self.stats_layout)
        scroll_area.setWidget(scroll_area_content)

        back_button = QPushButton("返回")
        back_button.clicked.connect(self.parent.back_to_main_ui)
        self.stats_layout.addWidget(back_button)

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
            self.stats_table.setItem(row, 0, QTableWidgetItem(word))
            self.stats_table.setItem(row, 1, QTableWidgetItem(str(attempts)))
            self.stats_table.setItem(row, 2, QTableWidgetItem(str(errors)))
            self.stats_table.setItem(row, 3, QTableWidgetItem(f"{error_rate:.2f}%"))
