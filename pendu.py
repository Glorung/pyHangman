#!/bin/python3

import sys, os

import curses

import Hangman


def runHangman(display):
    game = Hangman.Hangman(display)

    while (game.input != 27):

        game.update()

        game.display.middleBar()

        game.display.refresh()

        game.input = game.display.getKey()

def main():
    print('Hello world')
    curses.wrapper(runHangman)

if __name__ == "__main__":
    main()
