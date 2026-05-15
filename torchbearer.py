"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Seth Blanchard
Student ID:   131933669

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
    """

    explination = """
- **Why a single shortest-path run from S is not enough:**
    - The solution requires that the path include certian nodes (relic chambers) and the shortest path from the start to the exit doesn't necessarily include these nodes.

- **What decision remains after all inter-location costs are known:**
    - After all costs between the important nodes (relic chambers and start) are known, it is a matter of chosing the path between these nodes that produces the shortest path.

- **Why this requires a search over orders (one sentence):**
    - The cost of the path depends on the entire ordering of the nodes, thus local choices can lead to suboptimal paths requiring checking multiple different orderings to find the best path.
    """

    return explination


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.
    """

    # Create the list and add the spawn
    source_nodes = []
    source_nodes.append(spawn)

    # Add all relics to the search_nodes
    for node in relics:
        source_nodes.append(node)

    # Return the nodes to search
    return source_nodes


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').
    """

    heap = []
    finalized_nodes = []
    min_distances = {}

    # Test input is valid
    if (graph is None or source is None or len(graph) == 0):
        return min_distances

    # Initialize min distances to inf for all nodes in the graph
    for node in graph:
        min_distances[node] = float('inf')

    # Add the start node to solution
    min_distances[source] = float(0)
    heapq.heappush(heap, (0, source))

    # While there are remaining nodes to add keep iterating
    while heap:
        # Pop from the heap
        curr_dist, curr_node = heapq.heappop(heap)

        # Check if node is already finalized
        if curr_node in finalized_nodes:
            continue

        # Finalize the node
        finalized_nodes.append(curr_node)

        # Check adjacent nodes
        for next_node, dist in graph[curr_node]:
            # Check if current path is longer than min 
            if curr_dist + dist >= min_distances[next_node]:
                continue

            # Add this node to heap and min
            heapq.heappush(heap, (curr_dist + dist, next_node))
            min_distances[next_node] = float(curr_dist + dist)

    return min_distances


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.
    """

    dist_table = {}

    # Check input is valid
    if (graph is None or spawn is None or relics is None or exit_node is None or len(graph) == 0):
        return dist_table

    # Select the sources
    source_nodes = select_sources(spawn, relics, exit_node)

    # Run Dijkstras from each source
    for source in source_nodes:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.
    """
    explination = """
Part 3a: What the Invariant Means
- **For nodes already finalized (in S):**
    - The current distance to a given node v in S is the distance of the shortest path from the source to v.

- **For nodes not yet finalized (not in S):**
    - The current distance to a given node u not in S is the distance of the shortest path using only nodes in S from the source to u.


Part 3b: Why Each Phase Holds
- **Initialization : why the invariant holds before iteration 1:**
    - At the start, no nodes are in S and the only node that can be reached without going through any nodes is the source.
    - The current distance to the source from the source is 0, and since S is empty no other node can be reached and has an infinite distance from the source.

- **Maintenance : why finalizing the min-dist node is always correct:**
    - Taking a node w not in S that has the smallest current distance of all u, any path to w that is shorter than the current distance must take a path through nodes not in S.
    - Since all edge weights are nonnegative such a path can't be shorter than the current distance to w.

- **Termination : what the invariant guarantees when the algorithm ends:**
    - At the end, all nodes in the graph that can be reached are in S.
    - Thus for the nodes that could be reached from the source the current distance is the distance of the shortest path to that node, while nodes that couldn't be reached are an infinite distance away.


