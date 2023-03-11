'''「棒倒し法」のテスト'''
import random
import numpy as np

FLOOR = 0
WALL = 1

MAZE_WIDTH = 11
MAZE_HEIGHT = 9

maze = np.zeros((MAZE_WIDTH, MAZE_HEIGHT), dtype=int)

def make_maze():
    '''迷路生成'''
    #周りの壁をつくる
    maze[0, :] = 1
    maze[:, 0] = 1
    maze[:, MAZE_HEIGHT - 1] = 1
    maze[MAZE_WIDTH - 1, :] = 1

make_maze()
print(maze)
