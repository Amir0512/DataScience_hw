def read_file(file_to_read):
    with open(file_to_read, 'r', encoding='UTF-8') as f1:
        word = f1.read()
        words = word.split()
        unique_words = set(words)
        return unique_words


def save_file(file_to_save, unique_words):
    unique_words_count = len(unique_words)
    unique_words = sorted(unique_words)
    unique_words = ', '.join(unique_words)
    with open(file_to_save, 'w', encoding='UTF-8') as f2:
        f2.write(f'Уникальные слова:\n{unique_words}\nКоличество уникальных слов:{unique_words_count}')
