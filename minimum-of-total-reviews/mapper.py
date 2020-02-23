import csv
input = open("Hotel_Reviews.csv", "r")
output = open("output1.txt", "w")

counter = 0

for line in input:
    datalist = line.strip().split(",")    
    Hotel_Name, Reviewer_Reviews = datalist[4], datalist[11]
    output.write(Hotel_Name + "\t" + Reviewer_Reviews + "\n")
    counter = counter + 1


input.close()
output.close()