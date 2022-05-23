def breadthFirstSearch(problem):
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
                if successor[0] not in opened and successor[0] not in closed:
                    temp = actions.copy()
                    temp.append(successor[1])

                    paths.insert(0,temp)
                    opened.insert(0,successor[0])
    return []