# Computational Intelligence Lab 2: Nim Game

## Overview

This repository contains the code for a simple implementation of the game of Nim, along with different strategies for playing the game. The primary focus is on adaptive strategies that can dynamically adjust their parameters based on the current state of the game.

## Contents

- `nim.py`: Contains the implementation of the Nim and Nimply classes representing the game and a move, respectively.
- `strategies.py`: Defines various strategies for playing Nim, including random moves, a strategy based on choosing the maximum possible number of objects from the lowest row, and adaptive strategies.
- `evolutionary_strategy.py`: Implements an evolutionary strategy that evolves over generations using a genetic algorithm.
- `analysis.py`: Provides functions for analyzing the state of the game, computing the nim sum, and finding optimal moves.
- `main.py`: Demonstrates an oversimplified match between two strategies.

## How to Play

To play the Nim game with different strategies, you can modify the `strategy` variable in the `main.py` file. Simply set it to a tuple containing two strategy functions. The game will alternate between the two players, each using the specified strategy.

## Strategies

- `pure_random`: Chooses a completely random move.
- `gabriele`: Picks the maximum possible number of objects from the lowest row.
- `adaptive`: Adapts its parameters based on a predefined genome.
- `adaptive_alternative`: An alternative implementation of the adaptive strategy. #Instead of explicitly computing these values, the     strategy randomly selects a non-empty row and make a move based on the chosen row. This simplifies the strategy while still incorporating the adaptive parameter.
- `adaptive_dynamic`: Dynamically adjusts its parameters based on the percentage of empty rows. 

## Evolutionary Strategy

The repository includes an example of an evolutionary strategy in the `evolutionary_strategy.py` file. This strategy evolves over generations, and the best strategy is selected based on its performance in playing the game.
Extract the "love_small" parameter from the genome.
Calculate some values ​​based on the current state of the game and count the number of active rows, i.e. the number of rows still containing objects.   
Find the shortest row, i.e. the one with the fewest objects with he lambda function, that is used as the key to determine the MINIMUM/MAXIMUN based on the number of objects.
Find the longest line, i.e. the one with the most objects.
If "love_small" is greater than 0.5, choose the smallest move on the shortest row or activate row. Otherwise, choose the largest move on the longest row.

## Analysis

The `analysis.py` file provides functions for analyzing the state of the game, calculating the nim sum, and finding optimal moves. These functions contribute to the decision-making process of adaptive strategies.

## Oversimplified Match

The `main.py` file demonstrates a simple match between two strategies. You can observe how they take turns making moves until one player wins.

## License

This code is provided under the MIT License. See [LICENSE.md](https://github.com/squillero/computational-intelligence/blob/master/LICENSE.md) for details.

Feel free to explore and experiment with different strategies or even create your own!
