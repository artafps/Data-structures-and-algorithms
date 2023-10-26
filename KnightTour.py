
import pygame
import sys


KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


class KnightTour:
    def __init__(self, board_size):
        self.board_size = board_size  # tuple
        self.board = []
        for i in range(board_size[0]):
            temp = []
            for j in range(board_size[1]):
                temp.append(0)
            self.board.append(temp) # empty cell
        self.move = 1

    def print_board(self):
        print('board:')
        for i in range(self.board_size[0]):
            print(self.board[i])

    def warnsdroff(self, start_pos, GUI=False):
        x_pos,  y_pos = start_pos
        self.board[x_pos][y_pos] = self.move

        if not GUI:
            while self.move <= self.board_size[0] * self.board_size[1]:
                self.move += 1
                next_pos = self.find_next_pos((x_pos, y_pos))
                if next_pos:
                    x_pos, y_pos = next_pos
                    self.board[x_pos][y_pos] = self.move
                else:
                    self.print_board()
                    return self.board
        else:
            if self.move <= self.board_size[0] * self.board_size[1]:
                self.move += 1
                next_pos = self.find_next_pos((x_pos, y_pos))
                return next_pos

    def find_next_pos(self, current_pos):
        empty_neighbours = self.find_neighbours(current_pos)
        if len(empty_neighbours) is 0:
            return
        least_neighbour = 8
        least_neighbour_pos = ()
        for neighbour in empty_neighbours:
            neighbours_of_neighbour = self.find_neighbours(pos=neighbour)
            if len(neighbours_of_neighbour) <= least_neighbour:
                least_neighbour = len(neighbours_of_neighbour)
                least_neighbour_pos = neighbour
        return least_neighbour_pos

    def find_neighbours(self, pos):
        neighbours = []
        for dx, dy in KNIGHT_MOVES:
            x = pos[0] + dx
            y = pos[1] + dy
            if 0 <= x < self.board_size[0] and 0 <= y < self.board_size[1] and self.board[x][y] is 0:
                neighbours.append((x, y))
        return neighbours


# a = KnightTour((8, 8))
# a.warnsdroff((3, 3))

def draw_background():
    screen.fill(blackTileColor)
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, whiteTileColor, (tileSize * j, tileSize * i, tileSize, tileSize), 0)


def draw_tiles():
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if knight_pos == (i, j):
                pygame.draw.circle(screen, knightTileColor,
                                   (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4, 0)
            elif knight_tour.board[i][j] != 0:
                pygame.draw.circle(screen, visitedTileColor,
                                   (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4,  0)


def draw_line(start, end):
    pygame.draw.line(screen, lineColor,
                     (tileSize * start[1] + tileSize // 2, tileSize * start[0] + tileSize // 2),
                     (tileSize * end[1] + tileSize // 2, tileSize * end[0] + tileSize // 2), 10)


board_size = (8, 10)
screenSizeX = 800
screenSizeY = 800

if screenSizeX//board_size[1] >= screenSizeY//board_size[0]:
    tileSize = screenSizeY // board_size[0]
else:
    tileSize = screenSizeX // board_size[1]

knight_tour = KnightTour(board_size=board_size)
pygame.init()
screen = pygame.display.set_mode((tileSize*board_size[1], tileSize*board_size[0]))
clock = pygame.time.Clock()
fps = 1

whiteTileColor = (245, 245, 245)
blackTileColor = (100, 100, 100)
visitedTileColor = (255, 102, 102)
knightTileColor = (153, 51, 51)
lineColor = (255, 102, 102)

knight_pos = (0, 0)
draw_background()
draw_tiles()


skip = True
runUpdate = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                runUpdate = False

            if event.key == pygame.K_q:
                fps += 1
            if event.key == pygame.K_a:
                fps -= 1
                if fps == 0:
                    fps = 1
    if runUpdate:
        last_knight_pos = knight_pos
        if last_knight_pos:
            knight_pos = knight_tour.warnsdroff(knight_pos, GUI=True)
            board = knight_tour.board
            if knight_pos:
                draw_line(last_knight_pos, knight_pos)
            draw_tiles()
        else:
            knight_tour.print_board()
            runUpdate = False

    pygame.display.set_caption("Knight\'s Tour " + str(fps) + "fps")
    pygame.display.update()
