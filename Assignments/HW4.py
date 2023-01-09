from heapq import *
import os
import traceback


FAILURE_MESSAGE = "Not Possible!!"
DEBUG_FILENAME_UCS_TREE = "output_ucs_tree.txt"
DEBUG_FILENAME_UCS_GRAPH = "output_ucs_graph.txt"


WALL = -1
LAKE = 6
RIVER = 3
ISLAND = 1


class UniformCostSearchTree:
    def __init__(self, start_position, end_point, grid=[], debug_allowed=False, failure_message=FAILURE_MESSAGE, debug_filename=DEBUG_FILENAME_UCS_TREE):
        self.start_position = start_position
        self.end_point = end_point
        self.debug_allowed = debug_allowed
        self.grid = grid
        self.failure_message = failure_message
        self.debug_filename = debug_filename
        self.visited = set()
        # Using list for debugging, since this keeps track of sequence of visited nodes
        self.visited = []

        print("\n" + "**"*10 + " Uniform Cost Search Tree Mode " + "**"*10 + "\n")

        result = self.search()

        if result != FAILURE_MESSAGE:
            path, cost = result[0]
            print("Cheapest plan for robot to reach the destination is: ", path)
            print("Cost for robot to reach the destination is: ", cost)
            print("Total Visited nodes are: ", len(self.visited))
            # print(result)
            # print(self.visited)
        else:
            print('failure')

    def goal_test(self, current_loc):
        '''
        This function checks for the goal state
        '''
        return current_loc == self.end_point

    def successor_fcn(self, current_position, previous_path, cost):
        '''
        This function returns all the possible valid paths of the robot from the given position
        '''
        n, m = len(self.grid), len(self.grid[0])
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible_paths = []

        for x, y in neighbours:
            boundary_checks = 0 <= x + \
                current_position[0] < n and 0 <= y + current_position[1] < m

            if not boundary_checks:
                continue

            # if the present cell is having a wall, skip
            if self.grid[x + current_position[0]][y + current_position[1]] == WALL:
                continue

            # figure out the direction in which the robot has moved
            current_path = "D" if (x, y) == (1, 0) else "U" if (
                x, y) == (-1, 0) else "L" if (x, y) == (0, -1) else "R"

            # updating the robot possible positions from the given cell
            possible_paths.append(
                (cost + self.grid[x + current_position[0]][y + current_position[1]], (x + current_position[0], y + current_position[1]), previous_path + current_path))

        return possible_paths

    def check_edge_cases(self):

        if self.start_position == self.end_point:
            print('Start Point and End Point cannot be same!!')
            return self.failure_message

        n, m = len(self.grid), len(self.grid[0])

        if 0 > self.start_position[0] or self.start_position[0] >= n or 0 > self.start_position[1] or self.start_position[1] >= n:
            print("Invalid Start Point")
            return self.failure_message

        if 0 > self.end_point[0] or self.end_point[0] >= m or 0 > self.end_point[1] or self.end_point[1] >= m:
            print("Invalid End Point")
            return self.failure_message

        if os.path.exists(DEBUG_FILENAME_UCS_TREE):
            os.remove(DEBUG_FILENAME_UCS_TREE)

        return False

    def search(self):
        try:
            corner_cases = self.check_edge_cases()

            if corner_cases == self.failure_message:
                return corner_cases

            fringe = [[0, self.start_position, ""]]
            heapify(fringe)

            possible_paths = []

            while True:

                if not len(fringe):
                    return FAILURE_MESSAGE if not len(possible_paths) else possible_paths

                if self.debug_allowed:
                    with open(DEBUG_FILENAME_UCS_TREE, 'a') as f:
                        for i in fringe:
                            f.write(str(i) + ", ")
                        f.write('\n')

                cost, present_position, path = heappop(fringe)

                if self.goal_test(present_position):
                    possible_paths.append((path, cost))
                    return possible_paths

                self.visited.append(present_position)
                # getting all the valid possible paths for the current location
                ret = self.successor_fcn(present_position, path, cost)

                # updating the fringe
                for i in ret:
                    heappush(fringe, i)

        except Exception as e:
            traceback.print_exc()
            return self.failure_message


