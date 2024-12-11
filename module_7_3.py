import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                words = file.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
                all_words[name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        words = self.get_all_words()
        word_pos = {}

        for file_name, words_list in words.items():
            if word in words_list:
                word_pos[file_name] = words_list.index(word) + 1

        return word_pos

    def count(self, word):
        word = word.lower()
        words = self.get_all_words()
        word_count = {}

        for file_name, words_list in words.items():
            word_count[file_name] = words_list.count(word)

        return word_count

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))