# tweet-data-visualization
a local client's project to visualize tweet data from a training data csv - it showcases the trend of tweet posting time in the training data


# Tweet Analysis

This project analyzes tweet data and provides insights into the tweet volume by hour of the day. It extracts the hour from the "date of the tweet" column, calculates the average number of tweets per hour, and visualizes the tweet volume using a line graph.

## Getting Started

### Prerequisites

- Python 3.x
- pandas
- matplotlib

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/tweet-data-visualization.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Usage

1. Prepare your data:

   - Ensure you have a CSV file named `data.csv` in the same directory as the Python script.
   - The CSV file should contain a column named 'date of the tweet' that represents the date and time of each tweet.
   - The 'date of the tweet' column should be in the format: 'DayOfWeek Month Day Hour:Minute:Second PDT Year'. For example: 'Tue Jul 10 12:04:32 PDT 2023'.

2. Open a command prompt or terminal and navigate to the directory where the script and the data file are located.

3. Run the script:

   ```shell
   python line_graph.py
   ```

4. The script will process the data and generate the following outputs:

   - The original data, showing the first few rows.
   - The 'date of the tweet' column converted to datetime format.
   - The hour extracted from the 'date of the tweet' column and added as a new column.
   - The data with the hour extracted, showing the first few rows.
   - The average number of tweets per hour.
   - The total number of tweets analyzed.
   - A line graph representing the tweet volume by hour of the day.

5. By default, the graph will be displayed. You can close the graph window to continue. If you want to save the graph as an image file, pass the "download" argument:

   ```shell
   python line_graph.py download
   ```

   The graph will be saved as 'tweet_volume_graph.png' in the same directory.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and use the code as per your needs.

## Contact

For any inquiries or suggestions, please contact Maruf Bin Salim at marufbinsalim01@gmail.com.
If you don't have your own tweet data, you can use the training data provided [here](data.csv).

**Note: If you use the provided training data, please make sure to credit the source.**
```

Make sure to update the contact information with the appropriate email address or contact details.
