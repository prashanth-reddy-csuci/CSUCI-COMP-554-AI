from collections import deque
import os
import traceback


FAILURE_MESSAGE = "Not Possible!!"
DEBUG_FILENAME_BFS = "output_bfs.txt"
MAX_DEPTH = 10000


class BreadthFirstSearch:
    def __init__(self, start_point, end_point, grid=[], debug_allowed=False, failure_message=FAILURE_MESSAGE, debug_filename=DEBUG_FILENAME_BFS):
        self.start_point = start_point
        self.end_point = end_point
        self.debug_allowed = debug_allowed
        self.grid = grid
        self.failure_message = failure_message
        self.debug_filename = debug_filename

        print("\n" + "**"*10 + " Breadth First Search " + "**"*10 + "\n")

        result = self.search()

        if result != FAILURE_MESSAGE:
            print("Shortest plan for robot to reach the destination is: ", result)
            print("Cost for robot to reach the destination is: ", len(result))
        else:
            print('failure')

    def goal_test(self, current_loc):
        '''
        This function checks for the goal state
        '''
        return current_loc == self.end_point

    def successor_fcn(self, current_position, visited, previous_path):
        '''
        This function returns all the possible valid paths of the robot from the given position
        '''
        n, m = len(self.grid), len(self.grid[0])
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible_paths = []

        for x, y in neighbours:
            x_, y_ = x, y
            temp_visited = visited.copy()
            already_visited = False

            # move to the cells which does not hit the wall, outside of the grid and
            while 0 <= x_ + current_position[0] < n and 0 <= y_ + current_position[1] < m:

                # if we already visited the cell do not pass through because we end up in a infinte loop by travelling in the same way
                if (x_ + current_position[0], y_ + current_position[1]) in temp_visited:
                    already_visited = True
                    break

                # if the present cell is having a wall, move back
                if self.grid[x_ + current_position[0]][y_ + current_position[1]]:
                    x_ -= x
                    y_ -= y
                    break

                # update the visited cells
                temp_visited.add(
                    (x_ + current_position[0], y_ + current_position[1]))

                # move in the neighbours direction
                x_ += x
                y_ += y

            if 0 > x_ + current_position[0] or x_ + current_position[0] >= n or 0 > y_ + current_position[1] or y_ + current_position[1] >= m:
                x_ -= x
                y_ -= y

            if not already_visited and (x_ + current_position[0], y_ + current_position[1]) != current_position:

                # figure out the direction in which the robot has moved
                if (x, y) == (1, 0):
                    current_path = "D"
                elif (x, y) == (-1, 0):
                    current_path = "U"
                elif (x, y) == (0, -1):
                    current_path = "L"
                else:
                    current_path = "R"

                # updating the robot possible positions from the given cell
                possible_paths.append(
                    ((x_ + current_position[0], y_ + current_position[1]), temp_visited, previous_path + current_path))

        return possible_paths

    def search(self):
        try:

            if self.start_point == self.end_point:
                print('Start Point and End Point cannot be same!!')
                return self.failure_message

            n, m = len(self.grid), len(self.grid[0])

            if 0 > self.start_point[0] or self.start_point[0] >= n or 0 > self.start_point[1] or self.start_point[1] >= n:
                print("Invalid Start Point")
                return self.failure_message

            if 0 > self.end_point[0] or self.end_point[0] >= m or 0 > self.end_point[1] or self.end_point[1] >= m:
                print("Invalid End Point")
                return self.failure_message

            if self.grid[self.start_point[0]][self.start_point[1]]:
                print("Invalid Start Point")
                return self.failure_message

            if self.grid[self.end_point[0]][self.end_point[1]]:
                print("Invalid End Point")
                return self.failure_message

            if os.path.exists(DEBUG_FILENAME_BFS):
                os.remove(DEBUG_FILENAME_BFS)

            fringe = deque([[self.start_point, {self.start_point}, ""]])

            possible_paths = []

            while True:
                if not len(fringe):
                    return FAILURE_MESSAGE if not len(possible_paths) else possible_paths

                if self.debug_allowed:
                    with open(DEBUG_FILENAME_BFS, 'a') as f:
                        for i in fringe:
                            f.write(str(i) + ", ")
                        f.write('\n')

                if self.goal_test(fringe[0][0]):
                    possible_paths.append(fringe[0][2])

                    # comment the below line if you need to find out all the possible paths
                    return possible_paths[0]

                present_position, visited, path = fringe.popleft()

                # getting all the valid possible paths for the current location
                ret = self.successor_fcn(present_position, visited, path)

                # updating the fringe
                for i in ret:
                    fringe.append(i)

        except Exception as e:
            traceback.print_exc()
            return self.failure_message


def extract_plan(start_position, end_position):
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    BreadthFirstSearch(start_position, end_position,
                       grid)


if __name__ == "__main__":

    start_position = (2, 7)
    end_position = (7, 7)

    extract_plan(start_position, end_position)
