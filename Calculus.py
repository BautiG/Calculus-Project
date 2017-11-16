import math
#make sure that if you need to do trig or logs do "math.()"
#use paranthesis when pluging in an exponent in the equation
yFunction = str(input("y="))
reSet = int(input("Where does your interval start? "))
xValue2 = int(input("And where does it end? "))
accuracy = int(input("Between integers, how many times should the program check for slope? (The bigger the number the more accurate the second derivative is) "))


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
    
    yFunctionNew2 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew2 += str(xValue+1)
        else:
            yFunctionNew2 += yFunction[i]
    i += 1
    global yFunctionNew2
    yFunctionNew2=yFunctionNew2
    
    yFunctionNew3 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew3 += str(xValue-1)
        else:
            yFunctionNew3 += yFunction[i]
    i += 1
    global yFunctionNew3
    yFunctionNew3=yFunctionNew3
    
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        funcTion()
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        funcTion()
        xValue+=(1/accuracy)

maxXvalue = 0  #this just establishes a veriable
xValue=reSet
smallest=1000
biggest=-1000
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        funcTion()
        if int(eval(yFunctionNew))>=biggest:
            biggest=int(eval(yFunctionNew))
            maxXvalue = xValue  #this step makes that variable equal to the xvalue of the surent highest point
        else:
            biggest=biggest
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        funcTion()
        if eval(yFunctionNew)>=biggest:
            biggest=eval(yFunctionNew)
            maxXvalue = xValue  #this step makes that variable equal to the xvalue of the surent highest point
        else:
            biggest=biggest
        xValue+=(1/accuracy)

minXvalue = 0
xValue=reSet
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        funcTion()
        if eval(yFunctionNew)<=smallest:
            smallest=eval(yFunctionNew)
            minXvalue = xValue  #this step makes that variable equal to the xvalue of the surent highest point
        else:
            smallest=smallest
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        funcTion()
        if eval(yFunctionNew)<=smallest:
            smallest=eval(yFunctionNew)
            minXvalue = xValue  #this step makes that variable equal to the xvalue of the surent highest point
        else:
            smallest=smallest
        xValue+=(1/accuracy)

#this actualy works now so don't try to fix it!!!
print("Absolute Max at: y= (" + str(maxXvalue) + "," + str(biggest)+")")
print("Absolute Min at: y= (" + str(minXvalue) + "," + str(smallest)+")")



def nDer():
    yFunctionNewDer = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer += str(xValue+.001)
        else:
            yFunctionNewDer += yFunction[i]
    
    global positivePoint
    positivePoint=eval(yFunctionNewDer)
    
    yFunctionNewDer2 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer2 += str(xValue-.001)
        else:
            yFunctionNewDer2 += yFunction[i]
    
    global negativePoint
    negativePoint=eval(yFunctionNewDer2)
    
    global derSlope
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
    
    global negativePoint2
    negativePoint2=eval(yFunctionNewDer4)
    global derSlope2
    derSlope2=(positivePoint2-negativePoint2)/.002
    #print(derSlope2)
def nDer3():
    yFunctionNewDer5 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer5 += str(xValue-1+.001)
        else:
            yFunctionNewDer5 += yFunction[i]
    i += 1
    
    positivePoint3=eval(yFunctionNewDer5)
    
    yFunctionNewDer6 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNewDer6 += str(xValue-1-.001)
        else:
            yFunctionNewDer6 += yFunction[i]
    i += 1
    
    global negativePoint3
    negativePoint3=eval(yFunctionNewDer6)
    
    global derSlope3
    derSlope3=(positivePoint3-negativePoint3)/.002
    #print(derSlope2)

xValue=reSet
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        nDer()
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        nDer()
        xValue+=(1/accuracy)

xValue=reSet
for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
         nDer()
         nDer2()
         nDer3()
         if derSlope>=0 and derSlope2<=0:
             print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a relative max!")
         if derSlope<=0 and derSlope2>=0:
             print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a relative min!")
         if derSlope3<0 and derSlope==0 and derSlope2>0:
             print("there is a relative min at x="+str(derSlope))
         if derSlope3>0 and derSlope==0 and derSlope2<0:
             print("there is a relative max at x="+str(derSlope))
         xValue+=1
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        nDer()
        nDer2()
        nDer3()
        if derSlope>=0 and derSlope2<=0:
            print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a relative max!")
        if derSlope<=0 and derSlope2>=0:
            print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a relative min!")
        if derSlope3<0 and derSlope==0 and derSlope2>0:
            print("there is a relative min at x="+str(derSlope))
        if derSlope3>0 and derSlope==0 and derSlope2<0:
            print("there is a relative max at x="+str(derSlope))
        xValue+=1

