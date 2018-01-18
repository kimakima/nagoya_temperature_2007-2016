# -*- coding: utf-8 -*-

import csv
import datetime
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import MonthLocator

#np.set_printoptions(precision=1)
st_filename = "jma_temperature_data_nagoya_2008-2017_filtered.csv"

jma_temperature_data = {}
jma_temperature_list = []
jma_temperature_data_merge = {}
y_temperature = {}
max_temperature_err = []
min_temperature_err = []
a = []
x_axis_data = []
x_date = []
x_24sekki = []
y_24sekki = []
avg_temperature = []
max_temperature = []
max_temperature_upper_err = []
max_temperature_lower_err = []
min_temperature = []
min_temperature_upper_err = []
min_temperature_lower_err = []
g = []
avg = []

with open(st_filename, 'r') as fp_data:
	reader = csv.reader(fp_data)

	for row in reader:
		if row:
			yr = row[0].split("/")[0]
			mo = row[0].split("/")[1]
			dy = row[0].split("/")[2]
			deka = yr.zfill(4) + mo.zfill(2) + dy.zfill(2)
			jma_temperature_list.append([float(yr),float(mo),float(dy),float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])])
			deka_merge = mo.zfill(2) + dy.zfill(2)
			x_axis_data.append(deka_merge)

x = []
y = []
curr_yr = 2008
for data in jma_temperature_list:
	if data[0] == curr_yr:
		x.append(data)
	else:
		y.append(x)
		x = []
		x.append(data)
		curr_yr = curr_yr + 1
y.append(x)

ary3d_temperature = np.array(y, dtype=np.float32)
ary2d_avg_temperature = np.mean(ary3d_temperature, axis=0)
ary2d_avg_temperature = np.concatenate([ary2d_avg_temperature, np.array([ary2d_avg_temperature[0]])], axis=0)
print ary2d_avg_temperature
print len(ary2d_avg_temperature)
#print np.array([ary2d_avg_temperature[0]])

x_axis_data_uniq = list(set(x_axis_data))

max_temperature_upper_err = ary2d_avg_temperature[:,4] - ary2d_avg_temperature[:,8]
max_temperature_lower_err = ary2d_avg_temperature[:,8] - ary2d_avg_temperature[:,6]

min_temperature_upper_err = ary2d_avg_temperature[:,5] - ary2d_avg_temperature[:,9]
min_temperature_lower_err = ary2d_avg_temperature[:,9] - ary2d_avg_temperature[:,7]

for (month,day) in zip(ary2d_avg_temperature[:,1],ary2d_avg_temperature[:,2]):
	x_date.append(datetime.datetime(2018, month, day))
x_date.pop()
x_date.append(datetime.datetime(2019,1,1))

print x_date, len(x_date)
print ary2d_avg_temperature[:,3], len(ary2d_avg_temperature[:,3])

for (a,b) in zip(x_date, ary2d_avg_temperature[:,3]):
	print a,b

fig = plt.figure()
ax = fig.add_subplot(111)
dateFmt = matplotlib.dates.DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(dateFmt)

plt.title("Nagoya Temperature 2008-2017")
plt.xlabel("date [mm-dd]")
plt.ylabel("temperature [degc]")

plt.ylim(-5,45)
plt.xlim(datetime.datetime(2017,12,25),datetime.datetime(2019,1,5))
ax.plot(x_date, ary2d_avg_temperature[:,3],'o-', color='g')
#ax.plot(x_date, ary2d_avg_temperature[:,4],'o-')
#ax.plot(x_date, ary2d_avg_temperature[:,5],'o-')
#ax.plot(x_date, ary2d_avg_temperature[:,6],'o-')
#ax.plot(x_date, ary2d_avg_temperature[:,7],'o-')
ax.plot(x_date, ary2d_avg_temperature[:,8],'o-', color='r')
ax.plot(x_date, ary2d_avg_temperature[:,9],'o-', color='b')
#ax.errorbar(x_date,ary2d_avg_temperature[:,8], yerr=[max_temperature_lower_err,max_temperature_lower_err], fmt='o-')
#ax.errorbar(x_date,ary2d_avg_temperature[:,9], yerr=[min_temperature_lower_err,min_temperature_lower_err], fmt='o-')

ax.fill_between(x_date, ary2d_avg_temperature[:,4],ary2d_avg_temperature[:,6],facecolor='r', alpha=0.4)
ax.fill_between(x_date, ary2d_avg_temperature[:,5],ary2d_avg_temperature[:,7],facecolor='b', alpha=0.4)

