# Development Log – The Torchbearer

**Student Name:** Seth Blanchard
**Student ID:** 131933669

---

## Entry 1 – 5-7-2026: Initial Plan

To tackle this problem, I plan to start with part 1 and 2 of the assignment.
Starting with the simple function for selecting sources then moving onto getting the
dijkstras algorithm working and creating a test case to ensure it functions correctly.
After that moving onto the precomputing distances function and then creating its test
case. With the simpler parts out of the way it will be easier to tackle finding the
optimal route that includes all relic chambers.

---

## Entry 2 – 5-11-2026: Working Dijkstras Algorithm

Part 1 is filled out, and Part 2 is done up to the dijkstras algorithm.
A working implementation of Dijkstras in `run_dijkstras()` has been finished and tested to work correctly.
This tests that it works for a normal graph and finds the shortest path.
It also tests for how it handles the edge cases of a cycle, diconnected graph, single node, empty graph, and None.

---

## Entry 3 – 5-13-2026: Initial Route Planning Steps Done

Part 2 and 3 are completed with a working implementation of the `precompute_distances()` function which has been tested to work correctly.
This tests that it provides the correct distances for the two graphs used by Dijkstras tests with some small tweaks.

In addition, I corrected a problem in `run_dijkstras()` where it didn't check if the source is None which could cause the program to crash.

---

## Entry 4 – 5-14-2026: README Done

Finished writing up all parts of the `README.md` file and copying the required parts into functions in `torchbearer.py`.
Also improved the formating of previous devlog entries after remembering about the code block format for markdown.

---

## Entry 5 – 5-14-2026: Post-Implementation Reflection

The implementation has been compleeted and works for the given test cases.
Looking at this one thing that I would improve upon if I had more time is the pruning.
I did think of some better ways but couldn't think of how to make them work without modifying the function signatures.

The initial improvement is to find the minimum edge weight in the graph at the start and multiply that by the number of remaining nodes.
This would more closely follow and adapt to having more nodes left instead of just being a straight shot to the end however, if that minimum is very small due to one node that would reduce its effectiveness.

The next improvement I though of building on this was to find the minimum edge weight of each node in the graph excluding connections to the start and end nodes.
This would then be stored in a python dictionary to quickly lookup these values.
From this I could add the minimum edge weight of each of the remaining nodes and find which of these nodes has the shortest distance to the end node.
Adding all of these together would give the minimum remaining path length possible if all of these minimum connections happend to make one path from the current node to the end.
If that minimum remaining path length plus the current path length was longer than the best path length so far than I could safely prune that branch.

---

## Final Entry – 5-14-2026: Time Estimate

> Note: Part 1 to 6 only includes the time spent on `torchbearer.py`, and part 7 seems redundant and is thus left as 0. With all other time spent going under README and DEVLOG writing.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.15 |
| Part 2: Precomputation Design | 1.25 |
| Part 3: Algorithm Correctness | 0.15 |
| Part 4: Search Design | 0.15 |
| Part 5: State and Search Space | 1 |
| Part 6: Pruning | 0.15 |
| Part 7: Implementation | 0 |
| README and DEVLOG writing | 7.5 |
| **Total** | 10.35 |
