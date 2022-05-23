from util import PriorityQueue, find, contains, nullHeuristic

def aStarSearch(problem, heuristic=nullHeuristic):
    opened = PriorityQueue()
    opened.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))

    closed = []

    while not opened.isEmpty():
        state, actions, cost = opened.pop()

        if problem.isGoalState(state):
            return actions
        else:
            states = problem.getSuccessors(state)
            closed.append(state)

            for successor in states:

                s_state, s_actions, s_cost = successor

                g = cost + s_cost
                h = heuristic(s_state, problem)
                f = g + h

                index = find(opened, s_state)

                if index >= 0:
                    (_, _, old_cost) = opened.heap[index][2]
                    if g < old_cost:
                        opened.heap.pop(index)
                        temp = actions.copy()
                        temp.append(s_actions)

                        opened.push((s_state, temp, g), f)
                elif not contains(opened, s_state) and s_state not in closed:
                    temp = actions.copy()
                    temp.append(s_actions)

                    opened.push((s_state, temp, g), f)
    return []