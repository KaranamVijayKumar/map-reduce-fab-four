# Opening the output of mapper file and storing in variable s
s = open("output1.txt","r")
# Writing the output file in output2.txt and storing in r variable
r = open("output2.txt", "w")
thisKey = ""
thisValue = 0.0
# Skipping the firstline
next(s)
# for loop to iterate the file
for line in s:
    data = line.strip().split('\t')
    Hotel_Name, Reviewer_Reviews = data
    if Hotel_Name != thisKey:
        if thisKey:
            # output the last key value pair result
             r.write(thisKey + '\t' + str(thisValue)+'\n')
        # start over when changing keys
        thisKey = Hotel_Name 
        thisValue = 0.0
    # apply the aggregation function
    thisValue += float(Reviewer_Reviews)
list1 = [thisValue]
r.write(thisKey + '\t' + str(thisValue)+'\n')
r.write(str(list1))

# creating a dictionary for the output2 file
d = dict((line.strip().split('	') for line in open("output2.txt")))

# creating a list for values in it
abc = list((d.values()))
newList = []
# iterating over the list to find max value
for each in abc:
  newList.append(float(each))

maxValue = max((newList))

keyValue = "" 
# iterating over key value pairs and printing max value in console
for key, value in d.items():
  if float(value) == maxValue:
    keyValue = key
    break

# creating a final output file to store max value
output = open("finaloutput.txt", "w")
output.write(keyValue + '\t'+ str(maxValue)+'\n')

print(keyValue,' : ',maxValue)

s.close()
r.close()    
