def save_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def open_file(file_path):
    file = open(file_path, 'rb')
    return file.read()