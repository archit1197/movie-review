import csv
#l1 will be a list, the data type storing all information in file.
#Used this as it is easy to access
#first row contains headers, names of films
#subsequent rows contain user_name and list of all his ratings
from math import sqrt
l=list()
l1=list()
mo=list()
count=0
def csv_reader(file1):

	reader=csv.reader(file1,delimiter=',')
	global count	
	for line in reader:
		#print line[0]
		if(count==0):
			l1.append(line)
		else:
			line1=line[0]
			line=line[1:]
			line2=[float(i) for i in line]
			listfinal=[line1,line2]
			l1.append(listfinal)
			
		#print (line)
		#d[key]=line
		count+=1
		#del d[key]['Name']

with open("movie-ratings.csv") as fileobject:
	csv_reader(fileobject)
#print l1
count=0
def csv_reader(file1):

	global l
	global mo
	global count
	reader=csv.reader(file1,delimiter=',')
	for line in reader:
		if(count==0):
			mo=line
		else:
			l=[float(i) for i in line]
		count+=1
		#print l		
		if(count==2):
			break
		

with open("user-preference.csv") as fileobject:
	csv_reader(fileobject)
	
#print (l)
name=input("Please enter your name:")
print("Hello "+name+' ! ')

print (l1[0])
i=0
x=l
l1[0].append('Distance')
#print (x)
print (l1[1][1][l1[0].index(mo[1])])
#calculating euclidean distance
for i in range(1,len(l1)):
	distance=0
	for j in range(len(x)):
		
		if((l1[i][1][l1[0].index(mo[j])-1])!=-1 and x[j]!=-1):
			distance+=(l1[i][1][l1[0].index(mo[j])-1]-x[j])**2
	distance=sqrt(distance)
	l1[i].append(distance)

#print (l1)

list2=l1[1:]
#sorting the list according to the [2]th value, which is the euclidean distance 
list2.sort(key=lambda x: float(x[2]))
print (list2)



