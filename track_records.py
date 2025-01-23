import requests, json
from get_tokens import get_core_token

token = get_core_token()
time = requests.get('https://prod.trackmania.core.nadeo.online/v2/mapRecords/?accountIdList=d3d84336-fc5f-49fd-b866-b15ca80152a8&mapId=7cb84327-d8a2-4652-a6bf-3e954077f18c', headers={'Authorization':f'nadeo_v1 t={token}'})
print(time.text)
