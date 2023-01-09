from heapq import heappush, heappop


class State:
    def __init__(self, end, g_of_n, path, current):
        self.current = current
        self.end = end
        self.path = path
        self.g_of_n = g_of_n
        self.h_of_n = self.calculate_heuristic(current)
        self.cost = g_of_n + self.h_of_n

    def goal_state(self, word):
        return word == self.end

    def calculate_heuristic(self, start):
        i, j = 0, 0
        n, m = len(start), len(self.end)
        cnt = 0

        while i < n and j < m:
            if start[i] != self.end[j]:
                cnt += 1

            i += 1
            j += 1

        return cnt + (n - i) + (m - j)

    def __lt__(self, other):
        return self.cost < other.cost


def is_successor(start, end):
    i, j = 0, 0
    n, m = len(start), len(end)
    cnt = 0

    while i < n and j < m:
        if start[i] != end[j]:
            cnt += 1

        i += 1
        j += 1

    cnt += (n - i) + (m - j)

    return cnt == 1


def successor_fcn(words, start):
    successors = []

    for word in words:
        if word != start and is_successor(start, word):
            successors.append(word)

    return successors


def A_star(words, start, end):
    words = set(words)

    fringe = [State(end, 0, [], start)]
    visited = list()

    while fringe:
        state_obj = heappop(fringe)

        new_start = state_obj.current
        # print(state_obj.current, state_obj.g_of_n, state_obj.cost, state_obj.h_of_n, *state_obj.path)

        if state_obj.goal_state(new_start):
            # print("A*", state_obj.cost)
            return " --> ".join(state_obj.path + [state_obj.end])

        if new_start in visited:
            continue

        visited.append(new_start)

        for succesor in successor_fcn(words, new_start):
            # print(new_start, succesor)
            heappush(fringe, State(end, state_obj.g_of_n + 1,
                     state_obj.path + [new_start], succesor))

    return "Not Possible!!"


if __name__ == "__main__":

    dictionary = ["try", "toy", "cop", "cup", "coy", "fry", "cry", "bay", "lay", "boy", "bow", "fey"]

    start = "boy"
    end = "cup"

    answer = A_star(dictionary, start, end)
    print(answer)
