import json
from datetime import datetime

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

print(sorted_following)

#earliest following
earliest_following = sorted_following[0]
print(earliest_following)

#latest following
latest_following = sorted_following[-1]
print(latest_following)

    


