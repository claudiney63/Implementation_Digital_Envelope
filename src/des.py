import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt(key, plaintext):
    try:
        # Gerar uma chave de 8 bytes para o DES:
        key = key[:8]  # Se o tamanho da chave for maior que 8 bytes, pegamos apenas os primeiros 8 bytes
        iv = os.urandom(8) # Vetor de inicialização randomico

        # Criar um objeto Cipher com CBC
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())

        # Criar um objeto de padding PKCS7
        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()

        # Realizar o padding do texto plano
        padded_plaintext = padder.update(plaintext) + padder.finalize()

        # Criar um objeto de criptografia
        encryptor = cipher.encryptor()

        # Criptografar o texto plano com o padding
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        return iv + ciphertext
    except Exception as e:
        print("Erro durante a criptografia:", e)

def decrypt(key, ciphertext):
    try:
        iv = ciphertext[:8] # Extrair o IV do início do texto cifrado
        # Objeto Cipher com CBC:
        ciphertext = ciphertext[8:] 
        key = key[:8]  # Se o tamanho da chave for maior que 8 bytes, pegamos apenas os primeiros 8 bytes
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()# Objeto de descriptografia é criado 
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()# Descriptografar o texto cifrado

        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder() # Unpadding 
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize() # Remover o padding

        return plaintext
    # except Exception as e:
    #     print("Erro durante a descriptografia:", e)
    except:
        raise Exception

# Exemplo de uso
# def generate_key(size):
#     try:
#         return os.urandom(size)
#     except Exception as e:
#         print("Erro durante a geração da chave:", e)

# if __name__ == '__main__':
#     try:
#         key = generate_key(24)  # Tamanho da chave é 24 bytes para o TripleDES
#         plaintext = b'Ellem quer chocolate?'

#         ciphertext = encrypt(key, plaintext)
#         decrypted_text = decrypt(key, ciphertext)

#         print("Chave DES:", key)
#         print("Texto cifrado:", ciphertext)
#         print("Texto descriptografado:", decrypted_text)
#     except Exception as e:
#         print("Erro no exemplo de uso:", e)
