import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes

def aes_encrypt(key, plaintext):
    # Gerar uma chave de 256 bits
    backend = default_backend()
    key = key[:32]  # Se o tamanho da chave for maior que 32 bytes, pegamos apenas os primeiros 32 bytes

    # Gerar um vetor de inicialização (IV) de 16 bytes
    iv = os.urandom(16)

    # Criar um objeto Cipher usando a chave e o modo de operação CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # Criar um objeto de padding PKCS7
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    # Realizar o padding do texto plano
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Criar um objeto de criptografia
    encryptor = cipher.encryptor()

    # Criptografar o texto plano com o padding
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv + ciphertext

def aes_decrypt(key, ciphertext):
    # Extrair o IV do início do texto cifrado
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    # Criar um objeto Cipher usando a chave e o modo de operação CBC
    backend = default_backend()
    key = key[:32]  # Se o tamanho da chave for maior que 32 bytes, pegamos apenas os primeiros 32 bytes
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # Criar um objeto de descriptografia
    decryptor = cipher.decryptor()

    # Descriptografar o texto cifrado
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Criar um objeto de unpadding PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

    # Remover o padding do texto plano descriptografado
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

# Exemplo de uso
#key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10'
key = os.urandom(32)
plaintext = b'Texto para ser criptografado'

ciphertext = aes_encrypt(key, plaintext)
decrypted_text = aes_decrypt(key, ciphertext)

print("Chave AES", key)
print("Texto cifrado:", ciphertext)
print("Texto descriptografado:", decrypted_text)