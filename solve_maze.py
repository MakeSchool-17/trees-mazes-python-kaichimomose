import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    # TODO: Implement solve_dfs
    # create a stack for backtracking
    stack = []
    # set current cell to 0
    current_cell = 0
    # set visited cells to 0
    visited_cell = 0

    # while current cell not goal
    while current_cell != m.total_cells - 1:
        # get unvisited neighbors using cell_neighbors
        unvisited_neighbors = m.cell_neighbors(current_cell)
        # if at least one neighbor
        if len(unvisited_neighbors) > 0:
            # choose random neighbor to be new cell
            new_cell_index = random.randint(0, len(unvisited_neighbors) - 1)
            new_cell, compass_index = unvisited_neighbors[new_cell_index]
            # visit new cell using visit_cell
            m.visit_cell(current_cell, new_cell, compass_index)
            # push current cell to stack
            stack.append(current_cell)
            # set current cell to new cell
            current_cell = new_cell
            # add 1 to visited cells
            visited_cell += 1
        # else
        else:
            # backtrack current cell using backtrack method
            m.backtrack(current_cell)
            # pop from stack to current cell
            current_cell = stack.pop()
        # call refresh_maze_view to update visualization
        m.refresh_maze_view()
    # set state to 'idle'
    m.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    # create a queue
    queue = []
    # set current cell to 0
    current_cell = 0
    # set in direction to 0b0000
    direction = 0b0000
    # set visited cells to 0
    visited_cell = 0
    # enqueue (current cell, in direction)
    queue.append((current_cell, direction))

    # while current cell not goal and queue not empty
    while current_cell != m.total_cells - 1 and queue != []:
        # dequeue to current cell, in direction
        current_cell, direction = queue.pop(0)
        # visit current cell with bfs_visit_cell
        m.bfs_visit_cell(current_cell, direction)
        # add 1 to visited cells
        visited_cell += 1
        # call refresh_maze_view to update visualization
        m.refresh_maze_view()
        # get unvisited neighbors of current cell using cell_neighbors, add to queue
        queue.extend(m.cell_neighbors(current_cell))
    # trace solution path and update cells with solution data using reconstruct_solution
    m.reconstruct_solution(current_cell)
    # set state to 'idle'
    m.state = 'idle'

def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='bfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
