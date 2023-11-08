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

def is_game_over(current_lvl):
    return "A" not in current_lvl or "B" not in current_lvl

def evalution(level_num, mover_title):
    level_str = f"level_{level_num}"
    if not hasattr(levels, level_str): error("level not found")
    level_world = getattr(levels, level_str)

    if mover_title not in MOVERS: error("mover not found")
    mover: Mover = MOVERS.get(mover_title)()
    
    saver = Saver()
    while not is_game_over(level_world) and saver.i < MAX_ITERATIONS:
        saver.update(level_world)

        move = mover.get_next_move(level_world)
        level_world = apply_game_updates(level_world, move)
        time.sleep(random.random())

    saver.update(level_world)
    saver.finalize()
    
    success = "G" not in level_world
    print("Success?", success)

def startup():
    parser = argparse.ArgumentParser("evaluation.py")
    parser.add_argument("--level", required=True)
    parser.add_argument("--mover", required=True)
    args = parser.parse_args()

    evalution(args.level, args.mover)

if __name__ == "__main__":
    print("Starting up")
    startup()