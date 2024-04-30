import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for i in range(width)] for j in range(height)]

    def generate_maze(self):
        for i in range(self.width):
            for j in range(self.height):
                if random.random() < 0.5:
                    self.grid[j][i] = 1

    def print_maze(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j], end=" ")
            print()

class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.x = 0
        self.y = 0

    def move(self, direction):
        new_x, new_y = self.x, self.y
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

        if new_x < 0 or new_x >= self.maze.width or new_y < 0 or new_y >= self.maze.height:
            return False

        if self.maze.grid[new_y][new_x] == 1:
            return False

        self.x, self.y = new_x, new_y
        return True

    def find_path(self):
        visited = [[False for i in range(self.maze.width)] for j in range(self.maze.height)]
        queue = [(self.x, self.y)]

        while queue:
            x, y = queue.pop(0)

            if visited[y][x]:
                continue

            visited[y][x] = True

            if x == self.maze.width - 1 and y == self.maze.height - 1:
                return True

            for direction in ["up", "down", "left", "right"]:
                if self.move(direction):
                    queue.append((self.x, self.y))

        return False

if __name__ == "__main__":
    maze = Maze(3,3)
    maze.generate_maze()
    maze.print_maze()
    agent = Agent(maze)
    # agent.move()

    if agent.find_path():
        print("The agent found a path to the exit!")
    else:
        print("The agent could not find a path to the exit.")
