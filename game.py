import random
from src.game_status import GameStatus


class Game:
    def __init__(self):
        self.__filename = './words.txt'
        self.__corrects = 0
        self.__mistakes = 0
        self.__words = []
        self.__word = ''
        self.__length = 0
        self.__mistaken_words = []
        self.__correct_words = []
        self.__game_status = GameStatus.NOT_STARTED

    def get_data(self):
        with open(self.filename, 'r', encoding='utf8') as file:
            for line in file:
                self.__words.append(line[:-1])
            self.__length = len(self.__words)
            self.__game_status = GameStatus.STARTED

    def get_word(self):
        if self.game_status != GameStatus.STARTED:
            raise Exception(f'Not appropriate game status. Current: {self.game_status}')
        self.__word = self.__words[random.randint(0, self.length - 1)]
        return self.__word

    def check_answer(self, guess: bool):
        if guess:
            self.__correct_words.append(self.__word)
            self.__corrects += 1
            return True

        self.__mistaken_words.append(self.__word)
        self.__mistakes += 1
        return False

    @property
    def filename(self):
        return self.__filename

    @property
    def mistakes (self):
        return self.__mistakes

    @property
    def corrects(self):
        return self.__corrects

    @property
    def length(self):
        return self.__length

    @property
    def correct_words(self):
        return self.__correct_words

    @property
    def mistaken_words(self):
        return self.__mistaken_words

    @property
    def game_status(self):
        return self.__game_status