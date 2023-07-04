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

# Sort the letter counts by count value in descending order
sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

top_10_letters = [letter for letter, count in sorted_counts[:10]]
top_10_counts = [count for letter, count in sorted_counts[:10]]


# Calculate the percentages for each letter count
total_count = sum(top_10_counts)
percentages = [(count / total_count) * 100 for count in top_10_counts]

# Plot the top 10 most common letters bar chart with percentages
plt.figure(figsize=(10, 6))
bars = plt.bar(top_10_letters, top_10_counts, color='salmon')
plt.xlabel('Letter')
plt.ylabel('Count')
plt.title('Top 10 Most Common Letters')
plt.xticks(rotation=45)

for i, count in enumerate(top_10_counts):
    percentage = percentages[i]
    plt.text(i, count, f'{percentage:.1f}%', ha='center', va='bottom')

plt.grid(axis='y')
plt.tight_layout()
plt.show()
