# Giving the mapper's output as input to the reducer
s = open("output1.txt","r")
r = open("output2.txt", "w")

# Initializing the values
thisKey = ""
thisValue = 0.0
next(s)

for line in s:
    data = line.strip().split('\t')
    Hotel_Name, Reviewer_Reviews = data
    if Hotel_Name != thisKey:
        if thisKey:
             r.write(thisKey + '\t' + str(thisValue)+'\n')
        thisKey = Hotel_Name 
        thisValue = 0.0
    thisValue += float(Reviewer_Reviews)
list1 = [thisValue]
r.write(thisKey + '\t' + str(thisValue)+'\n')
r.write(str(list1))

# creatinng a dictionary 
d = dict((line.strip().split('	') for line in open("output2.txt")))

abc = list((d.values()))
newList = []
# loop for adding each value to newlist  
for each in abc:
  newList.append(float(each))

minValue = min((newList))

keyValue = "" 
# loop for finding minmum value
for key, value in d.items():
  if float(value) == minValue:
    keyValue = key
    break


output = open("finaloutput.txt", "w")
output.write(keyValue + '\t'+ str(minValue)+'\n')
# printing the key value pairs
print(keyValue,' : ',minValue)

s.close()
r.close()    
