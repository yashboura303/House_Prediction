from bs4 import BeautifulSoup
import requests
import csv
l = []
for i in range(30):
	source = requests.get(f'https://www.magicbricks.com/flats-in-mumbai-for-sale-pppfs/page-{i}').text
	soup = BeautifulSoup(source, 'lxml')
	for div in soup.find_all("div", class_='flex relative clearfix m-srp-card__container'):
		l.append(div)
		print("Price", end=" ")
		if div.find("span", class_="m-srp-card__price"):
			print(div.find("span", class_="m-srp-card__price").text)
		else:
			print("Call for price")
		for div in (div.find_all("div", class_="m-srp-card__summary__item")):
			print((div.find("div", class_="m-srp-card__summary__title").text), end=" ")
			print(div.find("div", class_="m-srp-card__summary__info").text)
	print("*"*50)
	print(i)
print("Count:", len(l))