import random
from game import Game, Move, Player
import time
from ReinforcedPlayer import ReinforcedPlayer
import os
import time
from tqdm import tqdm
from minimax_main import play_games, plot_statistics

class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = "RandomPlayer"

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move


class MyPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move






if __name__ == '__main__':
    total_wins = [0, 0]
    game_number= 5000
    player1 = ReinforcedPlayer(game_number= game_number)
    player2 = RandomPlayer()
   
    save_filename = f"./Computational_Intelligence/Quixo/reinforced_player_{game_number}.npy"

    try:
        player1.load()
        print("Loaded ReinforcedPlayer state successfully.")
    except FileNotFoundError:
        print("No saved state found for ReinforcedPlayer. Training from scratch.")

    if not os.path.exists(save_filename):
        for game_num in tqdm(range(game_number), desc="Playing games", unit="game"):
            g = Game()
            winner, _,_ = g.play(player1, player2)
            total_wins[winner] += 1

        current_time = time.time()
        win_percentage = (total_wins[0] / game_number) * 100
        print(f"Player 1 win percentage: {win_percentage:.2f}%")
        print(f"Player 2 win percentage: {100 - win_percentage:.2f}%")
        print(f"Total time elapsed: {time.time() - current_time} seconds")
        print(f"Average time per game: {(time.time() - current_time) / game_number} seconds")
        player1.save()

    num_games = 100
    total_wins = [0, 0]
    for game_num in tqdm(range(num_games), desc="Playing games", unit="game"):
            g = Game()
            winner, _,_ = g.play(player1, player2)
            
            total_wins[winner] += 1

    current_time = time.time()
    win_percentage = (total_wins[0] / num_games) * 100
    print(f"Player 1 win percentage: {win_percentage:.2f}%")
    print(f"Player 2 win percentage: {100 - win_percentage:.2f}%")
    print(f"Total time elapsed: {time.time() - current_time} seconds")
    print(f"Average time per game: {(time.time() - current_time) / num_games} seconds")

    
    player1 = ReinforcedPlayer(game_number= game_number)
    player2 = RandomPlayer()
    play_games(player1,player2,100)

    play_games(player2,player1,100)
    





