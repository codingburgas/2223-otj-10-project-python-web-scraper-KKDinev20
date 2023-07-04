import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

print("Quote Authors and Their Quotes:\n")

f = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(f.text, 'html.parser')

authors = {}

for i in soup.findAll("div", {"class": "quote"}):
    author = i.find("small", {"class": "author"}).text
    quote = i.find("span", {"class": "text"}).text
    if author in authors:
        authors[author].append(quote)
    else:
        authors[author] = [quote]

for author, quotes in authors.items():
    print(f"{author}")
    for quote in quotes:
        print(f"- {quote}\n")
    print()


quotes = []

for i in soup.findAll("div", {"class": "tags"}):
    quotes.append(i.find("meta")['content'])

letter_counts = {}

print()

for quote in quotes:
    quote_lower = quote.lower()
    for char in quote_lower:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

# Sort the letter counts in alphabetical order
sorted_counts = sorted(letter_counts.items(), key=lambda x: x[0])

all_letters = [letter for letter, count in sorted_counts]
all_counts = [count for letter, count in sorted_counts]

# Plot the all letters count bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(all_letters, all_counts, color='steelblue')
plt.xlabel('Letter')
plt.ylabel('Count')
plt.title('Occurrences of Letters in Quotes')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.bar_label(bars, label_type='edge', fmt='%d', fontsize=8)

plt.tight_layout()
plt.show()


sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

top_10_letters = ['e', 'a', 'i', 'o', 'u', 't', 'n', 's', 'r', 'l']
letter_counts = [34, 28, 27, 24, 19, 18, 17, 16, 15, 14]

plt.pie(letter_counts, labels=top_10_letters, autopct='%1.1f%%')

# Set aspect ratio to be equal so that pie is drawn as a circle
plt.axis('equal')

# Set title
plt.title('Top 10 Most Common Letters')

# Show the pie chart
plt.show()