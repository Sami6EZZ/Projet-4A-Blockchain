import hashlib
import datetime


class Block :
    def __init__(self, hash_block_precedent, Code_Barre , Nom_Entreprise, Service, Produit, Numero,date):
        self.previous_block_hash = hash_block_precedent
        self.Code_Barre = Code_Barre
        self.Nom_Entreprise = Nom_Entreprise
        self.Service = Service
        self.Produit = Produit
        self.Numero = Numero
        self.date = date
        self.hash = self.nouveau_hash()

    @staticmethod
    def nouveau_hash(self):
        header_bin = (str(self.previous_block_hash) +str(self.Code_Barre) +str(self.Nom_Entreprise) +str(self.Service) +str(self.Produit) + str(self.Numero) + str(self.date)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    