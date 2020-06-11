import csv


def ejemplo():

    cartelera = [["Top Gun", "Risky Business", "Minority Report"],
                 ["Titanic", "The Revenant", "Inception"],
                 ["Training Day", "Man on Fire", "Flight"]]

    with open('cine.csv', 'w') as f:
        write = csv.writer(f, delimiter=',')
        write = csv.writer(f, delimiter=',')
        for sala in cartelera:
            write.writerow(sala)


ejemplo()
