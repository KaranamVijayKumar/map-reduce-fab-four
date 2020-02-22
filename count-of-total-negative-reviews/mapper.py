# importing the csv file into mapper
import csv
# opening the csv file in read mode and assigning it to variable input
input = open("Hotel_Reviews.csv", "r")
# Created the 01.txt file and output variable to write mapper output in 01.txt
output = open("01.txt", "w")
# Created count variable to count the number of lines in 01.txt
counter = 0
# Wrote the for loop to iterate over each line in input variable,
#  removed the extra spaces after and before the line and stored
#  the comma seperated value into a list.
for line in input:
    datalist = line.strip().split(",")
    # Stored the respective columns into respective variables.
    Hotel_Name, Review_Total_Negative_Word_Counts = datalist[4], datalist[7]
