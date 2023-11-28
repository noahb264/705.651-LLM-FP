import numpy as np

def move_player(level_data, x, y, dx, dy):
    """Move a player in the level_data by dx and dy if possible."""
    player_symbol = level_data[x, y]
    new_x, new_y = x + dx, y + dy
    target_cell = level_data[new_x, new_y]

    if target_cell not in ['x', '&', 'v', '^', 'A', 'B', 'C', 'D', 'n', 'u']:  # fail if not solid

        if target_cell == 'k':  # key logic
            level_data[level_data == '&'] = '-'  # Open all doors
            level_data[new_x, new_y] = player_symbol
            level_data[x, y] = '-'

        elif target_cell == 'G':  # goal logic
            level_data[new_x, new_y] = player_symbol
            level_data[x, y] = '-'

        else:
            level_data[x, y], level_data[new_x, new_y] = '-', player_symbol

def jump_over(level_data, x, y, direction):
    offset = -1 if direction == 'left' else 1

    # Check if the jump is within bounds
    if not (0 <= x - 1 < 12) or not (0 <= y + 2*offset < 12):
        return (0, 0)

    # Check for laser at one up and one to the direction
    if level_data[x-1, y+offset] == 'z':
        return (None, None)

    # Check if one up and one to the direction is blocked by a non-laser
    if level_data[x-1, y+offset] in ['x', 'v', '^', '&', 'A', 'B', 'C', 'D']:
        return (0, 0)

    # Check if two to the direction and one up is blocked
    if level_data[x-1, y+2*offset] in ['x', 'v', '^', '&', 'A', 'B', 'C', 'D', 'z']:
        return (-1, offset)

    # If both checks pass, move two to the direction
    return (0, 2*offset)

def handle_player_action(level_data, player, action):
    x, y = np.where(level_data == player)
    if len(x) == 0:
        return level_data
    x, y = x[0], y[0]

    moves = {
        "move left": (0, -1),
        "move right": (0, 1),
        "jump on left": (-1, -1),
        "jump on right": (-1, 1),
        "jump over left": jump_over(level_data, x, y, 'left'),
        "jump over right": jump_over(level_data, x, y, 'right')
    }

    dx, dy = moves.get(action, (0, 0))
    if dx is None:
      level_data[x, y] = '-'
      return level_data

    if 0 <= x + dx < 12 and 0 <= y + dy < 12:  # Ensure within bounds
        move_player(level_data, x, y, dx, dy)

    return level_data

def apply_gravity(updated_data):
    players = ['A', 'B', 'C', 'D']

    for _ in range(11):
        for i in range(11, 0, -1):
            for j in range(12):
                cell = updated_data[i-1, j]
                if cell in players and updated_data[i, j] == '-':
                    updated_data[i-1, j], updated_data[i, j] = updated_data[i, j], updated_data[i-1, j]

    # Remove players if they fall into the bottom row
    for j in range(12):
        if updated_data[11, j] in players:
            updated_data[11, j] = '-'

    return updated_data

# Todo: move into apply interactions
def apply_button_interactions(updated_data):
    players = ['A', 'B', 'C', 'D']

    # Button Activation/Deactivation
    for i in range(11):
        for j in range(12):
            if updated_data[i, j] in players and updated_data[i+1, j] == 'n':
                updated_data[i+1, j] = 'u'
            elif updated_data[i, j] == '-' and updated_data[i+1, j] == 'u':
                updated_data[i+1, j] = 'n'

    # Laser Activation/Deactivation
    if 'u' in updated_data:  # If any button is activated
        updated_data[updated_data == 'z'] = '-'
    else:  # No button is activated
        for j in range(12):
            laser_active = False
            for i in range(12):
                if updated_data[i, j] == 'v':
                    laser_active = True
                elif updated_data[i, j] == '^':
                    laser_active = False
                elif laser_active and updated_data[i, j] not in ['x', '&', 'n', 'u', 'k', 'G']:
                    if updated_data[i, j] in players:
                        updated_data[i, j] = 'z'  # Keep the laser active even if a player was there
                    else:
                        updated_data[i, j] = 'z'

    return updated_data

def apply_actions(level_data, actions):
    updated_data = level_data.copy()
    for player, action in actions.items():
        updated_data = handle_player_action(updated_data, player, action)
    return updated_data

def apply_game_updates(level_data, actions):
    """Integrate all actions and interactions."""
    updated_data = apply_actions(level_data, actions)
    updated_data = apply_gravity(updated_data)
    updated_data = apply_button_interactions(updated_data)

    return updated_data

