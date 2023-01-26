import hashlib
import datetime


class Block :
    def __init__(self, previous_blockchain_hash, Code_Barre , Nom_Entreprise, Service, Produit, Numero,date):
        self.previous_block_hash = previous_blockchain_hash
        self.Code_Barre = Code_Barre
        self.Nom_Entreprise = Nom_Entreprise
        self.Service = Service
        self.Produit = Produit
        self.Numero = Numero
        self.date = date
        self.hash = self.get_hash()

    @staticmethod
    def create_genesis_block():
        return Block("0", "0", datetime.datetime.now())
    
    def get_hash(self):
        header_bin = (str(self.previous_block_hash) +str(self.Code_Barre) +str(self.Nom_Entreprise) +str(self.Service) +str(self.Produit) + str(self.Numero) + str(self.date)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    