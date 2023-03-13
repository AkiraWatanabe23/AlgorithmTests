'''「棒倒し法」のテスト'''
import random
import numpy as np

#壁、床の定数
FLOOR = 0
WALL = 1

#迷路のサイズ
MAZE_HEIGHT = 9
MAZE_WIDTH = 11

#探索を進める方向
X_DIR = [0, 1, 0, -1]
Y_DIR = [-1, 0, 1, 0]

#numpy.zeros(a, b) ... 縦a, 横b の二次元配列（要素は全て0）をつくる
maze = np.zeros((MAZE_HEIGHT, MAZE_WIDTH), dtype=int)
#↓下記でも同じものがつくれる
#maze = [[0] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]

def make_maze():
    '''迷路生成'''
    #周りの壁をつくる(以下のスライスの記述は、通常のListには使えない)
    maze[0, :] = WALL
    maze[:, 0] = WALL
    maze[:, MAZE_WIDTH - 1] = WALL
    maze[MAZE_HEIGHT - 1, :] = WALL

    #柱を立てる
    for y_pos in range(2, MAZE_HEIGHT - 2, 2):
        for x_pos in range(2, MAZE_WIDTH - 2, 2):
            maze[y_pos, x_pos] = WALL

    #壁をつくる
    for y_pos in range(2, MAZE_HEIGHT - 2, 2):
        for x_pos in range(2, MAZE_WIDTH - 2, 2):
            #random.randint(a, b) ... a <= n <= b のランダムな整数
            index = random.randint(0, 3)

            if x_pos > 2:
                index = random.randint(0, 2)

            #取得したランダム方向に壁を立てる
            maze[y_pos + Y_DIR[index]][x_pos + X_DIR[index]] = WALL

def view_maze():
    '''迷路描画'''
    for y_pos in range(MAZE_HEIGHT):
        for x_pos in range(MAZE_WIDTH):
            pos = maze[y_pos][x_pos]

            if pos == FLOOR:
                print('  ', end='')
            elif pos == WALL:
                print('🔳', end='')

        print()

make_maze()
view_maze()
