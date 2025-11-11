from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "496bedaa326204f2b2eda73435794394"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'temperature': round(data['main']['temp']),
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'feels_like': round(data['main']['feels_like']),
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure']
        }
        return render_template('result.html', weather=weather)
    else:
        return render_template('index.html', error="City not found! Please try again.")

if __name__ == '__main__':
    app.run(debug=True)