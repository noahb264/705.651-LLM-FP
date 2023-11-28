import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np

def print_to_string(level):
    level_string = ""
    for row in level:
      level_string = level_string + ','.join(row) + '\n'
    return level_string

# Color mapping for each tile
color_map = {
    '-': 'white',
    'x': 'gray',
    'A': 'blue',
    'B': 'green',
    'C': 'red',
    'D': 'purple',
    'k': 'yellow',
    'n': 'orange',
    'u': 'cyan',
    '&': 'brown',
    'z': 'pink',
    'v': 'lightblue',
    '^': 'lightgreen',
    'G': 'gold'
}

# Label mapping for each tile
label_map = {
    '-': '',
    'x': '',
    'A': 'P1',
    'B': 'P2',
    'C': 'P3',
    'D': 'P4',
    'k': 'key',
    'n': 'button',
    'u': 'button',
    '&': 'door',
    'z': 'laser',
    'v': 'laser \nemitter',
    '^': 'laser \nemitter',
    'G': 'goal'
}

def display_level_with_labels(level_data):

    # Convert tile symbols to RGB values using color map
    rows, cols = level_data.shape
    color_data = np.zeros((rows, cols, 4))
    for i in range(rows):
        for j in range(cols):
            color_data[i, j] = mcolors.to_rgba(color_map[level_data[i, j]])

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(color_data)

    # Add labels
    for i in range(rows):
        for j in range(cols):
            label = label_map[level_data[i, j]]
            ax.text(j, i, label, ha='center', va='center', color='black' if level_data[i, j] in ['-', 'k', 'G', 'u', 'n', 'z', 'v', '^'] else 'white')

    ax.set_xticks(np.arange(-0.5, 12, 1))
    ax.set_yticks(np.arange(-0.5, 12, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which='both', color='black', linewidth=2)
    ax.set_aspect('equal')

    # plt.show()
    return fig
