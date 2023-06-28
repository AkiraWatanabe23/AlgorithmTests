'''A*テスト'''
from enum import Enum

class Status(Enum):
    '''マスのステータスを表すenumを定義'''
    FLOOR = 0
    WALL = 1
    START = 2
    GOAL = 3
    OPEN = 4
    CLOSE = 5

class CellData:
    '''セルのデータを管理する構造体（ぽいもの）'''
    def __init__(self, status, opened_cell=(0, 0)):
        self.status = status #セルの状態（Enum）
        self.opened_cell = opened_cell #オープン元のセル（Tuple）

        self.simurate_cost = 0
        self.real_cost = 0
        self.score = 0

    def __eq__(self, other) -> bool:
        return self.opened_cell == other.opened_cell

def a_star():
    '''A*アルゴリズム'''
    pass

maze = [[CellData(Status.FLOOR) for _ in range(5)] for _ in range(5)]
scores = [[0] * 5 for _ in range(5)]

#迷路の二次元配列
maze[2][1] = CellData(Status.START)
maze[2][4] = CellData(Status.GOAL)
maze[1][2] = CellData(Status.WALL)
maze[3][1] = CellData(Status.WALL)
maze[3][2] = CellData(Status.WALL)
maze[3][3] = CellData(Status.WALL)

for r, line in enumerate(maze):
    for c, cell in enumerate(line):
        scores[r][c] = cell.score

for line in maze:
    for cell in line:
        match cell:
            case cell if cell.status == Status.FLOOR:
                print("  ", end="")
            case cell if cell.status == Status.WALL:
                print("🔳", end="")
            case cell if cell.status == Status.START:
                print("ス", end="")
            case cell if cell.status == Status.GOAL:
                print("ゴ", end="")

    print()
