package main

import (
	"container/heap"
	"fmt"
	"math"
)

// Coordinate represents a point in the grid
type Coordinate struct {
	X, Y int
}

// Node represents a node in the grid
type Node struct {
	Coord  Coordinate
	GCost  float64
	HCost  float64
	FCost  float64
	Parent *Node
	Index  int // index for the priority queue
}

// PriorityQueue implements heap.Interface and holds Nodes
type PriorityQueue []*Node

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].FCost < pq[j].FCost
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].Index = i
	pq[j].Index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := x.(*Node)
	n.Index = len(*pq)
	*pq = append(*pq, n)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	node := old[n-1]
	node.Index = -1 // for safety
	*pq = old[0 : n-1]
	return node
}

func (pq *PriorityQueue) update(node *Node, gCost, hCost, fCost float64, parent *Node) {
	node.GCost = gCost
	node.HCost = hCost
	node.FCost = fCost
	node.Parent = parent
	heap.Fix(pq, node.Index)
}

// Heuristic function (Manhattan distance)
func heuristic(a, b Coordinate) float64 {
	return math.Abs(float64(a.X-b.X)) + math.Abs(float64(a.Y-b.Y))
}

// AStar finds the shortest path between start and goal
func AStar(grid [][]int, start, goal Coordinate) ([]Coordinate, bool) {
	startNode := &Node{Coord: start, GCost: 0, HCost: heuristic(start, goal)}
	startNode.FCost = startNode.GCost + startNode.HCost

	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, startNode)

	cameFrom := make(map[Coordinate]*Node)
	cameFrom[start] = startNode

	closedSet := make(map[Coordinate]bool)

	directions := []Coordinate{
		{X: 0, Y: 1},  // right
		{X: 1, Y: 0},  // down
		{X: 0, Y: -1}, // left
		{X: -1, Y: 0}, // up
	}

	for pq.Len() > 0 {
		current := heap.Pop(&pq).(*Node)
		closedSet[current.Coord] = true

		if current.Coord == goal {
			return reconstructPath(current), true
		}

		for _, direction := range directions {
			neighborCoord := Coordinate{X: current.Coord.X + direction.X, Y: current.Coord.Y + direction.Y}

			if !isValidCoord(grid, neighborCoord) || closedSet[neighborCoord] {
				continue
			}

			tentativeGCost := current.GCost + 1
			hCost := heuristic(neighborCoord, goal)
			fCost := tentativeGCost + hCost

			neighbor, found := cameFrom[neighborCoord]
			if !found {
				neighbor = &Node{Coord: neighborCoord, GCost: tentativeGCost, HCost: hCost, FCost: fCost, Parent: current}
				cameFrom[neighborCoord] = neighbor
				heap.Push(&pq, neighbor)
			} else if tentativeGCost < neighbor.GCost {
				pq.update(neighbor, tentativeGCost, hCost, fCost, current)
			}
		}
	}

	return nil, false
}

// isValidCoord checks if a coordinate is valid within the grid and not an obstacle
func isValidCoord(grid [][]int, coord Coordinate) bool {
	if coord.X < 0 || coord.Y < 0 || coord.X >= len(grid) || coord.Y >= len(grid[0]) {
		return false
	}
	return grid[coord.X][coord.Y] == 0
}

// reconstructPath reconstructs the path from the goal node
func reconstructPath(node *Node) []Coordinate {
	var path []Coordinate
	for node != nil {
		path = append([]Coordinate{node.Coord}, path...)
		node = node.Parent
	}
	return path
}

// visualizeGrid displays the grid with the path, obstacles, start, and goal
func visualizeGrid(grid [][]int, path []Coordinate, start, goal Coordinate) {
	pathMap := make(map[Coordinate]bool)
	for _, coord := range path {
		pathMap[coord] = true
	}

	for i := range grid {
		for j := range grid[i] {
			coord := Coordinate{X: i, Y: j}
			if coord == start {
				fmt.Print("S ") // Start point
			} else if coord == goal {
				fmt.Print("G ") // Goal point
			} else if grid[i][j] == 1 {
				fmt.Print("# ") // Obstacle
			} else if pathMap[coord] {
				fmt.Print("* ") // Path
			} else {
				fmt.Print(". ") // Empty space
			}
		}
		fmt.Println()
	}
}

func main() {
	var rows, cols int

	bdebug := false
	if bdebug {
		fmt.Print("Enter number of rows: ")
		fmt.Scan(&rows)
		fmt.Print("Enter number of columns: ")
		fmt.Scan(&cols)
	} else {
		rows = 5
		cols = 4
	}

	// Initialize the grid
	grid := make([][]int, rows)
	for i := range grid {
		grid[i] = make([]int, cols)
	}

	// Input obstacles
	var numObstacles int
	if bdebug {
		fmt.Print("Enter number of obstacles: ")
		fmt.Scan(&numObstacles)

		for i := 0; i < numObstacles; i++ {
			var x, y int
			fmt.Printf("Enter obstacle %d coordinates (row col): ", i+1)
			fmt.Scan(&x, &y)
			grid[x][y] = 1 // Mark as obstacle
		}

	} else {
		numObstacles = 1
		grid[3][0] = 1
	}

	// Input start and goal coordinates
	var start, goal Coordinate
	if bdebug {
		fmt.Print("Enter start coordinates (row col): ")
		fmt.Scan(&start.X, &start.Y)
		fmt.Print("Enter goal coordinates (row col): ")
		fmt.Scan(&goal.X, &goal.Y)
	} else {
		start.X = 0
		start.Y = 0

		goal.X = 4
		goal.Y = 0
	}
	// Find the path using AStar
	path, found := AStar(grid, start, goal)
	if found {
		fmt.Println("Path found:")
		visualizeGrid(grid, path, start, goal)
	} else {
		fmt.Println("No path found.")
		visualizeGrid(grid, nil, start, goal)
	}
}
