import json

# open and load the JSON file
file_path = 'facebook/connections/followers/people_who_followed_you.json'
with open(file_path, "r", encoding="utf-8") as file:
    followers_data = json.load(file)

# print the data to see how it looks
print(followers_data)

#extract the list of followers
followers = followers_data['followers_v3']

#count the number of followers
total_followers = len(followers)

#print the result
print(f'Total nuber of followers: {total_followers}')


# visualizing follower data with bar charts
import matplotlib.pyplot as plt

plt.bar(["Followers"], [total_followers], color='skyblue')
plt.title("Total number of Followers")
plt.ylabel("Count")
plt.show()



# real world example: follower count over time

import pandas as pd

# # convert to pandas data frame
# df = pd.DataFrame(followers)

# # convert 'date' to a datetime object
# df['date'] = pd.to_datetime(df['date'])

# # plot the number of followers over time
# plt.figure(figsize=(8,5))
# df.groupby(df['date']).size().plot(marker='o', kind='line')
# plt.title("Follower Growth Over Time")
# plt.xlabel("Date")
# plt.ylabel("Number of Followers")
# plt.show()

# Convert to pandas DataFrame
df = pd.DataFrame(followers)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort data by date
df = df.sort_values(by='date')

# Count new followers per day
daily_followers = df.groupby(df['date']).size()

# Calculate cumulative sum to get total followers over time
total_followers_over_time = daily_followers.cumsum()

# Plot total followers over time
plt.figure(figsize=(8,5))
total_followers_over_time.plot(marker='o', linestyle='-')

# Add labels and title
plt.title("Total Followers Growth Over Time")
plt.xlabel("Date")
plt.ylabel("Total Followers")
plt.grid(True)

# Show the graph
plt.show()



# word cloud of follower names

from wordcloud import WordCloud

# join all names into one large string
names = " ".join(follower["name"] for follower in followers)

#generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(names)

#display the word cloud
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
