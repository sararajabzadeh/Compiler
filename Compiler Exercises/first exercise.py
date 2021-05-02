L = ["a","b","\n" ,"\t", "\"", "$"]
state = "A"
string = input()
# string+="$"
finalState=state
nextState=state
for i in range(len(string)):

    if string[i] not in L :
        print("Not in L")
        state="ERROR"
        break
    elif state=="A":
        if string[i]=="a":
            state = "B"
        elif string[i]=="b":
            state = "C"
        elif (string[i] == "\n" or string[i]=="\t" or string[i]=="\""):
            state = "D"
        elif string[i] == "$":
            state = "E"
        # print("EOFToken")
        # finalState=nextState
            break
    elif state=="B":
        if string[i]=="b":
            state = "G"
        elif string[i]=="a":
            state = "F"


    elif state=="C":
        if string[i]=="b":
            state = "C"
        elif string[i]=="a":
            state="H"
        elif string[i]=="a":
            state = "F"
        # finalState = nextState
            break
    elif state=="D":
        if string[i]=="\n\t":
            state="D"
    elif state =="G":
        if string[i]=="b":
            state="G"
        elif string[i]=="a":
            state="T"
    elif state=="F":
        if string[i]=="a" or string[i]=="b":
            state="T"
    elif state=="H":
        if string[i]=="a":
            state = "F"
        elif string[i]=="b":
            state="T"
    elif state=="T":
        if string[i]=="a" or string[i]=="b":
            state="T"
    # else:
    #     print("Not in L")
    # state=nextState
# print(state)
# print(finalState)
if state=="B":
    print("Third token")
elif state=="D":
    print("")
elif state=="E":
    print("EOFToken")
elif state=="G":
    print("FirstToken")
elif state=="F":
    print("SecondToken")
# elif state=="F" and string=="aa":
#     print("")
else:
    print("ERROR CONDITION")