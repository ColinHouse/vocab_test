# stats.py

import os
import json

STATS_DIR = 'stats'


def read_stats(vocab_name):
    stats_path = os.path.join(STATS_DIR, f"{vocab_name}.json")
    if not os.path.exists(stats_path):
        return {}
    with open(stats_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_stats(vocab_name, stats):
    if not os.path.exists(STATS_DIR):
        os.makedirs(STATS_DIR)
    stats_path = os.path.join(STATS_DIR, f"{vocab_name}.json")
    with open(stats_path, 'w', encoding='utf-8') as file:
        json.dump(stats, file, ensure_ascii=False, indent=4)
