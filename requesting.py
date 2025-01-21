import requests, base64, json
from base64 import b64encode
from passord import getPassord

hemmelig = getPassord()  # midlertidig løsning 

# # API token (step 1)
# token = b64encode(f"marius2.falise@gmail.com:{hemmelig}".encode("utf-8")).decode("ascii")
# x = requests.post('https://public-ubiservices.ubi.com/v3/profiles/sessions', headers={'Content-type':'application/json', 'Ubi-AppId':'86263886-327a-4328-ac69-527f0d20a237', 'Authorization':f"Basic {token}", 'User-Agent':'CrashmaniaProject'})
# print(x.text)

# Access token (step 2)
# data = {}
# data["audience"] = "NadeoServices" # Endre til NadeoLiveServices (i stedet for NadeoServices) hvis du skal ha annen API enn core
# json_data = json.dumps(data)
# print(json_data)
# api_token = "ewogICJ2ZXIiOiAiMSIsCiAgImFpZCI6ICI4NjI2Mzg4Ni0zMjdhLTQzMjgtYWM2OS01MjdmMGQyMGEyMzciLAogICJlbnYiOiAiUHJvZCIsCiAgInNpZCI6ICI4MzE2MzgwYS0zYTI2LTQ3NDQtYWVjNC0zMzEzYzAyMzYzZjYiLAogICJ0eXAiOiAiSldFIiwKICAiZW5jIjogIkExMjhDQkMiLAogICJpdiI6ICJYZzJ3WGtvU2RxTVY1aHpod0ZqRU1RIiwKICAiaW50IjogIkhTMjU2IiwKICAia2lkIjogIjQyOWNjYmEyLTE2ZDUtNDAwMS04MDExLTI1Y2FkNGVjYmYyNCIKfQ.v9jvYvpc6zKqPxrf657Nnl_7udxqkYq97YPtS3KnfeHHZ3eotrYbqKayVmGOC8vd2debNF6RkRLbp6orC0aFX1IAeRkpGG6l0mnGGATV8uXe1VwoojGpH8CjMikxqlvYnOgAT4EtEanFh-sXLYRXJEgSRUQd_KgQnSLhgt7IO2-Cexn1b7cm7aB9hfme3yezjitIqXD3rZfr9ddJaVLaezmrZr-ZbY3oa5JE-y3CmTzVQ0_1bUQK9mRFTTp8h0J3XdONsmJsWKtSE73XsSwUtp6P_zY_AA0a2Yw3vm9Tm8O2Q8uZT8pNS_fpMbwKBM6LYYq9szLpvZtpfxx9XQcrNcqWFVZyQ92nRoLNFeBc9SgGESApEtk8wWQeXeWjW8wDax0jiBNnlGZHJUpSgDPduxIsFg68QsdXGEJlvrGjs9z8FCFFTFpPYtNQlFzzFSQRFtdB6AhhpUSghKLS8BMJwkzM9XXC9C5nfz5P6JfO_lGRbl0qii_-8zL-HE-LeM_H70DD4cepvRwsvt0dmdXL6uiMByD27gz0Ynh9C45bH8RB73CDUZTWDo67QkGxiKiF67rw-5QSh8LklB457U1k3UD3BVVkIeyv676XzueshuV3WzveYcEvsAa-soXZQF3xtcLEKhvGvjeTfIwCEV1eM_FwPGRCy_yKFKVB1MmepJhfcgeCIfRXjxqbyXdPcSYCVbxmcdtKJndTjZyL8qD0rw8ygdH9dWzvyxiRnI_Du_DNeQUJoqp0NaEQYxMvFntgXzt3GKY-JJ4mzRijiMTftTXIfgG6PtS9WUDeqs2rAtPRsT8uIyyhyHAwqZJ8R4eBjscbbrTc3j3VPunOwKIDRDLWlbP3yrGFF01kp5ZxVZWXz92Q7XvBcNSYcSZBuikactI56FFBXlXJhmUZvxNWhcHns1BknnRKqvBliXOn2BMowDqfXDhbq87qlIwZOxmGZVFodxazCh7XjAzqgvAGBQnBQHjUJRLnOpqhyUOpAeM8CzMJIe4NFBwRfgqEIenYxi_XT8QA1R6epNym-eNjK3_ol9Sip1QN7pjzcXqPdaR27M9qLbVXvYwc7XHXgHyUKWqcxddveImwmAptlD6jTs_fj6DSiyJPW9OCTWM72HiVPNYnfGynjPkrpvr8pqr4aa3RX_Z24qpzG0fSVd5zA1XAwJ2wCrs_R64pZHyfaYwcqlCDk4Sgt3xr4DwJVj211x_dfodBgtdA1ecJs80yW58xqJ-G4ZqzkCk44goE72XJhemf5RZvgK05OWfx7IzKdtzidKkA_g3kfx3k7_7ZjQtaMs_V5xYMey5ayN436IYB23B-ROmb7eYGt--bdsrl47A6cJwxdjTYGURyZ5JgTO9cgbiDY4v5c_bcXexoiRBFr8qwIHXsGITPBXnnXQRYmvpwRzMrmajamV4uWqlFHQmqiND-o_32pTBLVt0NBir-pHqzfyLcHx8kGtiu7cUhjmeNsUZTTaOHNCkh9JvL5-9xjxejmzEydAEbbhyzrTDuADEkUdJCMkSK0n-Vd3Dw9lQk0FuvyJvdvo7D07WoWaXNiTBwwrtBBqcVN102eomJZB_zoAiylbaGWVhRlvMuTQ7WeCBIGbQU5TiL55vD5Z9vihxkL_J2j_6A20xvRg-9dxrp-3Dh4dDWJMsjT3B1So-0VuWsz09J9G2EKjgg9N81OfAdfjLoq0D72Wu3NI8g_q07hGMxgkyGm_ZGHwtnkUWJd-tiHQsW6lwTtJnYgSnES3SQV_mqTdA_kubeosfE6t9oifIwLn_7D4Rm0r5vxhhnHJqMOhAWrpVkpP7UrgTqubBERkAA7lrBfuCABtWhNX1GlmwpvYGvpn-ZOoQjmhF-edQnFnRkmmYriLtCsyKDdYsiM8iQ35Hcs1KnyZQ.fUfi-Z2ZTIiI8KblaJlo6pBWPLJNJAiARRZv6mTyL64"
# live_request = requests.post('https://prod.trackmania.core.nadeo.online/v2/authentication/token/ubiservices', headers={'Content-Type':'application/json', 'Authorization':f'ubi_v1 t={api_token}','User-Agent':'CrashmaniaProject'}, data=json_data)
# print(live_request.text)

