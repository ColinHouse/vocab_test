from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QPushButton, QHBoxLayout, QLabel, QComboBox, \
    QInputDialog, QMessageBox
from vocab import read_vocab, write_vocab, get_vocab_list, create_new_vocab
from stats import read_stats, write_stats
from add_vocab_ui import AddVocabUI
from test_vocab_ui import TestVocabUI
from stats_ui import StatsUI
from utils import choose_weighted_random_word  # 导入函数


class VocabApp(QWidget):
    def __init__(self):
        super().__init__()
        self.vocab_list = get_vocab_list()
        self.current_vocab = None
        self.vocab = {}
        self.stats = {}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("词汇测试")
        self.resize(700, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-family: Arial, sans-serif;
            }
            QLineEdit, QPushButton, QComboBox {
                font-size: 20px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton[disabled] {
                background-color: #7f8c8d;
            }
            QLabel {
                font-size: 22px;
                padding: 5px;
            }
            QVBoxLayout, QHBoxLayout {
                margin: 20px;
            }
        """)

        self.stack = QStackedWidget()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.stack)

        self.init_main_ui()

    def init_main_ui(self):
        self.main_ui = QWidget()
        layout = QVBoxLayout(self.main_ui)

        vocab_select_layout = QHBoxLayout()
        self.vocab_combo = QComboBox()
        self.vocab_combo.addItems(self.vocab_list)
        self.vocab_combo.currentIndexChanged.connect(self.change_vocab)
        vocab_select_layout.addWidget(QLabel("选择词库:"))
        vocab_select_layout.addWidget(self.vocab_combo)

        new_vocab_button = QPushButton("新建词库")
        new_vocab_button.clicked.connect(self.create_new_vocab)
        vocab_select_layout.addWidget(new_vocab_button)
        layout.addLayout(vocab_select_layout)

        button_layout = QHBoxLayout()
        add_vocab_button = QPushButton("添加词汇")
        add_vocab_button.clicked.connect(self.show_add_vocab_ui)
        test_vocab_button = QPushButton("开始测试")
        test_vocab_button.clicked.connect(self.show_test_vocab_ui)
        stats_button = QPushButton("查看统计信息")
        stats_button.clicked.connect(self.show_stats_ui)

        button_layout.addWidget(add_vocab_button)
        button_layout.addWidget(test_vocab_button)
        button_layout.addWidget(stats_button)

        layout.addLayout(button_layout)
        self.stack.addWidget(self.main_ui)

        self.add_vocab_ui = AddVocabUI(self)
        self.stack.addWidget(self.add_vocab_ui)

        self.test_vocab_ui = TestVocabUI(self)
        self.stack.addWidget(self.test_vocab_ui)

        self.stats_ui = StatsUI(self)
        self.stack.addWidget(self.stats_ui)

        self.stack.setCurrentWidget(self.main_ui)

        # 初始化选择的词库
        if self.vocab_list:
            self.change_vocab(0)
        else:
            QMessageBox.information(self, "提示", "没有找到词库，请新建一个词库。")

    def add_vocab(self, chinese, english):
        if chinese and english:
            self.vocab[chinese] = english
            write_vocab(self.current_vocab, self.vocab)
            if chinese not in self.stats:
                self.stats[chinese] = {'attempts': 0, 'errors': 0}
            write_stats(self.current_vocab, self.stats)

    def show_add_vocab_ui(self):
        self.stack.setCurrentWidget(self.add_vocab_ui)

    def show_test_vocab_ui(self):
        self.stack.setCurrentWidget(self.test_vocab_ui)

    def show_stats_ui(self):
        self.stats_ui.update_stats_table()  # 确保统计信息表在显示前是最新的
        self.stack.setCurrentWidget(self.stats_ui)

    def back_to_main_ui(self):
        self.stack.setCurrentWidget(self.main_ui)

    def change_vocab(self, index):
        if self.vocab_list:
            vocab_name = self.vocab_list[index]
            self.current_vocab = vocab_name
            self.vocab = read_vocab(vocab_name)
            self.stats = read_stats(vocab_name)
            self.initialize_stats()

    def create_new_vocab(self):
        vocab_name, ok = QInputDialog.getText(self, "新建词库", "请输入新词库名称:")
        if ok and vocab_name:
            create_new_vocab(vocab_name)
            self.vocab_list.append(vocab_name)
            self.vocab_combo.addItem(vocab_name)
            self.vocab_combo.setCurrentText(vocab_name)

    def initialize_stats(self):
        for word in self.vocab:
            if word not in self.stats:
                self.stats[word] = {'attempts': 0, 'errors': 0}
        write_stats(self.current_vocab, self.stats)

    def choose_weighted_random_word(self):  # 添加此方法
        return choose_weighted_random_word(self.vocab, self.stats)

    def update_stats(self):
        write_stats(self.current_vocab, self.stats)

    def write_vocab(self, vocab):  # 添加此方法
        write_vocab(self.current_vocab, vocab)

    def write_stats(self, stats):  # 添加此方法
        write_stats(self.current_vocab, stats)
