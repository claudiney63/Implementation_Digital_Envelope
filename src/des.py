import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt(key, plaintext):
    try:
        # Gerar uma chave de 8 bytes para o DES
        key = key[:8]  # Se o tamanho da chave for maior que 8 bytes, pegamos apenas os primeiros 8 bytes

        # Gerar um vetor de inicialização (IV) de 8 bytes
        iv = os.urandom(8)

        # Criar um objeto Cipher usando a chave e o modo de operação CBC
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
        # Extrair o IV do início do texto cifrado
        iv = ciphertext[:8]
        ciphertext = ciphertext[8:]

        # Criar um objeto Cipher usando a chave e o modo de operação CBC
        key = key[:8]  # Se o tamanho da chave for maior que 8 bytes, pegamos apenas os primeiros 8 bytes
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())

        # Criar um objeto de descriptografia
        decryptor = cipher.decryptor()

        # Descriptografar o texto cifrado
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Criar um objeto de unpadding PKCS7
        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()

        # Remover o padding do texto plano descriptografado
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        return plaintext
    except Exception as e:
        print("Erro durante a descriptografia:", e)

# Exemplo de uso
def generate_key(size):
    try:
        return os.urandom(size)
    except Exception as e:
        print("Erro durante a geração da chave:", e)

if __name__ == '__main__':
    try:
        key = generate_key(24)  # Tamanho da chave é 24 bytes para o TripleDES
        plaintext = b'Ellem quer chocolate?'

        ciphertext = encrypt(key, plaintext)
        decrypted_text = decrypt(key, ciphertext)

        print("Chave DES:", key)
        print("Texto cifrado:", ciphertext)
        print("Texto descriptografado:", decrypted_text)
    except Exception as e:
        print("Erro no exemplo de uso:", e)
