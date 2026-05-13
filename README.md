# The Torchbearer

**Student Name:** Seth Blanchard
**Student ID:** 131933669
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

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

- **Number of Dijkstra runs:** |M| + 1
- **Cost per run:** O((|V| + |E|)log|V|)
- **Total complexity:** O(|M|) * O((|V| + |E|)log|V|) = O(|M| (|V| + |E|)log|V|)
- **Justification (one line):** The total time complexity is the time it takes to run dijkstras |M| + 1 times which is the multiple of both

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

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
