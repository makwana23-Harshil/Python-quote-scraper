# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import csv

# def scrape_quotes():
#     url="http://quotes.toscrape.com"
#     print(f"Fetching data from {url}")
#     response=requests.get(url)

#     if response.status_code==200:
#         soup=BeautifulSoup(response.text,'html.parser')
#         quotes=soup.find_all('div',class_='quote')
#         scraped_data=[]
#         print(f"Found{len(quotes)} quotes.Extracting info...")
#         for quote in quotes:
#             text = quote.find('span',class_='text').text
#             author = quote.find('small',class_='author').text
#             scraped_data.append([author,text])
        

#         df = pd.DataFrame(scraped_data)
#         df.to_csv("quotes.csv", index=False, encoding="utf-8")
#         print("Data successfully saved as Pandas DataFrame → quotes.csv")
#         print("\n📄 Preview:")
#         print(df.head())

#     else:
#         print("Failed to retrive the webpage.")
# if __name__=="__main__":
#     scrape_quotes()

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    print(f"Fetching data from {url}")
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        scraped_data = []

        print(f"Found {len(quotes)} quotes. Pulling details now...")

        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            scraped_data.append([author, text])

        df = pd.DataFrame(scraped_data, columns=["Author", "Quote"])
        df.to_csv("quotes.csv", index=False, encoding="utf-8")
        print("Saved everything to quotes.csv")

        print("\nHere's a quick look at the data:")
        print(df.head())
    else:
        print("Couldn’t load the page. Something went wrong.")

if __name__ == "__main__":
    scrape_quotes()