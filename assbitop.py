#Assignment operators
no=10
no*=5
print(no)

no=10
no/=2
print(no)

no=20
no+=5
print(no)

no=10
no//=2
print(no)

no=10
no%=2
print(no)


#is isnot---->identity operator
# in notin--> membership operator


stmt="today it is raining here"
print('raining' is stmt)
print('drizziling'is not stmt)
name='devi'
print('d' is name)
print('l' is not name)




no1=input("enter first number:")
no2=input("enter second number:")
if no1>=no2:
	print("correct")
else:
	print("not correct")


#ternary operator

no1,no2=15,12
result=no1 if no1<no2 else no2
print(result)














