from sys import displayhook
from pymongo import MongoClient
import datetime
from pandas import DataFrame

client = MongoClient("mongodb+srv://projet_4A:projet_4A@cluster0.unojzpe.mongodb.net/?retryWrites=true&w=majority")
db = client.test
base_donnees = client.get_database('projet_4A_db')


blockch = base_donnees.blockchain

afficher = list(blockch.find({'Code_Barre' : '3103220025338'}))
df =   DataFrame(afficher)


print(df[['date','Code_Barre','Produit','Nom_Entreprise','Service']])







client.close()
