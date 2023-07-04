import tkinter as tk

import requests
from bs4 import BeautifulSoup

from Charts.bar_chart import view_bar_chart
from Charts.pie_chart import view_pie_chart


class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu")
        self.root.geometry("600x400")
        self.create_menu()

    def create_menu(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=20)

        authors_quotes_button = tk.Button(menu_frame, text="View Authors and Quotes", command=self.view_authors_quotes,
                                          width=20, height=4)
        authors_quotes_button.grid(row=0, column=0, padx=10, pady=10)

        bar_chart_button = tk.Button(menu_frame, text="View Bar Chart", command=view_bar_chart, width=20, height=4)
        bar_chart_button.grid(row=1, column=0, padx=10, pady=10)

        pie_chart_button = tk.Button(menu_frame, text="View Pie Chart", command=view_pie_chart, width=20, height=4)
        pie_chart_button.grid(row=2, column=0, padx=10, pady=10)

    def view_authors_quotes(self):
        authors_quotes_window = tk.Toplevel(self.root)
        authors_quotes_window.title("Authors and Quotes")
        authors_quotes_window.geometry("600x800")

        text_widget = tk.Text(authors_quotes_window, height=80, width=150)
        text_widget.pack(pady=120)

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
            text_widget.insert(tk.END, f"{author}\n")
            for quote in quotes:
                text_widget.insert(tk.END, f"- {quote}\n")
            text_widget.insert(tk.END, "\n")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    menu = Menu()
    menu.run()
