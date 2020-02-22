# opening the 01.txt file in read mode and assigning it to variable s
s = open("01.txt","r")
# Created the 02.txt file and r variable to write reducer output in 02.txt
r = open("02.txt", "w")
# added the variable thisKey with empty String and float variable thisValue
thisKey = ""
thisValue = 0.0
# Skipping the firstline in the 01.txt file
next(s)
#  Wrote the for loop to iterate over each line in input variable,
#  removed the extra spaces after and before the line and stored
#  the tab seperated value into a list.
for line in s:
    data = line.strip().split('\t')
    # Stored the respective columns into respective variables.
    Hotel, Review = data
    #  Checking whether the value for hotel is empty or not
    if Hotel != thisKey:
        if thisKey:
            # output the last key value pair result
             r.write(thisKey + '\t' + str(thisValue)+'\n')
        # start over when changing keys
        thisKey = Hotel 
        thisValue = 0.0
    # apply the aggregation function
    thisValue += float(Review)