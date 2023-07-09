import os
import src.envelope as envelope
import src.aes as aes
import src.des as des
import src.rc4 as rc4
import src.rsa as rsa
import src.utils as utils

def menu():
    menu = """
0 - Criar um par de chaves RSA
1 - Criar um envelope;
2 - Abrir um envelope;
3 - Sair
    """
    title = "Selecione uma opção:"
    options = [
        "[0] - Criar um par de chaves RSA;",
        "[1] - Criar um envelope;",
        "[2] - Abrir envelope",
        "[3] - Sair.",
    ]
    while True:

        index = input("Selecione uma opção:\n" + "\n".join(options) + "\n~ ")
        
        # Criar par de chaves
        if index == "0":
            filepath = input("\nCaminho de salvamento das chaves (deixar vazio para pasta atual):\n~ ")
            prefixo = input("\nPrefixo do arquivo (opcional):\n~ ")
            
            try:
                rsa.generate_key_pair(prefixo, filepath)
            except Exception as e:
                print(e)

            input("Tecle enter para voltar ao menu.")

        # Criar envelope
        if index == "1":
            plain_file_path = input("\nCaminho para arquivo que deseja criptografar:\n~ ")
            public_key_path = input("\nCaminho para a chave pública (.pem):\n~ ")
            encrypt_algorithm = input("\nAlgoritmo simétrico: [AES, DES, RC4]:\n> ")
            encrypt_algorithm = encrypt_algorithm.upper()

            try:
                envelope.create_envelope(plain_file_path, public_key_path, encrypt_algorithm)
            except Exception as e:
                print(e)

            input("Tecle enter para voltar ao menu.")
        
        # Abrir envelope
        if index == "2":
            
            encrypted_file_path = input("\nCaminho para o arquivo criptografado:\n~ ")
            encrypted_simetric_key_path = input("\nCaminho para a chave simétrica criptografada (.key):\n~ ")
            private_key_path = input("\nCaminho para a chave privada (.pem):\n~ ")
            decrypt_algorithm = input("\nAlgoritmo simétrico: [AES, DES, RC4]:\n> ")
            decrypt_algorithm = decrypt_algorithm.upper()

            try:
                envelope.open_envelope(encrypted_file_path, encrypted_simetric_key_path, private_key_path, decrypt_algorithm)
            except Exception as e:
                print(e)

            input("Tecle enter para voltar ao menu.\n")
        
        # Sair
        if index == "3":
            print("Programa finalizado.")
            return


if __name__ == "__main__":
    menu()
