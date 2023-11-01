import numpy as np
import matplotlib.pyplot as plt

# Parsing level from string format to a 2D numpy array
def parse_level(level_str):
    rows = level_str.strip().split("\n")
    return np.array([list(row.split(',')) for row in rows])

wall_test_str = """
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,A,-,-,-,-,-,-,-,-,G,-
x,x,-,x,x,x,x,x,x,x,x,x
"""
wall_test = parse_level(wall_test_str)

level_0_str = """
-,-,-,-,-,x,-,-,-,-,-,-
-,-,-,-,-,x,-,-,-,-,-,-
-,-,-,-,-,x,-,-,-,-,-,-
-,-,-,-,-,x,-,-,-,-,-,-
-,-,-,-,-,x,-,-,-,-,-,-
-,-,-,-,-,x,-,-,-,-,-,-
-,-,-,-,-,x,-,-,-,-,-,-
-,-,-,-,-,x,-,-,-,-,-,-
x,-,-,-,-,x,-,-,-,-,-,x
x,-,-,-,-,x,-,-,-,-,-,x
x,A,B,k,-,&,-,-,-,-,G,x
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_0 = parse_level(level_0_str)

level_1_str = """
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,-,-,-,x,-,-,-
-,-,-,-,-,k,-,-,x,-,-,-
-,-,-,-,-,x,-,-,x,-,-,-
-,A,B,-,-,-,-,-,&,-,G,-
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_1 = parse_level(level_1_str)

level_2_str = """
-,-,v,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
k,-,z,-,A,-,B,n,-,-,&,G
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_2 = parse_level(level_2_str)

level_3_str = """
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
-,-,z,-,-,-,-,-,-,-,x,-
k,-,^,-,A,-,B,n,-,-,&,G
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_3 = parse_level(level_3_str)

level_4_str = """
-,-,-,-,z,-,-,-,-,-,x,-
-,-,-,-,z,-,-,-,-,-,x,-
-,-,-,-,z,-,-,-,-,-,x,-
-,-,-,-,z,-,-,-,-,-,x,-
-,-,-,-,z,-,-,-,-,-,x,-
-,-,-,-,z,-,-,-,-,-,x,-
-,-,-,-,z,-,-,-,-,-,x,-
-,-,-,-,z,-,-,-,-,-,x,-
k,-,-,-,z,-,-,-,-,-,x,-
x,-,-,-,z,-,-,-,-,-,x,-
-,-,n,-,^,A,B,-,n,-,&,G
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_4 = parse_level(level_4_str)

level_5_str = """
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,x,-
A,B,-,k,-,k,-,k,-,&,x,G
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_5 = parse_level(level_5_str)

level_6_str = """
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,v,-,-,x,-,-,v,-,-,-
A,B,z,-,n,x,-,-,z,-,n,G
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_6 = parse_level(level_6_str)

level_7_str = """
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,x,-,-,-,-,-,-,-,-,-,-
-,x,x,-,-,-,-,-,-,-,-,-
-,x,x,x,-,-,-,-,-,-,-,-
-,v,v,v,x,-,-,-,-,-,-,-
k,z,z,z,-,-,A,B,-,n,-,G
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_7 = parse_level(level_7_str)

level_8_str = """
-,-,v,-,-,-,-,-,v,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,x,-
-,-,z,-,-,-,-,-,z,-,&,-
G,k,z,n,A,-,-,B,z,n,x,G
x,x,x,x,x,-,-,x,x,x,x,x
"""

level_8 = parse_level(level_8_str)

level_9_str = """
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,G
x,x,x,x,x,x,x,x,x,-,-,x
-,-,-,-,v,-,-,-,-,-,&,x
A,-,n,-,z,-,n,-,-,x,-,-
x,x,x,x,x,x,x,x,x,x,x,x
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,G
x,x,x,x,x,x,x,x,-,-,-,x
-,v,-,-,-,v,-,-,-,-,x,-
B,z,-,n,-,z,-,k,-,x,x,-
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_9 = parse_level(level_9_str)

level_10_str = """
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,-,-,-,-,-,-,-,-,-
-,-,-,x,-,-,-,-,-,-,-,-
-,-,x,x,-,x,x,-,-,-,-,-
k,x,x,x,-,x,x,x,-,-,-,-
x,x,x,x,&,x,x,x,x,-,-,-
x,x,x,x,G,x,x,x,x,x,A,B
x,x,x,x,x,x,x,x,x,x,x,x
"""

level_10 = parse_level(level_10_str)

