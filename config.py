import pymongo
import certifi

#this is the connection string that i got from the mongoDB connection
con_string = "mongodb+srv://daphane_elizabeth:plmplmplm1@cluster0.qgmiy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_string, tlsCAFile =certifi.where())
db = client.get_database("CrystalWiki")