import requests, base64, json
from base64 import b64encode
from passord import getPassord

hemmelig = getPassord()  # midlertidig løsning 

# # API token (step 1)
# token = b64encode(f"marius2.falise@gmail.com:{hemmelig}".encode("utf-8")).decode("ascii")
# x = requests.post('https://public-ubiservices.ubi.com/v3/profiles/sessions', headers={'Content-type':'application/json', 'Ubi-AppId':'86263886-327a-4328-ac69-527f0d20a237', 'Authorization':f"Basic {token}", 'User-Agent':'CrashmaniaProject'})
# print(x.text)

# # Access token (step 2)
# data = {}
# data["audience"] = "NadeoLiveServices" # Endre til NadeoLiveServices (i stedet for NadeoServices) hvis du skal ha annen API enn core
# json_data = json.dumps(data)
# print(json_data)
# api_token = "ewogICJ2ZXIiOiAiMSIsCiAgImFpZCI6ICI4NjI2Mzg4Ni0zMjdhLTQzMjgtYWM2OS01MjdmMGQyMGEyMzciLAogICJlbnYiOiAiUHJvZCIsCiAgInNpZCI6ICI2MzNhMTc0Mi03NjE0LTRjZTQtYjg1Ni1kMzUwMzVmOTllMDQiLAogICJ0eXAiOiAiSldFIiwKICAiZW5jIjogIkExMjhDQkMiLAogICJpdiI6ICJyV1hyYnBMYVlRNm4wZ0NQMEJ6ZXp3IiwKICAiaW50IjogIkhTMjU2IiwKICAia2lkIjogIjhmMmQ1MzliLTJiMmUtNGM5MS04MGNkLWZjOGI0ODJkNjdmOSIKfQ.wPsCzGbkN0vBc1Yfw9FAVv6bnzpIvnyXIv3mBes3sAhcL897lEjeMMzpPv0jWUwU_7gCZiha4YhoYZAPtGzCp0NRswAgV3XLfUjUl5JWZexhdNe-oui-QIqnSWiSJ8JWgPnsKY0OyRf79IUxcGJOx6vJMNXSFqjnudNVlIF8jPvxkwvB2xgPfO73KaEj-H_VjAnvB4QdfkLjF4JLy8z_OiFQjdhalZt8XdgQdxux2UrZRaxztt90QY7jVzug7H_JvyGtknMMn8YXO9eaJ3F908nEHny5BtpogBztz511Vx-ikX2ThweK-OvnsawvOJ8Tp2r59QjlUqFVUh0bw0ab-YUXSX4YpJreiacfvaOpaLvbzByN1hdbuSHIqbzlSdhhN0hv5xUtW4AnyRjPH7mZR-WBeTrcUVWwSfwaXw4vz-78ZxAFodEgge3wSmjClSSCcODiD4aRVXJ0DP65dWlo8zzTgAGqPvdXTH7qhgRL_OJEdp7Cl5WxR4Yh4mCc6RGUuOadqe5gpBZvr6ybstNjPJAYdM7G_9O_Do0oFTi_wuaXv8ZLN11JX0_zcq-JAu1oD5_duxdeKrvl7KzjeD9CxrpgL-YCkfo4u1b6YGgIW9XOGqRxcLEIts6HX_Y9lnAK1iZaB3UJ83lql6pvs-Q5ZA_5nHqIX9amLjywNoIRA7rl-V0Bezj7RvLUobsFWN1q9qH0v6zpP5LysnXUgkpz1fUoChB8NST9awWYNZOIV5_U0eKDkRQKveq5Rvu8okqZAMYqUV2Jys5jfQn9vYC2WGIKh8pBoOVokKOFWuRRLl3h835LLd7lSILqR3_QpoQdGFXJLcLJHQ5J5iHZ1rJBuzCzHcwSvYdViWAuLJfPYH0Ilhprn4acxOIBW8UUZb7AO4L0VhGgjQS5dhWZmDktu76RTnAwODXujkkN2BxEaa3oplBz-CZzj82oZKo7R5nNmVfI7YDr0Yw54VzcxrU6577W5t9bcT-RG2cFt8Iz0y0u-J0dHm9pELZGZC2nki97GRLl-F0KQ_uqa6RKKcfQVRF4a7celKp4B2X2SYHt1jPZEh6JaKFWrxuWaE5-VovZhh9tcm7fK-mz8zzOrAos7bFPy1TA87QXgG6WF_odCHCOGQkwaljAlp4NCEpUYrD4bPRaabXdwYd59yD0uEHW8R-nHa-BrSpmr-7TRhwHKI8k_5_6ZLsK8OeRnx28FkwK1jt5EWDo-2QDgY2iQ99dfuRGnFAffoeVbT4CPgHy7Ii-q2_0gRGvr82uyFWIXGzoDghYQQh1IYTC3QEWaBJ0ZsoBAC93yNJLYA8_jHVZYlvPIod3WFyAKFDtlrvvZNd68SSGc_mh8lmffT2YEhtvz64Ys1f5gEBysXDsuXfS2uEw1lgXY8adj6RYAhn6j0VeUFLYUBLv1F4LFkg2sqK-qM_B-89fF5JNF7Q4DdIkX0v4Efm-g1Z0c4LoGP0gFuokCPYlZ_NbVWCaNTu5_cT_pGOSFPLuUR10_JWk_pODOkjnUTuJDFVbmb9qmXKtWl-A9YVMmZwXmxWlPdwTqA4NKXW8KWSpOqZOCZfiar-Ym9Ayt-sIhxPIGg4EX_8yKZoGVeHgx0lRzeB8dVXFada-x6hz6ERN_anrGf0BXN2xnekykELFvV6eWiHSBuN96VxcnjTVksdwpjBXkDyWT9wIZO5Ii-4hd2HUZAcyPZV7IPUPLLiIXvf_QnuQikz_lGUDCytFlNHH4BR7OY9yJhKmrgRION9JI_WrJWkglPYdS7xKgwfswo0Cd2IyBkB1sfOeRqdA4NAW75Dy8O_xAMMXULJq04ucbTA4UdIHN6Rk2aEAMxhQL30yThFpTCMUqYcgdiY_6d_OMVv_Od0BDU_q8mTc15K_Nrd1_Xr0kitdYgY.2839ldKJHCgvOYf_h3bHXEifSXTbKl4d_pfhc9Gb7-M"
# live_request = requests.post('https://prod.trackmania.core.nadeo.online/v2/authentication/token/ubiservices', headers={'Content-Type':'application/json', 'Authorization':f'ubi_v1 t={api_token}','User-Agent':'CrashmaniaProject'}, data=json_data)
# print(live_request.text)

