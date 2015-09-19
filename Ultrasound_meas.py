import serial #import serial libray
from visual import * #import all vPython library (for visual interface)

arduinoSerialData = serial.Serial('com3',9600) #Create object for serial data from arduino

#set up virtual world
measuringRod = cylinder(length=50, color=color.yellow, radius=1, pos=(-15,0,0))
lengthLabel = label (text = 'Target Distance is: ', pos=(0,10,0), height=20, box=false)
target = box (color=color.green, length=2, width=10, height = 10, pos=(0,0,0))

while (1==1): #start forever loop to keep the program reading data
    rate(20) #rate of refresh required to draw
    if (arduinoSerialData.inWaiting()>0): #Check if we have data to read
        myData = arduinoSerialData.readline() #If data is present, it reads it
        distance = float(myData) #convert the string MyData to floating point
        myLabel = 'Target Distance is: '+ myData #string to plot the measurement (plot myData because is a string, distance is a number)
        lengthLabel.text = myLabel #update the label
        measuringRod.length=distance  #update cylinder size
        target.pos=(-15+distance,0,0) #update targe box position
