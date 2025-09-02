# Tic-Tac-Toe: Step 1 (using 9 variables)

# 1) Initialize all positions with "."
a1 = "."
a2 = "."
a3 = "."
b1 = "."
b2 = "."
b3 = "."
c1 = "."
c2 = "."
c3 = "."

# print the initial configuration
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)

# First move: Player 1 (X)
move1_row = input("Player 1: Enter first move - row number from {1, 2, 3}: ")
move1_column = input("Player 1: Enter first move - column number from {1, 2, 3}: ")

if move1_row == "1" and move1_column == "1":
    a1 = "X"
elif move1_row == "1" and move1_column == "2":
    a2 = "X"
elif move1_row == "1" and move1_column == "3":
    a3 = "X"
elif move1_row == "2" and move1_column == "1":
    b1 = "X"
elif move1_row == "2" and move1_column == "2":
    b2 = "X"
elif move1_row == "2" and move1_column == "3":
    b3 = "X"
elif move1_row == "3" and move1_column == "1":
    c1 = "X"
elif move1_row == "3" and move1_column == "2":
    c2 = "X"
elif move1_row == "3" and move1_column == "3":
    c3 = "X"
else:
    print("Invalid move")

# print board after first move
print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)

# Second move: Player 2 (O)
move2_row = input("Player 2: Enter second move - row number from {1, 2, 3}: ")
move2_column = input("Player 2: Enter second move - column number from {1, 2, 3}: ")

if move2_row == "1" and move2_column == "1":
    if a1 == ".":
        a1 = "O"
    else:
        print("Cell already taken")
elif move2_row == "1" and move2_column == "2":
    if a2 == ".":
        a2 = "O"
    else:
        print("Cell already taken")
elif move2_row == "1" and move2_column == "3":
    if a3 == ".":
        a3 = "O"
    else:
        print("Cell already taken")
elif move2_row == "2" and move2_column == "1":
    if b1 == ".":
        b1 = "O"
    else:
        print("Cell already taken")
elif move2_row == "2" and move2_column == "2":
    if b2 == ".":
        b2 = "O"
    else:
        print("Cell already taken")
elif move2_row == "2" and move2_column == "3":
    if b3 == ".":
        b3 = "O"
    else:
        print("Cell already taken")
elif move2_row == "3" and move2_column == "1":
    if c1 == ".":
        c1 = "O"
    else:
        print("Cell already taken")
elif move2_row == "3" and move2_column == "2":
    if c2 == ".":
        c2 = "O"
    else:
        print("Cell already taken")
elif move2_row == "3" and move2_column == "3":
    if c3 == ".":
        c3 = "O"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

# print board after second move
print()
print(a1,a2,a3)
print(b1, b2,b3)
print(c1, c2, c3)

# Third move: Player 1 (X)
move3_row = input("Player 1: Enter third move - row number from {1, 2, 3}: ")
move3_column = input("Player 1: Enter third move - column number from {1, 2, 3}: ")

if move3_row == "1" and move3_column == "1":
    if a1 == ".":
        a1 = "X"
    else:
        print("Cell already taken")
elif move3_row == "1" and move3_column == "2":
    if a2 == ".":
        a2 = "X"
    else:
        print("Cell already taken")
elif move3_row == "1" and move3_column == "3":
    if a3 == ".":
        a3 = "X"
    else:
        print("Cell already taken")
elif move3_row == "2" and move3_column == "1":
    if b1 == ".":
        b1 = "X"
    else:
        print("Cell already taken")
elif move3_row == "2" and move3_column == "2":
    if b2 == ".":
        b2 = "X"
    else:
        print("Cell already taken")
elif move3_row == "2" and move3_column == "3":
    if b3 == ".":
        b3 = "X"
    else:
        print("Cell already taken")
elif move3_row == "3" and move3_column == "1":
    if c1 == ".":
        c1 = "X"
    else:
        print("Cell already taken")
elif move3_row == "3" and move3_column == "2":
    if c2 == ".":
        c2 = "X"
    else:
        print("Cell already taken")
elif move3_row == "3" and move3_column == "3":
    if c3 == ".":
        c3 = "X"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

# print board after third move
print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)
# Fourth move: Player 2 (O)
move4_row = input("Player 2: Enter fourth move - row number from {1, 2, 3}: ")
move4_column = input("Player 2: Enter fourth move - column number from {1, 2, 3}: ")

if move4_row == "1" and move4_column == "1":
    if a1 == ".":
        a1 = "O"
    else:
        print("Cell already taken")
elif move4_row == "1" and move4_column == "2":
    if a2 == ".":
        a2 = "O"
    else:
        print("Cell already taken")
