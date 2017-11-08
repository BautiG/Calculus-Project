import math
yFunction = str(input("y="))
xValue = int(input("Where does your interval start?"))
xValue2 = int(input("And where does it end?"))
#Accuracy = input("How accurate do you want the graph to be?")

def funcTion():
    yFunctionNew = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew += str(xValue)
        else:
            yFunctionNew += yFunction[i]

    i += 1

    print (yFunctionNew)
    print (eval(yFunctionNew))
    
for i in range(xValue, xValue2):
    funcTion()
    xValue+=1