def secondDer():
    funcTion()
    nDer()
    global changeSlope
    changeSlope = ((((positivePoint-eval(yFunctionNew))/.001)-((eval(yFunctionNew)-negativePoint)/.001))/.001)
def secondDer2():
    funcTion()
    nDer2()
    global changeSlope2
    changeSlope2 = ((((positivePoint2-eval(yFunctionNew2))/.001)-((eval(yFunctionNew2)-negativePoint2)/.001))/.001)
def secondDer3():
    funcTion()
    nDer3()
    global changeSlope3
    changeSlope3 = ((((positivePoint3-eval(yFunctionNew3))/.001)-((eval(yFunctionNew3)-negativePoint3)/.001))/.001)
xValue=reSet
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        secondDer()
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        secondDer()
        xValue+=(1/accuracy)

inflecTion=xValue2
xValue=reSet
for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        secondDer()
        secondDer2()
        secondDer3()
        if changeSlope>=0 and changeSlope2<=0:
            print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a infelction point!")
            inflecTion=xValue
        if changeSlope<=0 and changeSlope2>=0:
            print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a infelction point!")
            inflecTion=xValue
        if changeSlope3<0 and changeSlope==0 and changeSlope2>0:
            print("there is an inflection point at x="+str(derSlope))
            inflecTion=xValue
        if changeSlope3>0 and changeSlope==0 and changeSlope2<0:
            print("there is an inflection point at x="+str(derSlope))
            inflecTion=xValue
        xValue+=1
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        secondDer()
        secondDer2()
        secondDer3()
        if changeSlope>=0 and changeSlope2<=0:
            print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a infelction point!")
            inflecTion=xValue
        if changeSlope<=0 and changeSlope2>=0:
            print("between x="+str(xValue-(1/accuracy))+" and x="+str(xValue+(1/accuracy))+" there is a infelction point!")
            inflecTion=xValue
        if changeSlope3<0 and changeSlope==0 and changeSlope2>0:
            print("there is an inflection point at x="+str(derSlope))
            inflecTion=xValue
        if changeSlope3>0 and changeSlope==0 and changeSlope2<0:
            print("there is an inflection point at x="+str(derSlope))
            inflecTion=xValue
        xValue+=1

xValue=reSet
secondDer()
if changeSlope>0:
    print("concave up on the interval: ["+str(reSet)+","+str(inflecTion)+"]")
    xValue=inflecTion+1
    secondDer()
    if changeSlope<0:
        print("concave down on the interval: ["+str(inflecTion)+","+str(xValue2)+"]")
xValue=reSet
secondDer()
if changeSlope<0:
    print("concave down on the interval: ["+str(reSet)+","+str(inflecTion)+"]")
    xValue=inflecTion+1
    secondDer()
    if changeSlope>0:
        print("concave up on the interval: ["+str(inflecTion)+","+str(xValue2)+"]")
        
        
xValue=reSet
xPoint = reSet
increasing = 3333 #random number, not likely to come out as slope
increasing2 = 0
decreasing = 2222
decreasing2 = 0
slopePositive = 0 #1 means positive, 2 means negative

if xValue < 0 and xValue2 > 0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        nDer() 
        #print(derSlope)
        
        if derSlope > 0 and increasing == 3333:
            increasing = xPoint
        if derSlope < 0 and decreasing == 2222:
            decreasing = xPoint
        elif derSlope>0:
            slopePositive = 1
            increasing2 = xPoint
        elif derSlope<0:
            slopePositive = 2
            decreasing2 = xPoint
        elif derSlope == 0 and slopePositive == 1:
            increasing2 = xPoint
            decreasing = xPoint
        elif derSlope == 0 and slopePositive == 2:
            decreasing2 = xPoint
            increasing = xPoint
            
        
        xPoint += (1/accuracy) 
        xValue += (1/accuracy)
            
    print("function is increasing between x=" + str(increasing) + " and x=" + str(increasing2))
    print("function is decreasing between x=" + str(decreasing) + " and x=" + str(decreasing2))    
else:    
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        nDer() 
        #print(derSlope)
        
        if derSlope > 0 and increasing == 3333:
            increasing = xPoint
        if derSlope < 0 and decreasing == 2222:
            decreasing = xPoint
        elif derSlope>0:
            slopePositive = 1
            increasing2 = xPoint
        elif derSlope<0:
            slopePositive = 2
            decreasing2 = xPoint
        elif derSlope == 0 and slopePositive == 1:
            increasing2 = xPoint
            decreasing = xPoint
        elif derSlope == 0 and slopePositive == 2:
            decreasing2 = xPoint
            increasing = xPoint
            
        
        xPoint += (1/accuracy) 
        xValue += (1/accuracy)
            
    print("function is increasing between x=" + str(increasing) + " and x=" + str(increasing2))
    print("function is decreasing between x=" + str(decreasing) + " and x=" + str(decreasing2)) 