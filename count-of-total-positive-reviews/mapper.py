#impoting CSV file ino mapper
import csv

#openning the CSV file
input = open ("Hotel_Reviews.csv", "r")
#creating output text file positive.txt
output = open ("positive.txt", "w")

# using for loop to iterate through the input
counter = 0
for line in input:
    datalist = line.strip().split(",")
    Hotel_Name, Review_Total_Positive_Word_Counts = datalist[4], datalist[10]
    output.write(Hotel_Name + "\t" + Review_Total_Positive_Word_Counts + "\n")
    counter = counter + 1

#closing input and output files

input.close()
output.close()