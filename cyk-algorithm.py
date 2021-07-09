grammar = [
    ['S', 'AB'],
    ['S', 'BC'],
    ['A', 'BA'],
    ['B', 'CC'],
    ['B', 'b'],
    ['A', 'a'],
    ['C', 'AB'],
    ['C', 'a']]

word = 'baaba'

print('Grammar: ', grammar)
# --------------------------------------------------------------------------


def index_of(s, e):  # this function returns the index of element e in set s
    index = -1
    for i, val in enumerate(s):
        if val == e:
            index = i
            break
    return index


# --------------------------------------------------------------------------
T = set()  # set of Terminals
for i in range(0, len(grammar)):  # filling the set according to the given grammar
    if len(grammar[i][1]) == 1:
        T.add(grammar[i][1])
print('Terminals: ', T)

# --------------------------------------------------------------------------
V = set()  # set of Variables
for i in range(0, len(grammar)):  # filling the set according to the given grammar
    V.add(grammar[i][0])
print('Variables: ', V)

print('Word: ', word)

# --------------------------------------------------------------------------
# a 3D array used in algorithm with size P[n][n][v]
# n = length of given word
# v = number of variables
P = [[[0 for i in range(len(V))] for k in range(len(word))] for j in range(len(word))]

# --------------------------------------------------------------------------
# Operating CYK algorithm:

# filling the first row of table:
for s in range(len(word)):  # looping through the substrings of length 1
    for r in grammar:  # looping through all production rules
        # if the derived alphabet equals the alphabet read
        # form the given word
        if r[1] == word[s]:
            P[0][s][index_of(V, r[0])] = 1  # add the variable in table


# filling the upper rows of table:
for l in range(2, len(word) + 1):  # looping through rows
    # (l = length of substring)
    # looping through different substrings of length l
    # (s = staring point of substring)
    for s in range(0, len(word) - l + 1):
        for p in range(1, l):  # partitioning the substring in two parts
            # (p = length of the first part)
            for r in grammar:  # looping through grammars to check if
                # substrings can be derived from them
                if len(r[1]) == 2:
                    # checking the possibility of derivation
                    if P[p - 1][s][index_of(V, r[1][0])] == 1 and \
                            P[l - p - 1][s + p][index_of(V, r[1][1])] == 1:
                        P[l - 1][s][index_of(V, r[0])] = 1  # adding the
                        # variable to table

# checking the top row to check the possibility of derivation from S (starting symbol)
print('Accepted: ', P[len(word) - 1][0][index_of(V, 'S')] == 1)
