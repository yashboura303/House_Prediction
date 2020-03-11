from bs4 import BeautifulSoup
import requests
import csv
l = []
with open('data_set.csv', 'w', newline='') as csvfile:
	fieldnames = [ 'carpet_area', 'bedrooms', 'bathrooms', 'car_parking', 'furnishing', 'transaction_type','floor', 'facing', 'overlooking', 'price']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(5):
		source = requests.get(f'https://www.magicbricks.com/flats-in-mumbai-for-sale-pppfs/page-{i}').text
		soup = BeautifulSoup(source, 'lxml')
		for div in soup.find_all("div", class_='flex relative clearfix m-srp-card__container'):
			dic ={}
			if div.find("span", class_="m-srp-card__price"):
				dic['price']=div.find("span", class_="m-srp-card__price").text
			# else:
			# 	# print("Call for price")
			if div.find("span", class_="m-srp-card__title__bhk"):
				dic['bedrooms']=div.find("span", class_="m-srp-card__title__bhk").text.split()[0]
			for div in (div.find_all("div", class_="m-srp-card__summary__item")):
				if div.find("div", class_="m-srp-card__summary__title").text == "bathroom":
					dic['bathrooms'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "furnishing":
					main_string = div.find("div", class_="m-srp-card__summary__info").text
					if main_string == "Furnished":
						dic['furnishing'] = 3
					elif main_string == "Unfurnished":
						dic['furnishing'] = 1
					else:
						dic['furnishing'] = 2
				if div.find("div", class_="m-srp-card__summary__title").text == "transaction":
					main_string = div.find("div", class_="m-srp-card__summary__info").text
					if main_string == "Resale":
						dic['transaction_type'] = 0
					else:
						dic['transaction_type'] = 1
						
				if div.find("div", class_="m-srp-card__summary__title").text == "super area":
					dic['carpet_area'] = int(div.find("div", class_="m-srp-card__summary__info").text.split()[0])/1.25
				if div.find("div", class_="m-srp-card__summary__title").text == "carpet area":
					dic['carpet_area'] = div.find("div", class_="m-srp-card__summary__info").text.split()[0]
				if div.find("div", class_="m-srp-card__summary__title").text == "floor":
					dic['floor'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "facing":
					dic['facing'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "overlooking":
					dic['overlooking'] = div.find("div", class_="m-srp-card__summary__info").text
				if div.find("div", class_="m-srp-card__summary__title").text == "car parking":
					main_string = div.find("div", class_="m-srp-card__summary__info").text.strip()
					if main_string:
						if len(main_string) > 10:
							dic['car_parking']=int(main_string.split(",")[0].split()[0]) + int(main_string.split(",")[1].split()[0])
						elif len(main_string) <= 10 and len(main_string)>1:
							dic["car_parking"] = int(main_string.split(",")[0].split()[0])
					else:
							dic["car_parking"] = 0
					# dic['car_parking'] = div.find("div", class_="m-srp-card__summary__info").text
			writer.writerow(dic)

