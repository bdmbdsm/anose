def read_file_at_once(location):
    file_data = None

    with open(location, 'r') as f:
        file_data = f.read()

    return file_data
