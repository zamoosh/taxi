import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

PATH = "./ABC_Taxi_Part1/ABC_Taxi_Data.csv"


# PATH = "./data.csv"


def main():
    df = pd.read_csv(PATH)  # Replace 'your_dataset.csv' with the actual dataset file name

    # Display the first few rows of the dataframe
    print(df.head())

    # Display the size of the dataframe
    print(df.shape)

    # Display basic statistics of the dataframe
    print(df.describe())

    # Display information about the dataframe
    print(df.info())

    # Convert data columns to datetime
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # Calculate trip duration in minutes
    df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60

    # Plot box plot of trip_distance
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='trip_distance')
    plt.title('Box Plot of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.show()

    # Plot histogram of trip_distance
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='trip_distance', bins=50, kde=True)
    plt.title('Histogram of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Frequency')
    plt.show()

    # Plot box plot of total_amount
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='total_amount')
    plt.title('Box Plot of Total Amount')
    plt.xlabel('Total Amount ($)')
    plt.show()

    # Plot histogram of total_amount
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='total_amount', bins=50, kde=True)
    plt.title('Histogram of Total Amount')
    plt.xlabel('Total Amount ($)')
    plt.ylabel('Frequency')
    plt.show()

    # Plot box plot of tip_amount
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='tip_amount')
    plt.title('Box Plot of Tip Amount')
    plt.xlabel('Tip Amount ($)')
    plt.show()

    # Plot histogram of tip_amount
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='tip_amount', bins=50, kde=True)
    plt.title('Histogram of Tip Amount')
    plt.xlabel('Tip Amount ($)')
    plt.ylabel('Frequency')
    plt.show()

    # Plot histogram of tip_amount by vendor
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='tip_amount', hue='VendorID', bins=50, kde=True)
    plt.title('Histogram of Tip Amount by Vendor')
    plt.xlabel('Tip Amount ($)')
    plt.ylabel('Frequency')
    plt.show()

    # Plot histogram of tip_amount by vendor for tips > $10
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df[df['tip_amount'] > 10], x='tip_amount', hue='VendorID', bins=50, kde=True)
    plt.title('Histogram of Tip Amount by Vendor for Tips > $10')
    plt.xlabel('Tip Amount ($)')
    plt.ylabel('Frequency')
    plt.show()

    # Calculate mean tips by passenger_count
    mean_tips_by_passenger_count = df.groupby('passenger_count')['tip_amount'].mean().reset_index()

    # Create bar plot for mean tips by passenger count
    plt.figure(figsize=(10, 6))
    sns.barplot(data=mean_tips_by_passenger_count, x='passenger_count', y='tip_amount')
    plt.title('Mean Tips by Passenger Count')
    plt.xlabel('Passenger Count')
    plt.ylabel('Mean Tip Amount ($)')
    plt.show()

    # Create a month column
    df['month'] = df['pickup_datetime'].dt.month

    # Create a day column
    df['day'] = df['pickup_datetime'].dt.day_name()

    # Get total number of rides for each month
    rides_per_month = df['month'].value_counts().sort_index()

    # Create a bar plot of total rides per month
    plt.figure(figsize=(10, 6))
    rides_per_month.plot(kind='bar')
    plt.title('Total Rides per Month')
    plt.xlabel('Month')
    plt.ylabel('Total Rides')
    plt.show()

    # Get total number of rides for each day of the week
    rides_per_day = df['day'].value_counts().sort_index()

    # Create bar plot for ride count by day
    plt.figure(figsize=(10, 6))
    rides_per_day.plot(kind='bar')
    plt.title('Total Rides per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Total Rides')
    plt.show()

    # Get total revenue by day of the week
    revenue_per_day = df.groupby('day')['total_amount'].sum().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # Create bar plot of total revenue by day
    plt.figure(figsize=(10, 6))
    revenue_per_day.plot(kind='bar')
    plt.title('Total Revenue per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Total Revenue ($)')
    plt.show()

    # Get total revenue by month
    revenue_per_month = df.groupby('month')['total_amount'].sum()

    # Create a bar plot of total revenue by month
    plt.figure(figsize=(10, 6))
    revenue_per_month.plot(kind='bar')
    plt.title('Total Revenue per Month')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue ($)')
    plt.show()

    # Get number of unique drop-off location IDs
    unique_dropoff_locations = df['DOLocationID'].nunique()

    # Calculate the mean trip distance for each drop-off location
    mean_distance_by_dropoff = df.groupby('DOLocationID')['trip_distance'].mean().sort_values(ascending=False)

    # Create a bar plot of mean trip distances by drop-off location in ascending order by distance
    plt.figure(figsize=(10, 6))
    mean_distance_by_dropoff.plot(kind='bar')
    plt.title('Mean Trip Distances by Drop-Off Location')
    plt.xlabel('Drop-Off Location ID')
    plt.ylabel('Mean Trip Distance (miles)')
    plt.show()


if __name__ == '__main__':
    main()
