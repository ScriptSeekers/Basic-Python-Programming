import csv
f_p=r"C:\Users\ScriptSeekers\OneDrive - Thakur College of Science and Commerce\Desktop\Data\csv_file_data.csv"
with open(f_p,mode='r') as file:
    csvfile=csv.DictReader(file)
    for line in csvfile:
        print(line)
