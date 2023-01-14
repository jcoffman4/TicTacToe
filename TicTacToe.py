import random

possible_letters = ["A", "B", "C"]
possible_numbers = ["1", "2", "3"]
possible_spots = 10

print("Lets play Tik Tak Toe, I'll go first")
print("\n   A  B  C")
first_row = ["1  -", "-", "-"]
second_row = ["2  -", "-", "-"]
third_row = ["3  -", "-", "-"]
 
print("  ".join(first_row) + "\n" + "  ".join(second_row) + "\n" + "  ".join(third_row))

while possible_spots != 0:
    position = input("Pick Your Position: ")

    # User choosing which position they want
    print("\n   A  B  C")
    if position == "A1":
        first_row[0] = "1  X"
    elif position == "A2":
        second_row[0] = "2  X"
    elif position == "A3":
        third_row[0] = "3  X"
 
    elif position == "B1":
        first_row[1] = "X"
    elif position == "B2":
        second_row[1] = "X"
    elif position == "B3":
        third_row[1] = "X"

    elif position == "C1":
        first_row[2] = "X"
    elif position == "C2":
        second_row[2] = "X"
    elif position == "C3":
        third_row[2] = "X"
    possible_spots -= 1

# Robot choosing randomly what position it wants
    possible_robot_answers = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    robotPosition = random.choice(possible_robot_answers)

    while robotPosition == position:
        robotPosition = random.choice(possible_robot_answers)
    if robotPosition == "A1":
        first_row[0] = "1  O"
    elif robotPosition == "A2":
        second_row[0] = "2  O"
    elif robotPosition == "A3":
        third_row[0] = "3  O"
 
    elif robotPosition == "B1":
        first_row[1] = "O"
    elif robotPosition == "B2":
        second_row[1] = "O"
    elif robotPosition == "B3":
        third_row[1] = "O"

    elif robotPosition == "C1":
        first_row[2] = "O"
    elif robotPosition == "C2":
        second_row[2] = "O"
    elif robotPosition == "C3":
        third_row[2] = "O"
    print("  ".join(first_row) + "\n" + "  ".join(second_row) + "\n" + "  ".join(third_row))
    possible_spots -= 1

    #HOW PLAYER CAN WIN

    #Up and Down
    if first_row[0] == "1 X" & second_row[0] == "2 X" & third_row[0] == "3 X":
        print("Congratulations, you win!")
    elif first_row[1] == "X" & second_row[1] == "X" & third_row[1] == "X":
        print("Congratulations, you win!")
    elif first_row[2] == "X" & second_row[2] == "X" & third_row[2] == "X":
        print("Congratulations, you win!")
    #Diagonal
    elif first_row[0] == "1 X" & second_row[1] == "X" & third_row[2] == "X":
        print("Congratulations, you win!")
    elif first_row[2] == "X" & second_row[1] == "X" & third_row[0] == "3 X":
        print("Congratulations, you win!")
    #Side to Side
    elif first_row[0] == "1 X" & first_row[1] == "X" & first_row[2] == "X":
        print("Congratulations, you win!")
    elif second_row[0] == "2 X" & second_row[1] == "X" & second_row[2] == "X":
        print("Congratulations, you win!")
    elif third_row[0] == "3 X" & third_row[1] == "X" & third_row[2] == "X":
        print("Congratulations, you win!")


        #HOW ROBOT CAN WIN
    
    #Up and Down
    if first_row[0] == "1 O" & second_row[0] == "2 O" & third_row[0] == "3 O":
        print("Congratulations, THE ROBOT wins!")
    elif first_row[1] == "O" & second_row[1] == "O" & third_row[1] == "O":
        print("Congratulations, THE ROBOT wins!")
    elif first_row[2] == "O" & second_row[2] == "O" & third_row[2] == "O":
        print("Congratulations, THE ROBOT wins!")
    #Diagonal
    elif first_row[0] == "1 O" & second_row[1] == "O" & third_row[2] == "O":
        print("Congratulations, THE ROBOT wins!")
    elif first_row[2] == "O" & second_row[1] == "O" & third_row[0] == "3 O":
        print("Congratulations, THE ROBOT wins!")
    #Side to Side
    elif first_row[0] == "1 O" & first_row[1] == "O" & first_row[2] == "O":
        print("Congratulations, THE ROBOT wins!")
    elif second_row[0] == "2 O" & second_row[1] == "O" & second_row[2] == "O":
        print("Congratulations, THE ROBOT wins!")
    elif third_row[0] == "3 O" & third_row[1] == "O" & third_row[2] == "O":
        print("Congratulations, THE ROBOT wins!")


print("Out of Spots!")
