import csv
import matplotlib.pyplot as plt


st_filename = "jma_temperature_data_nagoya_2007-2016.csv"

jma_temperature_data = {}
a = []

with open(st_filename, 'r') as fp_data:
	reader = csv.reader(fp_data)

	for row in reader:
		if row:
#			jma_temperature_data.append([row[0], row[2], row[5], row[8]])
#			jma_temperature_data.append([row[2], row[5], row[8]])
			yr   = row[0].split("/")[0]
			mo   = row[0].split("/")[1]
			da = row[0].split("/")[2]
#			print '{0:04d}'.format(yr) + '0:02d'.format(mo) + '0:02d'.format(deka)
			deka = yr.zfill(4) + mo.zfill(2) + da.zfill(2)
			jma_temperature_data[deka] = [row[2], row[5], row[8]]

for key, value in sorted(jma_temperature_data.items()):
	print key, value, "\n"
	a.append(value)
#print jma_temperature_data.values()
print a
plt.plot(a)
plt.show()
