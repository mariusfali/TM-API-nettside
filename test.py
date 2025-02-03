import requests
from get_tokens import get_live_token
live_token = get_live_token()

username = "hei."
if "." in username:
    username = username.replace(".", "")

print(username)


current_totd = requests.get('https://live-services.trackmania.nadeo.live/api/token/campaign/month?length=2', headers={'Authorization':f'nadeo_v1 t={live_token}'})
print(current_totd.text)