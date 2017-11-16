"""
welcom to our program! Billy and I bascially made a program that calculates a bunch of different things
about a function that the user gives the program. Just remember to use the proper python syntax.
and from this point on, anything in a "#" comentary on how the program works:
"""
import math #brings in the basic python math used in the rest of the program
#these lines below imput the information to run the program
yFunction = str(input("y="))
reSet = int(input("Where does your interval start? "))
xValue2 = int(input("And where does it end? "))
accuracy = int(input("Between integers, how many times should the program check for slope? (The bigger the number the more accurate the second derivative is) "))

xValue=reSet#this will allow us to reset the value of xValue after it is manipulated thoughout the program

#this defines a function that takes an x value and calculates a y value using "yFunction"
def funcTion():
    yFunctionNew = ""
    #this below goes though each vatiable and finds x and replaces it with your number
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew += str(xValue)
        else:
            yFunctionNew += yFunction[i]
    i += 1
    
    yFunctionNew=eval(yFunctionNew)
    #does the same thing but for x+1
    yFunctionNew2 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew2 += str(xValue+1)
        else:
            yFunctionNew2 += yFunction[i]
    i += 1
    global yFunctionNew2#makes the variable availeable outside of the function
    yFunctionNew2=yFunctionNew2
    #does the same thing but for x-1
    yFunctionNew3 = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew3 += str(xValue-1)
        else:
            yFunctionNew3 += yFunction[i]
    i += 1
    global yFunctionNew3#makes the variable availeable outside of the function
    yFunctionNew3=yFunctionNew3

#this below just calculates every y value on the interval(doesn't really get used unless the user edits)
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        funcTion()#this runs function
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        funcTion()
        xValue+=(1/accuracy)

xValue=reSet#resets xValue to original value
"""
every for loop has to run 2 seperate ways depending on the interval so I will only explain this
once here. If the interval starts negative and makes it to positive it has to do a different number of 
checks than if it were just negative or just positive. This means that we have to do an if statement 
with a different range check for each one. I will only explain the code on the top because the code on the
bottom is exactly identical.
"""
#this calculates if there is a zero on the interval
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
            funcTion()#this runs function
            if eval(yFunctionNew)==0:
                print("there is a zero at x="+str(xValue))#this prints the function
            xValue+=1
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        funcTion()
        if eval(yFunctionNew)==0:
            print("there is a zero at x="+str(xValue))
        xValue+=1


maxXvalue = 0  #this just establishes a veriable
xValue=reSet #this resets manipulated xValue
smallest=1000 #this just establishes a veriable
biggest=-1000 #this just establishes a veriable
#this calculates the abosolute max
if xValue<0 and xValue2>0: #this is another one of those special loops
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        funcTion()#this runs function
        if eval(yFunctionNew)>=biggest:
            biggest=eval(yFunctionNew)
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

#this calculates the absolue min
minXvalue = 0
xValue=reSet#this resets xValue
if xValue<0 and xValue2>0:#this is one of those special loops
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        funcTion()#this runs function
        if eval(yFunctionNew)<=smallest: 
            smallest=eval(yFunctionNew)
            minXvalue = xValue  #this step makes that variable equal to the xvalue of the surent lowest point
        else:
            smallest=smallest
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        funcTion()
        if eval(yFunctionNew)<=smallest:
            smallest=eval(yFunctionNew)
            minXvalue = xValue  #this step makes that variable equal to the xvalue of the surent lowest point
        else:
            smallest=smallest
        xValue+=(1/accuracy)

#these print the cordinates of the absolute min and max
print("Absolute Max at: y= (" + str(maxXvalue) + "," + str(biggest)+")")
print("Absolute Min at: y= (" + str(minXvalue) + "," + str(smallest)+")")
#this is how the derivative function is calculated
"""
how this works is it calculates a y value right after a point, right before a point
and then plugs it in to the limit formula for slope at a point.
"""
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

#this calculates the slope at the point 1 unit after the xValue
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
#this calculates the slope at the point 1 unit before the xValue
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

xValue=reSet#this resets xvalue
#this calculates the derivative at any point. It does nothing unless the user inserts a print into the code
if xValue<0 and xValue2>0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        nDer()
        xValue+=(1/accuracy)
else:
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        nDer()
        xValue+=(1/accuracy)

xValue=reSet#this resets xvalue
"""
this finds relative maxes and mins by chekcing the xvalues that comes before and value that come after
by calculating the slope at those points and seeing if there is a sign change. If it lands exactly on a zero,
it will say that there is a min/max at that point. But if there is no zero, only a sign change, it will give a 
range in which the min/max can be found.
"""
for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
         nDer()#calculates derivative at point
         nDer2()#calculates derivative 1 after point
         nDer3()#calculates derivative 1 before point
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
#this calculates the second derivative
def secondDer():
    funcTion()#runs function(calculates y value)
    nDer()#runs Derivative(calculates slope at point)
    global changeSlope#this makes the varibale global(availeable outside of the function)
    #this below calculates the second derivative by calculating change in slope
    changeSlope = ((((positivePoint-eval(yFunctionNew))/.001)-((eval(yFunctionNew)-negativePoint)/.001))/.001)
#this does the same thing as secondDer() except that it does it for xValue+1
def secondDer2():
    funcTion()
    nDer2()
    global changeSlope2
    changeSlope2 = ((((positivePoint2-eval(yFunctionNew2))/.001)-((eval(yFunctionNew2)-negativePoint2)/.001))/.001)
#this does the same thing as secondDer() except that it does it for xValue-1
def secondDer3():
    funcTion()
    nDer3()
    global changeSlope3
    changeSlope3 = ((((positivePoint3-eval(yFunctionNew3))/.001)-((eval(yFunctionNew3)-negativePoint3)/.001))/.001)
xValue=reSet#this resets xValue to its original value
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
increasingList = []
decreasingList = []

if xValue < 0 and xValue2 > 0:
    for i in range(0, (abs(xValue)*accuracy+abs((xValue2)*accuracy)+1)):
        nDer()
        nDer2()
        nDer3()
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
        if derSlope3>0 and derSlope2 <0 and derSlope == 0: #max
           increasingList.extend([increasing, increasing2])
           print(increasingList)
           increasing=reSet
           
        if derSlope3<0 and derSlope2 >0 and derSlope == 0: #min
           decreasingList.extend([decreasing, decreasing2])
           print(decreasingList)    
        
        xPoint += (1/accuracy) 
        xValue += (1/accuracy)
        
    if decreasing != 2222:
        print("function is increasing between x=" + str(increasing) + " and x=" + str(increasing2))
    if increasing != 3333:
        print("function is decreasing between x=" + str(decreasing) + " and x=" + str(decreasing2)) 
           
else:    
    for i in range(xValue*accuracy, ((xValue2)*accuracy)+1):
        nDer()
        nDer2()
        nDer3()
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
        elif derSlope3>0 and derSlope2 <0 and derSlope == 0: #max
           increasingList.extend(increasing, increasing2)
           print(increasingList)
        elif derSlope3<0 and derSlope2 >0 and derSlope == 0: #min
           decreasingList.extend(decreasing, decreasing2)
           print(decreasingList)
            
            
            
        
        xPoint += (1/accuracy) 
        xValue += (1/accuracy)
    if decreasing != 2222:
        print("function is increasing between x=" + str(increasing) + " and x=" + str(increasing2))
    if increasing != 3333:
        print("function is decreasing between x=" + str(decreasing) + " and x=" + str(decreasing2)) 