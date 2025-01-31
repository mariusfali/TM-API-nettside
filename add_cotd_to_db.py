import requests, json, time, datetime
from get_tokens import get_live_token, get_core_token, get_oauth_token

live_token = get_live_token()


## --------------
import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://crashmania-website-1-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference("/")
## --------------

cotd_result = requests.get("https://meet.trackmania.nadeo.club/api/matches/26637/results?length=10", headers={'Authorization':f'nadeo_v1 t={live_token}'})
print(cotd_result.text)