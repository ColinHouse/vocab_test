import os

# 定义词汇文件夹路径
VOCAB_DIR = 'vocabs'


def get_vocab_list():
    if not os.path.exists(VOCAB_DIR):
        os.makedirs(VOCAB_DIR)
    return [f for f in os.listdir(VOCAB_DIR) if os.path.isfile(os.path.join(VOCAB_DIR, f))]


def read_vocab(vocab_name):
    """读取词汇文件"""
    vocab_path = os.path.join(VOCAB_DIR, vocab_name)
    vocab = {}
    if not os.path.exists(vocab_path):
        return vocab
    with open(vocab_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                chinese, english = parts
                vocab[chinese] = english
    return vocab


def write_vocab(vocab_name, vocab):
    vocab_path = os.path.join(VOCAB_DIR, vocab_name)
    with open(vocab_path, 'w', encoding='utf-8') as file:
        for chinese, english in vocab.items():
            file.write(f'{chinese}\t{english}\n')


def create_new_vocab(vocab_name):
    vocab_file = os.path.join(VOCAB_DIR, f'{vocab_name}.txt')
    if not os.path.exists(vocab_file):
        with open(vocab_file, 'w', encoding='utf-8'):
            pass  # create empty file
