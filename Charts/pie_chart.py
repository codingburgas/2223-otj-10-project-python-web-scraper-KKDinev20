import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


def view_pie_chart():
    f = requests.get('http://quotes.toscrape.com/')
    soup = BeautifulSoup(f.text, 'html.parser')

    quotes = []

    for i in soup.findAll("div", {"class": "tags"}):
        quotes.append(i.find("meta")['content'])

    letter_counts = {}

    for quote in quotes:
        quote_lower = quote.lower()
        for char in quote_lower:
            if char.isalpha():
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1

    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    top_10_letters = [letter for letter, count in sorted_counts[:10]]
    letter_counts = [count for letter, count in sorted_counts[:10]]

    plt.figure(figsize=(8, 8))
    plt.pie(letter_counts, labels=top_10_letters, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Top 10 Most Common Letters')
    plt.show()