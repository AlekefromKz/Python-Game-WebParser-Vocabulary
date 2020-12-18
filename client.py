from src.game import Game
import os.path
from src.parser import get_words


filename = "words.txt"
if not os.path.isfile(filename):
    get_words()

game = Game()
game.get_data()

print('Game started. To quit enter "stop" during the game\n')

while True:
    print('Word:', game.get_word())
    word = input('Do you know this word? "y/n": ')

    while word != 'y' and word != 'n' and word != 'stop':
        word = input('Please, enter on of the valid options: "y/n". Enter "stop" to quit: ')

    if word == 'stop':
        break

    game.check_answer(word == 'y')
    print()


print('\n\n\nCorrect answers:', game.corrects)
print('Mistakes:', game.mistakes, '\n\n\n')

if input('Do you want to see words you do not know? y/n: ') == 'y':
    print()
    for word in game.mistaken_words:
        print(word)

print('\n\n\n')

if input('Do you want to see words you know? y/n: ') == 'y':
    print()
    for word in game.correct_words:
        print(word)
