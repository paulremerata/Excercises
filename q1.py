def convert():
	x=raw_input("Convert to Fahrenheit or Celsius (f/c)?\n")
	y=raw_input("Enter Value:")
	if x=="f":
		print str(9*float(y)/5+32)+" F"
	elif x=="c":
		print str((float(y)-32)*5/9)+" C"
	else: 
		print "wrong input"
	again(raw_input("Again?(y/n)"))
def again(x):
	if x=="y":
		convert()
	elif x=="n":
		1+1
	else:
		again(raw_input("Again?(y/n)"))
convert()
