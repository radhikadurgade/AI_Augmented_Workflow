# SLE-3: Architectural Design using C4 Model
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM136  
**Name:** Radhika Vijay Durgade  
**Institution:** DKTE's Textile and Engineering Institute  

---

## 📌 Project Overview
This project presents the architectural design and implementation of a **Graph Search System** using the **C4 Architectural Model**. The system executes Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms to find traversal paths between nodes in a graph and provides performance profiling (execution time and memory usage).

---

## 🏗️ C4 Model Architecture
The architecture is structured into three progressive C4 abstraction levels:

1. **Level 1: System Context Diagram (`Level1_Context.png.png`)**
   - Illustrates the high-level interaction between the **User** and the **Graph Search System**.
   - **Inputs:** Graph structure, Start Node, Goal Node, Algorithm Choice (BFS/DFS).
   - **Outputs:** Search Path, Traversal Results, and Performance Metrics.

2. **Level 2: Container Diagram (`Level2_Container.png.png`)**
   - Breaks down the system into core functional containers[cite: 2]:
     - **Input Module:** Parses user inputs[cite: 2].
     - **BFS & DFS Search Modules:** Core traversal logic[cite: 2].
     - **Visited / Search Memory:** Tracks state history[cite: 2].
     - **Performance Profiling Module:** Measures runtime & space complexity[cite: 2].
     - **Output Module:** Displays search path and benchmarks[cite: 2].

3. **Level 3: Component Diagram (`Level3_Component.png.png`)**
   - Zoomed-in view of the **BFS Search Module** components[cite: 3]:
     - **Search Controller:** Manages traversal flow[cite: 3].
     - **Queue:** FIFO structure for frontier expansion[cite: 3].
     - **Visited Set:** Prevents infinite loops/cycles[cite: 3].
     - **Goal Test:** Evaluates target node conditions[cite: 3].

---

## 📂 Repository Contents
| File Name | Description |
| :--- | :--- |
| `agent.py` / `profiling.py` | Python implementation of BFS, DFS, and Performance Profiling |
| `SLE3_25UAM136_RadhikaDurgade.docx` | Final SLE-3 Architecture & Verification Report |
| `Level1_Context.png.png` | C4 Level 1 - System Context Diagram |
| `Level2_Container.png.png` | C4 Level 2 - Container Diagram[cite: 2] |
| `Level3_Component.png.png` | C4 Level 3 - Component Diagram[cite: 3] |

---

## 🚀 How to Run the Code
1. Clone the repository:
   ```bash
   git clone [https://github.com/radhikadurgade/AI_Augmented_Workflow.git](https://github.com/radhikadurgade/AI_Augmented_Workflow.git)
