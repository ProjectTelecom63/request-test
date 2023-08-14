from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# List to store the values
values_list = []

@app.route('/')
def home():
    return "Hello! This is the Flask app."

@app.route('/data', methods=['GET'])
def append_values():
    id = request.args.get('id')
    temp = request.args.get('temp')
    humi = request.args.get('humi')
    lat = request.args.get('lat')  # Include latitude
    lon = request.args.get('lon')  # Include longitude

    if temp is not None and humi is not None and id is not None:
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        values_list.append((timestamp, id, temp, humi, lat, lon))  # Include lat and lon
        
        hours, minutes, seconds = now.hour, now.minute, now.second
        return f"Values appended successfully! at {hours}h {minutes}m {seconds}s"
    else:
        return "Missing values"

@app.route('/show')
def show_values():
    table_rows = [
        f"<tr><td>{timestamp}</td><td>{id}</td><td>{temp}</td><td>{humi}</td><td>{lat}</td><td>{lon}</td></tr>"
        for timestamp, id, temp, humi, lat, lon in values_list  # Include lat and lon
    ]
    table_html = f"""
        <table border="1">
            <tr>
                <th>Timestamp</th>
                <th>Device ID</th>
                <th>Temp</th>
                <th>Humidity</th>
                <th>Latitude</th>
                <th>Longitude</th>
            </tr>
            {''.join(table_rows)}
        </table>
    """

    return table_html


@app.route('/delete')
def delete_values():
    global values_list
    values_list = []  # Clear the list
    return "All values deleted successfully!"

if __name__ == '__main__':
    app.run(host='192.168.1.3', port="5000")
