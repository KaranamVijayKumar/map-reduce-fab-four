# Opening the output of mapper file and storing in variable s
s = open("output1.txt","r")
# Writing the output file in output2.txt and storing in r variable
r = open("output2.txt", "w")
thisKey = ""
thisValue = 0.0
# Skipping the firstline
next(s)