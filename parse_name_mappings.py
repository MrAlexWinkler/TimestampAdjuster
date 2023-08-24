def parse_name_mappings(file_path):
    name_url_mapping = {}
    with open(file_path, 'r') as f:
        for line in f:
            if ': ' in line:
                name, url = line.strip().split(': ')
                name_url_mapping[name] = url
    return name_url_mapping