elif move4_row == "1" and move4_column == "3":
    if a3 == ".":
        a3 = "O"
    else:
        print("Cell already taken")
elif move4_row == "2" and move4_column == "1":
    if b1 == ".":
        b1 = "O"
    else:
        print("Cell already taken")
elif move4_row == "2" and move4_column == "2":
    if b2 == ".":
        b2 = "O"
    else:
        print("Cell already taken")
elif move4_row == "2" and move4_column == "3":
    if b3 == ".":
        b3 = "O"
    else:
        print("Cell already taken")
elif move4_row == "3" and move4_column == "1":
    if c1 == ".":
        c1 = "O"
    else:
        print("Cell already taken")
elif move4_row == "3" and move4_column == "2":
    if c2 == ".":
        c2 = "O"
    else:
        print("Cell already taken")
elif move4_row == "3" and move4_column == "3":
    if c3 == ".":
        c3 = "O"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)

# Fifth move: Player 1 (X)
move5_row = input("Player 1: Enter fifth move - row number from {1, 2, 3}: ")
move5_column = input("Player 1: Enter fifth move - column number from {1, 2, 3}: ")

if move5_row == "1" and move5_column == "1":
    if a1 == ".":
        a1 = "X"
    else:
        print("Cell already taken")
elif move5_row == "1" and move5_column == "2":
    if a2 == ".":
        a2 = "X"
    else:
        print("Cell already taken")
elif move5_row == "1" and move5_column == "3":
    if a3 == ".":
        a3 = "X"
    else:
        print("Cell already taken")
elif move5_row == "2" and move5_column == "1":
    if b1 == ".":
        b1 = "X"
    else:
        print("Cell already taken")
elif move5_row == "2" and move5_column == "2":
    if b2 == ".":
        b2 = "X"
    else:
        print("Cell already taken")
elif move5_row == "2" and move5_column == "3":
    if b3 == ".":
        b3 = "X"
    else:
        print("Cell already taken")
elif move5_row == "3" and move5_column == "1":
    if c1 == ".":
        c1 = "X"
    else:
        print("Cell already taken")
elif move5_row == "3" and move5_column == "2":
    if c2 == ".":
        c2 = "X"
    else:
        print("Cell already taken")
elif move5_row == "3" and move5_column == "3":
    if c3 == ".":
        c3 = "X"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)

# Sixth move: Player 2 (O)
move6_row = input("Player 2: Enter sixth move - row number from {1, 2, 3}: ")
move6_column = input("Player 2: Enter sixth move - column number from {1, 2, 3}: ")

if move6_row == "1" and move6_column == "1":
    if a1 == ".":
        a1 = "O"
    else:
        print("Cell already taken")
elif move6_row == "1" and move6_column == "2":
    if a2 == ".":
        a2 = "O"
    else:
        print("Cell already taken")
elif move6_row == "1" and move6_column == "3":
    if a3 == ".":
        a3 = "O"
    else:
        print("Cell already taken")
elif move6_row == "2" and move6_column == "1":
    if b1 == ".":
        b1 = "O"
    else:
        print("Cell already taken")
elif move6_row == "2" and move6_column == "2":
    if b2 == ".":
        b2 = "O"
    else:
        print("Cell already taken")
elif move6_row == "2" and move6_column == "3":
    if b3 == ".":
        b3 = "O"
    else:
        print("Cell already taken")
elif move6_row == "3" and move6_column == "1":
    if c1 == ".":
        c1 = "O"
    else:
        print("Cell already taken")
elif move6_row == "3" and move6_column == "2":
    if c2 == ".":
        c2 = "O"
    else:
        print("Cell already taken")
elif move6_row == "3" and move6_column == "3":
    if c3 == ".":
        c3 = "O"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)

# Seventh move: Player 1 (X)
move7_row = input("Player 1: Enter seventh move - row number from {1, 2, 3}: ")
move7_column = input("Player 1: Enter seventh move - column number from {1, 2, 3}: ")

if move7_row == "1" and move7_column == "1":
    if a1 == ".":
        a1 = "X"
    else:
        print("Cell already taken")
elif move7_row == "1" and move7_column == "2":
    if a2 == ".":
        a2 = "X"
    else:
        print("Cell already taken")
elif move7_row == "1" and move7_column == "3":
    if a3 == ".":
        a3 = "X"
    else:
        print("Cell already taken")
elif move7_row == "2" and move7_column == "1":
    if b1 == ".":
        b1 = "X"
    else:
        print("Cell already taken")
elif move7_row == "2" and move7_column == "2":
    if b2 == ".":
        b2 = "X"
    else:
        print("Cell already taken")
