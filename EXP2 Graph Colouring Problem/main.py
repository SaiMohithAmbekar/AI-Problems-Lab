def vacc():
    # 0 for clean and 1 for dirty
    goal_state = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    cost = 0
    # Vacuum cleaner is the agent of this program
    # Getting agent's environment from user
    vacuum_pos = input("Enter location of vacuum(A/B/C/D): ")
    # Getting the status of environment from user
    for i in goal_state:
        goal_state[i] = int(input("Enter the status of " + i + "(0/1): "))

    print("**************")
    print("Vacuum is placed in Location " + vacuum_pos)

    # Checking the current room status
    if goal_state[vacuum_pos] == 1:
        pos = vacuum_pos
        print("Location " + vacuum_pos + " is Dirty.")
        goal_state[vacuum_pos] = 0
        cost += 1                # Cost For Cleaning
        print("Cost for Cleaning " + i + ":" + str(cost))
        print("Location " + pos + " is cleaned")
        print("__________")
    else:
        print("location " + vacuum_pos + " is already clean")
        print("__________")

    # reversing the dict for reducing the time complexity
    if vacuum_pos == 'C' or vacuum_pos == 'D':
        goal_state = dict(reversed(list(goal_state.items())))

    # Checking the status of other rooms
    for i in goal_state:
        # Excludes the current agent room
        if i == vacuum_pos:
            continue
        elif goal_state[i] == 1:
            print("Moving to the location " + i)
            cost += 1               # Cost For Moving
            print("cost for moving to " + i + ":" + str(cost))
            print("Location " + i + " is Dirty.")
            goal_state[i] = 0
            cost += 1               # Cost For Cleaning
            print("Cost for Cleaning " + i + ":" + str(cost))
            print("Location " + i + " is cleaned")
            print("__________")
        else:
            print("Moving to the location " + i)
            cost += 1               # Cost For Moving
            print("cost for moving to " + i + ":" + str(cost))
            print("location " + i + " is already clean")
            print("__________")

    if vacuum_pos == 'C' or vacuum_pos == 'D':
        goal_state = dict(reversed(list(goal_state.items())))

    # done cleaning
    print("Goal State: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))


vacc()
