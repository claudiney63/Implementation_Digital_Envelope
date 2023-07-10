# Salva arquivo
# Entrada: caminho para o arquivo, informações que serão salvas
# Saída: nada

import os
import base64
import tkinter as tk
from tkinter import filedialog

def encode_text_to_base64(file_path):
    with open(file_path, 'rb') as file:
        text = file.read()
        encoded_text = base64.b64encode(text)
        return encoded_text
    
def b64_encode(encrypted_file_path):
    try:
        with open(encrypted_file_path, 'rb') as file:
            text = file.read()
            encoded_text = base64.b64encode(text)
            return encoded_text
    except FileNotFoundError:
        raise FileNotFoundError("\n! Arquivo não encontrado!\n")
    except Exception as e:
        print(e)

def save_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def save_encrypted_key(key_path, data):
    with open(key_path, 'wb') as file:
        file.write(base64.b64encode(data))

# Abre arquivo
# Entrada: caminho para o arquivo
# Saída: arquivo lido
def open_file(file_path):
    try:
        file = open(file_path, 'rb')
        return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("\n! Arquivo não encontrado!\n")
    except Exception as e:
        print(e)

def open_encrypted_key(key_path):
    try:
        file = open(key_path, 'rb')
        return base64.b64decode(file.read())
    except FileNotFoundError:
        raise FileNotFoundError("\n! Chave não encontrada!\n")
    except Exception as e:
        print(e)

def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False
    

if __name__ == '__main__':
    print("")
    #save_encrypted_key("b64.key",open_file("encrypted_simetric_key.key"))
    #print(base64.b64decode(open_file("b64.key")))