import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://crashmania-website-1-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = db.reference("/")

#db.reference("/").set({"crashmania-totd":True})
#db.reference("/").set({"crashmania-cotd":True})
#db.reference("/").set({"player-information":True})

#for i in range(1,13): # Lage alle 12 månedene
    #db.reference("/crashmania-totd").set({f"{i}":True})
    ##db.reference(f"/{i}").delete()

#for i in range(1,32): # Lage 31 dager i januar
#    db.reference("/1").set({f"{i}":True})
#    db.reference(f"/1/{i}").delete()
#db.reference("/1/26").delete()
#db.reference("/1/27").delete()
#db.reference("/1/28").delete()
