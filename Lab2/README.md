# Computational Intelligence Lab 2: Nim Game

## Overview

This repository contains the code for implementation of the game of Nim, along with different strategies for playing the game. The primary focus is on adaptive strategies that can dynamically adjust their parameters based on the current state of the game.


### Nim Game

The Nim game involves two players taking turns. Each turn, a player selects a pile and removes a certain number of objects from that pile. The game continues until no piles remain.

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
Find the shortest row, i.e. the one with the fewest objects with he lambda function, that is used as the key to determine the MINIMUM/MAXIMUM based on the number of objects.
Find the longest line, i.e. the one with the most objects.
If "love_small" is greater than 0.5, choose the smallest move on the shortest row or activate row. Otherwise, choose the largest move on the longest row.


## Analysis

The `analysis.py` file provides functions for analyzing the state of the game, calculating the nim sum, and finding optimal moves. These functions contribute to the decision-making process of adaptive strategies.

## Oversimplified Match

The `main.py` file demonstrates a simple match between two strategies. You can observe how they take turns making moves until one player wins.

## Algorithm Explanation



### Genetic Algorithm

1. **Initialization**: Create an initial population of individuals, each representing a strategy for playing the Nim game.

2. **Training Loop**: The genetic algorithm runs for a fixed number of generations. In each generation, a new population of offspring is generated from the current population through a combination of selection, mutation, and crossover operations.

3. **Selection**: Use tournament selection to choose individuals for the next generation. A subset of individuals is randomly chosen, and the most fit individual from that subset becomes a parent.

4. **Mutation**: With a certain probability, a random individual undergoes mutation. Mutation involves changing a move in the strategy to introduce diversity.

5. **Crossover**: Pairs of parents are selected, and a crossover operation combines their strategies to create


