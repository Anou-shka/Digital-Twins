from flask import Flask, request
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)

## Set up the Google Sheet Credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Specify Google Sheet URL
sheet_url = 'https://docs.google.com/spreadsheets/d/17kuUgLq9pMk_KvxmGSau8qpLwPOhwNH4lPg8_WLuM0s/edit?usp=sharing'
sheet = client.open_by_url(sheet_url).sheet1

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        data = request.json  # ✅ Directly extracting JSON object

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Extract values safely
        temp_C = data.get('temperature_C', 'N/A')
        temp_F = data.get('temperature_F', 'N/A')
        humidity = data.get('humidity', 'N/A')
        # ADC = data.get('ADC', 'N/A')
        # Voltage = data.get('Voltage', 'N/A')
        # pressure = data.get('pressure', 'N/A')

        # Create a row with timestamp
        data_with_timestamp = [timestamp, temp_C, temp_F, humidity, ADC, Voltage, pressure]
        
        # Append to Google Sheets
        sheet.append_row(data_with_timestamp)

        return 'Data Uploaded Successfully'
    
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run()  # host="0.0.0.0", port=3000
