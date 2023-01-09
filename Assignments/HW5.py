from heapq import heappop, heappush


START_STATE = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]
# START_STATE = [[1, 4, 2], [0, 3, 5], [6, 7, 8]]
# START_STATE = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
# START_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# START_STATE = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]
# START_STATE = [[13, 2, 10, 3], [1, 12, 8, 4], [5, 0, 9, 6], [15, 14, 11, 7]]
# START_STATE = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]
# START_STATE = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
# START_STATE = [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 11], [13, 14, 15, 12]]
# START_STATE = [[15, 2, 1, 12], [8, 5, 6, 11], [4, 9, 10, 7], [3, 14, 13, 0]]
# START_STATE = [[12,1,10,2],[7,0,4,14],[5,11,9,15],[8,13,6,3]]
# START_STATE = [[4,15,3,7],[5,14,10,6],[11,2,8,12],[9,13,0,1]]
# START_STATE = [[4,7,15,0],[1,14,10,12],[13,5,11,3],[9,6,8,2]]
# START_STATE = [[13,2,11,11],[4,0,9,8],[10,3,6,1],[5,15,14,7]]
# START_STATE = [[1,15,3,0],[6,8,2,4],[13,12,7,10],[5,9,11,14]]

# GOAL_STATE = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
# GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

GOAL_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# START_STATE = [[8, 1, 2], [0, 4, 3], [7, 6, 5]]


class State:
    def __init__(self, g_of_n, h_of_n, board, path=""):
        self.path = path
        self.board = board
        self.g_of_n = g_of_n
        self.h_of_n = h_of_n
        self.cost = h_of_n + g_of_n
        self.start = self.get_start()

    def get_start(self):
        return [(i, a.index(0)) for i, a in enumerate(self.board) if 0 in a][0]

    def __lt__(self, cmp):
        return self.cost < cmp.cost


class PuzzleGame:
    def __init__(self, board, goal_state, heuristic_function):
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.goal_state = goal_state
        self.heuristic_function = "self." + heuristic_function

    def goal_test(self, board):
        return board == self.goal_state

    def calculate_heuristic(self, **kwargs):
        return eval(self.heuristic_function + f"({kwargs})")

    def misplaced_heuristic(self, kwargs):
        board = kwargs["board"]
        cnt = 0
        for i in range(self.rows):
            for j in range(self.cols):
                cnt += self.goal_state[i][j] != board[i][j]

        return int(cnt)

    def manhattan_distance_heuristic(self, kwargs):
        positions = {}
        board = kwargs["board"]
        total_manhattan_distance = 0

        for i in range(self.rows):
            for j in range(self.cols):
                positions[self.goal_state[i][j]] = (i, j)

        for x in range(self.rows):
            for y in range(self.cols):
                x1, y1 = positions[board[x][y]]
                total_manhattan_distance += abs(x1 - x) + abs(y1 - y)

        return total_manhattan_distance

    def successor_fcn(self, level, current_position, board, previous_path):
        neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        possible_paths = []

        for x, y in neighbours:
            new_board = [row.copy() for row in board]
            new_x, new_y = x + current_position[0], y + current_position[1]

            if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                new_board[current_position[0]][current_position[1]
                                               ], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[current_position[0]][current_position[1]]
                selected_path = "D" if (x, y) == (1, 0) else "U" if (
                    x, y) == (-1, 0) else "L" if (x, y) == (0, -1) else "R"

                possible_paths.append(State(level + 1, self.calculate_heuristic(
                    board=new_board), new_board, previous_path + selected_path))

        return possible_paths

    def solvability(self):
        '''
        We can check the solvability of a puzzle 
        by using Counting Inversions concept. A Inversion is basically counting the no
        of numbers that are greater than the current number after current number index in the puzzle 

        The idea is if the goal state in the puzzle contains the even inversions count. then any
        start state with even inversions can be solved and the same for odd inversion count.
        Because, in a puzzle when you slide the tile by right or left then there will be no change in the
        inversions count of the state but when you slide the up or down tile, we can find inversion count
        varies by +2/-2 which is still even. so by this we can conclude that inversion caount can varies by
        even number. So, if the goal state is having a even inversions then any start state with even inversions
        can be solvable and the same applicable for odd inversion count
        '''
        start_state = self.board
        end_state = self.goal_state
        start_state = [int(j) for i in start_state for j in i]
        end_state = [int(j) for i in end_state for j in i]

        start_state_inversion_count = 0
        end_state_inversion_count = 0

        for i in range(len(start_state)):
            for j in range(i + 1, len(start_state)):
                if start_state[i] != 0 and start_state[j] != 0 and start_state[i] > start_state[j]:
                    start_state_inversion_count += 1

        for i in range(len(end_state)):
            for j in range(i + 1, len(end_state)):
                if end_state[i] != 0 and end_state[j] != 0 and  end_state[i] > end_state[j]:
                    end_state_inversion_count += 1

        return start_state_inversion_count % 2 == end_state_inversion_count % 2

    def solve(self):
        fringe = [State(0, self.calculate_heuristic(
            board=self.board), self.board, "")]
        closed = set()
        closed = list()
        cnt = 0

        while fringe:

            state_obj = heappop(fringe)
            # print(len(fringe), state_obj.start)

            # print("------------------------")
            # for i in state_obj.board:
            #     print(*i)
            # print("cost {} backward {} forward {}".format(
            #     state_obj.cost, state_obj.g_of_n, state_obj.h_of_n))
            # print("------------------------")

            if self.goal_test(state_obj.board):
                print(state_obj.path)
                print(cnt)
                return state_obj.path

            cnt += 1
            if state_obj.board in closed:
                continue

            closed.append([i.copy() for i in state_obj.board])

            a = self.successor_fcn(
                state_obj.g_of_n, state_obj.start, state_obj.board, state_obj.path)
            for i in a:
                heappush(fringe, i)


def get_start_position(board):
    return [(i, a.index(0)) for i, a in enumerate(board) if 0 in a][0]


def main(user_input):

    game_grid = START_STATE
    goal_state = GOAL_STATE

    if user_input == "1":
        heuristic_function = "misplaced_heuristic"
    elif user_input == "2":
        heuristic_function = "manhattan_distance_heuristic"

    puzzle_game_obj = PuzzleGame(
        board=game_grid, goal_state=goal_state, heuristic_function=heuristic_function)


    puzzle_game_obj.solve()

    # *****
    # for checking solvability please uncomment the below code and comment the above line
    # *****
    
    # if puzzle_game_obj.solvability():
    #     puzzle_game_obj.solve()
    # else:
    #     print('Puzzle Not Solvable!!')


if __name__ == "__main__":
    user_input = input(
        "Please Select the Heuristic function \n 1. Number of the misplaced tiles \n 2. Danhattan distance \n Please enter your choice: ")
    if user_input.lower() in ["1", "2"]:
        main(user_input)
    else:
        print("Please try again with valid input")
