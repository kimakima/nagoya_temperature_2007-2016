import csv
import re
import matplotlib.pyplot as plt

st_filename = "jma_temperature_data_nagoya_2007-2016.csv"

jma_temperature_data = {}
jma_temperature_data_merge = {}
a = []
x_axis_data = []
max_temperature = []
g = []

with open(st_filename, 'r') as fp_data:
	reader = csv.reader(fp_data)

	for row in reader:
		if row:
			yr = row[0].split("/")[0]
			mo = row[0].split("/")[1]
			dy = row[0].split("/")[2]
			deka = yr.zfill(4) + mo.zfill(2) + dy.zfill(2)
			jma_temperature_data[deka] = [row[2], row[5], row[8]]
			deka_merge = mo.zfill(2) + dy.zfill(2)
			x_axis_data.append(deka_merge);

x_axis_data_uniq = list(set(x_axis_data))

for x_axis in sorted(x_axis_data_uniq):
	print "-----"
	for key, value in sorted(jma_temperature_data.items()):
		pat = re.compile(r'.*{0}$'.format(x_axis))
		matchObj = pat.match(key)
		if matchObj:
			max_temperature.append(value[0])
#			print matchObj.group()
	print max_temperature
	print sum(map(float, max_temperature))/len(map(float, max_temperature))
	g.append(sum(map(float, max_temperature))/len(map(float, max_temperature)))
	max_temperature[:] = []
			

#for key, value in sorted(jma_temperature_data.items()):
#	print key, value
#	a.append(value)
print g
plt.plot(g)
plt.show()
