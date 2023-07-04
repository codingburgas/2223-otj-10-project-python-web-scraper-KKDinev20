import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


def view_bar_chart():
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

    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[0])

    all_letters = [letter for letter, count in sorted_counts]
    all_counts = [count for letter, count in sorted_counts]

    # Plot the all letters count bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(all_letters, all_counts, color='green')
    plt.xlabel('Letter')
    plt.ylabel('Count')
    plt.title('Occurrences of Letters in Quotes')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    plt.bar_label(bars, label_type='edge', fmt='%d', fontsize=8)

    plt.tight_layout()
    plt.show()
