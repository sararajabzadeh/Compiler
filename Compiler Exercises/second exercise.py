L = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",
     "W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
     "s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9",">","<","="]
letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",
        "W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
        "s","t","u","v","w","x","y","z"]
letterNumber = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
                "U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                "o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7",
                "8","9"]
state = "A"
string = input()
for i in range(len(string)):

    if string[i] not in L :
        print("Not in L")
        state="ERROR"
        break

    elif state=="A":
        if string[i]=="<":
            state = "B"
        elif string[i]==">":
            state = "C"
        elif string[i] in letter:
            state = "D"
        else:
            state="Z"
            break

    elif state=="B":
        if string[i]=="=":
            state = "E"
        else:
            state="Z"
            break

    elif state=="C":
        if string[i]=="=":
            state = "F"
        else:
            state = "Z"
            break

    elif state=="D":
        if string[i] in letterNumber:
            state="D"
        else:
            state="Z"
            break
    elif state=="E":
        if i != 1:
            state="Z"
    elif state=="F":
        if i != 1:
            state="Z"

if state=="B":
    print("Less")
elif state=="C":
    print("Greater")
elif state=="D":
    print("LetterAndNumber")
elif state=="E":
    print("LessEqual")
elif state=="F":
    print("GreaterEqual")
else:
    print("ERROR CONDITION")