# 📝 Python Quote Scraper

This is a straightforward Python project that grabs quotes and their authors from a website, then saves everything in a CSV file. It runs on BeautifulSoup and Pandas—nothing too fancy, just practical and clean.

---
## 🚀 Features

- Pulls quotes and their authors straight from a website
- Parses HTML with BeautifulSoup
- Saves everything neatly in a CSV
- Gives you a quick look at the data you’ve scraped
- Great for beginners looking to get started with web scraping

---

## 🛠️ Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- pandas

---
How to Run the Quote Scraper

1. First, make sure you have Python. Open your terminal and type:

python --version

If nothing shows up, or you get an error, you’ll need to grab Python 3.x from the official website and install it.

2. Next, grab the code. Just run:

git clone https://github.com/makwana23-Harshil/python-quote-scraper.git

3. Jump into the project folder:

cd python-quote-scraper

4. Before you do anything else, install the libraries the script needs:

pip install requests beautifulsoup4 pandas

5. Now, run the scraper:

python quote_scraper.py

6. What happens next?

You’ll see a new file called quotes.csv in your folder. The terminal will also show you a sneak peek at the quotes it found.

Example Output:
Fetching data from http://quotes.toscrape.com
Found 10 quotes. Pulling details now...
Saved everything to quotes.csv

A couple quick notes:

- You need to be online for this to work.
- The script only scrapes the first page.
- This is just for learning and playing around, not for anything commercial.

