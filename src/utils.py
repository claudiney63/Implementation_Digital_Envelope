# Salva arquivo
# Entrada: caminho para o arquivo, informações que serão salvas
# Saída: nada

import os
import base64

def encode_text_to_base64(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        encoded_text = base64.b64encode(text.encode()).decode()
        return encoded_text

def has_txt_extension(file_path):
    return file_path.lower().endswith('.txt')

def save_file(file_path, data):
    # if has_txt_extension(file_path):
    #     encoded_text = encode_text_to_base64(file_path)
    #     with open(file_path, 'wb') as file:
    #         file.write(encoded_text)
    # else:
    with open(file_path, 'wb') as file:
        file.write(data)


# Abre arquivo
# Entrada: caminho para o arquivo
# Saída: arquivo lido
def open_file(file_path):
    try:
        file = open(file_path, 'rb')
        return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("\n! ! ! Arquivo não encontrado ! ! !\n")
    except Exception as e:
        print(e)

def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False
    

if __name__ == '__main__':
    try:
        open_file("testa.txt")
    except Exception as e:
        print(e)