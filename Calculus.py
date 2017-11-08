import math
"""
Function = input("What is your function?")
Interval1 = int(input("Where does your interval start?"))
Interval2 = int(input("And where does it end?"))
#Accuracy = input("How accurate do you want the graph to be?")
"""
def funcTion():
    yFunction = str(input("y="))
    print (yFunction)
    xInput = input("x=")
    xValue = int(xInput)
    yFunctionNew = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew += str(xValue)
        else:
            yFunctionNew += yFunction[i]
            
    i += 1

    print (yFunctionNew)
    print (eval(yFunctionNew))

funcTion()
