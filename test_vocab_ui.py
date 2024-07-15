# test_vocab_ui.py
import time

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout

import utils


class TestVocabUI(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.test_label = QLabel("请翻译这个中文词组:")
        layout.addWidget(self.test_label)

        self.test_entry = QLineEdit()
        layout.addWidget(self.test_entry)

        self.check_button = QPushButton("提交答案")
        self.check_button.clicked.connect(self.check_answer)
        layout.addWidget(self.check_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        button_layout = QHBoxLayout()
        self.random_test_button = QPushButton("开始随机测试")
        self.random_test_button.clicked.connect(self.random_test)
        button_layout.addWidget(self.random_test_button)

        self.back_button = QPushButton("返回")
        self.back_button.clicked.connect(self.parent.back_to_main_ui)
        button_layout.addWidget(self.back_button)

        layout.addLayout(button_layout)

    def random_test(self):
        if not self.parent.vocab:
            self.result_label.setText("词汇表为空，请先添加词汇。")
            return
        chinese = self.parent.choose_weighted_random_word()
        self.test_label.setText(f"请翻译这个中文词组: {chinese}")
        self.test_entry.clear()
        self.test_entry.setFocus()
        self.current_chinese = chinese

    def check_answer(self):
        chinese = self.current_chinese
        user_answer = self.test_entry.text()
        correct_answer = self.parent.vocab[chinese]

        if user_answer == correct_answer:
            self.result_label.setText("正确！")
            self.result_label.setStyleSheet("color: green;")
        else:
            utils.highlight_differences(self, user_answer, correct_answer)

        self.parent.stats[chinese]['attempts'] += 1
        if user_answer != correct_answer:
            self.parent.stats[chinese]['errors'] += 1

        self.parent.update_stats()

        self.disable_check_button()

    def disable_check_button(self):
        self.check_button.setDisabled(True)
        for i in range(3, 0, -1):
            self.check_button.setText(f"提交答案 ({i}s)")
            QCoreApplication.processEvents()
            time.sleep(1)
        self.check_button.setDisabled(False)
        self.check_button.setText("提交答案")
