pimport SPDecisionTree
from SPDecisionTree import predicted 
from SPDecisionTree import df
from SPDecisionTree import x
from SPDecisionTree import predictions
import csv

items = []

with open('datasetf.csv') as csvfile:    
	csvReader = csv.reader(csvfile)    
	for row in csvReader:        
		items.append(row[0]) 

print(items)

print(df.loc[df['No.'] == int(items[3]), 'Source'])

ip = df[['Source']].values 

for i in range(len(ip)):
	if any((ip)) == any(predictions):
		print("The following is a bot!")
	else:
		print("The following is a normal user")

