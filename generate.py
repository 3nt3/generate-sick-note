from os import system
import os
import csv
from sys import argv

# create csv file and add data
with open('data.csv', 'w') as csvfile:
    csv.writer(csvfile).writerow(['date', 'date_range'])
    csv.writer(csvfile).writerow([argv[1], argv[2]])

# generate sla
system("python2 ~/src/other/ScribusGenerator/ScribusGeneratorCLI.py ~/Documents/entschuldigung.sla -c data.csv -n output -o /tmp/entschuldigung")

# remove csv
os.remove('data.csv')

# generate pdf
system("scribus -g -py ~/src/other/ScribusGenerator/to-pdf.py -- /tmp/entschuldigung/output.sla")

system("zathura /tmp/entschuldigung/output.pdf")
