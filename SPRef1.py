import SPDecisionTree

import csv

items = []

with open('datasetf.csv') as csvfile:    
	csvReader = csv.reader(csvfile)    
	for row in csvReader:        
		items.append(row[0]) 

print(items)


#### Create a function for retreiveing the ip addresses of potential bots in the system