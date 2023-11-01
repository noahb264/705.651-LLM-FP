from levels import *
from engine import *
from render import *

moves = [
{
    "A": "do nothing"
},

{
    "A": "jump over right"
}
]

current_lvl =  level_3.copy()

for move in moves:
  current_lvl = apply_game_updates(current_lvl, move)
  display_level_with_labels(current_lvl)
