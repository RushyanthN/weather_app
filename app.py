from flask import Flask ,render_template, request
import requests
import  json

app = Flask(__name__)

@app.route('/rushy_project')
def homepage():
    return render_template("index.html")



@app.route('/weatherapp',methods =['POST','GET'])
def weather_data():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {
        'q':request.form.get('city'),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
    }

    response = requests.get(url,param)
    data = response.json()
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5005)