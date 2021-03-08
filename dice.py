#import module
import random
#create a dice
small = 1
large = 6
print("Please enter a number of dice to roll: ")
userin = int(input())
for i in range(userin) :
	print("Dice ", i + 1 , " result:", random.randint(small, large),"\n")
	

