import requests, json, time
from get_tokens import get_live_token, get_core_token, get_oauth_token

live_token = get_live_token()
core_token = get_core_token()
oauth_token = get_oauth_token()




current_totd = requests.get('https://live-services.trackmania.nadeo.live/api/token/campaign/month?length=1', headers={'Authorization':f'nadeo_v1 t={live_token}'})
totd_info = json.loads(current_totd.content.decode("utf-8"))
#print(totd_info)
for i in totd_info["monthList"][0]["days"]:
    if i["monthDay"] == 22: # erstatt tall med datoen for nyeste totd
        totd_uid = i["mapUid"]
#print(totd_uid)


amountOfPlayers = 5
player = requests.get(f'https://live-services.trackmania.nadeo.live/api/token/leaderboard/group/Personal_Best/map/{totd_uid}/club/38508/top?length={amountOfPlayers}&offset=0', headers={'Authorization':f'nadeo_v1 t={live_token}'})
#print(player.text)
leaderboard_data = json.loads(player.content.decode("utf-8"))


for i in leaderboard_data["top"]:
    account_id = i["accountId"]
    score = i["score"]
    #print(account_id)
    #print(score)
    username = requests.get(f'https://api.trackmania.com/api/display-names?accountId[]={account_id}', headers={'Authorization':f'Bearer {oauth_token}'})
    actual_username = json.loads(username.content.decode("utf-8"))
    #print(actual_username[f"{account_id}"])
    print(f"{actual_username[f'{account_id}']} drove a time of {score}")

    time.sleep(1)