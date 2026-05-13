import os
import nacl.secret
import nacl.utils

# Générer une clé secrète de 32 bytes
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# Créer la boîte secrète
box = nacl.secret.SecretBox(key)

# === Chiffrement ===
message = b"Message Top secret !"
encrypted = box.encrypt(message)
print(" Message chiffré :", encrypted.hex())

# === Déchiffrement ===
decrypted = box.decrypt(encrypted)
print("✅ Message déchiffré :", decrypted.decode())