# Refresh token (refreshing step 2, not mandatory)



# # Oauth token (for getting playernames from accountids)
# data1 = {}
# data1["grant_type"] = "client_credentials"
# data1["client_id"] = "0b6ad88e899829853a19"
# data1["client_secret"] = "88c8c9386dbd91150d056cc19f74a87dec353408"
# json_data1 = json.dumps(data1)
# oauth_token = requests.post('https://api.trackmania.com/api/access_token', headers={'Content-Type':'application/x-www-form-urlencoded'}, data=data1)
# print(oauth_token.text)





# test = requests.get('https://live-services.trackmania.nadeo.live/api/token/club/38508/member?length=53&offset=0', headers={'Authorization':'nadeo_v1 t=eyJhbGciOiJIUzI1NiIsImVudiI6InRyYWNrbWFuaWEtcHJvZCIsInZlciI6IjEifQ.eyJqdGkiOiI1ZGU4ZmNiYS1kNzQ4LTExZWYtOTQ3Yy0wYWUwZDI2NjQyZDMiLCJpc3MiOiJOYWRlb1NlcnZpY2VzIiwiaWF0IjoxNzM3Mzg5MTI4LCJyYXQiOjE3MzczOTA5MjgsImV4cCI6MTczNzM5MjcyOCwiYXVkIjoiTmFkZW9MaXZlU2VydmljZXMiLCJ1c2ciOiJDbGllbnQiLCJzaWQiOiI1ZGU4ZjhiZS1kNzQ4LTExZWYtYWIyNy0wYWUwZDI2NjQyZDMiLCJzYXQiOjE3MzczODkxMjgsInN1YiI6IjUxZDhmZGE0LWVjOTAtNDY0NC04NzJhLWMwMmMzMjZjZjUyMiIsImF1biI6IkFuZHliYWNvZGUiLCJydGsiOmZhbHNlLCJwY2UiOmZhbHNlLCJ1YmlzZXJ2aWNlc191aWQiOiJmZmY4Njk1NC02ZmE2LTQ5ODgtYTdhZi00ODc3MDYzYmIzMTgifQ.L9j1D-Ts93Gg2eh4W43nCUCp4yZTEsPi8i7iYpslLW0'})
# print(test.text)
# members_data = json.loads(test.content.decode("utf-8"))




#print(members_data["clubMemberList"])
#with open("database.txt", "w") as f:
    #f.write(str(members_data["clubMemberList"]))
#    for i in members_data["clubMemberList"]:
#        f.write(str(i["accountId"]))
    #     print(i["accountId"])

