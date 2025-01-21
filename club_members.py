import requests, json

with open("databasetest.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    live_token = "eyJhbGciOiJIUzI1NiIsImVudiI6InRyYWNrbWFuaWEtcHJvZCIsInZlciI6IjEifQ.eyJqdGkiOiJlYWYxMDM2ZS1kODE1LTExZWYtOWNmYi0wMmQyZDkzYWYwNGQiLCJpc3MiOiJOYWRlb1NlcnZpY2VzIiwiaWF0IjoxNzM3NDc3NDExLCJyYXQiOjE3Mzc0NzkyMTEsImV4cCI6MTczNzQ4MTAxMSwiYXVkIjoiTmFkZW9MaXZlU2VydmljZXMiLCJ1c2ciOiJDbGllbnQiLCJzaWQiOiJlYWYwZmZmZS1kODE1LTExZWYtOTg2Ni0wMmQyZDkzYWYwNGQiLCJzYXQiOjE3Mzc0Nzc0MTEsInN1YiI6IjUxZDhmZGE0LWVjOTAtNDY0NC04NzJhLWMwMmMzMjZjZjUyMiIsImF1biI6IkFuZHliYWNvZGUiLCJydGsiOmZhbHNlLCJwY2UiOmZhbHNlLCJ1YmlzZXJ2aWNlc191aWQiOiJmZmY4Njk1NC02ZmE2LTQ5ODgtYTdhZi00ODc3MDYzYmIzMTgifQ.FVRvG9sflF6_QkDFIDW26uF4k7Hy4hXaelnePERTCeQ"
    for i in range(0,1):
        #print(data[i])
        #print(i)
        amountOfPlayers = 3
        player = requests.get(f'https://live-services.trackmania.nadeo.live/api/token/leaderboard/group/Personal_Best/map/rMs2G52XPsbICMTjLLCFeBOKJF4/club/38508/top?length={amountOfPlayers}&offset=0', headers={'Authorization':f'nadeo_v1 t={live_token}'})
        #print(player.text)

    leaderboard_data = json.loads(player.content.decode("utf-8"))
    

    core_token = "eyJhbGciOiJIUzI1NiIsImVudiI6InRyYWNrbWFuaWEtcHJvZCIsInZlciI6IjEifQ.eyJqdGkiOiI3MzA4NTNhNC1kODE4LTExZWYtYmFiNi0wYTU4YTlmZWFjMDIiLCJpc3MiOiJOYWRlb1NlcnZpY2VzIiwiaWF0IjoxNzM3NDc4NDk5LCJyYXQiOjE3Mzc0ODAyOTksImV4cCI6MTczNzQ4MjA5OSwiYXVkIjoiTmFkZW9TZXJ2aWNlcyIsInVzZyI6IkNsaWVudCIsInNpZCI6IjczMDg1MWE2LWQ4MTgtMTFlZi05MmY3LTBhNThhOWZlYWMwMiIsInNhdCI6MTczNzQ3ODQ5OSwic3ViIjoiNTFkOGZkYTQtZWM5MC00NjQ0LTg3MmEtYzAyYzMyNmNmNTIyIiwiYXVuIjoiQW5keWJhY29kZSIsInJ0ayI6ZmFsc2UsInBjZSI6ZmFsc2UsInViaXNlcnZpY2VzX3VpZCI6ImZmZjg2OTU0LTZmYTYtNDk4OC1hN2FmLTQ4NzcwNjNiYjMxOCJ9.onR6wafiPYNVjxXI2LN3Y7vsmgUeaERnyWfHF_ebTto"
    oauth_token = ""

    username = requests.get('https://api.trackmania.com/api/display-names?accountId[]=d3d84336-fc5f-49fd-b866-b15ca80152a8', headers={'Authorization':f'Bearer {oauth_token}'})
    print(username)

    for i in leaderboard_data["top"]:
        account_id = i["accountId"]
        time = i["score"]
        print(account_id)
        print(time)
        

    



