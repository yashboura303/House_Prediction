from bs4 import BeautifulSoup
import requests
import csv
l = []
with open('data_set.csv', 'w', newline='') as csvfile:
	fieldnames = ['super_area', 'carpet_area', 'bedrooms', 'bathrooms', 'car_parking', 'furnishing', 'transaction_type','floor', 'facing', 'overlooking', 'price']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(10):
		source = requests.get(f'https://www.magicbricks.com/flats-in-mumbai-for-sale-pppfs/page-{i}').text
		soup = BeautifulSoup(source, 'lxml')
		for div in soup.find_all("div", class_='flex relative clearfix m-srp-card__container'):
			dic ={}
			if div.find("span", class_="m-srp-card__price"):
				dic['price']=div.find("span", class_="m-srp-card__price").text
			else:
				print("Call for price")
			if div.find("span", class_="m-srp-card__title__bhk"):
				dic['bedrooms']=div.find("span", class_="m-srp-card__title__bhk").text
			for div in (div.find_all("div", class_="m-srp-card__summary__item")):
				if div.find("div", class_="m-srp-card__summary__title").text == "society":
					continue
				if div.find("div", class_="m-srp-card__summary__title").text == "bathroom":
					dic['bathrooms'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "furnishing":
					dic['furnishing'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "transaction":
					dic['transaction_type'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "super area":
					dic['super_area'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "carpet area":
					dic['carpet_area'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "floor":
					dic['floor'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "facing":
					dic['facing'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "overlooking":
					dic['overlooking'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "car parking":
					dic['car_parking'] = div.find("div", class_="m-srp-card__summary__info").text
			writer.writerow(dic)