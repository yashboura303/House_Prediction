# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=Borivali-West&cityName=Mumbai')
# # elems = browser.find_elements_by_class_name('m-srp-card__container')
# elems = browser.find_element_by_xpath('//*[@id="resultBlockWrapper44133713"]/div[2]')
# # print(elems)
# # for e in elems:
# # 	print(e)
# # 	e.click()
# elems.click()

# # bedroom = browser.find_element_by_css_selector('#firstFoldDisplay > div:nth-child(1) > div.p_value > div')
# browser.switch_to.window(browser.window_handles[1])
# bedroom = browser.find_element_by_class_name('seeBedRoomDimen')
# print(bedroom.text)



from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://www.magicbricks.com/flats-in-mumbai-for-sale-pppfs?mbtracker=google_paid_brand_desk_mumbai&ccode=brand_sem&gclid=CjwKCAiA-vLyBRBWEiwAzOkGVI3lRH2j0GAq63CcWfhIZNteavyVerPR2L-xgcmwLqbpgwdvcCQRUxoC68QQAvD_BwE').text
soup = BeautifulSoup(source, 'lxml')
l = []
for div in soup.find_all("div", class_='flex relative clearfix m-srp-card__container')[:2]:
	print("Price", end=" ")
	print(div.find("div", class_="m-srp-card__price").text)
	# l.append(div)
	for div in (div.find_all("div", class_="m-srp-card__summary__item")):
		print((div.find("div", class_="m-srp-card__summary__title").text), end=" ")
		print(div.find("div", class_="m-srp-card__summary__info").text)
	print("*"*50)

# for e in l:
# 	print(e)
# 	print("*"*50)
