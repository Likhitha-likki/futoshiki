puzzle = []
print("welcome to FUTOSHIKI game")
print("if Easy : 4\n   Medium: 5\n   Hard : 6 ")
print("select levels")
n=int(input("choose your level here : "))
if (n == 4):
    game = (" _>_>_ _  \n        \n _ _ _ _ \n   ^ V   \n _ _ _>_ \n         \n _<_ _ _")
    print(game)
    print("enter numbers")
    for i in range(n):
        lst = []
        for j in range(n):
            value = int(input("value--"))
            if value > n:
                print("enter the number in the range 1-n")
                value = int(input("Value--"))
                lst.append(value)
            else:
                lst.append(value)
        puzzle.append(lst)
        print(lst)
    print(puzzle)
    if (n == 4):
        logic = [
                [">", ">", ""],
                ["  ", " ", "  ", ""],
    
                ["", "", ""],
                ["  ", "^", " V ", ""],
    
                ["", "", ">"],
                ["  ", "  ", "  ", " "],
    
                ["<", "", ""],
                ["", "", "", ""], 
                 ]
    def futo_puzzle(puzzle, logic):
        for i,l_line in enumerate(logic):
            if(i % 2 == 0):
                line = ""
                for j in range(len(puzzle[0]) - 1):
                    line += "{n}{l:1}".format(n = puzzle[i // 2][j],l=l_line[j])
                line += "{}".format(puzzle[i // 2][-1])
                print(line)
            else:
                line = ""
                for l in range(len(l_line)):
                    line += "{:1}".format(l_line[l])
                print(line)

    def number_there(puzzle, row, col, num):
        for x in range(n):
            if futo_puzzle[row][x] == num:
                return False
        for x in range(n):
            if [x][col] == num:
                return False
        if ([0][1] < puzzle[1][1]):
            return True
        if (puzzle[1][2] < puzzle[2][2]):
            return True
        if (puzzle[2][3] < puzzle[3][3]):
            return True
        if (puzzle[0][3] > puzzle[1][3]):
            return True
        if (puzzle[2][0] > puzzle[2][1]):
            return True
    def futo_ans(puzzle,row,col):
        if (row == n-1 and col == n):
            return True
        if (col == n):
            row +=1
            col = 0
        if puzzle[row][col] > 0:
            return futo_ans(puzzle,row,col + 1)
        for num in range(1,n+1):
            if number_there(puzzle,row,col,num):
                puzzle[row][col] = num
                if futo_ans(puzzle,row,col+1):
                    return True
            puzzle[row][col] = 0
        return False
    def final_ans():
        print("solution")
        if futo_ans(puzzle,0,0):
            futo_puzzle(puzzle,logic)
        else:
            print("not possible")
    final_ans()
    result = [[4, 3, 1, 2], [2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3]]
    if (result == puzzle):
        print("Your answer is correct")
        print("Congratulatios")
    else:
        print("Your answer is wrong")
        print("Try again")

elif (n == 5):
    game = (" _>_>_ _ _  \n        \n _<_ _ _ _ \n          \n _ _<_<_ _ \n         \n _ _ _ _ _ \n       ^ \n _<_ _ _ _ ")
    print(game)
    print("enter numbers")
    for i in range(n):
        lst = []
        for j in range(n):
            value = int(input("value--"))
            if value > n:
                print("enter the number in the range 1-n")
                value = int(input("Value--"))
                lst.append(value)
            else:
                lst.append(value)
        puzzle.append(lst)
        print(lst)
    print(puzzle)
    if (n == 5):
        logic =logic = [
                       [">", " ", ">", ""],
                       ["  ", " ", "  ", "  ","  "],
    
                       ["<", "", "", ""],
                       ["  ", " ", "   ", "",""],
    
                       ["", "", "<","<"],
                       ["  ", "  ", "  ", " ",""],

                       ["", "", " "," "],
                       ["  ", "  ", "  ", "^ ",""],
    
                       ["<", "", "",""],
                       ["", "", "", "",""],
]
    def futo_puzzle(puzzle, logic):
        for i,l_line in enumerate(logic):
            if(i % 2 == 0):
                line = ""
                for j in range(len(puzzle[0]) - 1):
                    line += "{n}{l:1}".format(n = puzzle[i // 2][j],l=l_line[j])
                line += "{}".format(puzzle[i // 2][-1])
                print(line)
            else:
                line = ""
                for l in range(len(l_line)):
                    line += "{:1}".format(l_line[l])
                print(line)

    def number_there(puzzle, row, col, num):
        for x in range(n):
            if futo_puzzle[row][x] == num:
                return False
        for x in range(n):
            if [x][col] == num:
                return False
        if ([0][0] > puzzle[0][1]):
            return True
        if (puzzle[0][2] > puzzle[0][3]):
            return True
        if (puzzle[1][0] < puzzle[1][1]):
            return True
        if (puzzle[2][2] < puzzle[2][3]):
            return True
        if (puzzle[2][3] < puzzle[2][4]):
            return True
        if (puzzle[3][3] < puzzle[4][3]):
            return True
        if (puzzle[4][0] < puzzle[4][1]):
            return True
    def futo_ans(puzzle,row,col):
        if (row == n-1 and col == n):
            return True
        if (col == n):
            row +=1
            col = 0
        if puzzle[row][col] > 0:
            return futo_ans(puzzle,row,col + 1)
        for num in range(1,n+1):
            if number_there(puzzle,row,col,num):
                puzzle[row][col] = num
                if futo_ans(puzzle,row,col+1):
                    return True
            puzzle[row][col] = 0
        return False
    def final_ans():
        print("solution")
        if futo_ans(puzzle,0,0):
            futo_puzzle(puzzle,logic)
        else:
            print("not possible")
    final_ans()
    result = [[4, 3, 2, 1, 5], [3, 5, 4, 2, 1], [5, 2, 1, 3, 4], [2, 1, 5, 4, 3], [1, 4, 3, 5, 2]]
    if (result == puzzle):
        print("Your answer is correct")
        print("Congratulations")
    else:
        print("Your ansewr is incorrect")
        print("Better luck next time")


else:
    game = (" _ _ _ _<_ _ \n         \n _>_ _>_ _ _ \n     v     v \n _ _ _ _ _ _\n v   v ^     \n _ _ _ _ _ _ \n   ^     ^ \n _ _ _ _<_ _ \n     v     ^\n _ _<_ _ _>_")
    print(game)
    print("enter numbers")
    for i in range(n):
        lst = []
        for j in range(n):
            value = int(input("value--"))
            if value > n:
                print("enter the number in the range 1-n")
                value = int(input("Value--"))
                lst.append(value)
            else:
                lst.append(value)
        puzzle.append(lst)
        print(lst)
    print(puzzle)
    if (n == 6):
        logic =[
               [" ", " ", " ", "<", " "],
               ["  ", " ", "  ", "  ","  ", " "],
    
               [">", " ", ">", " ", " "],
               [" ", " ", "v", " "," ", "v"],
    
               [" ", " ", " "," ", " "],
               ["v", "  ", "v", "^"," "," "],
    
               [" ", "", "","", " "],
               [" ", "^", " ", " ", "^", " "],

               [" ", " ", " ", "<", " "],
               ["  ", " ", "  ", " v","  ", "^"],

               [" ", "<", " ", ">", " "],
               ["  ", " ", "  ", "  ","  ", " "],
]
    def futo_puzzle(puzzle, logic):
        for i,l_line in enumerate(logic):
            if(i % 2 == 0):
                line = ""
                for j in range(len(puzzle[0]) - 1):
                    line += "{n}{l:1}".format(n = puzzle[i // 2][j],l=l_line[j])
                line += "{}".format(puzzle[i // 2][-1])
                print(line)
            else:
                line = ""
                for l in range(len(l_line)):
                    line += "{:1}".format(l_line[l])
                print(line)

    def number_there(puzzle, row, col, num):
        for x in range(n):
            if futo_puzzle[row][x] == num:
                return False
        for x in range(n):
            if [x][col] == num:
                return False
        if ([0][3] < puzzle[0][4]):
            return True
        if (puzzle[1][0] > puzzle[1][1]):
            return True
        if (puzzle[1][2] > puzzle[1][3]):
            return True
        if (puzzle[2][2] < puzzle[1][2]):
            return True
        if (puzzle[2][5] < puzzle[1][5]):
            return True
        if (puzzle[3][0] < puzzle[2][0]):
            return True
        if (puzzle[3][2] < puzzle[2][2]):
            return True
        if (puzzle[3][3] > puzzle[2][3]):
            return True
        if (puzzle[4][1] > puzzle[3][1]):
            return True
        if (puzzle[4][3] < puzzle[4][4]):
            return True
        if (puzzle[4][4] > puzzle[3][4]):
            return True
        if (puzzle[5][1] < puzzle[5][2]):
            return True
        if (puzzle[5][3] < puzzle[4][3]):
            return True
        if (puzzle[5][4] > puzzle[5][5]):
            return True
        if (puzzle[5][5] > puzzle[4][5]):
            return True
        
    def futo_ans(puzzle,row,col):
        if (row == n-1 and col == n):
            return True
        if (col == n):
            row +=1
            col = 0
        if puzzle[row][col] > 0:
            return futo_ans(puzzle,row,col + 1)
        for num in range(1,n+1):
            if number_there(puzzle,row,col,num):
                puzzle[row][col] = num
                if futo_ans(puzzle,row,col+1):
                    return True
            puzzle[row][col] = 0
        return False
    def final_ans():
        print("solution")
        if futo_ans(puzzle,0,0):
            futo_puzzle(puzzle,logic)
        else:
            print("not possible")
    final_ans()
    result = [[6, 3, 1, 4, 5, 2], [4, 1, 5, 3, 2, 6], [2, 6, 3, 5, 1, 4], [1, 4, 2, 6, 3, 5], [3, 5, 6, 2, 4, 1], [5, 2, 4, 1, 6, 3]]
    if (result == puzzle):
        print(" Your answer is correct")
        print("congratulations")
    else:
        print(" Your answer is incorrect")
        print("Better luck next time")
