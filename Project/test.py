import csv

listip=['192.168.0.4','192.168.0.5']

with open('main.csv') as csvfile:
    data=csv.reader(csvfile)
    for row in data:
        for ip in listip:
            if ip in row:
                print row