months = MonthLocator(range(1,13), bymonthday=1,interval=1)
ax.xaxis.set_major_locator(months)
ax.grid(which='major', color='grey', linestyle='-')

ax.axvline(datetime.datetime(2018, 3,21), color='g', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 4, 5), color='g', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 4,20), color='g', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 5, 5), color='g', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 5,21), color='g', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 6, 6), color='g', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 6,21), color='r', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 7, 7), color='r', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 7,23), color='r', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 8, 7), color='r', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 8,23), color='r', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 9, 8), color='r', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 9,23), color='y', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018,10, 8), color='y', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018,10,23), color='y', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018,11, 7), color='y', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018,11,22), color='y', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018,12, 7), color='y', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018,12,21), color='b', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 1, 5), color='b', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 1,20), color='b', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 2, 4), color='b', linestyle='-', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 2,19), color='b', linestyle=':', linewidth=0.5)
ax.axvline(datetime.datetime(2018, 3, 6), color='b', linestyle=':', linewidth=0.5)

ax.axvspan(datetime.datetime(2018, 1, 1),datetime.datetime(2018, 3,21), color='b', alpha=0.125)
ax.axvspan(datetime.datetime(2018, 3,21),datetime.datetime(2018, 6,21), color='g', alpha=0.125)
ax.axvspan(datetime.datetime(2018, 6,21),datetime.datetime(2018, 9,23), color='r', alpha=0.125)
ax.axvspan(datetime.datetime(2018, 9,23),datetime.datetime(2018,12,21), color='y', alpha=0.125)
ax.axvspan(datetime.datetime(2018,12,21),datetime.datetime(2019, 1, 1), color='b', alpha=0.125)

ax.text(datetime.datetime(2018, 3,21), 42, u'春分',horizontalalignment='center')
ax.text(datetime.datetime(2018, 4, 5), 40, u'清明',horizontalalignment='center')
ax.text(datetime.datetime(2018, 4,20), 38, u'穀雨',horizontalalignment='center')
ax.text(datetime.datetime(2018, 5, 5), 42, u'立夏',horizontalalignment='center')
ax.text(datetime.datetime(2018, 5,21), 40, u'小満',horizontalalignment='center')
ax.text(datetime.datetime(2018, 6, 5), 38, u'芒種',horizontalalignment='center')
ax.text(datetime.datetime(2018, 6,21), 42, u'夏至',horizontalalignment='center')
ax.text(datetime.datetime(2018, 7, 7), 40, u'小暑',horizontalalignment='center')
ax.text(datetime.datetime(2018, 7,22), 38, u'大暑',horizontalalignment='center')
ax.text(datetime.datetime(2018, 8, 7), 42, u'立秋',horizontalalignment='center')
ax.text(datetime.datetime(2018, 8,23), 40, u'処暑',horizontalalignment='center')
ax.text(datetime.datetime(2018, 9, 7), 38, u'白露',horizontalalignment='center')
ax.text(datetime.datetime(2018, 9,23), 42, u'秋分',horizontalalignment='center')
ax.text(datetime.datetime(2018,10, 8), 40, u'秋分',horizontalalignment='center')
ax.text(datetime.datetime(2018,10,23), 38, u'秋分',horizontalalignment='center')
ax.text(datetime.datetime(2018,11, 7), 42, u'立冬',horizontalalignment='center')
ax.text(datetime.datetime(2018,11,22), 40, u'小雪',horizontalalignment='center')
ax.text(datetime.datetime(2018,12, 7), 38, u'大雪',horizontalalignment='center')
ax.text(datetime.datetime(2018,12,21), 42, u'冬至',horizontalalignment='center')
ax.text(datetime.datetime(2018, 1, 5), 40, u'小寒',horizontalalignment='center')
ax.text(datetime.datetime(2018, 1,20), 38, u'大寒',horizontalalignment='center')
ax.text(datetime.datetime(2018, 2, 4), 42, u'立春',horizontalalignment='center')
ax.text(datetime.datetime(2018, 2,18), 40, u'雨水',horizontalalignment='center')
ax.text(datetime.datetime(2018, 3, 5), 38, u'啓蟄',horizontalalignment='center')

loc, label = plt.xticks()
plt.setp(label, rotation=90)
plt.show()
