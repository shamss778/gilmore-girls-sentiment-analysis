import pandas as pd
import os

# Specify the folder path containing your CSV files
folder_path = 'C:/Users/asus/Desktop/Gilmore_girls_sentiment_analysis/CSV'

# Initialize a dictionary to store DataFrames
dataframes = {}

# Iterate over CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Drop 'Line' and 'Page' columns
        df = df.drop(['Line', 'Page'], axis=1)
        
        # Store the DataFrame in the dictionary, using the filename as the key
        dataframes[filename] = df

# Now you can access each DataFrame using the filename as the key
for filename, df in dataframes.items():
    print(f"DataFrame for {filename}:")
    print(df)
    print("\n")
