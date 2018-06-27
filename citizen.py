import pandas as pd
import csv

ss_csvfile ="/Users/stephensim/Documents/citizen/NYPD_Complaint_Data_Historic.csv"

# Upload Dataset
print("Loading data...")
df = pd.read_csv(ss_csvfile)
print("Loading data complete!")
print("Dataset has %d rows." % ( df["CMPLNT_NUM"].size)) #%d acts as a placeholder#

# Removes columns that are not used
def cleanData(dataset):
	columns_drop = ['CMPLNT_TO_DT','CMPLNT_TO_TM','PD_CD','PD_DESC','PARKS_NM','HADEVELOPT','X_COORD_CD','Y_COORD_CD','Latitude','Longitude','Lat_Lon']
	dataset = dataset.drop(columns_drop, 1)

	return dataset

# Adds Year, Month, Day, Weekday, Hour and Season to dataset. ALso removes years less than 2005
def addData(dataset):
	dataset['CMPLNT_FR_DT'] = pd.to_datetime(df['CMPLNT_FR_DT'],format = '%m/%d/%Y',errors='coerce')
	dataset['YEAR'] = dataset['CMPLNT_FR_DT'].dt.year
	dataset['MONTH'] = dataset['CMPLNT_FR_DT'].dt.month
	dataset['WEEKDAY'] = dataset['CMPLNT_FR_DT'].dt.weekday
	dataset['HOUR'] = pd.to_datetime(dataset['CMPLNT_FR_TM'],format = '%H:%M:%S',errors='coerce').dt.hour
	dataset['SEASON'] = (dataset['MONTH']%12 +3)//3
	dataset = dataset[dataset['YEAR'] > 2005]

	return dataset

#Apply functions
dataset = addData(cleanData(df))

#save a new csv file
print("Exporting data...")
dataset.to_csv('cleanData.csv', encoding='utf-8')
print("Export complete!")