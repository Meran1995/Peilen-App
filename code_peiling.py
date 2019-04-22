import csv

bestand = (r'C:\Users\meran\OneDrive\Bureaublad\Python\Peilen.Lodi\voorbeeld_peiling.csv')

with open(bestand, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:

        def search_for_empty_input():

            van_naar = (row[0])
            x_coordinatie = (row[1])
            y_coordinatie = (row[2])
            leeg_vak = (row[3])
            app_input = (row[4])
        
            if '' == row[4]:
                print(van_naar + ' '+ x_coordinatie + '. ' + y_coordinatie + '. ' + ' Need to go back! ')
            else:
                print(row)

        search_for_empty_input()