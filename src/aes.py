import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt(key, plaintext):
    try:
        backend = default_backend() # Criação de uma chave de 256 bits
        key = key[:32]  # Se o tamanho da chave for maior que 32 bytes, pegamos apenas os primeiros 32 bytes
        iv = os.urandom(16) # Gera um vetor de inicialização (IV) de 16 bytes
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend) # Cria um objeto Cipher com a chave e o modo de operação CBC
        
        padder = padding.PKCS7(algorithms.AES.block_size).padder() # Cria um objeto de padding PKCS7
        padded_plaintext = padder.update(plaintext) + padder.finalize() # Realiza o padding do texto plano
        encryptor = cipher.encryptor() # Cria um objeto de criptografia
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize() # Criptografa o texto plano com o padding

        return iv + ciphertext
    except Exception as e:
        print("Erro durante a criptografia:", e)

def decrypt(key, ciphertext):
    try:
        iv = ciphertext[:16] # Obtém o IV do início do texto cifrado
        ciphertext = ciphertext[16:]

        backend = default_backend() # Cria um objeto Cipher com a chave e o modo de operação CBC
        key = key[:32]  # Se o tamanho da chave for maior que 32 bytes, pegamos apenas os primeiros 32 bytes
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()

        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize() # Descriptografa o texto cifrado
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder() # Cria um objeto de unpadding PKCS7
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize() # Remove o padding do texto plano descriptografado

        return plaintext
    # except Exception as e:
    #     print("Erro durante a descriptografia:", e)
    except:
        raise Exception

def generate_key(size):
    try:
        return os.urandom(size)
    except Exception as e:
        print("Erro durante a geração da chave:", e)
    

    
    
