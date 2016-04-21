from math import pi
from os import system
def multiplier(count,number,number1,):
	return number if count==1 else multiplier(count-1,number+number1,number1,)
def rectangle():
	l,w=int(raw_input("Length:")),int(raw_input("Width:"))
	print "The area is "+ str(multiplier(l,w,w))
def square():
	s=int(raw_input("Side:"))
	print "The area is "+ str(multiplier(s,s,s))
def circle():
	r=int(raw_input("Enter radius:"))
	print "The area is "+ str(multiplier(multiplier(r,r,r),pi,pi))
def triangle():
	b,h=int(raw_input("Base:")),int(raw_input("Height:"))
	print "The area is "+ str(multiplier(multiplier(b,h,h),0.5,0.5))
def main():
	system('clear')
	shape=raw_input("Choose a shape(circle,rectangle,square,triangle):")
	if shape.lower()=="circle":
		circle()
	elif shape.lower()=="rectangle":
		rectangle()
	elif shape.lower()=="triangle":
		triangle()
	elif shape.lower()=="square":
		square()
	else:
		print "Invalid input!"
	main() if raw_input("Again? (y/n)")=="y" else 1+1
main()

