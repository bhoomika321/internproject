import csv
def get_login_data(filepath, type_filter=None):
    data = []
    with open(filepath,newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if type_filter is None or row['type'].lower() == type_filter.lower():
                data.append(row)
    return data
