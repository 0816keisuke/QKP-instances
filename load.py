file = "instances/sample.txt"
# file = "instances/group1/jeu_100_25_1.txt"

# Load the instance file and set each variables: num_var, values, capacity, weights
with open(file, "r") as f:
    i = 1
    values_from_file = []
    for line in f:
        if i == 1:
            num_var = int(line)
        elif 2 <= i <= num_var + 1:
            values_from_file.append([int(s) for s in line.split()])
        elif i == num_var + 3:
            capacity = int(line)
        elif i == num_var + 4:
            weights = [int(s) for s in line.split()]
        i += 1
    values = [[0 for i in range(num_var)] for j in range(num_var)]
    for i in range(num_var):
        values[i][i] = values_from_file[0][i]
        if i  < num_var - 1:
            values[i][i+1:] = values_from_file[i+1]


# Display the problem’s formulation
# Objective function
print("max:   ", end="")

# Lineat term
for i in range(num_var):
    if values[i][i] == 0:
        continue
    if i < num_var - 1:
        print(f"{values[i][i]} x_{i+1} + ", end="")
    else:
        print(f"{values[i][i]} x_{i+1}")

# Quadratic term
for i in range(num_var):
    if i < num_var - 1:
        print("    ", end="")
    for j in range(i+1, num_var):
        if values[i][j] == 0:
            if j == num_var - 1:
                print()
            continue
        if j < num_var - 1:
            print(f" + {values[i][j]} x_{i+1} x_{j+1}", end="")
        else:
            print(f" + {values[i][j]} x_{i+1} x_{j+1}")
print()

# Constraint
print("s.t. ", end="")
for i in range(num_var):
    if values[i][i] == 0:
        continue
    if i < num_var - 1:
        print(f"{weights[i]} x_{i+1} + ", end="")
    else:
        print(f"{weights[i]} x_{i+1} <= {capacity}")
