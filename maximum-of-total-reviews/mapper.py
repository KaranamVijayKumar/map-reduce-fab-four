# imported csv package to read file
import csv
# Reading Hotel_Reviews CSV file into input variable
input = open("Hotel_Reviews.csv", "r")
# Writing the mapper output to output1.txt
output = open("output1.txt", "w")
# Initializing the counter variable to 0
counter = 0
# Writing for each loop to iterate over the input file
for line in input:
    datalist = line.strip().split(",")
    # Storing values of Hotel_name and Reviewer_Reviews
    Hotel_Name, Reviewer_Reviews = datalist[4], datalist[11]
    output.write(Hotel_Name + "\t" + Reviewer_Reviews + "\n")
    counter = counter + 1