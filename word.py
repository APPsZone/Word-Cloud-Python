import sys
from typing import Text
import numpy as np
from PIL import Image
import wikipedia # to extract an information
from wordcloud import WordCloud, STOPWORDS

# we will import STOPWORDS to remove common words like "the, a, than, here, after"

a = str(input("Enter the name of which you want to make word cloud: "))
title = wikipedia.search(a)[0] # it will search the title from the wikipedia
page = wikipedia.page(title) # it will search the page related to given topic in wikipedia
text = page.content # to extract the content of that topic
print(text)

bg = np.array(Image.open("black wallpaper.jpg")) # background image which our words will be printed
unwanted_words = set(STOPWORDS)
wordcloud = WordCloud(background_color="black", max_words=400, mask = bg, stopwords=unwanted_words)
wordclo.generate(text)
wordclo.to_file("sample.png") # the name of  your file you want to save
