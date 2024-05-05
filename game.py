import random
import linecache


class Game:

    def __init__(self):
        pass


def get_random_line(textfile: str):
    f = open(textfile, "r")
    lines = len(f.readlines())
    rl = random.randrange(1, lines + 1)
    f.close()
    return rl


def get_word(textfile: str, line: int):
    word = linecache.getline(textfile, line)
    return word.strip()


def get_random_word():
    return get_word("words.txt", get_random_line("words.txt"))


def hide_word(word: str, exceptions=None):
    if exceptions is None:
        exceptions = set()
    a = ""
    for i in word:
        if i in exceptions:
            a += i
        else:
            a += "_"
    return a


def print_graphic(fails=0):
    global i
    for i in range(fails * 7 + 1, fails * 7 + 8):
        print(linecache.getline("graphic", i).strip('\n'))


def should_start_again():
    new_game = input("New game? (y/n):")
    return new_game == "y"


def main():
    play_again = True
    while play_again:
        og_word = get_random_word()
        guesses = set()
        fail = 0
        print_graphic()

        while True:
            h_word = hide_word(og_word, guesses)
            print(h_word)
            if h_word == og_word:
                print("You have won")
                play_again = should_start_again()
                break

            guess = input("enter single letter ")
            guesses.add(guess)
            if guess not in og_word:
                fail += 1
            print_graphic(fail)
            if fail == 15:
                print("you loose")
                play_again = should_start_again()
                break

            print(chr(27) + "[2J")
    print("Good Bye")


if __name__ == '__main__':
    main()
