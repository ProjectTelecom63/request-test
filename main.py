from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# List to store the values
values_list = []

@app.route('/')
def home():
    return "Hello! This is the Flask app."

@app.route('/data', methods=['POST'])
def append_values():
    data = request.json

    id = data.get('id')
    temp = data.get('temp')
    humi = data.get('humi')

    if temp is not None and humi is not None and id is not None:
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        values_list.append((timestamp, id, temp, humi))
        
        hours, minutes, seconds = now.hour, now.minute, now.second
        return f"Values appended successfully! at {hours}h {minutes}m {seconds}s"
    else:
        return "Missing values"

@app.route('/show')
def show_values():
    return "<br>".join([f"<b>Timestamp</b>: {timestamp}, <b>Device ID</b>: {id}, <b>Temp</b>: {temp}, <b>Humidity</b>: {humi}" for timestamp, id, temp, humi in values_list])

@app.route('/delete')
def delete_values():
    global values_list
    values_list = []  # Clear the list
    return "All values deleted successfully!"

if __name__ == '__main__':
    app.run(debug=True,port=80)
