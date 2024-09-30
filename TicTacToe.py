#TicTacToe

l = [["-","-","-"],["-","-","-"],["-","-","-"]]

def check():
    countx = 0
    counto = 0
    #L Diagonal check
    for j in range(3):
        if l[j][j] == "x":
            countx += 1
        elif l[j][j] == "o":
            counto += 1
    if (countx==3 or counto==3):
        print("Won! L Diagonal")
        return 0

    #R Diagonal check
   
    counto=countx=0
    if l[0][2] == "x" and l[1][1] == "x" and l[2][0] == "x":
        print("X Won! L Diagonal")
        return 0
    elif l[0][2] == "o" and l[1][1] == "o" and l[2][0] == "o":
        print("X Won! L Diagonal")
        return 0

    #Row Check
    counto=countx=0
    for i in range(3):
        for k in range(3):
            if l[i][k]=="x":
                countx+=1
            elif l[i][k]=="o":
                counto+=1
            if (countx==3 or counto==3):
                print("Won! Row ", (i+1))
                return 0
        counto=countx=0
    


    #Column Check
    counto=countx=0
    for i in range(3):
        for k in range(3):
            if l[k][i]=="x":
                countx+=1
            elif l[k][i]=="o":
                counto+=1
            if (countx==3 or counto==3):
                print("Won! Column ", (i+1))
                return 0
        counto=countx=0        
    
            
counting=0
for i in range(9):
    print("Block:")
    for x in range(len(l)):
        for y in range(len(l[1])):
            print(l[x][y], end=" ")
        print()
    
    if counting%2==0:
        var="x"
    else:
        var="o"

    print("Where do you want to place "+var)
    print(""" 
    11 | 12 | 13
    ____________
    21 | 22 | 23
    ____________
    31 | 32 | 33
    """)

    choice = int(input("Choice: "))

    if choice not in (11, 12, 13, 21, 22, 23, 31, 32, 33):
        continue
    else:
        l[(choice//10)-1][(choice%10)-1] = var
    
    finish=check()
    if finish==0:
        break
    else:
        counting+=1
else:
    print("Draw")

    