# Refresh token (refreshing step 2, not mandatory)



# Oauth token (for getting playernames from accountids)
data1 = {}
data1["grant_type"] = "client_credentials"
data1["client_id"] = "0b6ad88e899829853a19"
data1["client_secret"] = "88c8c9386dbd91150d056cc19f74a87dec353408"
json_data1 = json.dumps(data1)
oauth_token = requests.post('https://api.trackmania.com/api/access_token', headers={'Content-Type':'application/CrashmaniaProject'}, data=data1)
print(oauth_token.text)

# test = requests.get('https://live-services.trackmania.nadeo.live/api/token/club/38508/member?length=53&offset=0', headers={'Authorization':'nadeo_v1 t=eyJhbGciOiJIUzI1NiIsImVudiI6InRyYWNrbWFuaWEtcHJvZCIsInZlciI6IjEifQ.eyJqdGkiOiI1ZGU4ZmNiYS1kNzQ4LTExZWYtOTQ3Yy0wYWUwZDI2NjQyZDMiLCJpc3MiOiJOYWRlb1NlcnZpY2VzIiwiaWF0IjoxNzM3Mzg5MTI4LCJyYXQiOjE3MzczOTA5MjgsImV4cCI6MTczNzM5MjcyOCwiYXVkIjoiTmFkZW9MaXZlU2VydmljZXMiLCJ1c2ciOiJDbGllbnQiLCJzaWQiOiI1ZGU4ZjhiZS1kNzQ4LTExZWYtYWIyNy0wYWUwZDI2NjQyZDMiLCJzYXQiOjE3MzczODkxMjgsInN1YiI6IjUxZDhmZGE0LWVjOTAtNDY0NC04NzJhLWMwMmMzMjZjZjUyMiIsImF1biI6IkFuZHliYWNvZGUiLCJydGsiOmZhbHNlLCJwY2UiOmZhbHNlLCJ1YmlzZXJ2aWNlc191aWQiOiJmZmY4Njk1NC02ZmE2LTQ5ODgtYTdhZi00ODc3MDYzYmIzMTgifQ.L9j1D-Ts93Gg2eh4W43nCUCp4yZTEsPi8i7iYpslLW0'})
# print(test.text)
# members_data = json.loads(test.content.decode("utf-8"))





#print(members_data["clubMemberList"])
#with open("database.txt", "w") as f:
    #f.write(str(members_data["clubMemberList"]))
#    for i in members_data["clubMemberList"]:
#        f.write(str(i["accountId"]))
    #     print(i["accountId"])

