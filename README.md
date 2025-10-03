# Tom and Jerry Maze Pathfinding Visualization

## Overview
This project implements various pathfinding algorithms to visualize Tom searching for Jerry in a maze. Written in Python, the project includes implementations of A*, BFS, DFS, cost-based, and greedy algorithms, each designed to navigate a maze and find the shortest or optimal path from Tom's starting position to Jerry's location. The maze is represented as a grid, with obstacles and the characters' positions visually updated during the search process.

## Features
- **Multiple Algorithms**: Implements A* (AstarAlgorithm.py), BFS (bfsAlgorithm.py), DFS (dfsAlgorithm.py), cost-based (costAlgorithm.py), and greedy (greedyAlgorithm.py) pathfinding algorithms.
- **Maze Visualization**: Visualizes Tom's movement through the maze as he searches for Jerry.
- **Performance Metrics**: Tracks expanded nodes, search depth, and computation time for each algorithm.
- **Interactive Setup**: Allows for customization of the maze and initial positions through code configuration.

## Requirements
- Python 3.x
- NumPy (for array operations)
- Time (for performance tracking, included in standard library)

## Installation
1. Clone or download the project repository.
2. Ensure Python 3.x and NumPy are installed:
   ```bash
   pip install numpy
   ```
3. Run using
    ```bash
    python main.py
    ```

## Example: A* Algorithm
### Code Snippet
The A* algorithm uses a heuristic (Manhattan distance) to efficiently find the shortest path from Tom to Jerry.

## Code Structure
- **AstarAlgorithm.py**: Implements the A* algorithm with heuristic-based search.
- **bfsAlgorithm.py**: Implements Breadth-First Search for exhaustive exploration.
- **dfsAlgorithm.py**: Implements Depth-First Search for deeper exploration.
- **costAlgorithm.py**: Implements a cost-based search prioritizing path cost.
- **greedyAlgorithm.py**: Implements a greedy search using heuristic guidance.
- **node.py**: Defines the `Node` class for representing maze states and movements.

