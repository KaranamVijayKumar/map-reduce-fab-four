import csv
# opened the input and output files
input = open("Hotel_Reviews.csv", "r")
output = open("output1.txt", "w")

counter = 0

for line in input:
    datalist = line.strip().split(",")    
    Hotel_Name, Reviewer_Reviews = datalist[4], datalist[11]
    # writing output to the output files
    output.write(Hotel_Name + "\t" + Reviewer_Reviews + "\n")
    counter = counter + 1
# Closed the input and output files
input.close()
output.close()