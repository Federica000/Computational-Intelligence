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
- `adaptive_alternative`: An alternative implementation of the adaptive strategy.
- `adaptive_dynamic`: Dynamically adjusts its parameters based on the percentage of empty rows.

## Evolutionary Strategy

The repository includes an example of an evolutionary strategy in the `evolutionary_strategy.py` file. This strategy evolves over generations, and the best strategy is selected based on its performance in playing the game.

## Analysis

The `analysis.py` file provides functions for analyzing the state of the game, calculating the nim sum, and finding optimal moves. These functions contribute to the decision-making process of adaptive strategies.

## Oversimplified Match

The `main.py` file demonstrates a simple match between two strategies. You can observe how they take turns making moves until one player wins.

## License

This code is provided under the MIT License. See [LICENSE.md](https://github.com/squillero/computational-intelligence/blob/master/LICENSE.md) for details.

Feel free to explore and experiment with different strategies or even create your own!
