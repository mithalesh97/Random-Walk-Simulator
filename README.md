# Random Walk Simulator (Python)

## 1. Project Overview

The Random Walk Simulator is a Python project that simulates the random movement of multiple walkers in a two-dimensional (2D) space.

Each walker starts at a randomly selected position and moves in one of four directions: up, down, left, or right.

The simulation uses Python's `random` module to generate movements and Matplotlib to visualize the walking paths.

## 2. Project Objectives

- Understand the concept of random walks.
- Simulate movement in a 2D coordinate system.
- Generate multiple independent random walks.
- Visualize walking paths using Matplotlib.
- Practice Python loops, conditions, lists, and random numbers.

## 3. Features

- Simulates 50 independent walkers.
- Assigns random starting positions.
- Moves walkers in four possible directions.
- Gives each walker a random number of steps between 50 and 200.
- Stores the X and Y coordinates of each movement.
- Displays all walking paths on one graph.
- Marks starting points in green and ending points in red.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Random module | Generates random positions and movements |
| Matplotlib | Visualizes the random walks |

## 5. How Random Walk Works

A random walk is a mathematical process in which an object moves randomly from one position to another.

In this project, each walker can move in four directions:

| Direction | Coordinate Change |
|---|---|
| Right | X increases by 1 |
| Left | X decreases by 1 |
| Up | Y increases by 1 |
| Down | Y decreases by 1 |

For example, if the current position is `(2, 3)`:

- Right → `(3, 3)`
- Left → `(1, 3)`
- Up → `(2, 4)`
- Down → `(2, 2)`

## 6. Python Concepts Used

- Variables: Store the current X and Y positions.
- Lists: Store the coordinates of each walk.
- Loops: Repeat movements and simulate multiple walkers.
- Conditional statements: Determine movement direction.
- Random numbers: Generate random starting positions and step counts.
- Matplotlib: Draw and visualize the paths.

## 7. How to Run the Project

**Step 1:** Install Python.

**Step 2:** Install Matplotlib:

```bash
pip install matplotlib
```

**Step 3:** Create a Python file named:

```text
random_walk.py
```

**Step 4:** Run the program:

```bash
python random_walk.py
```

## 8. Expected Output

The program generates a graph containing 50 random walking paths.

- Green dots represent starting positions.
- Red dots represent ending positions.
- Lines represent the paths taken by the walkers.

## 9. Learning Outcomes

Through this project, I learned how to:

- Implement a 2D random walk using Python.
- Work with X and Y coordinates.
- Use nested loops to simulate multiple walkers.
- Generate random values using Python.
- Store movement history using lists.
- Visualize data using Matplotlib.

## 10. Conclusion

This project helped me understand random walks through practical programming. It improved my understanding of Python fundamentals, randomness, coordinate systems, loops, and data visualization.

The simulator can be extended in the future with obstacles, boundaries, animations, and statistical analysis of the walkers' movements.