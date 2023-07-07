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
    file = open(file_path, 'rb')
    return file.read()
    

if __name__ == '__main__':
    open_file("testa.txt")