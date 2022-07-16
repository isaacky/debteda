import pandas as pd
import numpy as np
from datetime import datetime, timedelta

#d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
df = pd.read_csv('data/managers18052022.csv', parse_dates=['MAX_DUE_DATE'], index_col='MAX_DUE_DATE', usecols=['MAX_DUE_DATE','ACCOUNT_NUMBER','REGION','COUNTY','LAST_MONTHLY_BILL','OVERDUE_AMOUNT','TOTAL_BALANCE','COD_TARIF','DEPOSIT','Y_COORDS','X_COORDS'])
df['DEPOSIT'] = df['DEPOSIT'].fillna(0)
today = datetime.today()
thirty_days_ago = today - timedelta(days=38)
filt = (df.index >= thirty_days_ago)
df['AGE'] = today - df.index
df['AGE'] = df['AGE'] / np.timedelta64(1,'D')
df['DAY'] = df.index.day_name()
print(df[df['AGE'] >= 38])
df3 = df.groupby('COUNTY').aggregate({'LAST_MONTHLY_BILL':'sum','OVERDUE_AMOUNT':'sum'})
print(df3)
df3.to_csv('data/result.csv')
# remove unwanted columns
# df_drop_col = df.drop(['OFFICE_NAME', 'READING_UNIT','BUSINESS_UNIT','LEGACY_NUMBER','CONTRACT_DATE','TERMINATION_DATE','CUSTOMER_CATEGORY','ADMD'], axis=1)
# # change nan to 0
# df_drop_col['DEPOSIT'] = df_drop_col['DEPOSIT'].fillna(0)
# #set date index
# df_drop_col.set_index('MAX_DUE_DATE', inplace=True)


#df_drop_col['AGE'] = datetime.strptime(df_drop_col['MAX_DUE_DATE'], "%d/%m/%Y").date()

#df_drop_col['MAX_DUE_DATE'] = pd.to_datetime(df_drop_col['MAX_DUE_DATE'], format="%d%m%Y")
# def age(maxduedt):
# 	maxduedt = datetime.strptime(maxduedt, "%d-%m-%Y").date()
# 	today = date.today()
# 	return today.year - maxduedt.year - ((today.month,
# 	                                  today.day) < (maxduedt.month,
# 	                                                maxduedt.day))
#
# df_drop_col['AGE'] = df_drop_col['MAX_DUE_DATE'].apply(age)
# print(df_drop_col['AGE'])




# Identify given date as date month and year
#gvn_DOB = datetime.strptime(born, "%d/%m/%Y").date()
#change_format = date_sr.dt.strftime('%d,%m,%Y')
# date_sr = pd.to_datetime(pd.Series("2012-09-02"))
# change_format = date_sr.dt.strftime('%d-%m-%Y')
# gvn_DOB = datetime(1977, 6, 6)
#
# current_date = datetime.today()
# age_in_days = current_date - gvn_DOB
# # Get today's date
# tdelta = datetime.timedelta(days=7)
# today = datetime.date.today()
