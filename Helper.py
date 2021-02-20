
def generate_file_path(base_path, file_name):
    return base_path + "/" + file_name


def generate_json_file(json_data, file_name):
    import json
    with open(file_name, 'w') as f:
        json.dump(json_data, f)


def copy_data(data_to_copy):
    return data_to_copy.copy()