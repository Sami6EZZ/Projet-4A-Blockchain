from pymongo import MongoClient
import datetime
from blockchain import Block
from pandas import DataFrame



client = MongoClient("mongodb+srv://projet_4A:projet_4A@cluster0.unojzpe.mongodb.net/?retryWrites=true&w=majority")

base_donnees = client.get_database('projet_4A_db')


blockch = base_donnees.blockchain

#blockch.insert_one(nouveau_block)

def systeme ():
  fonction = True
  while fonction == True:  
    commande = input("\n\n\nPour consulter les informations d'un produit saisissez : \'consulter'. \nPour ajouter un nouveau block saisisser : \'ajouter'. \nPour quitter saisissez : \'exit'. \n >>>")

    if commande == 'ajouter':
        codeBarre = input("Veuillez saisir le code barre du produit : ")
        trouver = blockch.find({'Code_Barre' : codeBarre })
        lenght = len(list(trouver))
        NomEntreprise = input("Veuillez saisir le nom de l'entreprise : ")
        produit = input("Veuillez saisir le nom du produit : ")
        Services = input("Veuillez saisir le service : ")
        numéro = lenght+1
        if lenght == 0:
            b = [Block("0",codeBarre,NomEntreprise, Services,produit, numéro,datetime.datetime.now() )]
            aj = { 'hash':  b[-1].hash,
                  'Code_Barre': b[-1].Code_Barre,
                    'Nom_Entreprise': b[-1].Nom_Entreprise,
                    'Service': b[-1].Service,
                    'Produit' : b[-1].Produit,
                    'Numero': b[-1].Numero,
                    'date' : str(b[-1].date)
                
            }
            blockch.insert_one(aj)
            print("Une nouvelle chaine a été crée")
            afficher = list(blockch.find({'Code_Barre' : codeBarre}))
            df =   DataFrame(afficher)

            print(df[['date','Code_Barre','Produit','Nom_Entreprise','Service']])

        
        else :
            trouver_h = blockch.find({'Code_Barre' : codeBarre , 'Numero' : lenght})

            for p in  trouver_h:
                p_hash = p['hash']
                print(p_hash)
            b = [Block(p_hash,codeBarre,NomEntreprise, Services,produit, numéro,datetime.datetime.now() )]
            aj = { 'hash':  b[-1].hash,
                  'Code_Barre': b[-1].Code_Barre,
                    'Nom_Entreprise': b[-1].Nom_Entreprise,
                    'Service': b[-1].Service,
                    'Produit' : b[-1].Produit,
                    'Numero': b[-1].Numero,
                    'date' : str(b[-1].date)
                
            }
            blockch.insert_one(aj)
            print("Enregistré avec succàs")
            afficher = list(blockch.find({'Code_Barre' : codeBarre}))
            df =   DataFrame(afficher)

            print(df[['date','Code_Barre','Produit','Nom_Entreprise','Service']])



    if commande == 'consulter':
        codeBarre = input("Veuillez saisir le code barre du produit : ")
        trouver = blockch.find({'Code_Barre' : codeBarre })
        lenght = len(list(trouver))
        if lenght == 0: print("Il n y'a aucune infirmation enregistrée pour ce code bare.")
        else:
            afficher = list(blockch.find({'Code_Barre' : codeBarre}))
            df =   DataFrame(afficher)

            print(df[['date','Code_Barre','Produit','Nom_Entreprise','Service']])


    if commande == 'exit':
        fonction = False
    else:
        print("Commande non identifiée. Veuillez saisir la commande en minuscule.")

systeme()

client.close()
