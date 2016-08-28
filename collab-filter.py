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

#print (l1[0])
i=0
x=l
l1[0].append('Distance')


for i in range(1,len(l1)):
	pearson=0
	list_of_indices=[]
	mean_x=0
	mean_y=0
	for j in range(len(x)):
		if(l1[i][1][l1[0].index(mo[j])-1]!=-1 and x[j]!=-1):
			list_of_indices.append(j)
			mean_y+=l1[i][1][l1[0].index(mo[j])-1]
			mean_x+=x[j]
	#calculation of mean of user input ratings and for the user values already input
	mean_x=mean_x/len(list_of_indices)
	mean_y=mean_y/len(list_of_indices)
	numerator=0
	denominator1=0
	denominator2=0
	for j in list_of_indices:
		#calculation of pearson coefficient
		numerator+=(x[j]-mean_x)*(l1[i][1][l1[0].index(mo[j])-1]-mean_y)
		denominator1+=(x[j]-mean_x)*(x[j]-mean_x)
		denominator2+=(l1[i][1][l1[0].index(mo[j])-1]-mean_y)*(l1[i][1][l1[0].index(mo[j])-1]-mean_y)
	
	if(denominator1*denominator2!=0):
		pearson=numerator/sqrt(denominator1*denominator2)
	else:
		pearson=0
	l1[i].append(pearson)

#print (l1)

list2=l1[1:]
#sort values according to the pearson correlation calculated
list2.sort(key=lambda x: float(x[2]))
print (list2)



