# The Torchbearer

**Student Name:** Seth Blanchard
**Student ID:** 131933669
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
    - The solution requires that the path include certian nodes (relic chambers) and the shortest path from the start to the exit doesn't necessarily include these nodes.

- **What decision remains after all inter-location costs are known:**
    - After all costs between the important nodes (relic chambers and start) are known, it is a matter of chosing the path between these nodes that produces the shortest path.

- **Why this requires a search over orders (one sentence):**
    - The cost of the path depends on the entire ordering of the nodes, thus local choices can lead to suboptimal paths requiring checking multiple different orderings to find the best path.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Entrance | Where the path must start from |
| Relic Chamber | Where the path must go to, and lead from |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Hash Map |
| What the keys represent | Nodes in the graph |
| What the values represent | Minimum cost to reach the node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | This is the time to calculate the hash before going directly to the value |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** k + 1
- **Cost per run:** O(m log(n))
- **Total complexity:** O(km log(n))
- **Justification (one line):** The total time complexity is the time it takes to run dijkstras k + 1 times which is the multiple of both

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
    - The current distance to a given node v in S is the distance of the shortest path from the source to v.

- **For nodes not yet finalized (not in S):**
    - The current distance to a given node u not in S is the distance of the shortest path using only nodes in S from the source to u.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
    - At the start, no nodes are in S and the only node that can be reached without going through any nodes is the source.
    - The current distance to the source from the source is 0, and since S is empty no other node can be reached and has an infinite distance from the source.

- **Maintenance : why finalizing the min-dist node is always correct:**
    - Taking a node w not in S that has the smallest current distance of all u, any path to w that is shorter than the current distance must take a path through nodes not in S.
    - Since all edge weights are nonnegative such a path can't be shorter than the current distance to w.

- **Termination : what the invariant guarantees when the algorithm ends:**
    - At the end, all nodes in the graph that can be reached are in S.
    - Thus for the nodes that could be reached from the source the current distance is the distance of the shortest path to that node, while nodes that couldn't be reached are an infinite distance away.

### Part 3c: Why This Matters for the Route Planner

With the correct shortest distance torchbearer can make correct decisions about which path to take without waisting fuel on longer paths or ending up at a dead end.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:**
    - This problem's structure has overlapping subproblems
- **Counter-example setup:**
    - S: (R1, 1), (R2, 2), (T, 5)
    - R1: (R2, 20), (T, 4)
    - R2: (R1, 3), (T, 5)
    - T:
- **What greedy picks:**
    - Picks lowest cost connection to unvisited nodes excluding T which is chosen last
    - Start at S, pick R1 which has the lowest cost
    - From R1 must pick R2
    - From R2 must pick T
    - Total Cost: 1 + 20 + 5 = 26
- **What optimal picks:**
    - S -> R2 -> R1 -> T
    - Total Cost: 2 + 3 + 4 = 9
- **Why greedy loses:**
    - Greedy lost because the choice of one node for the path prevents exploring other potential paths

### What the Algorithm Must Explore

- The algorithm must explore the different orderings of the nodes to find the order with the shortest path length

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current\_loc | node | The current node that is being explored |
| Relics already collected | relics\_visited\_order | list | Relics that have been collected in order |
| Fuel cost so far | cost\_so\_far | float | The cost of the fuel up to this location |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | Hash Map (node, bool) |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Hash Map provides quick lookup and change and this will be used often |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** k!
- **Why:** In the worst case all orderings must be considered which is the permutation of the k elements

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** Best distance so far
- **When it is used:** Distance to End Node + Current Path Length > Best So Far
- **What it allows the algorithm to skip:** Paths that can't produce a better distance than the best so far

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** Distance to end node
- **What the lower bound accounts for:** The minimum remaining distance would make the path longer than the best so far
- **Why it never overestimates:** The distance to the end is the minimum path from the current node to the end, and any path from this node will be at least that long

### Part 6c: Pruning Correctness

- Only if the best path from the current node to the end produces a longer path than the best path so far is the branch pruned
- Thus even if all remaining nodes are on this best path it would be imposible to make a better path than the current best and it is safe to prune this branch

---

## References

- Lecture Notes
