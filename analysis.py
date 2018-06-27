import pandas as pd
import csv

ss_cleanData_csvfile = "/Users/stephensim/Documents/citizen/cleanData.csv"

# Upload Dataset
print("Loading data...")
cleanData = pd.read_csv(ss_cleanData_csvfile)
print("Loading data complete!")

df_bymonth = cleanData.groupby(['OFNS_DESC', 'YEAR', 'MONTH', 'HOUR'], as_index=False)[['CMPLNT_NUM']].count()
df_byyear = cleanData.groupby(['LAW_CAT_CD', 'OFNS_DESC', 'YEAR'], as_index=False)[['CMPLNT_NUM']].count()
df_byhour = cleanData.groupby(['BORO_NM', 'LAW_CAT_CD', 'OFNS_DESC', 'HOUR'], as_index=False)[['CMPLNT_NUM']].count()
df_byseason = cleanData.groupby(['BORO_NM', 'LAW_CAT_CD', 'OFNS_DESC', 'SEASON', 'HOUR'], as_index=False)[['CMPLNT_NUM']].count()
df_byweekday = cleanData.groupby(['BORO_NM', 'LAW_CAT_CD', 'OFNS_DESC', 'SEASON', 'WEEKDAY', 'HOUR'], as_index=False)[['CMPLNT_NUM']].count()


cleanData['SEASON'] = cleanData['SEASON'].astype(str)
cleanData['SEASON'] = cleanData['SEASON'].replace('1.0','WINTER')
cleanData['SEASON'] = cleanData['SEASON'].replace('2.0','SPRING')
cleanData['SEASON'] = cleanData['SEASON'].replace('3.0','SUMMER')
cleanData['SEASON'] = cleanData['SEASON'].replace('4.0','FALL')


cleanData['WEEKDAY'] = cleanData['WEEKDAY'].astype(str)
cleanData['WEEKDAY'] = cleanData['WEEKDAY'].replace('0.0','MONDAY')
cleanData['WEEKDAY'] = cleanData['WEEKDAY'].replace('1.0','TUESDAY')
cleanData['WEEKDAY'] = cleanData['WEEKDAY'].replace('2.0','WEDNESDAY')
cleanData['WEEKDAY'] = cleanData['WEEKDAY'].replace('3.0','THURSDAY')
cleanData['WEEKDAY'] = cleanData['WEEKDAY'].replace('4.0','FRIDAY')
cleanData['WEEKDAY'] = cleanData['WEEKDAY'].replace('5.0','SATURDAY')
cleanData['WEEKDAY'] = cleanData['WEEKDAY'].replace('6.0','SUNDAY')


#save a new csv file
print("Exporting data...")
df_bymonth.to_csv('df_bymonth.csv', encoding='utf-8')
df_byyear.to_csv('df_byyear.csv', encoding='utf-8')
df_byhour.to_csv('df_byhour.csv', encoding='utf-8')
df_byseason.to_csv('df_byseason.csv', encoding='utf-8')
df_byweekday.to_csv('df_byweekday.csv', encoding='utf-8')
print("Export complete!")