elif move7_row == "2" and move7_column == "3":
    if b3 == ".":
        b3 = "X"
    else:
        print("Cell already taken")
elif move7_row == "3" and move7_column == "1":
    if c1 == ".":
        c1 = "X"
    else:
        print("Cell already taken")
elif move7_row == "3" and move7_column == "2":
    if c2 == ".":
        c2 = "X"
    else:
        print("Cell already taken")
elif move7_row == "3" and move7_column == "3":
    if c3 == ".":
        c3 = "X"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)

# Eighth move: Player 2 (O)
move8_row = input("Player 2: Enter eighth move - row number from {1, 2, 3}: ")
move8_column = input("Player 2: Enter eighth move - column number from {1, 2, 3}: ")

if move8_row == "1" and move8_column == "1":
    if a1 == ".":
        a1 = "O"
    else:
        print("Cell already taken")
elif move8_row == "1" and move8_column == "2":
    if a2 == ".":
        a2 = "O"
    else:
        print("Cell already taken")
elif move8_row == "1" and move8_column == "3":
    if a3 == ".":
        a3 = "O"
    else:
        print("Cell already taken")
elif move8_row == "2" and move8_column == "1":
    if b1 == ".":
        b1 = "O"
    else:
        print("Cell already taken")
elif move8_row == "2" and move8_column == "2":
    if b2 == ".":
        b2 = "O"
    else:
        print("Cell already taken")
elif move8_row == "2" and move8_column == "3":
    if b3 == ".":
        b3 = "O"
    else:
        print("Cell already taken")
elif move8_row == "3" and move8_column == "1":
    if c1 == ".":
        c1 = "O"
    else:
        print("Cell already taken")
elif move8_row == "3" and move8_column == "2":
    if c2 == ".":
        c2 = "O"
    else:
        print("Cell already taken")
elif move8_row == "3" and move8_column == "3":
    if c3 == ".":
        c3 = "O"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)

# Ninth move: Player 1 (X)
move9_row = input("Player 1: Enter ninth move - row number from {1, 2, 3}: ")
move9_column = input("Player 1: Enter ninth move - column number from {1, 2, 3}: ")

if move9_row == "1" and move9_column == "1":
    if a1 == ".":
        a1 = "X"
    else:
        print("Cell already taken")
elif move9_row == "1" and move9_column == "2":
    if a2 == ".":
        a2 = "X"
    else:
        print("Cell already taken")
elif move9_row == "1" and move9_column == "3":
    if a3 == ".":
        a3 = "X"
    else:
        print("Cell already taken")
elif move9_row == "2" and move9_column == "1":
    if b1 == ".":
        b1 = "X"
    else:
        print("Cell already taken")
elif move9_row == "2" and move9_column == "2":
    if b2 == ".":
        b2 = "X"
    else:
        print("Cell already taken")
elif move9_row == "2" and move9_column == "3":
    if b3 == ".":
        b3 = "X"
    else:
        print("Cell already taken")
elif move9_row == "3" and move9_column == "1":
    if c1 == ".":
        c1 = "X"
    else:
        print("Cell already taken")
elif move9_row == "3" and move9_column == "2":
    if c2 == ".":
        c2 = "X"
    else:
        print("Cell already taken")
elif move9_row == "3" and move9_column == "3":
    if c3 == ".":
        c3 = "X"
    else:
        print("Cell already taken")
else:
    print("Invalid move")

print()
print(a1, a2, a3)
print(b1, b2, b3)
print(c1, c2, c3)
# Check win (no return, no function)
if a1 == a2 == a3 and a1 != ".":
    print("Player 1 wins!" if a1 == "X" else "Player 2 wins!")
    exit()
if b1 == b2 == b3 and b1 != ".":
    print("Player 1 wins!" if b1 == "X" else "Player 2 wins!")
    exit()
if c1 == c2 == c3 and c1 != ".":
    print("Player 1 wins!" if c1 == "X" else "Player 2 wins!")
    exit()
if a1 == b1 == c1 and a1 != ".":
    print("Player 1 wins!" if a1 == "X" else "Player 2 wins!")
    exit()
if a2 == b2 == c2 and a2 != ".":
    print("Player 1 wins!" if a2 == "X" else "Player 2 wins!")
    exit()
if a3 == b3 == c3 and a3 != ".":
    print("Player 1 wins!" if a3 == "X" else "Player 2 wins!")
    exit()
if a1 == b2 == c3 and a1 != ".":
    print("Player 1 wins!" if a1 == "X" else "Player 2 wins!")
    exit()
if a3 == b2 == c1 and a3 != ".":
    print("Player 1 wins!" if a3 == "X" else "Player 2 wins!")
    exit()