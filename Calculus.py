import math
#make sure that if you need to do trig do "math.()"
yFunction = str(input("y="))
reSet = int(input("Where does your interval start? "))
xValue2 = int(input("And where does it end? "))
#Accuracy = input("How accurate do you want the graph to be?")

xValue=reSet
def funcTion():
    yFunctionNew = ""
    
    for i in range(len(yFunction)):
        if yFunction[i] == "x":
            yFunctionNew += str(xValue)
        else:
            yFunctionNew += yFunction[i]

    i += 1

    #print (yFunctionNew)
    print (eval(yFunctionNew))
    
for i in range(xValue, xValue2+1):
    funcTion()
    xValue+=1

xValue=reSet
smallest=1000
biggest=-1000
for i in range(xValue, xValue2+1):
    if xValue>=biggest:
        biggest=xValue
    if xValue<=smallest:
        smallest=xValue
    xValue+=1

print("Absolute Max at: x={0}".format(biggest))
print("Absolute Min at: x={0}".format(smallest))