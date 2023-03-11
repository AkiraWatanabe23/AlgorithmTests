'''「棒倒し法」のテスト'''
import random
import numpy as np

FLOOR = 0
WALL = 1

MAZE_WIDTH = 11
MAZE_HEIGHT = 9

X_DIR = [0, 1, 0, -1]
Y_DIR = [-1, 0, 1, 0]

#numpy.zeros(a, b) ... 縦a, 横b の二次元配列（要素は全て0）をつくる
maze = np.zeros((MAZE_HEIGHT, MAZE_WIDTH), dtype=int)

def make_maze():
    '''迷路生成'''
    #周りの壁をつくる
    maze[0, :] = 1
    maze[:, 0] = 1
    maze[:, MAZE_WIDTH - 1] = 1
    maze[MAZE_HEIGHT - 1, :] = 1

    #柱を立てる
    for y_pos in range(2, MAZE_HEIGHT - 2, 2):
        for x_pos in range(2, MAZE_WIDTH - 2, 2):
            maze[y_pos, x_pos] = 1

    #壁をつくる
    for y_pos in range(2, MAZE_HEIGHT - 2, 2):
        for x_pos in range(2, MAZE_WIDTH - 2, 2):
            index = random.randint(0, 3)

            if x_pos > 2:
                index = random.randint(0, 2)

            maze[y_pos + Y_DIR[index]][x_pos + X_DIR[index]] = 1

def view_maze():
    '''迷路描画'''
    for y_pos in range(MAZE_HEIGHT):
        for x_pos in range(MAZE_WIDTH):
            pos = maze[y_pos][x_pos]

            if pos == 0:
                print('　', end='')
            elif pos == 1:
                print('🔳', end='')

        print()

make_maze()
view_maze()
