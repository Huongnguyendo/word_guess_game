import bs4
from bs4 import BeautifulSoup as soup
import pandas as pd
import csv

#find most common English words
my_url = r'https://1000mostcommonwords.com/1000-most-common-english-words/'

# Returns list of all tables on page
tables = pd.read_html(my_url) 

# Choose the first table in the list
word_table = tables[0]

# Turn the words column into a list
col_two_list = word_table[2][1:].tolist()

# Choose only words that longer than 5 letters
word_list = [word for word in col_two_list if len(word) > 5]

# create a csv file with the word list above
with open('secret_words.csv', 'w') as file:
    for word in word_list:
        file.write(word + "\n")

