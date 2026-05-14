# Development Log – The Torchbearer

**Student Name:** Seth Blanchard
**Student ID:** 131933669

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

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
A working implementation of Dijkstras in `run\_dijkstras()` has been finished and tested to work correctly.
This tests that it works for a normal graph and finds the shortest path.
It also tests for how it handles the edge cases of a cycle, diconnected graph, single node, empty graph, and None.

---

## Entry 3 – 5-13-2026: Initial Route Planning Steps Done

Part 2 and 3 are completed with a working implementation of the `precompute\_distances()` function which has been tested to work correctly.
This tests that it provides the correct distances for the two graphs used by Dijkstras tests with some small tweaks.

In addition, I corrected a problem in `run\_dijkstras()` where it didn't check if the source is None which could cause the program to crash.

---

## Entry 4 – 5-14-2026: README Done

Finished writing up all parts of the `README.md` file and copying the required parts into functions in `torchbearer.py`.
Also improved the formating of previous devlog entries after remembering about the code block format for markdown.

---

## Entry 5 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.15 |
| Part 2: Precomputation Design | 1.25 |
| Part 3: Algorithm Correctness | 0.15 |
| Part 4: Search Design | 0.15 |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | 7 |
| **Total** | |
