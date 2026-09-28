# SLE-2: Profiling Report – BFS vs DFS

## Student Details

- Name: Radhika Vijay Durgade
- PRN: 25UAM136
- Division: B
- Course: 02AML204 – Introduction to Artificial Intelligence

## Project Title

BFS vs DFS Profiling – Empirical Performance Analysis

## Objective

The objective of this project is to compare the performance of Breadth First Search (BFS) and Depth First Search (DFS) using empirical performance analysis.

The algorithms are compared based on:
- Average execution time
- Number of nodes expanded

## Algorithms Used

### BFS – Breadth First Search

BFS explores the graph level by level using a queue.

### DFS – Depth First Search

DFS explores a path deeply before moving to another path using a stack.

## Graph Details

- Start Node: A
- Goal Node: Z
- Number of Runs: 10,000

Both BFS and DFS were executed on the same graph.

## Profiling Method

Python's `time.perf_counter()` was used to measure the execution time.

A manual node counter was used to count the number of nodes expanded by each algorithm.

## Results

| Algorithm | Average Time (ms) | Nodes Expanded |
|------------|-------------------|----------------|
| BFS        | 0.009288          | 26             |
| DFS        | 0.013311          | 23             |

## Observation

BFS recorded a lower average execution time, while DFS expanded fewer nodes in the tested graph.

The results depend on the graph structure and execution environment.

## Conclusion

The experiment helped compare BFS and DFS using actual performance measurements. BFS and DFS showed different execution times and numbers of expanded nodes on the same graph.

## Tools Used

- Python
- VS Code
- time.perf_counter()
- GitHub

## AI Contribution

ChatGPT was used to understand BFS and DFS concepts, prepare the profiling structure, and interpret the experimental results.