import csv
import os
def get_form_data():
    filepath = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'form_data.csv')
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            if any(row.values()):
                data.append((
                    row["first_name"].strip(),
                    row["middle_name"].strip(),
                    row["last_name"].strip(),
                    row["employee_id"].strip(),
                    row["other_id"].strip(),
                    row["license_number"].strip(),
                    row["license_expiry"].strip(),
                    row["nationality"].strip(),
                    row["marital_status"].strip(),
                    row["date_of_birth"].strip(),
                    row["gender"].strip()
                ))
        return data

