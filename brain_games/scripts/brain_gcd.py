#!/usr/bin/env python3
from brain_games.game_engine import game_engine
from brain_games.games.gcd import qra_list, game_desc


def main():
    game_engine(qra_list, game_desc)


if __name__ == '__main__':
    main()
