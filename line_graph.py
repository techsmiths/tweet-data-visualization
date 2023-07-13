import pandas as pd
import matplotlib.pyplot as plt
import sys

# Set the number of rows to read
n_rows = None

# Read the CSV file, specifying the encoding and number of rows to read
data = pd.read_csv('data.csv', encoding='latin1', nrows=n_rows)

print("Original data:")
print(data.head())
print()

# Convert the 'date of the tweet' column to datetime format
print("Converting 'date of the tweet' column to datetime format...")
data['date of the tweet'] = pd.to_datetime(data['date of the tweet'], format='%a %b %d %H:%M:%S PDT %Y')
print()

# Extract the hour from the 'date of the tweet' column
print("Extracting hour from 'date of the tweet' column...")
data['hour'] = data['date of the tweet'].dt.hour
print()

print("Data with hour extracted:")
print(data.head())
print()

# Group the data by hour and calculate the average tweets per hour
print("Calculating the average tweets per hour...")
hourly_tweets = data.groupby('hour').size()
print()

print("Hourly tweet count:")
print(hourly_tweets)
print()

# Print total tweet count
total_tweets = hourly_tweets.sum()
print(f"Number of Total tweets analyzed: {total_tweets}")
print()

# Create the line graph
print("Creating the line graph...")
plt.plot(hourly_tweets.index, hourly_tweets.values)
plt.xlabel('Hour of Day')
plt.ylabel('Tweet Volume')
plt.title('Volume of Tweets by Hour of Day')
plt.xticks(range(25))
plt.grid(True)
print()

# Check if "download" argument is passed
if "download" in sys.argv:
    # Save the graph as an image file
    plt.savefig('tweet_volume_graph.png')
    print("Graph saved as 'tweet_volume_graph.png'")
else:
    # Display the graph
    print("Displaying the graph...")
    plt.show()

