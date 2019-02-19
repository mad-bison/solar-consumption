# importing pandas module
import pandas as pd
import numpy as np
import csv
#import datetime

# making data frame from csv file
data = pd.read_csv("consumption.csv", delimiter = ',',header = None, skiprows = 700)

data.drop(data.columns[0], axis=1, inplace = True)
data.drop(data.columns[49:54], axis=1, inplace = True)

data = pd.DataFrame(data.values, columns = ['DATE', '00:00 - 00:30', '00:30 - 01:00', '01:00 - 01:30', '01:30 - 02:00', '02:00 - 02:30', '02:30 - 03:00', '03:00 - 03:30', '03:30 - 04:00', '04:00 - 04:30', '04:30 - 05:00', '05:00 - 05:30', '05:30 - 06:00', '06:00 - 06:30', '06:30 - 07:00', '07:00 - 07:30', '07:30 - 08:00', '08:00 - 08:30', '08:30 - 09:00', '09:00 - 09:30', '09:30 - 10:00', '10:00 - 10:30', '10:30 - 11:00', '11:00 - 11:30', '11:30 - 12:00', '12:00 - 12:30', '12:30 - 13:00', '13:00 - 13:30', '13:30 - 14:00', '14:00 - 14:30', '14:30 - 15:00', '15:00 - 15:30', '15:30 - 16:00', '16:00 - 16:30', '16:30 - 17:00', '17:00 - 17:30', '17:30 - 18:00', '18:00 - 18:30', '18:30 - 19:00', '19:00 - 19:30', '19:30 - 20:00', '20:00 - 20:30', '20:30 - 21:00', '21:00 - 21:30', '21:30 - 22:00', '22:00 - 22:30', '22:30 - 23:00', '23:00 - 23:30', '23:30 - 00:00' ])
#print(Frame.head(5))
data.insert(0, 'NMI', '62038495142')
data.insert(1, 'METER SERIAL NUMBER', '123456')
data.insert(2, 'CON/GEN', 'Consumption')
data.insert(4, 'ESTIMATED?', 'No')
#print(Frame.head(5))

data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d')
data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d').dt.strftime('%d' + '/' + '%m' + '/' + '%Y')
#Frame['DATE'].dt.strftime('%m%d%Y')

# Print the full import
#print(data)
#print(len(data.index))
#total_rows = len(data.index)

#print('Total Rows = ')
#print(rows)
rows = len(data.index)-12
data = data.drop(data.index[0:rows])
data = data.reset_index(drop = True)

last = len(data.index)-1
print(last)
data = data.drop(data.index[last])


data.to_csv("newconsumption.csv", index = False)


print(data)

# Print just the first "x" lines
#print(data.head())

# Print just the last "x" lines
#print(data.tail(10))
