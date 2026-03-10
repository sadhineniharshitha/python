
Fee=50000
gpa=float(input("Enter the CGPA:"))
if gpa>=9.0:
    totalfee=Fee-(Fee*0.3)
    print("Your College Fee is with 30 percent discount",totalfee)
elif gpa>=8.5 and gpa<9.0:
    totalfee=Fee-(Fee*0.2)
    print("Your College Fee is with 20 percent discount",totalfee)  
elif gpa>=8.0 and gpa<8.5:
    totalfee=Fee-(Fee*0.1)
    print("Your College Fee is with 20 percent discount",totalfee)  
else:
    print("Your College Fee without any discount",Fee)    