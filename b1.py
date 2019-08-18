#input data
st=input("Enter a list of binary numbers \nNote that the numbers must be separated by commas: ")  
inputlist=st.split(',')
print("The list of numbers entered: {}".format(inputlist))
result=[]
#checking condition
l=len(inputlist)
for num in inputlist:
	n=int(num,2)
	if n%5==0:
		result.append(num)
#output 
print("Numbers divisible by 5 are: {}".format(','.join(result)))


