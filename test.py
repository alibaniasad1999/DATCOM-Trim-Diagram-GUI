import csv
a = []
with open('export/Trim_diag.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        a.append(i)

print(a)