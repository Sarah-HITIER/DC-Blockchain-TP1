## 2.6
from coinBlock import CoinBlock # Importez la classe CoinBlock du fichier coinBlock.py

# Créez une instance représentant le premier bloc de la blockchain (le bloc genèse)
block1 = CoinBlock(previous_block_hash="0", transaction_list=[])

# Créez des transactions en utilisant la méthode create_transaction
# block1.create_transaction(sender="Billy", receiver="Alison", amount=2)
# block1.create_transaction(sender="Charlie", receiver="David", amount=5)

# Affichez les propriétés du premier bloc
# print(f"Block 1 data: {block1.block_data}")
# print(f"Block 1 hash: {block1.block_hash}")
# Block 1 data: 0-
# Block 1 hash: 6e6dda45bc2724d386e74b5f88e6cb4ebeac1caa5c70fa8f24d409da32a91934

## 2.7
# Créez une liste de transactions pour les blocs suivants
transactions_list_2 = ["Alice sends 3 CB to Bob", "Eve sends 1 CB to Mallory"]
transactions_list_3 = ["Bob sends 1 CB to Carol", "Mallory sends 2 CB to Dave"]
transactions_list_4 = ["Carol sends 5 CB to Alice", "Dave sends 3 CB to Eve"]
transactions_list_5 = ["Eve sends 2 CB to Bob", "Mallory sends 1 CB to Carol"]

# Créez les blocs suivants en utilisant la méthode create_next_block
block2 = block1.create_next_block(transactions_list_2)
block3 = block2.create_next_block(transactions_list_3)
block4 = block3.create_next_block(transactions_list_4)
block5 = block4.create_next_block(transactions_list_5)

## 2.8
# Modifiez une transaction dans le bloc 3
# block3.transaction_list[0] = "New transaction: Bob sends 10 CB to Carol"
## Fin 2.8

## 2.10
print(f"Transaction list in Block 3: {block3.transaction_list}")
## Fin 2.10

## 2.13
block3.transaction_list = ["New transaction: Alice sends 5 CB to Bob", "Mallory sends 3 CB to Eve"]
## Fin 2.13

# Affichez les propriétés de chaque bloc
print(f"Block 1 data: {block1.block_data}")
print(f"Block 1 hash: {block1.block_hash}")
print(f"Block 2 data: {block2.block_data}")
print(f"Block 2 hash: {block2.block_hash}")
print(f"Block 3 data: {block3.block_data}")
print(f"Block 3 hash: {block3.block_hash}")
print(f"Block 4 data: {block4.block_data}")
print(f"Block 4 hash: {block4.block_hash}")
print(f"Block 5 data: {block5.block_data}")
print(f"Block 5 hash: {block5.block_hash}")
# Block 1 data: 0-
# Block 1 hash: 6e6dda45bc2724d386e74b5f88e6cb4ebeac1caa5c70fa8f24d409da32a91934
# Block 2 data: 6e6dda45bc2724d386e74b5f88e6cb4ebeac1caa5c70fa8f24d409da32a91934-Alice sends 3 CB to Bob, Eve sends 1 CB to Mallory
# Block 2 hash: 3d8edcce39388b33bd0462fca51e7f5f00df43da26cdf4964483a23ddaa55918
# Block 3 data: 3d8edcce39388b33bd0462fca51e7f5f00df43da26cdf4964483a23ddaa55918-Bob sends 1 CB to Carol, Mallory sends 2 CB to Dave
# Block 3 hash: 1e9118d6bc22cf415e3c3e70661a3aeb208b5848a2bf63375bce79f07a34c152
# Block 4 data: 1e9118d6bc22cf415e3c3e70661a3aeb208b5848a2bf63375bce79f07a34c152-Carol sends 5 CB to Alice, Dave sends 3 CB to Eve
# Block 4 hash: 8707ee27fcac55e1e2e4a6bb9fb4ecaa0701f780d4f16c0a68e0d21e5312ed41
# Block 5 data: 8707ee27fcac55e1e2e4a6bb9fb4ecaa0701f780d4f16c0a68e0d21e5312ed41-Eve sends 2 CB to Bob, Mallory sends 1 CB to Carol
# Block 5 hash: 60285e6a429c3a3a12e614d214a7cbc2a0e9e2831ca6c1f5fed6279909ad6874

