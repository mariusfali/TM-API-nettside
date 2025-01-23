import requests, base64, json
from base64 import b64encode
from passord import getPassord

hemmelig = getPassord()  # midlertidig løsning 

def generate_api_token():
    token = b64encode(f"marius2.falise@gmail.com:{hemmelig}".encode("utf-8")).decode("ascii")
    x = requests.post('https://public-ubiservices.ubi.com/v3/profiles/sessions', headers={'Content-type':'application/json', 'Ubi-AppId':'86263886-327a-4328-ac69-527f0d20a237', 'Authorization':f"Basic {token}", 'User-Agent':'CrashmaniaProject'})
    object = json.loads(x.content.decode("utf-8"))
    return object["ticket"]

def generate_live_token():
    api_token = generate_api_token()
    data = {}
    data["audience"] = "NadeoLiveServices" 
    json_data = json.dumps(data)
    live_request = requests.post('https://prod.trackmania.core.nadeo.online/v2/authentication/token/ubiservices', headers={'Content-Type':'application/json', 'Authorization':f'ubi_v1 t={api_token}','User-Agent':'CrashmaniaProject'}, data=json_data)
    object = json.loads(live_request.content.decode("utf-8"))
    return object["accessToken"]

def generate_core_token():
    api_token = generate_api_token()
    data = {}
    data["audience"] = "NadeoServices" 
    json_data = json.dumps(data)
    live_request = requests.post('https://prod.trackmania.core.nadeo.online/v2/authentication/token/ubiservices', headers={'Content-Type':'application/json', 'Authorization':f'ubi_v1 t={api_token}','User-Agent':'CrashmaniaProject'}, data=json_data)
    object = json.loads(live_request.content.decode("utf-8"))
    return object["accessToken"]

def generate_oauth_token():
    data1 = {}
    data1["grant_type"] = "client_credentials"
    data1["client_id"] = "0b6ad88e899829853a19"
    data1["client_secret"] = "88c8c9386dbd91150d056cc19f74a87dec353408"
    #json_data1 = json.dumps(data1)
    oauth_token = requests.post('https://api.trackmania.com/api/access_token', headers={'Content-Type':'application/x-www-form-urlencoded'}, data=data1)
    object = json.loads(oauth_token.content.decode("utf-8"))
    return object["access_token"]


def write_all_tokens_to_file():
    with open("tokens.txt", "w") as f:
        live_token = str(generate_live_token())
        core_token = str(generate_core_token())
        oauth_token = str(generate_oauth_token())
        #print(live_token)
        #print(core_token)
        #print(oauth_token)
        f.write(live_token)
        f.write("\n")
        f.write(core_token)
        f.write("\n")
        f.write(oauth_token)


write_all_tokens_to_file()

# # Oauth token (for getting playernames from accountids)
# data1 = {}
# data1["grant_type"] = "client_credentials"
# data1["client_id"] = "0b6ad88e899829853a19"
# data1["client_secret"] = "88c8c9386dbd91150d056cc19f74a87dec353408"
# json_data1 = json.dumps(data1)
# oauth_token = requests.post('https://api.trackmania.com/api/access_token', headers={'Content-Type':'application/x-www-form-urlencoded'}, data=data1)
# print(oauth_token.text)