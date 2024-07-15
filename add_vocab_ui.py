from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class AddVocabUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        chinese_layout = QHBoxLayout()
        chinese_label = QLabel("输入中文词组:")
        self.chinese_entry = QLineEdit()
        chinese_layout.addWidget(chinese_label)
        chinese_layout.addWidget(self.chinese_entry)

        english_layout = QHBoxLayout()
        english_label = QLabel("输入对应的英文词组:")
        self.english_entry = QLineEdit()
        english_layout.addWidget(english_label)
        english_layout.addWidget(self.english_entry)

        add_button = QPushButton("添加词汇")
        add_button.clicked.connect(self.add_vocab)

        back_button = QPushButton("返回")
        back_button.clicked.connect(self.parent.back_to_main_ui)

        layout.addLayout(chinese_layout)
        layout.addLayout(english_layout)
        layout.addWidget(add_button)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def add_vocab(self):
        chinese = self.chinese_entry.text()
        english = self.english_entry.text()
        if chinese and english:
            self.parent.add_vocab(chinese, english)
            QMessageBox.information(self, "提示", "词汇已添加！")
            self.chinese_entry.clear()
            self.english_entry.clear()
        else:
            QMessageBox.warning(self, "警告", "请输入完整的词组。")
