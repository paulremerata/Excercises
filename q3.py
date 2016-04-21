from random import randint
from os import system
def main(number,count):
	guess=guessCheck(int(raw_input("Enter a number from 1 to 100:")),number,count)
	count+=1
	if guess==number:
		print "It took you %i tries to guess the number" %(count)
	else:
		system('clear')
		print( "Higher!!!" if guess<number else "Lower!!!")
		main(number,count)
def guessCheck(guess,number,count):
	system('clear')
	return guess if 1<=guess<=100 else main(number,count)
main(randint(1,100),0)
