a=[]
arr=[]
def assign(n):
	for i in range (0,n):
		a.append(i+1)
def printIt(i,n):
	if i==n:
		string=""
		for j in range(0,n):
			string=string+str(a[j])
		arr.append(string)
	else:
		for j in range(i,n):
			a[i],a[j]=a[j],a[i]
			printIt(i+1,n)
			a[i],a[j]=a[j],a[i]
t=int(raw_input())
for i in range(0,t):
	n=int(raw_input())
	assign(n)
	printIt(0,n)
	arr.sort();
	print (" ".join(arr))
	a[:]=[]
	arr[:]=[]
