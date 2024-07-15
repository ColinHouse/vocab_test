# utils.py
import random


def choose_weighted_random_word(vocab, stats):
    words = list(vocab.keys())
    weights = [(stats[word]['errors'] + 1) for word in words]
    total_weight = sum(weights)
    probabilities = [weight / total_weight for weight in weights]
    return random.choices(words, weights=probabilities, k=1)[0]

def highlight_differences(correct, user):
    correct_words = correct.split()
    user_words = user.split()
    highlighted = []
    for c_word, u_word in zip(correct_words, user_words):
        if c_word == u_word:
            highlighted.append(c_word)
        else:
            highlighted.append(f"<span style='color: red;'>{u_word}</span>")
    highlighted_text = ' '.join(highlighted)
    return highlighted_text
