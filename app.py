from flask import Flask,request,jsonify,render_template
import requests
app=Flask(__name__)
#mentor api:b2f7276693524dc1283929277faa0eae
#my api:8ef065fabaee20d930c7227703f446a2




@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/weatherapp",methods=['POST','GET'])
def get_weatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"
    params={
        'q':request.form['city'],
        'appid':request.form['apikey'],
        'units':request.form['units']
    }
    
    response=requests.get(url,params=params)
    data=response.json()
    return f"data :{data}"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5003)