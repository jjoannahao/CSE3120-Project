"""
title: player class
author: joanna hao
date-created: 2023-11-28
"""
from a_dice import Dice


class Player:
    """
    the player for the game 'Ship, Captain, Crew!'
    """
    def __init__(self, NAME):
        self.__NAME = NAME
        self.__DICE = [Dice(6), Dice(6), Dice(6), Dice(6), Dice(6)]
        self.__SCORE = 0
        self.__CAPTAIN_FOUND = False
        self.__SHIP_FOUND = False
        self.__CREW_FOUND = False

    # --- Modifier Methods
    def addScore(self, POINTS):
        self.__SCORE += POINTS

    def rollDice(self):
        """
        rolls all dice in DICE
        :return: None
        """
        for die in self.__DICE:
            die.rolLDie()

    def updateFound(self, DIE):
        """
        update whether player has found captain/ship/crew
        :param DIE: list (int)
        :return: None
        """
        # update each separately since captain, ship, and crew don't have to be found in the same roll
        if not self.__CAPTAIN_FOUND and 6 in DIE:
            self.CAPTAIN_FOUND = True
            print("Captain is found!")
        if self.CAPTAIN_FOUND and not self.__SHIP_FOUND and 5 in DIE:  # captain is already found
            self.__SHIP_FOUND = True
            print("Ship is found!")
        if self.CAPTAIN_FOUND and self.__SHIP_FOUND and not self.__CREW_FOUND and 4 in DIE:  # captain & ship already found
            self.__CREW_FOUND = True
            print("Crew is found!")

    # --- Accessor Methods
    def __str__(self):
        return self.__NAME

    def getDice(self):
        return self.__DICE

    def getScore(self):
        return self.__SCORE

    def displayDice(self):
        """
        prints the dice values
        :return: None
        """
        for i in range(len(self.__DICE)):
            print(f" Dice {i+1} rolled a {self.__DICE[i].getDieNumber()}")


if __name__ == "__main__":
    # --- input --- #
    PLAYER1_NAME = input("Player 1 Name: ")
    PLAYER2_NAME = input("Player 2 Name: ")

    # --- processing --- #
    PLAYER1 = Player(PLAYER1_NAME)
    PLAYER2 = Player(PLAYER2_NAME)
