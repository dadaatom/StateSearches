from util import PriorityQueue, find, contains

def uniformCostSearch(problem):
    opened = PriorityQueue()
    opened.push((problem.getStartState(), [], 0), 0)

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

                total = cost + s_cost

                index = find(opened, s_state)

                if index >= 0:
                    (_, _, old_cost) = opened.heap[index][2]
                    if total < old_cost:
                        opened.heap.pop(index)
                        temp = actions.copy()
                        temp.append(s_actions)

                        opened.push((s_state, temp, total), total)
                elif not contains(opened, s_state) and s_state not in closed:
                    temp = actions.copy()
                    temp.append(s_actions)

                    opened.push((s_state, temp, total), total)
    return []