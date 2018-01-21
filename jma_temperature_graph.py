# -*- coding: utf-8 -*-

import csv
import datetime
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import MonthLocator

#font = {"family":"SourceHanSans"}
#matplotlib.rc('font', **font)
#font_path = '/Users/kima/Library/Fonts/TanukiMagic.ttf'
font_path = '/Users/kima/Library/Fonts/SourceHanSans-Regular.otf'
font_prop = matplotlib.font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams["font.size"] = 16

#plt.rcParams["font.family"] = 'SourceHanSans'
#plt.rcParams["font.family"] = 'AppleGothic'
#plt.rcParams["font.family"] = 'TanukiMagic'

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

max_temperature_upper_err = ary2d_avg_temperature[:, 4] - ary2d_avg_temperature[:, 8]
max_temperature_lower_err = ary2d_avg_temperature[:, 8] - ary2d_avg_temperature[:, 6]

min_temperature_upper_err = ary2d_avg_temperature[:, 5] - ary2d_avg_temperature[:, 9]
min_temperature_lower_err = ary2d_avg_temperature[:, 9] - ary2d_avg_temperature[:, 7]

for (month,day) in zip(ary2d_avg_temperature[:, 1],ary2d_avg_temperature[:, 2]):
	x_date.append(datetime.datetime(2018, month, day))
x_date.pop()
x_date.append(datetime.datetime(2019, 1, 1))

print x_date, len(x_date)
print ary2d_avg_temperature[:, 3], len(ary2d_avg_temperature[:, 3])

for (a, b) in zip(x_date, ary2d_avg_temperature[:, 3]):
	print a,b

fig = plt.figure()
ax = fig.add_subplot(111)
dateFmt = matplotlib.dates.DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(dateFmt)
#plt.tight_layout()
plt.title("Nagoya High&Low Temperature in 2008-2017")
plt.xlabel("date [mm-dd]")
plt.ylabel("temperature [degC]")

plt.ylim(-5, 45)
plt.xlim(datetime.datetime(2017, 12, 25), datetime.datetime(2019, 1, 5))
#ax.plot(x_date, ary2d_avg_temperature[:,3],'o-', color='g')
#ax.plot(x_date, ary2d_avg_temperature[:,4],'o-')
#ax.plot(x_date, ary2d_avg_temperature[:,5],'o-')
#ax.plot(x_date, ary2d_avg_temperature[:,6],'o-')
#ax.plot(x_date, ary2d_avg_temperature[:,7],'o-')
ax.plot(x_date, ary2d_avg_temperature[:, 8], 'o-', color='r')
ax.plot(x_date, ary2d_avg_temperature[:, 9], 'o-', color='b')
#ax.errorbar(x_date,ary2d_avg_temperature[:,8], yerr=[max_temperature_lower_err,max_temperature_lower_err], fmt='o-')
#ax.errorbar(x_date,ary2d_avg_temperature[:,9], yerr=[min_temperature_lower_err,min_temperature_lower_err], fmt='o-')

ax.fill_between(x_date, ary2d_avg_temperature[:, 4], ary2d_avg_temperature[:, 6], facecolor='r', alpha=0.4)
ax.fill_between(x_date, ary2d_avg_temperature[:, 5], ary2d_avg_temperature[:, 7], facecolor='b', alpha=0.4)

months = MonthLocator(range(1,13), bymonthday=1,interval=1)
ax.xaxis.set_major_locator(months)
ax.grid(which='major', color='grey', linestyle='-')
ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1))

ax.axvspan(datetime.datetime(2018, 1, 1), datetime.datetime(2018, 3,21), color='b', alpha=0.125)
ax.axvspan(datetime.datetime(2018, 3,21), datetime.datetime(2018, 6,21), color='g', alpha=0.125)
ax.axvspan(datetime.datetime(2018, 6,21), datetime.datetime(2018, 9,23), color='r', alpha=0.125)
ax.axvspan(datetime.datetime(2018, 9,23), datetime.datetime(2018,12,21), color='y', alpha=0.125)
ax.axvspan(datetime.datetime(2018,12,21), datetime.datetime(2019, 1, 1), color='b', alpha=0.125)

li_24seasons = []
li_24seasons.append([2018, 1, 5, u'小寒', 'b', 14])
li_24seasons.append([2018, 1,20, u'大寒', 'b', 16])
li_24seasons.append([2018, 2, 4, u'立春', 'b', 18])
li_24seasons.append([2018, 2,18, u'雨水', 'b', 20])
li_24seasons.append([2018, 3, 5, u'啓蟄', 'b', 22])
li_24seasons.append([2018, 3,21, u'春分', 'g', 24])
li_24seasons.append([2018, 4, 5, u'清明', 'g', 27])
li_24seasons.append([2018, 4,20, u'穀雨', 'g', 29])
li_24seasons.append([2018, 5, 5, u'立夏', 'g', 31])
li_24seasons.append([2018, 5,21, u'小満', 'g', 33])
li_24seasons.append([2018, 6, 5, u'芒種', 'g', 34])
li_24seasons.append([2018, 6,21, u'夏至', 'r', 36])
li_24seasons.append([2018, 7, 7, u'小暑', 'r', 38])
li_24seasons.append([2018, 7,22, u'大暑', 'r', 39])
li_24seasons.append([2018, 8, 7, u'立秋', 'r', 39])
li_24seasons.append([2018, 8,23, u'処暑', 'r', 38])
li_24seasons.append([2018, 9, 7, u'白露', 'r', 36])
li_24seasons.append([2018, 9,23, u'秋分', 'y', 33])
li_24seasons.append([2018,10, 8, u'寒露', 'y', 31])
li_24seasons.append([2018,10,23, u'霜降', 'y', 28])
li_24seasons.append([2018,11, 7, u'立冬', 'y', 25])
li_24seasons.append([2018,11,22, u'小雪', 'y', 22])
li_24seasons.append([2018,12, 7, u'大雪', 'y', 20])
li_24seasons.append([2018,12,21, u'冬至', 'b', 18])

for (x_date_data,li_24season) in zip(x_date,li_24seasons):
	ax.text(datetime.datetime(li_24season[0],li_24season[1], li_24season[2]), li_24season[5], li_24season[3], horizontalalignment='center', rotation=90)
	ax.axvline(datetime.datetime(li_24season[0],li_24season[1],li_24season[2]), color=li_24season[4], linestyle=':', linewidth=0.5)

loc, label = plt.xticks()
plt.setp(label, rotation=90)
plt.show()
