# utils.py
import random


def choose_weighted_random_word(vocab, stats):
    words = list(vocab.keys())
    weights = [(stats[word]['errors'] + 1) for word in words]
    total_weight = sum(weights)
    probabilities = [weight / total_weight for weight in weights]
    return random.choices(words, weights=probabilities, k=1)[0]


def highlight_differences(self, user_answer, correct_answer):
    user_words = user_answer.split()
    correct_words = correct_answer.split()

    highlighted_text = []
    for user_word, correct_word in zip(user_words, correct_words):
        if user_word == correct_word:
            highlighted_text.append(correct_word)
        else:
            highlighted_text.append(f'<span style="color: red;">{correct_word}</span>')

    if len(user_words) > len(correct_words):
        for extra_word in user_words[len(correct_words):]:
            highlighted_text.append(f'<span style="color: red;">{extra_word}</span>')

    if len(correct_words) > len(user_words):
        for extra_word in correct_words[len(user_words):]:
            highlighted_text.append(f'<span style="color: red;">{extra_word}</span>')

    self.result_label.setText(f"错误，正确答案是: {' '.join(highlighted_text)}")
    self.result_label.setStyleSheet("font-size: 24px;")