import csv
import matplotlib.pyplot as plt


st_filename = "jma_temperature_data_nagoya_2007-2016.csv"

jma_temperature_data = []

with open(st_filename, 'r') as fp_data:
	reader = csv.reader(fp_data)
	header = next(reader)
	header = next(reader)
	header = next(reader)
	header = next(reader)
	header = next(reader)
	header = next(reader)

	for row in reader:
		if row:
#			jma_temperature_data.append([row[0], row[2], row[5], row[8]])
			jma_temperature_data.append([row[2], row[5], row[8]])

print jma_temperature_data
plt.plot(jma_temperature_data)
plt.show()
