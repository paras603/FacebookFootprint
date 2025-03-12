import json
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#read json file
with open("facebook/connections/followers/who_you've_followed.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#convert unix timestamp format to readable time format
for entry in data['following_v3']:
    timestamp = entry['timestamp']
    readable_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    entry['timestamp'] = readable_date

    # Print updated data with readable dates
# for entry in data["following_v3"]:
#     print(f"Name: {entry['name']}, Followed On: {entry['timestamp']}")


#sort the list according to date
sorted_following = sorted(data['following_v3'], key=lambda x: datetime.strptime(x["timestamp"], '%Y-%m-%d %H:%M:%S'))

# print(sorted_following)

#earliest following
earliest_following = sorted_following[0]
# print(earliest_following)

#latest following
latest_following = sorted_following[-1]
# print(latest_following)



# Create a dictionary to store following people by year and month
following_by_month = defaultdict(list)

# Loop through followers and group by year and month
for entry in data["following_v3"]:
    # Extract year and month from timestamp
    follow_date = datetime.strptime(entry["timestamp"], '%Y-%m-%d %H:%M:%S')

    year_month = follow_date.strftime('%Y-%m')  # Format as 'YYYY-MM'
    
    following_by_month[year_month].append(entry["name"])


# Print followers grouped by year and month
for year_month, followers in following_by_month.items():
    print(f"{year_month}: {len(followers)}")


from collections import defaultdict

# Create a dictionary to count followers per day
followers_per_day = defaultdict(int)

# Convert timestamps to 'YYYY-MM-DD' format and count
for follower in data["following_v3"]:
    date = follower['timestamp']
    followers_per_day[date] += 1

# Convert to a sorted list of (date, count) tuples
sorted_followers_per_day = sorted(followers_per_day.items())

# Print the result
print(sorted_followers_per_day)


# matplotlib

# Extract dates and counts
dates, counts = zip(*sorted_followers_per_day)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(dates, counts, marker='o', linestyle='-', color='b')

# Labels
plt.xlabel("Date Followed")
plt.ylabel("Number of Followers")
plt.title("Followers Per Day")
plt.xticks(rotation=45)
plt.grid()

# Show plot
plt.show()

    


