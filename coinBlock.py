## 2.2
import hashlib

## Ouvrez un prompt python ou Jupyter et effectuez des tests pour comprendre le fonctionnement l’utilité de la méthode hashlib.sha256().
# import hashlib
# # Créez un objet de hachage sha256
# sha256 = hashlib.sha256()
# # Ajoutez des données à hasher
# data = "Exemple de données à hasher"
# sha256.update(data.encode('utf-8')) // permet d'encoder les données en utf-8
# # Obtenez le résultat du hachage
# result = sha256.hexdigest()
# print(result)
# # 1ce55287f34888444ec613ff2a077b5c35d758509c61fdfe66ff29ed06848159

## Ajoutez une brève explication justifiant l'importation de hashlib.
# Le module hashlib est importé pour utiliser la fonction de hachage sha256.
# Cette fonction est cruciale pour créer des hachages sécurisés des données dans la blockchain,
# garantissant l'intégrité des blocs et la sécurité du réseau.


## 2.3
# Cette classe CoinBlock a une méthode d'initialisation (__init__) qui prend en paramètre le hachage du bloc précédent (previous_block_hash) et la liste des transactions (transaction_list).
# Elle crée alors les propriétés block_data et block_hash en utilisant les méthodes generate_block_data et generate_block_hash respectivement.
class CoinBlock:

## 2.4 
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = self.generate_block_data()  # Appel de la méthode pour générer les données du bloc
        self.block_hash = self.generate_block_hash()  # Appel de la méthode pour générer le hachage du bloc

    def generate_block_data(self):
        # Générer les données du bloc en combinant le hachage précédent et la liste des transactions
        return f"{self.previous_block_hash}-{', '.join(self.transaction_list)}"

    def generate_block_hash(self):
        # Générer le hachage du bloc en utilisant hashlib.sha256()
        sha256 = hashlib.sha256()
        sha256.update(self.block_data.encode('utf-8'))
        return sha256.hexdigest()

## 2.5
    def create_transaction(self, sender, receiver, amount):
        # Créer une transaction sous forme de chaîne
        transaction = f"{sender} sends {amount} CB to {receiver}"
        # Ajouter la transaction à la liste des transactions
        self.transaction_list.append(transaction)

## 2.7
    def create_next_block(self, transaction_list):
        # Créer un nouveau bloc avec le hachage actuel comme hachage précédent
        return CoinBlock(previous_block_hash=self.block_hash, transaction_list=transaction_list)

## 2.9 et 2.10
    @property
    def transaction_list(self):
        # Méthode getter pour l'attribut _transaction_list
        return self._transaction_list

## 2.11
    @transaction_list.setter
    def transaction_list(self, new_transaction_list):
        # Méthode setter pour l'attribut _transaction_list
        self._transaction_list = new_transaction_list
        # Mettez à jour les propriétés liées au bloc après la modification de la liste des transactions
        self.block_data = self.generate_block_data()
        self.block_hash = self.generate_block_hash()