def depthFirstSearch(problem):
    paths = [[]]

    opened = [problem.getStartState()]
    closed = []

    while len(opened) > 0:
        state = opened.pop()
        actions = paths.pop()

        if problem.isGoalState(state):
            return actions
        else:
            states = problem.getSuccessors(state)
            closed.append(state)

            for successor in states:
                if successor[0] not in closed:
                    temp = actions.copy()
                    temp.append(successor[1])

                    paths.append(temp)
                    opened.append(successor[0])
    return []