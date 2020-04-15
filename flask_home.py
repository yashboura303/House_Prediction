from flask import Flask, render_template, request, redirect, url_for
from geocoder import opencage
app = Flask(__name__)
from geocoder import opencage
import json
from main import dic, predict_price
@app.route("/")  
def home():
	return render_template("home.html")

@app.route("/pricePredict", methods=["GET", "POST"])
def pricePredict():
	if request.method == "POST":
		print(request.form)
		carpet_area = float(request.form["area"])
		bedrooms = float(request.form["bedrooms"])
		bathrooms = int(request.form["bathrooms"])
		carpet_area = int(request.form["area"])
		car_parking = int(request.form["car_parking"])
		transaction = (request.form["transaction"])
		if transaction == "Resale" or transaction=="resale":
			transaction = 0.0
		else:
			transaction = 1.0
		furnishing = request.form["furnishing"]
		if furnishing == "Furnished":
			furnishing = 3
		elif furnishing == "Unfurnished":
			furnishing = 1
		else:
			furnishing = 2
		floor = float(request.form["floor"])
		total_floors = float(request.form["total_floors"])
		facing = (request.form["facing"])
		#get facing code
		for el in dic:
			if facing == dic[el]:
				facing = el
		#get lat and long from address
		json_response = opencage(request.form["location"], key='cbc71a92fe6d4b28be97142b285a3693')
		json_response = json_response.json
		lat = float(json_response["raw"]["geometry"]["lat"])
		lng = float(json_response["raw"]["geometry"]["lng"])

		predicted_price = predict_price([[carpet_area,bedrooms,bathrooms,car_parking,furnishing,transaction,floor, total_floors,lat, lng, facing]])
		print("Price", predict_price)
		return render_template("explore.html", result=round(predicted_price[0], 2))

	else:
		return render_template("explore.html")
if __name__ == "__main__":
    app.run(debug=True)