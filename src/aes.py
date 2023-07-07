import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes

def encrypt(key, plaintext):
    backend = default_backend() #criação de chave d 256 bits
    key = key[:32]  # Se o tamanho da chave for maior que 32 bytes, pegamos apenas os primeiros 32 byte
    iv = os.urandom(16) # Gerar um vetor de inicialização (IV) de 16 bytes
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend) #utilizada da chave + CBC para criar objeto cripher
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder() #cria objeto padding PKS7
    padded_plaintext = padder.update(plaintext) + padder.finalize() #padding do texto plano
    encryptor = cipher.encryptor() # cria objeto de criptografia
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize() #texto plano + padding

    return iv + ciphertext

def decrypt(key, ciphertext):

    iv = ciphertext[:16] #pegar o vetor de iniciação do começo do texto cifrado
    ciphertext = ciphertext[16:]

    backend = default_backend() #cria backend com a chave e modo de operação CBC
    key = key[:32]  # Se o tamanho da chave for maior que 32 bytes, pegamos apenas os primeiros 32 bytes
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize() # Descriptografar o texto cifrado
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder() #unpandding PKCS7
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize() # Remover o padding do texto plano descriptografado

    return plaintext

def generate_key(size):
    return os.urandom(size)
    
# Exemplo de uso
#key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10'
if __name__ == '__main__':
    key = os.urandom(32)
    plaintext = b'Texto para ser criptografado AES'

    ciphertext = encrypt(key, plaintext)
    decrypted_text = decrypt(key, ciphertext)

    print("Chave AES", key)
    print("Texto cifrado:", ciphertext)
    print("Texto descriptografado:", decrypted_text)