## 2.8
# Block 1 data: 0-
# Block 1 hash: 6e6dda45bc2724d386e74b5f88e6cb4ebeac1caa5c70fa8f24d409da32a91934
# Block 2 data: 6e6dda45bc2724d386e74b5f88e6cb4ebeac1caa5c70fa8f24d409da32a91934-Alice sends 3 CB to Bob, Eve sends 1 CB to Mallory
# Block 2 hash: 3d8edcce39388b33bd0462fca51e7f5f00df43da26cdf4964483a23ddaa55918
# Block 3 data: 3d8edcce39388b33bd0462fca51e7f5f00df43da26cdf4964483a23ddaa55918-Bob sends 1 CB to Carol, Mallory sends 2 CB to Dave
# Block 3 hash: 1e9118d6bc22cf415e3c3e70661a3aeb208b5848a2bf63375bce79f07a34c152
# Block 4 data: 1e9118d6bc22cf415e3c3e70661a3aeb208b5848a2bf63375bce79f07a34c152-Carol sends 5 CB to Alice, Dave sends 3 CB to Eve
# Block 4 hash: 8707ee27fcac55e1e2e4a6bb9fb4ecaa0701f780d4f16c0a68e0d21e5312ed41
# Block 5 data: 8707ee27fcac55e1e2e4a6bb9fb4ecaa0701f780d4f16c0a68e0d21e5312ed41-Eve sends 2 CB to Bob, Mallory sends 1 CB to Carol
# Block 5 hash: 60285e6a429c3a3a12e614d214a7cbc2a0e9e2831ca6c1f5fed6279909ad6874

# Un block a été modifié mais pourtant le hachage du bloc 3 n'a pas changé. Normalement, la blockchain devrait être rompue.

## 2.13
# Block 1 data: 0-
# Block 1 hash: 6e6dda45bc2724d386e74b5f88e6cb4ebeac1caa5c70fa8f24d409da32a91934
# Block 2 data: 6e6dda45bc2724d386e74b5f88e6cb4ebeac1caa5c70fa8f24d409da32a91934-Alice sends 3 CB to Bob, Eve sends 1 CB to Mallory
# Block 2 hash: 3d8edcce39388b33bd0462fca51e7f5f00df43da26cdf4964483a23ddaa55918
# Block 3 data: 3d8edcce39388b33bd0462fca51e7f5f00df43da26cdf4964483a23ddaa55918-New transaction: Alice sends 5 CB to Bob, Mallory sends 3 CB to Eve
# Block 3 hash: e333409ba0b2bea69900f3cc3a4c15a6ca6437fe504249f62739cee0f8970a95
# Block 4 data: 1e9118d6bc22cf415e3c3e70661a3aeb208b5848a2bf63375bce79f07a34c152-Carol sends 5 CB to Alice, Dave sends 3 CB to Eve
# Block 4 hash: 8707ee27fcac55e1e2e4a6bb9fb4ecaa0701f780d4f16c0a68e0d21e5312ed41
# Block 5 data: 8707ee27fcac55e1e2e4a6bb9fb4ecaa0701f780d4f16c0a68e0d21e5312ed41-Eve sends 2 CB to Bob, Mallory sends 1 CB to Carol
# Block 5 hash: 60285e6a429c3a3a12e614d214a7cbc2a0e9e2831ca6c1f5fed6279909ad6874

# Le bloc 3 a été modifié et son hachage a changé. La blockchain est donc rompue car le bloc 4 pointe sur un hash et donc sur un bloc qui n'exiiste plus.


## 3.5
from blockchain import Blockchain

