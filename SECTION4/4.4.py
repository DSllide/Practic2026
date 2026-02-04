import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding


message = "Привіт, світ!"
sha256_hash = hashlib.sha256(message.encode()).hexdigest()
print("SHA-256 геш повідомлення:", sha256_hash)


from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(32)
iv = os.urandom(16)

padder = padding.PKCS7(128).padder()
padded_data = padder.update(message.encode()) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()
print("AES зашифроване повідомлення (bytes):", ciphertext)

decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
print("Розшифроване AES повідомлення:", decrypted.decode())


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()


signature = private_key.sign(
    message.encode(),
    asym_padding.PSS(
        mgf=asym_padding.MGF1(hashes.SHA256()),
        salt_length=asym_padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Цифровий підпис (bytes):", signature)


try:
    public_key.verify(
        signature,
        message.encode(),
        asym_padding.PSS(
            mgf=asym_padding.MGF1(hashes.SHA256()),
            salt_length=asym_padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Підпис підтверджено ✅")
except Exception as e:
    print("Підпис не підтверджено ❌", e)


print("\nПояснення:")
print("- SHA-256 геш: неможливо відновити оригінальне повідомлення з хешу. Це одностороння функція.")
print("- AES: можна зашифрувати і потім розшифрувати повідомлення, якщо є ключ. Це двостороннє шифрування.")
print("- RSA цифровий підпис дозволяє підтвердити авторство повідомлення, не розкриваючи приватний ключ.")
