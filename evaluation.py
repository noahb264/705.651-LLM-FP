import argparse
import levels
from engine import apply_game_updates
from mover import MOVERS, Mover
import time
import random
from saver import Saver

MAX_ITERATIONS = 100

def error(message):
    print("Error:", message)
    exit(1)

def is_game_over(current_lvl, original_lvl):
    players = ["A", "B", "C", "D"]
    for player in players:
        if player in original_lvl and player not in current_lvl:
            return True

    if "G" not in current_lvl:
        return True

    return False

def switch_player(player, world):
    if player == "A":
        if "B" in world:
            return "B"
        else:
            return "A"

    elif player == "B":
        if "C" in world:
            return "C"
        else:
            return "A"

    elif player == "C":
        if "D" in world:
            return "D"
        else:
            return "A"
    
    elif player == "D":
        return "A"

    else:
        error("invalid player")

def evaluation(level_str, mover_title):
    if not hasattr(levels, level_str): error("level not found")
    level_world = getattr(levels, level_str)
    level_world_orig = level_world.copy()

    if mover_title not in MOVERS: error("mover not found")
    mover: Mover = MOVERS.get(mover_title)()
    
    saver = Saver()
    player = "A"
    moves = []
    comms = []
    try:
        while not is_game_over(level_world, level_world_orig) and saver.i < MAX_ITERATIONS:
            saver.update(level_world)

            move, communication = mover.get_next_move(level_world, player, moves, comms)
            moves.append(list(move.items())[0])
            comms.append(list(communication.items())[0])
            level_world = apply_game_updates(level_world, move)
            player = switch_player(player, level_world)

    finally:
        saver.update(level_world)
        saver.finalize(level_world, moves, comms)

def startup():
    parser = argparse.ArgumentParser("evaluation.py")
    parser.add_argument("--level", required=True)
    parser.add_argument("--mover", required=True)
    args = parser.parse_args()

    evaluation(args.level, args.mover)

if __name__ == "__main__":
    print("Starting up")
    startup()