class State:
    def __init__(self, score, lst):
        self.score = score
        self.lst = lst

    def __repr__(self):
        return f"{self.lst} --> {self.score}"


def successors(state, is_min_player=False):
    directions = ["Left", "Right"]
    successors_states = []

    for direction in directions:
        if direction.lower() == "left":
            score = state.score + state.lst[0] if not is_min_player else state.score - state.lst[0]
            new_state_obj = State(score, state.lst[1:])
        elif direction.lower() == "right":
            score = state.score + state.lst[-1] if not is_min_player else state.score - state.lst[-1]
            new_state_obj = State(score, state.lst[:-1])

        successors_states.append((direction, new_state_obj))

    return successors_states


def terminal(state):
    return len(state.lst) == 0


def utility_score(state):
    return state


def max_player(state):
    if terminal(state):
        return utility_score(state)

    v = float('-inf')
    for a, s in successors(state):
        v = max(v, min_player(s).score)

    state.score = v
    # print(state.lst, state.score)
    return state


def min_player(state):
    if terminal(state):
        return utility_score(state)

    v = float('inf')
    for a, s in successors(state, is_min_player=True):
        v = min(v, max_player(s).score)

    state.score = v
    # print(state.lst, state.score)
    return state


l = [1, 2, 5, 2]
state_obj = State(0, l)
max_player(state_obj)

print(state_obj.score > 0)