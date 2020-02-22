# opening the positive.txt file
p = open("positive.txt", "r")
# Created output file reduce_positive.txt
rp = open("reduce_positive.txt", "w")

thisKey = ""
next(p)
#using for loop to iterate through the input
for line in p:
    data = line.strip().split('\t')
    Hotel, Review = data
    if Hotel != thisKey:
        if thisKey:
             rp.write(thisKey + '\t' + str(thisValue)+'\n')
        
        thisKey = Hotel 
        thisValue = 0

    thisValue += int(Review)
list1 = [thisValue]

rp.write(thisKey + '\t' +  str(thisValue)+'\n')
rp.write(str(list1))
#closing input and output files
p.close()
rp.close()    