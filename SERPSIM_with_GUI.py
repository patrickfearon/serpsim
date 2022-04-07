import requests
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter URL: ")


def urlclick():
    URLs = input()
    myLabel = Label(root)
    myLabel.pack()
    for url in URLs:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        metas = soup.find_all('meta')

        print("\n" + "Title of the website is : ")
        print(soup.find_all('title')[0].get_text() + "\n")

        print([meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description'])


myButton = Button(root, text="Scrape Meta Data", padx=50, pady=20, command=urlclick)
myButton.pack()

root.mainloop()


