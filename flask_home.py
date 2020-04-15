from flask import Flask, render_template, request, redirect, url_for
from geocoder import opencage
app = Flask(__name__)
from geocoder import opencage
import json

@app.route("/")  
def home():
	return render_template("home.html")

@app.route("/pricePredict", methods=["GET", "POST"])
def pricePredict():
	if request.method == "POST":
		carpet_area = (request.form["area"])
		bedrooms = (request.form["bedrooms"])
		bathrooms = (request.form["bathrooms"])
		carpet_area = (request.form["area"])
		car_parking = (request.form["car_parking"])
		transaction = (request.form["transaction"])
		if transaction == "Resale" or transaction="resale":
			transaction = 0
		else:
			transaction = 1
		furnishing = request.form["furnishing"]
		if furnishing == "Furnished":
			furnishing = 3
		elif furnishing == "Unfurnished":
			furnishing = 1
		else:
			furnishing = 2
		floor = (request.form["floor"])
		total_floors = (request.form["total_floors"])
		facing = (request.form["facing"])
		json_response = opencage(request.form["location"], key='cbc71a92fe6d4b28be97142b285a3693')
		json_response = json_response.json
		lat = json_response["raw"]["geometry"]["lat"]
		lng = json_response["raw"]["geometry"]["lng"]
		[[carpet_area,bedrooms,bathrooms,car_parking,furnishing,transaction,floor, total_floors,lat, lng]]
		return redirect(url_for("home"))
	else:
		return render_template("explore.html")
if __name__ == "__main__":
    app.run(debug=True)