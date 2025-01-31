import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://crashmania-website-1-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference("/")
db.reference("/").set({"Test":True})
print(ref.get())
db.reference("/Test").set({"Test2":False})
print(db.reference("/Test").get())
print(db.reference("/Test/Test2").get())
db.reference("/Test").delete()