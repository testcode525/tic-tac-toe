# Tic-Tac-Toe:

a1 = "."                                
a2 = "."
a3 = "."
b1 = "."
b2 = "."
b3 = "."
c1 = "."
c2 = "."
c3 = "."

# Input Board 

print("  _1___2___3_")
print("1|", a1 ,"|", a2, "|", a3 ,"|")
print("  -----------")
print("2|", b1 ,"|", b2 ,"|", b3 ,"|")
print("  -----------")
print("3|", c1 ,"|", c2 ,"|", c3 ,"|")
print("  ___________")


# Check for invalid moves and already taken cells

move_count = 0
while move_count < 9:
    
    if move_count % 2 == 0:
        symbol = "O"
        player = "Player 1"
    else:
        symbol = "X"
        player = "Player 2"
    valid_move = False
    while valid_move==False:
        move_row = input(player + ":Enter row {{1, 2, 3}}: ")
        move_column = input(player + ":Enter column {{1, 2, 3}}: ")
        if move_row == "1" and move_column == "1":
            if a1 == ".":
                a1 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "1" and move_column == "2":
            if a2 == ".":
                a2 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "1" and move_column == "3":
            if a3 == ".":
                a3 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "2" and move_column == "1":
            if b1 == ".":
                b1 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "2" and move_column == "2":
            if b2 == ".":
                b2 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "2" and move_column == "3":
            if b3 == ".":
                b3 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "3" and move_column == "1":
            if c1 == ".":
                c1 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "3" and move_column == "2":
            if c2 == ".":
                c2 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        elif move_row == "3" and move_column == "3":
            if c3 == ".":
                c3 = symbol
                valid_move = True
            else:
                print("Cell already taken")
        else:
            print("Please enter number between 1 and 3")
    print()
    print("  _1___2___3_")
    print("1|", a1 ,"|", a2, "|", a3 ,"|")
    print("  -----------")
    print("2|", b1 ,"|", b2 ,"|", b3 ,"|")
    print("  -----------")
    print("3|", c1 ,"|", c2 ,"|", c3 ,"|")
    print("  ___________")


    # Win check after every move
    
    if a1 == a2 == a3 and a1 != ".":
        print("Player 1 wins!" if a1 == "O" else "Player 2 wins!")
        break
    if b1 == b2 == b3 and b1 != ".":
        print("Player 1 wins!" if b1 == "O" else "Player 2 wins!")
        break
    if c1 == c2 == c3 and c1 != ".":
        print("Player 1 wins!" if c1 == "O" else "Player 2 wins!")
        break
    if a1 == b1 == c1 and a1 != ".":
        print("Player 1 wins!" if a1 == "O" else "Player 2 wins!")
        break
    if a2 == b2 == c2 and a2 != ".":
        print("Player 1 wins!" if a2 == "O" else "Player 2 wins!")
        break
    if a3 == b3 == c3 and a3 != ".":
        print("Player 1 wins!" if a3 == "O" else "Player 2 wins!")
        break
    if a1 == b2 == c3 and a1 != ".":
        print("Player 1 wins!" if a1 == "O" else "Player 2 wins!")
        break
    if a3 == b2 == c1 and a3 != ".":
        print("Player 1 wins!" if a3 == "O" else "Player 2 wins!")
        break
    move_count += 1
    if move_count==9:
        if a1 == a2 == a3 and a1 != ".":
        
            break
        if b1 == b2 == b3 and b1 != ".":
        
            break
        if c1 == c2 == c3 and c1 != ".":
       
            break
        if a1 == b1 == c1 and a1 != ".":
        
            break
        if a2 == b2 == c2 and a2 != ".":
        
            break
        if a3 == b3 == c3 and a3 != ".":
        
            break
        if a1 == b2 == c3 and a1 != ".":
        
            break
        if a3 == b2 == c1 and a3 != ".":
        
            break
        else :
            print("Its a draw")
