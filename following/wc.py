import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#read json file
with open("facebook/connections/followers/who_you've_followed.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#extract following names
follower_names = [entry["name"] for entry in data["following_v3"]]

#combine all names for wordcloud as a single string with space separated
names_text = " ".join(follower_names)

# create word cloud
wordcloud = WordCloud(
    width = 800,
    height = 400,
    background_color = 'white',
    colormap = 'viridis',
    max_words = 200,
    min_font_size = 10
).generate(names_text)

#display the word cloud

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Followers Name Word Cloud', fontsize = 18, pad=15)
plt.show()
