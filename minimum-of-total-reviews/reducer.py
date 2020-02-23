s = open("output1.txt","r")
r = open("output2.txt", "w")
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


d = dict((line.strip().split('	') for line in open("output2.txt")))

abc = list((d.values()))
newList = []

for each in abc:
  newList.append(float(each))

maxValue = min((newList))

keyValue = "" 

for key, value in d.items():
  if float(value) == maxValue:
    keyValue = key
    break


output = open("finaloutput.txt", "w")
output.write(keyValue + '\t'+ str(maxValue)+'\n')

print(keyValue,' : ',maxValue)

s.close()
r.close()    