# Créez une instance de la classe Blockchain
my_blockchain = Blockchain()

# Générez le bloc initial (le bloc genèse)
my_blockchain.generate_genesis_block()

# Créez des blocs à partir de transactions
transactions_list_1 = ["Alice sends 3 CB to Bob", "Eve sends 1 CB to Mallory"]
transactions_list_2 = ["Bob sends 1 CB to Carol", "Mallory sends 2 CB to Dave"]
transactions_list_3 = ["Carol sends 5 CB to Alice", "Dave sends 3 CB to Eve"]

my_blockchain.create_block_from_transaction(transactions_list_1)
my_blockchain.create_block_from_transaction(transactions_list_2)
my_blockchain.create_block_from_transaction(transactions_list_3)

# Affichez la chaîne de blocs
print("Blockchain before modification:")
my_blockchain.display_chain()
# Block data: 0-Genesis Block
# Block hash: cf6c2cda16ce8b5307669c4c04f7f87007f81437dbfe8806e9b5a98ee0ade6bf
# Block data: cf6c2cda16ce8b5307669c4c04f7f87007f81437dbfe8806e9b5a98ee0ade6bf-Alice sends 3 CB to Bob, Eve sends 1 CB to Mallory
# Block hash: d3d8e15c16daf40186b91d6ead97d5c49e4710623eb57d6c8df4f3799a0c3485
# Block data: d3d8e15c16daf40186b91d6ead97d5c49e4710623eb57d6c8df4f3799a0c3485-Bob sends 1 CB to Carol, Mallory sends 2 CB to Dave
# Block hash: 6aceab1d95cebfe6f8bbb27e58735ed586244b6c73ac0e71a617e969b3e68ad2
# Block data: 6aceab1d95cebfe6f8bbb27e58735ed586244b6c73ac0e71a617e969b3e68ad2-Carol sends 5 CB to Alice, Dave sends 3 CB to Eve
# Block hash: b8e8990e09035f2ec1da4e755af209969ab7c7d58734cc0cac86334a8c1d7ad4

## 3.6
# Vérifiez la validité de la blockchain
if Blockchain.is_valid(my_blockchain):
    print("Blockchain is valid.")
else:
    print("Blockchain is not valid.")
# Blockchain is valid.

my_blockchain.chain[2].transaction_list = ["Modified transaction: Carol sends 10 CB to Bob", "Bob sends 2 CB to Dave"]

# Affichez la chaîne de blocs après modification
print("Blockchain after modification:")
my_blockchain.display_chain()
# Block data: 0-Genesis Block
# Block hash: cf6c2cda16ce8b5307669c4c04f7f87007f81437dbfe8806e9b5a98ee0ade6bf
# Block data: cf6c2cda16ce8b5307669c4c04f7f87007f81437dbfe8806e9b5a98ee0ade6bf-Alice sends 3 CB to Bob, Eve sends 1 CB to Mallory
# Block hash: d3d8e15c16daf40186b91d6ead97d5c49e4710623eb57d6c8df4f3799a0c3485
# Block data: d3d8e15c16daf40186b91d6ead97d5c49e4710623eb57d6c8df4f3799a0c3485-Modified transaction: Carol sends 10 CB to Bob, Bob sends 2 CB to Dave
# Block hash: 4d0568533d89abccda4dc13c81ef3df1240843152163022a6b6bdbbd78828313
# Block data: 6aceab1d95cebfe6f8bbb27e58735ed586244b6c73ac0e71a617e969b3e68ad2-Carol sends 5 CB to Alice, Dave sends 3 CB to Eve
# Block hash: b8e8990e09035f2ec1da4e755af209969ab7c7d58734cc0cac86334a8c1d7ad4

## 3.6
# Vérifiez la validité de la blockchain
if Blockchain.is_valid(my_blockchain):
    print("Blockchain is valid.")
else:
    print("Blockchain is not valid.")
# Blockchain is not valid.