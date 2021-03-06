"""
Code to split the train data into two samples - dev and val. Last four months of 2014 is used as val sample
__author__ : SRK
"""
import csv
from datetime import datetime

with open("../../Data/train.csv") as train_file:
	dev_file = open("../../Data/dev.csv","w")
	val_file = open("../../Data/val.csv","w")

	dev_writer = csv.writer(dev_file)
	val_writer = csv.writer(val_file)

	reader = csv.reader(train_file)
	header = reader.next()
	dev_writer.writerow(["id"] + header)
	val_writer.writerow(["id"] + header)
	date_index = header.index("date_time")

	dev_counter = 0
	val_counter = 0
	total_counter = 0
	for row in reader:
		#print row
		date_val = datetime.strptime(row[date_index], "%Y-%m-%d %H:%M:%S")
		if date_val.year == 2014 and date_val.month >= 9:
			val_writer.writerow([total_counter]+row)
			val_counter += 1
		else:
			dev_writer.writerow([total_counter]+row)
			dev_counter += 1
		total_counter += 1
		if total_counter % 1000000 == 0:
			print total_counter, dev_counter, val_counter

	dev_file.close()
	val_file.close()

