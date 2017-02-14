from os import path
from wordcloud import WordCloud, STOPWORDS
import pandas as pd


d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'single_page_consumer_complaints.json')).read()

#all_complaints  = pd.read_json('paged_consumer_complaints.json')

#print (all_complaints.head())

stopwords = set(STOPWORDS)

stopwords.add("u00e2")
stopwords.add("u0080")
stopwords.add("u00c2")
stopwords.add("u0080")
stopwords.add("u0094")
stopwords.add("u201d")
stopwords.add("complaint")
stopwords.add("title")
stopwords.add("createdby")
stopwords.add("u20ac")
stopwords.add("feb")



# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
