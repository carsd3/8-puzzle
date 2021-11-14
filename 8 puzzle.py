import copy as c
puzzle = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]

goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

def h(t):
#Function that defines the heuristic value of a state (regarding the number of misplaced numbers)
    h = 0
    for i in range(len(t)):
        for j in range(len(t[0])):    
            if t[i][j] == 0:
                continue
            if t[i][j] != i*3+j:
                h+=1
    return h

#A* with heuristic algorithm
sequence = []
#Find where the empty space is ubicated on the puzzle
for i in range(len(puzzle)):
    if 0 in puzzle[i]:
        ind = i
        break

#Initialize the necesary variables for the algorithm
empty_pos = [ind, puzzle[ind].index(0)]
sol = puzzle.copy()
it = 0
he = h(puzzle)

#The fringe is represented by two lists
fringe_val = [he] #This lists contains the values of f(x) of each state 
fringe = [(sol, sequence)] #This list contains a tuple with each state and the sequence of movements until that state
visited = [] #This list contains the states that has been already been visited

#Loop where the algorithm A* with heuristic value takes place
while sol != goal and it < 10000:
    #Calculate the next movements from the actual state
    left = []
    right = []
    up = []
    down = []
    #Left
    if empty_pos[1] != 0:
        left = c.deepcopy(sol)
        left_pos = empty_pos.copy()
        left_pos[1] -= 1
        t = left[left_pos[0]][left_pos[1]]
        left[left_pos[0]][left_pos[1]] = 0
        left[empty_pos[0]][empty_pos[1]] = t
        if left not in visited:
            fringe.append((left, sequence + ["L"]))
            fringe_val.append(h(left) + len(sequence)+1)

    #Right
    if empty_pos[1] != 2:
        right = c.deepcopy(sol)
        right_pos = empty_pos.copy()
        right_pos[1] += 1
        t = right[right_pos[0]][right_pos[1]]
        right[right_pos[0]][right_pos[1]] = 0
        right[empty_pos[0]][empty_pos[1]] = t
        if right not in visited:
            fringe.append((right, sequence + ["R"]))
            fringe_val.append(h(right) + len(sequence)+1)
        
    #Up
    if empty_pos[0] != 0:
        up = c.deepcopy(sol)
        up_pos = empty_pos.copy()
        up_pos[0] -= 1
        t = up[up_pos[0]][up_pos[1]]
        up[up_pos[0]][up_pos[1]] = 0
        up[empty_pos[0]][empty_pos[1]] = t
        if up not in visited:
            fringe.append((up, sequence + ["U"]))
            fringe_val.append(h(up) + len(sequence)+1)
        
    #Down
    if empty_pos[0] != 2:
        down = c.deepcopy(sol)
        down_pos = empty_pos.copy()
        down_pos[0] += 1
        t = down[down_pos[0]][down_pos[1]]
        down[down_pos[0]][down_pos[1]] = 0
        down[empty_pos[0]][empty_pos[1]] = t
        if down not in visited:
            fringe.append((down, sequence + ["D"]))
            fringe_val.append(h(down) + len(sequence)+1)

    #Actualize the fringe
    visited.append(sol)
    fringe_val.pop(fringe.index((sol, sequence)))
    fringe.remove((sol, sequence))

    #Choose the next state that has the minimal value
    direction = fringe_val.index(min(fringe_val))
    
    #Actualize the variables
    he = fringe_val[direction]
    sol = fringe[direction][0]
    sequence = fringe[direction][1]

    #Find the new empty space on the new state
    ind = 0
    for i in range(len(sol)):
        if 0 in sol[i]:
            ind = i
            break
    empty_pos = [ind, sol[ind].index(0)]

    it+=1

print("A*")
print(f"The algorithm has found the solution in {it} iterations")
print(f"The sequence of movements has been the following: {sequence}")
print(sol, end = "\n\n")

#A* without heuristic algorithm
sequence = []

#Find where the empty space is ubicated on the puzzle
for i in range(len(puzzle)):
    if 0 in puzzle[i]:
        ind = i
        break

#Initialize the necesary variables for the algorithm
empty_pos = [ind, puzzle[ind].index(0)]
sol = puzzle.copy()
it = 0
he = 0

#The fringe is represented by two lists
fringe_val = [he] #This lists contains the values of f(x) of each state 
fringe = [(sol, sequence)] #This list contains a tuple with each state and the sequence of movements until that state
visited = [] #This list contains the states that has been already been visited

#Loop where the algorithm A* without heuristic value (UCS) takes place
while sol != goal:
    #Calculate the next movements from the actual state
    left = []
    right = []
    up = []
    down = []
    #Left
    if empty_pos[1] != 0:
        left = c.deepcopy(sol)
        left_pos = empty_pos.copy()
        left_pos[1] -= 1
        t = left[left_pos[0]][left_pos[1]]
        left[left_pos[0]][left_pos[1]] = 0
        left[empty_pos[0]][empty_pos[1]] = t
        if left not in visited:
            fringe.append((left, sequence + ["L"]))
            fringe_val.append(len(sequence)+1)

    #Right
    if empty_pos[1] != 2:
        right = c.deepcopy(sol)
        right_pos = empty_pos.copy()
        right_pos[1] += 1
        t = right[right_pos[0]][right_pos[1]]
        right[right_pos[0]][right_pos[1]] = 0
        right[empty_pos[0]][empty_pos[1]] = t
        if right not in visited:
            fringe.append((right, sequence + ["R"]))
            fringe_val.append(len(sequence)+1)
        
    #Up
    if empty_pos[0] != 0:
        up = c.deepcopy(sol)
        up_pos = empty_pos.copy()
        up_pos[0] -= 1
        t = up[up_pos[0]][up_pos[1]]
        up[up_pos[0]][up_pos[1]] = 0
        up[empty_pos[0]][empty_pos[1]] = t
        if up not in visited:
            fringe.append((up, sequence + ["U"]))
            fringe_val.append(len(sequence)+1)
        
    #Down
    if empty_pos[0] != 2:
        down = c.deepcopy(sol)
        down_pos = empty_pos.copy()
        down_pos[0] += 1
        t = down[down_pos[0]][down_pos[1]]
        down[down_pos[0]][down_pos[1]] = 0
        down[empty_pos[0]][empty_pos[1]] = t
        if down not in visited:
            fringe.append((down, sequence + ["D"]))
            fringe_val.append(len(sequence)+1)

    #Actualize the fringe
    visited.append(sol)
    fringe_val.pop(fringe.index((sol, sequence)))
    fringe.remove((sol, sequence))

    #Choose the next state that has the minimal value
    direction = fringe_val.index(min(fringe_val))

    #Actualize the variables
    he = fringe_val[direction]
    sol = fringe[direction][0]
    sequence = fringe[direction][1]

    #Find the new empty space on the new state
    ind = 0
    for i in range(len(sol)):
        if 0 in sol[i]:
            ind = i
            break
    empty_pos = [ind, sol[ind].index(0)]
    it+=1

print("A* with h(x) = 0 (UCS)")
print(f"The algorithm has found the solution in {it} iterations")
print(f"The sequence of movements has been the following: {sequence}")
print(sol)