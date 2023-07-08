# Salva arquivo
# Entrada: caminho para o arquivo, informações que serão salvas
# Saída: nada
def save_file(file_path, data):
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
        raise FileNotFoundError("Arquivo não encontrado")
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    try:
        open_file("testa.txt")
    except Exception as e:
        print(e)