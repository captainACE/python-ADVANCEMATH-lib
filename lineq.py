#START PROGRAM
print ("SOLVE A LINEAR EQUATION BY CRAMER'S RULE OF DISCRIMINANTS")


#ax+by+c=0



#EQUATION 1 INPUTS
print("Equation.no.1")
a=int(input("number for 'a' term: "))
b=int(input("number for 'b' term: "))
c=int(input("number for 'c' term: "))




#EQUATION 1 CONDITIONS
if a == 0:
    print ('x','+',b,'y','=',c)

elif b == 0:
    print (a,'x','+','y','=',c)

elif c ==0:
    print (a,'x','+',b,'y','=',c)
	
elif c !=0:
    print (a,'x','+',b,'y','=',c)
	
elif b !=0:
    print (a,'x','+',b,'y','=',c)
elif a !=0:
    print (a,'x','+',b,'y','=',c)
	
else:
    print("u wot m8?")





#EQUATION 2 INPUTS
print("----------------------------")    
print("Equation.no.2")
k=int(input("number for 'k' term: "))
l=int(input("number for 'l' term: "))
m=int(input("number for 'm' term: "))




#EQUATION 2 CONDITIONS
if k == 0:
    print ('x','+',l,'y','=',m,)

elif l == 0:
    print (k,'x','+','y','=',m)

elif m ==0:
    print (k,'x','+',l,'y','=',m)
	
elif m !=0:
    print (k,'x','+',l,'y','=',m)
	
elif l !=0:
    print (k,'x','+',l,'y','=',m)

elif k !=0:
    print (k,'x','+',l,'y','=',m)
	
else:
    print("u wot m8?")



	

#EQUATION SOLVING LOGIC
print("--------------------------------------------")
print("The equation will be solved by cramer's rule")




#MATH LOGIC FOR CRAMER'S RULE
d =a*k-b*l
dx=b*l-c*m
dy=a*k-c*m
x =(dx/d)
y=(dy/d)




#FINAL PRINT COMMANDS
print('d=',d)
print('dx=',dx)
print('dy=',dy)
print('x=',x)
print('y=',y)

