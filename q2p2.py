print "-"*30+"\nPersonal Information\n"+"-"*30
fullname=raw_input("Fullname:") 
address=raw_input("Address:")
age=raw_input("Age:")
mobile=raw_input("Mobile #:")
hobby=raw_input("Hobby:")
print "-"*30+"\nSchool\n"+"-"*30
school_name=raw_input("School Name:")
year=raw_input("Year:")
course=raw_input("Course:")
print "-"*30+"\nOutput Message\n"+"-"*30
print "Hi my name is %s and I live at %s. I am %s years old. My mobile number is %s. My hobby is %s. I am a %srd year %s student at %s"%(fullname,address,age,mobile,hobby,year,course,school_name)
