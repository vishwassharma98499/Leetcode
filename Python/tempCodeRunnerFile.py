import heapq
import math

# Coordinate represents a point in the grid
class Coordinate:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __hash__(self):
        return hash((self.X, self.Y))

# Node represents a node in the grid
class Node:
    def __init__(self, coord, g_cost, h_cost, parent=None):
        self.Coord = coord
        self.GCost = g_cost
        self.HCost = h_cost
        self.FCost = g_cost + h_cost
        self.Parent = parent
        self.Index = 0

    def __lt__(self, other):
        return self.FCost < other.FCost

# PriorityQueue implements heapq and holds Nodes
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, node):
        heapq.heappush(self.elements, node)

    def pop(self):
        return heapq.heappop(self.elements)

    def update(self, node, g_cost, h_cost, f_cost, parent):
        node.GCost = g_cost
        node.HCost = h_cost
        node.FCost = f_cost
        node.Parent = parent
        heapq.heapify(self.elements)

    def __len__(self):
        return len(self.elements)

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a.X - b.X) + abs(a.Y - b.Y)

# AStar finds the shortest path between start and goal
def AStar(grid, start, goal):
    start_node = Node(start, 0, heuristic(start, goal))
    
    pq = PriorityQueue()
    pq.push(start_node)

    came_from = {start: start_node}
    closed_set = set()

    directions = [Coordinate(0, 1), Coordinate(1, 0), Coordinate(0, -1), Coordinate(-1, 0)]

    while len(pq) > 0:
        current = pq.pop()
        closed_set.add(current.Coord)

        if current.Coord == goal:
            return reconstruct_path(current), True

        for direction in directions:
            neighbor_coord = Coordinate(current.Coord.X + direction.X, current.Coord.Y + direction.Y)

            if not is_valid_coord(grid, neighbor_coord) or neighbor_coord in closed_set:
                continue

            tentative_g_cost = current.GCost + 1
            h_cost = heuristic(neighbor_coord, goal)
            f_cost = tentative_g_cost + h_cost

            neighbor = came_from.get(neighbor_coord)
            if neighbor is None:
                neighbor = Node(neighbor_coord, tentative_g_cost, h_cost, current)
                came_from[neighbor_coord] = neighbor
                pq.push(neighbor)
            elif tentative_g_cost < neighbor.GCost:
                pq.update(neighbor, tentative_g_cost, h_cost, f_cost, current)

    return None, False

# isValidCoord checks if a coordinate is valid within the grid and not an obstacle
def is_valid_coord(grid, coord):
    if coord.X < 0 or coord.Y < 0 or coord.X >= len(grid) or coord.Y >= len(grid[0]):
        return False
    return grid[coord.X][coord.Y] == 0

# reconstructPath reconstructs the path from the goal node
def reconstruct_path(node):
    path = []
    while node is not None:
        path.insert(0, node.Coord)
        node = node.Parent
    return path

# visualizeGrid displays the grid with the path, obstacles, start, and goal
def visualize_grid(grid, path, start, goal):
    path_map = {coord: True for coord in path}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            coord = Coordinate(i, j)
            if coord == start:
                print("S ", end="")
            elif coord == goal:
                print("G ", end="")
            elif grid[i][j] == 1:
                print("# ", end="")
            elif coord in path_map:
                print("* ", end="")
            else:
                print(". ", end="")
        print()

def findShortestPath(nrow,ncolumn,startCoord,endCoordinate):
        # Initialize the grid
    grid = [[0 for _ in range(ncolumn)] for _ in range(nrow)]

    # Input obstacles
    grid[3][0] = 1
    # Find the path using AStar
    path, found = AStar(grid, startCoord, endCoordinate)
    print(path)
    if found:
        print("Path found:")
        visualize_grid(grid, path, startCoord, endCoordinate)
    else:
        print("No path found.")
        visualize_grid(grid, [], start, goal)


def main():
    rows, cols = 5, 4
      # Input start and goal coordinates
    start = Coordinate(0, 0)
    goal = Coordinate(4, 0)
    findShortestPath(rows,cols,start,goal)


if __name__ == "__main__":
    main()
