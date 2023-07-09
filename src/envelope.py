if __name__ == '__main__':
    # Importar módulos necessários de acordo com o contexto
    import aes
    import des
    import rc4
    import rsa
    import utils
else:
    import src.aes as aes
    import src.des as des
    import src.rc4 as rc4
    import src.rsa as rsa
    import src.utils as utils

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

def create_envelope(plain_file_path, public_key_path, algorithm):
    try:
        # Carregar a chave pública do destinatário
        public_key = rsa.load_public_key(public_key_path)
        
        # Abrir o arquivo em claro
        plain_file = utils.open_file(plain_file_path)
        
        # Verificar se a chave pública é válida
        if not isinstance(public_key, RSAPublicKey):
            raise Exception("! A chave pública não é válida")
        
        if algorithm == 'AES':
            # Gerar uma chave simétrica AES de 32 bytes
            simetric_key = aes.generate_key(32)
            
            # Criptografar o arquivo em claro usando a chave simétrica AES
            encrypted_file = aes.encrypt(simetric_key, plain_file)
        
        elif algorithm == 'DES':
            # Gerar uma chave simétrica DES de 8 bytes
            simetric_key = des.generate_key(8)
            
            # Criptografar o arquivo em claro usando a chave simétrica DES
            encrypted_file = des.encrypt(simetric_key, plain_file)
        
        elif algorithm == 'RC4':
            # Gerar uma chave simétrica RC4
            simetric_key = rc4.generate_rc4_key()
            
            # Criptografar o arquivo em claro usando a chave simétrica RC4
            encrypted_file = rc4.encrypt_decrypt(simetric_key, plain_file)
        
        else:
            raise Exception("! Algoritmo simétrico não encontrado")

        # Criptografar a chave simétrica usando a chave pública do destinatário
        encrypted_key = rsa.encrypt(public_key, simetric_key)

        # Salvar a chave criptografada em um arquivo
        utils.save_file("encrypted_simetric_key.key", encrypted_key)
        
        # Salvar o arquivo criptografado em um arquivo
        utils.save_file("encrypted_" + plain_file_path, encrypted_file)

        print("\n> > Envelope criado com sucesso!\n")
    except Exception as e:
        print("! Erro ao criar envelope:", e)

def open_envelope(encrypted_file_path, encrypted_key_path, private_key_path, algorithm):
    try:
        # Carregar a chave privada do destinatário
        private_key = rsa.load_private_key(private_key_path)
        
        # Carregar a chave simétrica criptografada
        encrypted_key = utils.open_file(encrypted_key_path)
        
        # Carregar o arquivo criptografado
        encrypted_file = utils.open_file(encrypted_file_path)

        # Descriptografar a chave simétrica usando a chave privada do destinatário
        simetric_key = rsa.decrypt(private_key, encrypted_key)
        
        if algorithm == 'AES':
            # Descriptografar o arquivo usando a chave simétrica AES
            decrypted_file = aes.decrypt(simetric_key, encrypted_file)

        elif algorithm == 'DES':
            # Descriptografar o arquivo usando a chave simétrica DES
            decrypted_file = des.decrypt(simetric_key, encrypted_file)
        
        elif algorithm == 'RC4':
            # Descriptografar o arquivo usando a chave simétrica RC4
            decrypted_file = rc4.encrypt_decrypt(simetric_key, encrypted_file)

        else:
            raise Exception("! Algoritmo simétrico não encontrado")

        # Salvar o arquivo descriptografado em um arquivo
        utils.save_file("decrypted_" + encrypted_file_path, decrypted_file)

        print("\n> > Envelope aberto com sucesso!\n")
    except Exception as e:
        print("! Erro ao abrir envelope:", e)

if __name__ == '__main__':
    #cifrar
    # try:
    #     create_envelope("image.png", "ellem_public_key.pem", "AES")
    # except Exception as e:
    #     print(e)

    
    #decifrar
    try:
        open_envelope("encrypted_image.png", "encrypted_simetric_key.key", "ellem_private_key.pem","AES")
    except Exception as e:
        print(e)


    print("fim")
