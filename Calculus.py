import math
#make sure that if you need to do trig or logs do "math.()"
#use paranthesis when pluging in an exponent in the equation
yFunction = str(input("y="))
reSet = int(input("Where does your interval start? "))
xValue2 = int(input("And where does it end? "))
accuracy = int(input("Between integers, how many times should the program check for slope? "))

xValue=reSet

def funcTion():
    yFunctionNew = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew += str(xValue)
        else:
            yFunctionNew += yFunction[i]
    i += 1
    
    yFunctionNew=eval(yFunctionNew)
    print (yFunctionNew)
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
            funcTion()
            xValue+=(1/accuracy)
    else:
        for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
            funcTion()
            xValue+=(1/accuracy)
"""
maxXvalue = 0  #this just establishes a veriable
xValue=reSet
smallest=1000
biggest=-1000
for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
    funcTion()
    if int(eval(yFunctionNew))>=biggest:
        biggest=int(eval(yFunctionNew))
        maxXvalue = xValue  #this step makes that variable equal to the xvalue of the surent highest point
    else:
        biggest=biggest
    xValue+=(1/accuracy)

minXvalue = 0
xValue=reSet
for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
    funcTion()
    if int(eval(yFunctionNew))<=smallest:
        smallest=int(eval(yFunctionNew))
        minXvalue = xValue
    else:
        smallest=smallest
    xValue+=(1/accuracy)

print("Absolute Max at: y= (" + str(maxXvalue) + "," + str(biggest)+")") 
print("Absolute Min at: y= (" + str(minXvalue) + "," + str(smallest)+")")

xValue=reSet
def nDer():
    yFunctionNewDer = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer += str(xValue+.001)
        else:
            yFunctionNewDer += yFunction[i]
    i += 1
    
    positivePoint=eval(yFunctionNewDer)
    
    yFunctionNewDer2 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer2 += str(xValue-.001)
        else:
            yFunctionNewDer2 += yFunction[i]
    i += 1
    
    negativePoint=eval(yFunctionNewDer2)
    
    derSlope=(positivePoint-negativePoint)/.002
    #print(derSlope)

def nDer2():
    yFunctionNewDer3 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer3 += str(xValue+1+.001)
        else:
            yFunctionNewDer3 += yFunction[i]
    i += 1
    
    positivePoint2=eval(yFunctionNewDer3)
    
    yFunctionNewDer4 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer4 += str(xValue+1-.001)
        else:
            yFunctionNewDer4 += yFunction[i]
    i += 1
    
    negativePoint2=eval(yFunctionNewDer4)
    
    derSlope2=(positivePoint2-negativePoint2)/.002
    #print(derSlope2)

for i in range(xValue, xValue2+1):
    nDer()
    xValue+=(1/accuracy)

for i in range(xValue, xValue2+1):
    nDer()
    nDer2()
    if derSlope>0 and derSlope2<0:
        print("max")
    if derSlope<0 and derSlope2>0:
        print("min")
    else:
        print("what the herrrr")
    xValue+=1
"""
