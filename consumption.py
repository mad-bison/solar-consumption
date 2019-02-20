# Import Modules
import pandas as pd
import csv

# Read data from consumption.csv (from Powercor myEnergyDashboard)and skip first 700 rows
data = pd.read_csv("consumption.csv", delimiter = ',',header = None, skiprows = 700)

# Drop first column
data.drop(data.columns[0], axis=1, inplace = True)
# Drop last 5 columns
data.drop(data.columns[49:54], axis=1, inplace = True)

# Create Header with current Data from CSV
data = pd.DataFrame(data.values, columns = ['DATE', '00:00 - 00:30', '00:30 - 01:00', '01:00 - 01:30', '01:30 - 02:00', '02:00 - 02:30', '02:30 - 03:00', '03:00 - 03:30', '03:30 - 04:00', '04:00 - 04:30', '04:30 - 05:00', '05:00 - 05:30', '05:30 - 06:00', '06:00 - 06:30', '06:30 - 07:00', '07:00 - 07:30', '07:30 - 08:00', '08:00 - 08:30', '08:30 - 09:00', '09:00 - 09:30', '09:30 - 10:00', '10:00 - 10:30', '10:30 - 11:00', '11:00 - 11:30', '11:30 - 12:00', '12:00 - 12:30', '12:30 - 13:00', '13:00 - 13:30', '13:30 - 14:00', '14:00 - 14:30', '14:30 - 15:00', '15:00 - 15:30', '15:30 - 16:00', '16:00 - 16:30', '16:30 - 17:00', '17:00 - 17:30', '17:30 - 18:00', '18:00 - 18:30', '18:30 - 19:00', '19:00 - 19:30', '19:30 - 20:00', '20:00 - 20:30', '20:30 - 21:00', '21:00 - 21:30', '21:30 - 22:00', '22:00 - 22:30', '22:30 - 23:00', '23:00 - 23:30', '23:30 - 00:00' ])

# Insert your NMI, Serial, Consumption and Estimated Columns
data.insert(0, 'NMI', '62038495142')
data.insert(1, 'METER SERIAL NUMBER', '123456')
data.insert(2, 'CON/GEN', 'Consumption')
data.insert(4, 'ESTIMATED?', 'No')

# Reformat date from %Y%m%d (20190106) to %d/&m/%Y (06/01/2019)
data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d').dt.strftime('%d' + '/' + '%m' + '/' + '%Y')

# Get total number of rows minus 12 records to import
rows = len(data.index)-12
# Drop all but final rows
data = data.drop(data.index[0:rows])
# Reset Index on dataFrame and drop old index
data = data.reset_index(drop = True)

# Drop final row of CSV which is usually junk text
data = data.drop(data.index[len(data.index)-1])

# Save data to a new CSV ready for import into PVOutput.org
data.to_csv("newconsumption.csv", index = False, float_format = '%.3f')

# Print data as a visual check.
print(data)

# Print just the first 5 lines
#print(data.head())

# Print just the last 5 lines
#print(data.tail())
