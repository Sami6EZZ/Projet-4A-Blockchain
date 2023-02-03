from pymongo import MongoClient
import datetime
from blockchain import Block
from pandas import DataFrame
#Bibliothéques à installer
#Ajouter l'extention 'PowerShell (pour pouvour installer les bibliothéque directement via le terminal de vs code)
#pip install pandas
#pip install pymongo


#connexion evec le cluster
client = MongoClient("mongodb+srv://projet_4A:projet_4A@cluster0.unojzpe.mongodb.net/?retryWrites=true&w=majority")
#connecxion avec la base de données
base_donnees = client.get_database('projet_4A_db')
#l'importation du tableau nommé 'blockchain'
Blockchaine = base_donnees.blockchain

#blockch.insert_one(nouveau_block)

def systeme ():
  fonction = True
  #une boucle while qui se termine après la saisi de la commande 'exit'
  while fonction == True:  
    #ajouter un block ou consulter une chaie de blocks ou quitter
    commande = input("\n\n\nTraçabilité de la fourche à la fourchette.\n\nPour consulter les informations d'un produit, saisissez : \'consulter'. \nPour ajouter un nouveau block, saisisser : \'ajouter'. \nPour quitter, saisissez : \'exit'. \n >>>")

    if commande == 'ajouter':
        codeBarre = input("Veuillez saisir le code barre du produit : ")
        #recherch de tous les blocks contenants le même code barre
        trouver = Blockchaine.find({'Code_Barre' : codeBarre })
        NomEntreprise = input("Veuillez saisir le nom de l'entreprise : ")
        produit = input("Veuillez saisir le nom du produit : ")
        Services = input("Veuillez saisir le service : ")
        #nombre des blocks enregistrés
        lenght = len(list(trouver))
        numéro = lenght+1
        #si le dictionnaire est vide, on crée un nouveau block avec un hash égal à "0"
        if lenght == 0:
            b = [Block("0",codeBarre,NomEntreprise, Services,produit, numéro,datetime.datetime.now() )]
            #dictionnaire contenant les élements du block à enregistrés dans la base de données
            aj = { 'hash':  b[-1].hash,
                  'Code_Barre': b[-1].Code_Barre,
                    'Nom_Entreprise': b[-1].Nom_Entreprise,
                    'Service': b[-1].Service,
                    'Produit' : b[-1].Produit,
                    'Numero': b[-1].Numero,
                    'date' : str(b[-1].date)
                
            }
            Blockchaine.insert_one(aj)
            print("\nUne nouvelle chaine a été crée")
            #convertir le block en une liste
            afficher = list(Blockchaine.find({'Code_Barre' : codeBarre}))
            #convertir la liste en 'DataFrame' pour facilité l'affichage du tableau
            df =   DataFrame(afficher)

            print(df[['date','Code_Barre','Produit','Nom_Entreprise','Service']])

        #si le dictionnaire n'est pas vide
        else :
            #on cherche le hash du dérnier élément en utilisant le numéro de dérie
            trouver_h = Blockchaine.find({'Code_Barre' : codeBarre , 'Numero' : lenght})

            for p in  trouver_h:
                p_hash = p['hash']
                print(p_hash)
            b = [Block(p_hash,codeBarre,NomEntreprise, Services,produit, numéro,datetime.datetime.now() )]
            #dictionnaire contenant les élements du block à enregistrés dans la base de données
            aj = { 'hash':  b[-1].hash,
                  'Code_Barre': b[-1].Code_Barre,
                    'Nom_Entreprise': b[-1].Nom_Entreprise,
                    'Service': b[-1].Service,
                    'Produit' : b[-1].Produit,
                    'Numero': b[-1].Numero,
                    'date' : str(b[-1].date)
                
            }
            Blockchaine.insert_one(aj)
            print("Enregistré avec succàs")
            #convertir le block en une liste
            afficher = list(Blockchaine.find({'Code_Barre' : codeBarre}))
            #convertir la liste en 'DataFrame' pour facilité l'affichage du tableau
            df =   DataFrame(afficher)

            print(df[['date','Code_Barre','Produit','Nom_Entreprise','Service']])



    elif commande == 'consulter':
        codeBarre = input("Veuillez saisir le code barre du produit : ")
        trouver = Blockchaine.find({'Code_Barre' : codeBarre })
        lenght = len(list(trouver))
        #sil n y'a aucune information enregistrée avec ce code barre, le code retourne un message d'erreur
        if lenght == 0: print("Il n y'a aucune infirmation enregistrée pour ce code bare.")
        else:
            afficher = list(Blockchaine.find({'Code_Barre' : codeBarre}))
            df =   DataFrame(afficher)

            print(df[['date','Code_Barre','Produit','Nom_Entreprise','Service']])


    elif commande == 'exit':
        #sortir de la boucle while
        fonction = False

    elif commande !='exit' and commande !='ajouter' and commande !='consulter':
        print("Commande non identifiée. Veuillez saisir la commande en minuscule.")

systeme()

client.close()
