import requests, json, time, datetime
from get_tokens import get_live_token, get_core_token, get_oauth_token


## --------------
import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://crashmania-website-1-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference("/")
## --------------


live_token = get_live_token()
core_token = get_core_token()
oauth_token = get_oauth_token()




current_totd = requests.get('https://live-services.trackmania.nadeo.live/api/token/campaign/month?length=1', headers={'Authorization':f'nadeo_v1 t={live_token}'})
totd_info = json.loads(current_totd.content.decode("utf-8"))


if (datetime.datetime.now()).hour < 19:
    current_day = (datetime.datetime.now()).day-1
else:
    current_day = (datetime.datetime.now()).day



totd_records = {}
for i in range(current_day,29,-1): # Hvilke datoer som skal skaffes
    
    for j in totd_info["monthList"][0]["days"]:
        if j["monthDay"] == i:
            totd_uid = j["mapUid"]


    amountOfPlayers = 5
    player = requests.get(f'https://live-services.trackmania.nadeo.live/api/token/leaderboard/group/Personal_Best/map/{totd_uid}/club/38508/top?length={amountOfPlayers}&offset=0', headers={'Authorization':f'nadeo_v1 t={live_token}'})
    #print(player.text)
    leaderboard_data = json.loads(player.content.decode("utf-8"))

    print(f"Dato: {i}. januar")
    totd_records[i] = {}


    for j in leaderboard_data["top"]:
        account_id = j["accountId"]
        score = j["score"]
        #print(account_id)
        #print(score)
        username = requests.get(f'https://api.trackmania.com/api/display-names?accountId[]={account_id}', headers={'Authorization':f'Bearer {oauth_token}'})
        actual_username = json.loads(username.content.decode("utf-8"))
        #print(actual_username[f"{account_id}"])
        print(f"{actual_username[f'{account_id}']} drove a time of {score}")
        correctly_formatted_time = float(f"{str(score)[:2]}.{str(score)[2:]}")
        correctly_formatted_time = format(correctly_formatted_time, '.3f') # Legger til 0ere i tiden
        #print(correctly_formatted_time)
        totd_records[i][actual_username[f'{account_id}']] = correctly_formatted_time

        #new_username = str(actual_username[f'{account_id}'])
        #db.reference(f"/{i}").update({f"{new_username}":f"{str(correctly_formatted_time)}"})

        time.sleep(1)
    
    db.reference(f"/crashmania-totd/1").update({f"{i}":f"{totd_records[i]}"})
    time.sleep(2)


print(totd_records)
#db.reference("/totd").delete()
#ref.update({"totd":str(totd_records)})




## Til txt fil

#with open("temp_database.txt", "w") as f:
#    f.write(str(totd_records))