Part 3c: Why This Matters for the Route Planner
With the correct shortest distance torchbearer can make correct decisions about which path to take without waisting fuel on longer paths or ending up at a dead end.
    """
    return explination


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.
    """
    explination = """
Why Greedy Fails
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

What the Algorithm Must Explore
- The algorithm must explore the different orderings of the nodes to find the order with the shortest path length
    """
    return explination


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    relics_remaining = {}
    best = [float('inf'), []]

    # Initialize the relics_remaining
    for node in relics:
        relics_remaining[node] = True

    # Explore from the spawn
    _explore(dist_table, spawn, relics_remaining, [], 0, exit_node, best)

    return best


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : dict[node, bool]
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.
    """
    # Base case
    if len(relics_remaining) == len(relics_visited_order):
        # Add the distance to the exit node and check how it matches
        cost_so_far += dist_table[current_loc][exit_node]

        # Check if this path is better than the best so far
        if (best[0] > cost_so_far):
            best[0] = cost_so_far
            best[1] = relics_visited_order.copy()

        # Backtrack the added distance and return to the previous level
        cost_so_far -= dist_table[current_loc][exit_node]
        return


    # Pruning Check
    # Checks if the shortest path from this node to the exit node added to the current path is longer than the current best path.
    # Since any path from this node through the remaining relic nodes will be at least this long it is safe prune this branch if true.
    if (best[0] < cost_so_far + dist_table[current_loc][exit_node]):
        return

    # Explore the remaining nodes
    for node in relics_remaining:
        # Check if the node has been used in the solution already
        if not relics_remaining[node]:
            continue
        
        # Add this node to the current solution
        relics_remaining[node] = False
        relics_visited_order.append(node)
        cost_so_far += dist_table[current_loc][node]

        # Do the recursive exploration
        _explore(dist_table, node, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)

        # Backtrack
        relics_remaining[node] = True
        relics_visited_order.pop()
        cost_so_far -= dist_table[current_loc][node]

    # All paths from this node are done exploring
    return



# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    # Create the distance table
    dist_table = precompute_distances(graph, spawn, relics, exit_node)

    # Run the backtracking to find the optimal route
    best_route = find_optimal_route(dist_table, spawn, relics, exit_node)

    return best_route


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")

def run_dijkstra_tests():
    # Test 1: Simple graph
    # Check that it works in the normal case
    graph_1 = {
        'A': [('B', 1), ('C', 6)],
        'B': [('C', 4), ('D', 2)],
        'C': [],
        'D': [('C', 1)]
    }

    solution_1 = {
        'A': float(0),
        'B': float(1),
        'C': float(4),
        'D': float(3)
    }

    min_distances = run_dijkstra(graph_1, 'A')
    assert min_distances == solution_1, f"Test 1 FAILED: expected {solution_1}, got {min_distances}"

    # Test 2: Cycle and disconnected graph
    # Check if it handles cycles and disconnected graphs
    graph_2 = {
        'A': [('B', 1)],
        'B': [('C', 2)],
        'C': [('A', 3)],
        'D': [('C', 1)]
    }

    solution_2a = {
        'A': float(0),
        'B': float(1),
        'C': float(3),
        'D': float('inf')
    }

    solution_2b = {
        'A': float(4),
        'B': float(5),
        'C': float(1),
        'D': float(0)
    }
    
    min_distances = run_dijkstra(graph_2, 'A')
    assert min_distances == solution_2a, f"Test 2a FAILED: expected {solution_2a}, got {min_distances}"

    min_distances = run_dijkstra(graph_2, 'D')
    assert min_distances == solution_2b, f"Test 2b FAILED: expected {solution_2b}, got {min_distances}"

    # Test 3: Single node
    # Check if it correctly handles a single node
    graph_3 = {
        'A': []
    }

    solution_3 = {
        'A': float(0)
    }

    min_distances = run_dijkstra(graph_3, 'A')
    assert min_distances == solution_3, f"Test 3 FAILED: expected {solution_3}, got {min_distances}"

    # Test 4: Empty graph
    # Check that it doesn't crash when given an empty graph and that it returns an empty dictionary
    graph_4 = {}
    solution_4 = {}

    min_distances = run_dijkstra(graph_4, None)
    assert min_distances == solution_4, f"Test 4 FAILED: expected {solution_4}, got {min_distances}"

    # Test 5: None given
    # Check that it doesn't crash when given None and that it returns an empty dictionary
    min_distances = run_dijkstra(None, None)
    assert min_distances == solution_4, f"Test 5a FAILED: expected {solution_4}, got {min_distances}"

    min_distances = run_dijkstra(graph_1, None)
    assert min_distances == solution_4, f"Test 5b FAILED: expected {solution_4}, got {min_distances}"

    # All Tests were passed
    print("\nAll Dijkstra tests passed.")

def run_precompute_tests():
    # Test 1: Simple graph
    # Check that it works in the normal case
    graph_1 = {
        'A': [('B', 1), ('C', 6)],
        'B': [('C', 4), ('D', 2)],
        'C': [],
        'D': [('A', 1), ('C', 1)]
    }

    solution_1a = {
        'A': float(0),
        'B': float(1),
        'C': float(4),
        'D': float(3)
    }

    solution_1b = {
        'A': float(1),
        'B': float(2),
        'C': float(1),
        'D': float(0)
    }

    solution_1 = {}
    solution_1['A'] = solution_1a
    solution_1['D'] = solution_1b

    dist_table = precompute_distances(graph_1, 'A', ['D'], 'C')
    assert dist_table == solution_1, f"Test 1 FAILED: expected {solution_1}, got {dist_table}"

    # Test 2: Cycle and disconnected graph
    # Check to see that it runs the two test cases for cycle and diconnected graph from the singular function
    graph_2 = {
        'A': [('B', 1)],
        'B': [('C', 2)],
        'C': [('A', 3)],
        'D': [('C', 1)]
    }

    solution_2a = {
        'A': float(0),
        'B': float(1),
        'C': float(3),
        'D': float('inf')
    }

    solution_2b = {
        'A': float(4),
        'B': float(5),
        'C': float(1),
        'D': float(0)
    }

    solution_2 = {}
    solution_2['A'] = solution_2a

    dist_table = precompute_distances(graph_2, 'A', [], 'C')
    assert dist_table == solution_2, f"Test 2a FAILED: expected {solution_2}, got {dist_table}"

    solution_2['D'] = solution_2b
    dist_table = precompute_distances(graph_2, 'A', ['D'], 'C')
    assert dist_table == solution_2, f"Test 2b FAILED: expected {solution_2}, got {dist_table}"

    # All Tests were passed
    print("\nAll Precompute tests passed.")



if __name__ == "__main__":
    #run_dijkstra_tests()
    #run_precompute_tests()
    _run_tests()
