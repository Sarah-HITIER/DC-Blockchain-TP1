from coinBlock import CoinBlock

## 3.1
class Blockchain:
## 3.2
    def __init__(self):
        self.chain = []  # Une liste pour stocker tous les blocs de la blockchain

    def generate_genesis_block(self):
        # Méthode pour générer le bloc initial ou genèse de la chaîne
        genesis_block = CoinBlock(previous_block_hash="0", transaction_list=["Genesis Block"])
        self.chain.append(genesis_block)
        return genesis_block

## 3.3
    def create_block_from_transaction(self, transaction_list):
        # Méthode pour créer un nouveau bloc avec les transactions, l'ajouter à la chaîne et le retourner
        previous_block_hash = self.chain[-1].block_hash  # Le hachage du dernier bloc dans la chaîne
        new_block = CoinBlock(previous_block_hash, transaction_list)
        self.chain.append(new_block)
        return new_block

## 3.4
    def display_chain(self):
        # Méthode pour parcourir la chaîne de blocs et imprimer chaque bloc
        for block in self.chain:
            print(f"Block data: {block.block_data}")
            print(f"Block hash: {block.block_hash}")

## 3.6
    @classmethod
    def is_valid(cls, blockchain):
        # Méthode de classe pour vérifier la validité de la blockchain
        for i in range(1, len(blockchain.chain)):
            current_block = blockchain.chain[i]
            previous_block = blockchain.chain[i - 1]

            # Vérifier si le hachage du bloc précédent correspond réellement au hachage du bloc actuel
            if current_block.previous_block_hash != previous_block.block_hash:
                return False

        return True