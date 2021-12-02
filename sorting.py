#sorting

l=[2,6,1,9,8,7]
for i in range(len(l)):
	for j in range(i,len(l)):
		if l[i]>l[j]:
			temp=l[i]
			l[i]=l[j]
			l[j]=temp
print(l)

#sort in ascending order
l=[2,5,9,3,7]
l.sort()
print(l)
#sort in descending order
l=['b','d','a','c']
l.sort(reverse=True)
print(l)
#sort using key
l=['cc','aaa','dddd','b']
l.sort(key=len)
print(l)

#Ascending order based on the position

a=[[1,3],[4,2],[2,1]]
a.sort()
print(a)

print("--------------------------------")

def fun(element):
	return element[1]
a.sort(key=fun)
print(a)

#Bubble sort

l=[4,2,1,7,9,8]
for i in range(len(l)-1,-1,-1):
	for j in range(i):
		if l[j]>l[j+1]:
			temp=l[j]
			l[j]=l[j+1]
			l[j+1]=temp
print(l)


#max

a=[7,3,2,1,9]
maxvalue=0
for i in a:
	if i>maxvalue:
		maxvalue=i
else:
	print(maxvalue)


#min

l=[10,45,100,5,30]
minvalue=l[0]
for i in l:
	if i<=minvalue:
		minvalue=i
else:
	print(minvalue)

#sum

l=[10,20,30,40,50]
sum=0
for i in l:
	sum+=i
print(sum)

#avg

l=[10,20,30,40,50]
sum=0
for i in l:
	sum+=i
else:
	val=sum//len(l)
	print(val)



#clear

l=[10,20,50,60]
l=[]
print(l)


#copy

l=['a',10,'True',30.0]
a=l
print(a)

#count

l=[10,20,'a','x','c','d','a','b','c','a',20]
count=0
for i in range(len(l)):
	if l[i] in ['a']:
		count+=1
print(count)


#reverse

l=[10,'ab',10.0,'True']
l2=[]
for i in range(len(l)-1,-1,-1):
	print(i)
	l2.append(l[i])
print(l2)





























	



















			
