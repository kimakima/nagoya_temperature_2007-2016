import csv
import datetime
import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import MonthLocator


st_filename = "jma_temperature_data_nagoya_2007-2016.csv"

jma_temperature_data = {}
jma_temperature_data_merge = {}
y_temperature = {}
a = []
x_axis_data = []
x_date = []
x_24sekki = []
y_24sekki = []
max_temperature = []
avg_temperature = []
min_temperature = []
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
	x_date.append(datetime.datetime(2016,int(x_axis[0:2]),int(x_axis[2:4])))
	
	for key, value in sorted(jma_temperature_data.items()):
		pat = re.compile(r'.*{0}$'.format(x_axis))
		matchObj = pat.match(key)
		if matchObj:
			avg_temperature.append(value[0])
			max_temperature.append(value[1])
			min_temperature.append(value[2])

	avg = sum(map(float, avg_temperature))/len(map(float, avg_temperature))
	max = sum(map(float, max_temperature))/len(map(float, max_temperature))
	min = sum(map(float, min_temperature))/len(map(float, min_temperature))
	y_temperature[x_axis] = [avg, max, min]
	avg_temperature[:] = []
	max_temperature[:] = []
	min_temperature[:] = []
			
for key, value in sorted(y_temperature.items()):
	a.append(value)

print x_date
print a
fig = plt.figure()
ax = fig.add_subplot(111)
dateFmt = matplotlib.dates.DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(dateFmt)

plt.title("Nagoya 2006-2015")
plt.xlabel("date [mm-dd]")
plt.ylabel("temperature [degc]")

ax.plot(x_date, a,'o-')

months = MonthLocator(range(1,13), bymonthday=1,interval=1)
ax.xaxis.set_major_locator(months)
ax.grid(which='major', color='lightgrey', linestyle=':')

ax.axvline(datetime.datetime(2016,2,4), color='g', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2016,3,21), color='g', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2016,5,5), color='r', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2016,6,21), color='r', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2016,8,7), color='y', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2016,9,21), color='y', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2016,11,7), color='b', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2016,12,21), color='b', linestyle='-', linewidth=0.5)

loc, label = plt.xticks()
plt.setp(label, rotation=90)
plt.show()
