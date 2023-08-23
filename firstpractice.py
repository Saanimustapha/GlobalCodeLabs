#Converts 32 degrees to radian
from math import pi
import time

degrees = 32
radians = (32/180)* pi
radians = round(radians,2)
print(str(degrees)+' degees is equivalent to '+str(radians)+ ' radians.')


#Asks the user for a radius then prints out the surface area and volume of a sphere.
radius = int(input('Enter the radius: '))
surfaceArea = 4*(pi*(radius**2))
surfaceArea = round(surfaceArea,2)
volume = 4/3 * (pi*(radius**3))
volume = round(volume,2)
print('Surface area: '+ str(surfaceArea) + ' square units.')
print('Volume: '+ str(volume) + ' cubic units.')


#Tells the user what time of day it is, in a nice format.
timeInSeconds = time.time()
organizedTime = time.ctime(timeInSeconds)
print(organizedTime)

#Splits a sentence into its words
sentence = 'My name is kelvin cudjoe'
print(sentence.split())


#Joins a list of words into a sentence. Find TWO ways to do this!
#Method 1
listOfWords = ['My ','name ','is ','kelvin ','cudjoe']
lengthOfList = len(listOfWords)
count = 0
word = ''
while count <= (lengthOfList-1):
    word += listOfWords[count]
    count += 1
print(word)

#Method 2
print(''.join(listOfWords))