class UniformCostSearchGraph:
    def __init__(self, start_position, end_point, grid=[], debug_allowed=False, failure_message=FAILURE_MESSAGE, debug_filename=DEBUG_FILENAME_UCS_GRAPH):
        self.start_position = start_position
        self.end_point = end_point
        self.debug_allowed = debug_allowed
        self.grid = grid
        self.failure_message = failure_message
        self.debug_filename = debug_filename
        self.visited = set()
        # Using list for debugging, since this keeps track of sequence of visited nodes
        self.visited = []

        print("\n" + "**"*10 + " Uniform Cost Search Graoh Mode " + "**"*10 + "\n")

        result = self.search()

        if result != FAILURE_MESSAGE:
            path, cost = result[0]
            print("Cheapest plan for robot to reach the destination is: ", path)
            print("Cost for robot to reach the destination is: ", cost)
            print("Total Visited nodes are: ", len(self.visited))
            # print(result)
            # print(self.visited)
        else:
            print('failure')

    def goal_test(self, current_loc):
        '''
        This function checks for the goal state
        '''
        return current_loc == self.end_point

    def successor_fcn(self, current_position, previous_path, cost):
        '''
        This function returns all the possible valid paths of the robot from the given position
        '''
        n, m = len(self.grid), len(self.grid[0])
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible_paths = []

        for x, y in neighbours:

            x_, y_ = x + current_position[0], y + current_position[1]
            boundary_checks = 0 <= x_ < n and 0 <= y_ < m

            if not boundary_checks:
                continue

            # if the present cell is having a wall, skip
            if self.grid[x_][y_] == WALL:
                continue

            # figure out the direction in which the robot has moved
            current_path = "D" if (x, y) == (1, 0) else "U" if (
                x, y) == (-1, 0) else "L" if (x, y) == (0, -1) else "R"

            # updating the robot possible positions from the given cell
            possible_paths.append(
                (cost + self.grid[x_][y_], (x_, y_), previous_path + current_path))

        return possible_paths

    def check_edge_cases(self):

        if self.start_position == self.end_point:
            print('Start Point and End Point cannot be same!!')
            return self.failure_message

        n, m = len(self.grid), len(self.grid[0])

        if 0 > self.start_position[0] or self.start_position[0] >= n or 0 > self.start_position[1] or self.start_position[1] >= n:
            print("Invalid Start Point")
            return self.failure_message

        if 0 > self.end_point[0] or self.end_point[0] >= m or 0 > self.end_point[1] or self.end_point[1] >= m:
            print("Invalid End Point")
            return self.failure_message

        if os.path.exists(DEBUG_FILENAME_UCS_GRAPH):
            os.remove(DEBUG_FILENAME_UCS_GRAPH)

        return False

    def search(self):
        try:

            corner_cases = self.check_edge_cases()

            if corner_cases == self.failure_message:
                return corner_cases

            fringe = [[0, self.start_position, ""]]
            heapify(fringe)

            possible_paths = []

            while True:

                if not len(fringe):
                    return FAILURE_MESSAGE if not len(possible_paths) else possible_paths

                if self.debug_allowed:
                    with open(DEBUG_FILENAME_UCS_GRAPH, 'a') as f:
                        for i in fringe:
                            f.write(str(i) + ", ")
                        f.write('\n')

                cost, present_position, path = heappop(fringe)

                if self.goal_test(present_position):
                    possible_paths.append((path, cost))
                    return possible_paths

                if present_position in self.visited:
                    continue

                self.visited.append(present_position)
                # getting all the valid possible paths for the current location
                ret = self.successor_fcn(present_position, path, cost)

                # updating the fringe
                for i in ret:
                    heappush(fringe, i)

        except Exception as e:
            traceback.print_exc()
            return self.failure_message


def extract_plan(start_position, end_position):

    grid = [
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
        [WALL, 0, LAKE, LAKE, LAKE, LAKE, LAKE, RIVER, RIVER, RIVER, RIVER, ISLAND, WALL],
        [WALL, RIVER, RIVER, LAKE, ISLAND, LAKE, ISLAND, RIVER, RIVER, RIVER, WALL, LAKE, WALL],
        [WALL, ISLAND, ISLAND, ISLAND, ISLAND, LAKE, ISLAND, ISLAND, ISLAND, ISLAND, WALL, LAKE, WALL],
        [WALL, WALL, WALL, WALL, WALL, LAKE, ISLAND, ISLAND, ISLAND, ISLAND, LAKE, LAKE, WALL],
        [WALL, ISLAND, ISLAND, ISLAND, ISLAND, LAKE, ISLAND, LAKE, WALL, ISLAND, WALL, RIVER, WALL],
        [WALL, ISLAND, ISLAND, LAKE, LAKE, WALL, WALL, WALL, ISLAND, ISLAND, WALL, RIVER, WALL],
        [WALL, ISLAND, ISLAND, LAKE, LAKE, LAKE, 0, ISLAND, RIVER, ISLAND, WALL, RIVER, WALL],
        [WALL, ISLAND, ISLAND, ISLAND, ISLAND, ISLAND, RIVER, RIVER, RIVER, RIVER, WALL, RIVER, WALL],
        [WALL, LAKE, ISLAND, ISLAND, ISLAND, ISLAND, RIVER, RIVER, RIVER, RIVER, RIVER, RIVER, WALL],
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
    ]

    UniformCostSearchGraph(start_position, end_position,
                           grid, debug_allowed=False)

    UniformCostSearchTree(start_position, end_position,
                          grid, debug_allowed=False)


if __name__ == "__main__":

    start_position = (1, 1)
    end_position = (7, 6)

    extract_plan(start_position, end_position)
