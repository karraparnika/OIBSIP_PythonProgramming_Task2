from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "e08d2ba26ac2888c4dec15d5d7d2ab9d"


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                 "feels_like": data["main"]["feels_like"],"wind": data["wind"]["speed"]  
            }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)


