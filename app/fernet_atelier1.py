import os
from cryptography.fernet import Fernet

# Récupère la clé depuis le secret GitHub (variable d'environnement)
key = os.environ.get("FERNET_KEY")

if not key:
    print(" FERNET_KEY non défini !")
    exit(1)

fernet = Fernet(key.encode())

# Chiffrement
with open("secret.txt", "rb") as f:
    data = f.read()

token = fernet.encrypt(data)

with open("secret.enc", "wb") as f:
    f.write(token)

print(" Fichier chiffré : secret.enc")

# Déchiffrement
with open("secret.enc", "rb") as f:
    encrypted = f.read()

decrypted = fernet.decrypt(encrypted)

with open("secret.dec.txt", "wb") as f:
    f.write(decrypted)

print(" Fichier déchiffré : secret.dec.txt")
print(" Contenu :", decrypted.decode())