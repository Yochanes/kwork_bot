import json
import requests
from bs4 import BeautifulSoup

def get_first_news():
	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
	}

	url = "https://www.kwork.ru/projects/"
	r = requests.get(url=url, headers=headers)

	soup = BeautifulSoup(r.text, "lxml")
	articles_cards = soup.find_all("div", class_="card")

	news_dict = {}

	for article in articles_cards:
		article_url = article.find("a").get("href")
		article_title = article.find("a").text.strip()
		article_price = article.find("div", class_="wants-card__header-price").text.strip()

		article_id = article_url.split("/")[-1]

		# print(f"{article_title} | {article_price} | {article_url} | {article_id}")

		news_dict[article_id] = {
			"article_url": article_url,
			"article_title": article_title,
			"article_price": article_price
		}
	with open("news_dict.json", "w", encoding='utf-8') as file:
		json.dump(news_dict, file, indent=3, ensure_ascii=False)

def check_news_update():
	with open("news_dict.json", encoding='utf-8') as file:
		news_dict = json.load(file)

	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
	}

	url = "https://www.kwork.ru/projects/"
	r = requests.get(url=url, headers=headers)

	soup = BeautifulSoup(r.text, "lxml")
	articles_cards = soup.find_all("div", class_="card")

	fresh_news = {}

	for article in articles_cards:
		article_url = article.find("a").get("href")
		article_id = article_url.split("/")[-1]

		if article_id in news_dict:
			continue
		else:
			article_title = article.find("a").text.strip()
			article_price = article.find("div", class_="wants-card__header-price").text.strip()

			news_dict[article_id] = {
				"article_url": article_url,
				"article_title": article_title,
				"article_price": article_price
			}
			fresh_news[article_id] = {
				"article_url": article_url,
				"article_title": article_title,
				"article_price": article_price
			}
	with open("news_dict.json", "w", encoding='utf-8') as file:
		json.dump(news_dict, file, indent=3, ensure_ascii=False)
	return fresh_news


def main():
	# get_first_news()
	print(check_news_update())


if __name__ == '__main__':
	main()