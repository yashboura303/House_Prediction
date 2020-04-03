from bs4 import BeautifulSoup
import requests
import csv
l = []
def get_lat(strr):
	lat = strr.split(';')[1][16:].split(',')[0]
	lat = lat[1:len(lat)-1]
	return lat
def get_long(strr):
	long = strr.split(';')[1][16:].split(',')[1]
	long = long[1:len(long)-1]
	return long
with open('data_set.csv', 'w', newline='') as csvfile:
	fieldnames = [ 'carpet_area', 'bedrooms', 'bathrooms', 'car_parking', 'furnishing', 'transaction_type','floor','total_floors', 'facing', 'overlooking', 'price', 'lat', 'long']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(200):
		source = requests.get(f'https://www.magicbricks.com/flats-in-mumbai-for-sale-pppfs/page-{i}').text
		# source = requests.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&Locality=Borivali-East,Borivali-West&cityName=Mumbai').text
		soup = BeautifulSoup(source, 'lxml')
		for div in soup.find_all("div", class_='flex relative clearfix m-srp-card__container'):
			try:
				dic ={}
				if div.find("span", class_="m-srp-card__price"):
					price = div.find("span", class_="m-srp-card__price").text
					price = price.split()
					if price[1] == "Cr":
						dic['price'] = float(price[0])
					else:
						dic['price'] = float(price[0])/100
				else:
					continue
				if div.find("span", class_="m-srp-card__title__bhk"):
					if "Studio" not in div.find("span", class_="m-srp-card__title__bhk").text:
						dic['bedrooms']=div.find("span", class_="m-srp-card__title__bhk").text.split()[0]
				if div.find("div", class_='m-srp-card__link m-srp-card__link--nearby'):
					if get_lat(div.find("div", class_='m-srp-card__link m-srp-card__link--nearby').get('onclick')) == '0.0':
						continue
					else:
						# print(get_lat(div.find("div", class_='m-srp-card__link m-srp-card__link--nearby').get('onclick')))
						dic['lat'] = get_lat(div.find("div", class_='m-srp-card__link m-srp-card__link--nearby').get('onclick'))
						dic['long'] = get_long(div.find("div", class_='m-srp-card__link m-srp-card__link--nearby').get('onclick'))
				else:
					continue
						
				dic["car_parking"] = 0
				for div in (div.find_all("div", class_="m-srp-card__summary__item")):
					if div.find("div", class_="m-srp-card__summary__title").text == "car parking":
						main_string = div.find("div", class_="m-srp-card__summary__info").text.strip()
						if "119" not in main_string:
							# print(main_string)
							if main_string:
								if len(main_string) > 10:
									dic['car_parking']=int(main_string.split(",")[0].split()[0]) + int(main_string.split(",")[1].split()[0])
								elif len(main_string) <= 10 and len(main_string)>1:
									dic["car_parking"] = int(main_string.split(",")[0].split()[0])
						# else:
						# 		dic["car_parking"] = 0
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
						floor_text = div.find("div", class_="m-srp-card__summary__info").text
						# print(floor_text)
						if "floors" in floor_text:
							if "Ground" in floor_text:
								floor_text = floor_text.split()
								dic["total_floors"] = floor_text[3]
								dic["floor"] = 0
							elif "Basement" in floor_text:
								floor_text = floor_text.split()
								dic["total_floors"] = floor_text[3]
								dic["floor"] = -1
							else:
								floor_text = floor_text.split()
								dic["total_floors"] = floor_text[3]
								dic["floor"] = floor_text[0]

					if div.find("div", class_="m-srp-card__summary__title").text == "facing":
						dic['facing'] = div.find("div", class_="m-srp-card__summary__info").text
					if div.find("div", class_="m-srp-card__summary__title").text == "overlooking":
						dic['overlooking'] = div.find("div", class_="m-srp-card__summary__info").text
					
						# dic['car_parking'] = div.find("div", class_="m-srp-card__summary__info").text
				writer.writerow(dic)
			except:
				continue

