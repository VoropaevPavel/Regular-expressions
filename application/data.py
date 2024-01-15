import csv

def get_raw(raw_data_path):
    with open(raw_data_path, encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        result = list(rows)
    return result

def save_phonebook(data, phonebook):
    with open(phonebook, "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)