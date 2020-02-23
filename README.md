# map-reduce-fab-four
This repo is created to do a map-reduce group project on a simple data set.

# Map-Reduce-Fab-Four
## Course: BIG DATA SP20
## Developers
1. Vijay Kumar Karanam
2. Harsha Vardhan Reddy Nallavolu
3. Lavanya Reddy Uppula
4. Prajakt Uttamrao Khawase

## Links
- [Source_Repo](https://github.com/KaranamVijayKumar/map-reduce-fab-four)
- [Website](https://karanamvijaykumar.github.io/map-reduce-fab-four/)
- [Issue_Tracker](https://github.com/KaranamVijayKumar/map-reduce-fab-four/issues)
- [Data_Source](https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe)

## Introduction
The data was scraped from Booking.com. All data in the file is publicly available to everyone already. Data is originally owned by Booking.com.

## V's of the data

The key attributes of the data set are Hotel_Name, Review_Total_Negative_Word_Counts, Total_Number_of_Reviews, and Review_Total_Positive_Word_Counts.

- V's for the new Identified Data set: -

1. Volume: - The Volume of the data is 227 MB and it contains 17 fields.

2. Variety: - The data is structured in CSV format and it is clean.

3. Velocity: - Currently the velocity of the data set is zero as all the data is historical data and no incoming data will come to the data set.

4. Veracity: - The data is clean and contains 515,000 customer reviews and scoring of 1493 luxury hotels across Europe.

5. Value: - We can cluster the hotels based on the reviews and perform sentimental analysis on the reviews.

## Big Data Problems

Below are a few problem statements we can phrase from the data set.

- For each Hotel, find the count of positive_word_reviews.
- For each Hotel, find the count of negative_word_reviews.
- For each Reviewer_Nationality, find the average of reviewer_score.
