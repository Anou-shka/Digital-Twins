from flask import Flask, request
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json
import pytz
import os 

app = Flask(__name__)

# ## Set up the Google Sheet Credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# ✅ Read Google Sheets Credentials from Environment Variable'
# sheet_url = "https://docs.google.com/spreadsheets/d/17kuUgLq9pMk_KvxmGSau8qpLwPOhwNH4lPg8_WLuM0s/edit?usp=sharing"
creds_json = os.getenv("GOOGLE_SHEETS_CREDS_JSON")

if not creds_json:
    raise ValueError("⚠️ GOOGLE_SHEETS_CREDS_JSON environment variable is missing!")

try:
    creds_dict = json.loads(creds_json)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
except Exception as e:
    raise ValueError(f"⚠️ Failed to authenticate with Google Sheets: {e}")

# ✅ Read Google Sheets URL from Environment Variable
sheet_url = os.getenv("GOOGLE_SHEET_URL")

if not sheet_url:
    raise ValueError("⚠️ GOOGLE_SHEET_URL environment variable is missing!")

try:
    sheet = client.open_by_url(sheet_url).sheet1
except Exception as e:
    raise ValueError(f"⚠️ Failed to open Google Sheet: {e}")

# ✅ Homepage Route (Check if Flask is Running)
@app.route('/')
def home():
    return "✅ Flask App is Running on Render!"

# ✅ Data Upload Route
@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        data = request.json  # Extract JSON payload
        utc_now = datetime.utcnow()
        sgt = pytz.timezone("Asia/Singapore")
        timestamp = datetime.now(pytz.utc).astimezone(sgt).strftime('%Y-%m-%d %H:%M:%S')

        # ✅ Extract values safely (default to 'N/A' if missing)
        temp_C = data.get('temperature_C', 'N/A')
        temp_F = data.get('temperature_F', 'N/A')
        humidity = data.get('humidity', 'N/A')
        ADC = data.get('ADC', 'N/A')
        Voltage = data.get('Voltage', 'N/A')
        pressure = data.get('pressure', 'N/A')
        airspeed = data.get('airspeed', 'N/A')
        co2 = data.get('co2', 'N/A')
       

        # ✅ Prepare row for Google Sheets
        data_with_timestamp = [timestamp, temp_C, temp_F, humidity, ADC, Voltage, pressure, co2]
        sheet.append_row(data_with_timestamp)

        return '✅ Data Uploaded Successfully', 200
    
    except Exception as e:
        return f"❌ Error: {e}", 500

# ✅ Run Flask App on Render (Dynamic Port)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Render assigns a port dynamically
    app.run(host="0.0.0.0", port=port)
