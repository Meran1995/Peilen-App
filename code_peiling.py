import csv

BESTAND = (r'C:\Users\meran\OneDrive\Bureaublad\Python\Peilen.Lodi\voorbeeld_peiling.csv')

def search_for_empty_input(row):
    van_naar = row[0]
    x_coordinatie = row[1]
    y_coordinatie = row[2]
    leeg_vak = row[3]
    app_input = row[4]

    if '' == row[4]:
        print(van_naar + ' '+ x_coordinatie + '. ' + y_coordinatie + '. ' + ' Need to go back! ')



with open(BESTAND, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:

        search_for_empty_input(row)
