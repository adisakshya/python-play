# import function play from player module
from .player import play_it
import sys

# main function


def main():
    try:
        play_it(sys.argv[1])
    except IndexError:
        print('Usage: python -m python_play <path/to/audio>')

if __name__ == '__main__':
    main()
