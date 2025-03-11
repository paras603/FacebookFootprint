import json
import os


# LOAD AND INSPECT JSON FILES

# Define the folder where the extracted JSON files are located
comments_folder_path = "facebook/facebook_activity/comments_and_reactions" # Change this to your actual folder path

# List JSON files
files = [f for f in os.listdir(comments_folder_path) if f.endswith(".json")]
print("Available JSON files:", files)

# Load a sample file (e.g., messages.json)
file_path = os.path.join(comments_folder_path, "comments.json")
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Print the keys (structure of the file)
print("Data keys:", data.keys())

# Preview some data
print(json.dumps(data, indent=4)[:1000])  # Print only the first 1000 characters for readability





# EXTRACT AND ANALYSE INTERACTION DATA
# EXTRACT FRIENDS AND MESSAGES DATA


# import json
# import os
import pandas as pd
from datetime import datetime

# Define the folder where the extracted JSON files are located
folder_path = "path_to_your_extracted_facebook_data"  # Update with your actual path

# Load messages.json
file_path = os.path.join(folder_path, "messages.json")
with open(file_path, "r", encoding="utf-8") as f:
    messages_data = json.load(f)

# Convert to DataFrame
messages_df = pd.DataFrame(messages_data["messages"])

# Display first few rows of the DataFrame
print(messages_df.head())  # Check the first few rows to understand the structure

# Convert timestamp to a readable format
messages_df["timestamp_ms"] = pd.to_datetime(messages_df["timestamp_ms"], unit="ms")

# Filter messages from the last 2 years
two_years_ago = datetime.now() - pd.DateOffset(years=2)
active_friends = messages_df[messages_df["timestamp_ms"] > two_years_ago]

# Get unique friends interacted with
active_friend_list = active_friends["sender_name"].unique()

# Print the list of active friends
print("Friends you've interacted with in the last 2 years:", active_friend_list)



# IDENTIFY INACTIVE FRIENDS

# import json
# import os
# import pandas as pd

# Define the folder where the extracted JSON files are located
folder_path = "path_to_your_extracted_facebook_data"  # Update with your actual path

# Load friends.json
file_path = os.path.join(folder_path, "friends.json")
with open(file_path, "r", encoding="utf-8") as f:
    friends_data = json.load(f)

# Extract friend names
# Ensure the correct key name based on the structure of your friends.json file
all_friends = [friend["name"] for friend in friends_data["friends"]]  # Change key if necessary

# Find inactive friends by comparing with the active friends list
inactive_friends = list(set(all_friends) - set(active_friend_list))

# Print inactive friends
print("Inactive friends:", inactive_friends)

# Save to CSV for manual unfriending
pd.DataFrame(inactive_friends, columns=["Friend Name"]).to_csv("inactive_friends.csv", index=False)




# VISUALIZING YOUR INTERACTION TRENDS
# PLOT INTERACTIONS OVER TIME

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'messages_df' is the DataFrame that contains your messages data, with 'timestamp_ms' already converted to datetime

# Set up the plot
plt.figure(figsize=(10, 5))  # Set the figure size

# Plot histogram with KDE to show interactions over time
sns.histplot(messages_df['timestamp_ms'], bins=50, kde=True)

# Customize the plot
plt.title("Your Interaction Trend Over Time")  # Title of the plot
plt.xlabel("Date")  # Label for the x-axis
plt.ylabel("Number of Interactions")  # Label for the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the plot
plt.tight_layout()
plt.show()

