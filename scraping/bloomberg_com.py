from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_article(data):
    return dict(
        headline = data.get_text(),
        link = "https://www.bloomberg.com" + data['href']
    )

def bloomberg_com():

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = requests.get("https://www.bloomberg.com/fx-center", headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    headline = soup.select_one(".single-story-module__headline-link")

    all_links = []
    all_links.append(get_article(headline))

    grid_articles = soup.select(".grid-module-story__headline-link")
    [all_links.append(get_article(x)) for x in grid_articles]

    side_articles = soup.select(".story-list-story__info__headline-link")
    [all_links.append(get_article(x)) for x in side_articles]

    return all_links