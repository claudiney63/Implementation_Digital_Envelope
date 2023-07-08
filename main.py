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

        index = input("Selecione uma opção:\n" + "\n".join(options) + "\n")
        
        # Criar par de chaves
        if index == "0":
            filepath = input("Informe em que pasta ficarão as chaves (deixar vazio para pasta atual):\n~ ")
            prefixo = input("Informe o prefixo do arquivo (opcional):\n~ ")
            
            rsa.generate_key_pair(prefixo, filepath)
            print(f"\nPar de chaves criado\n")

            input("Tecle enter para voltar ao menu.")

        # Criar envelope
        if index == "1":
            #criar arquivo em claro
			#arquivo da chave RSA pública
			#algoritmo
            plain_file_path = input("Informe o arquivo que deseja criptografar:\n~ ")
            public_key_path = input("Informe a chave pública que deseja utilizar:\n~ ")
            encrypt_algorithm = input("Qual algoritmo deseja usar: [AES, DES, RC4]:\n> ")

            try:
                envelope.create_envelope(plain_file_path, public_key_path, encrypt_algorithm)
            except Exception as e:
                print(e)
            else:
                print("Envelope criado com sucesso\n")

            input("Tecle enter para voltar ao menu.")
        
        # Abrir envelope
        if index == "2":
            cipher_file_path = input("Informe o caminho até o arquivo criptografado do envelope:\n~ ")
            cipher_key_path = input("Informe a chave criptografada:\n~ ")
            cipher_file = utils.open_file(cipher_file_path)
            cipher_key = utils.open_file(cipher_key_path)
            decrypt_algorithm = input("Qual algoritmo deseja usar: [AES, DES, RC4]:\n> ")
            private_key_path = input("Informe o local da chave privada:")
            private_key = rsa.load_private_key(private_key_path)
            
            envelope.open_envelope(cipher_file, cipher_key, decrypt_algorithm, private_key)
                # is_valid = verify_envelop(
                #     ph.abspath(file),
                #     ph.abspath(signature_file),
                #     ph.abspath(key_file),
                #     hash_algorithm,
                #     verbose=True
                # )
                # if is_valid:
                #     print("O envelope é válido.")
                # else:
                #     print("O envelope não é válido.")

            input("Tecle enter para voltar ao menu.")
        
        # Sair
        if index == "3":
            print("Programa finalizado.")
            return


if __name__ == "__main__":
    menu()
