import numpy as np
import pandas as pd

df = pd.read_csv('startup_funding.csv')
df.drop(columns=['Remarks'],inplace=True)
df.set_index('Sr No',inplace=True)
df.rename(columns={
    'Date dd/mm/yyyy': 'date',
    'Startup Name' : 'startup',
    'Industry Vertical' : 'vertical',
    'SubVertical' : 'subvertical',
    'City  Location' : 'city',
    'Investors Name' : 'investors',
    'InvestmentnType' : 'round',
    'Amount in USD' : 'amount'
},inplace=True)
df.dropna(inplace=True)
df['amount'] = df['amount'].str.replace(',','')
df['amount'] = df['amount'].str.replace('.','')
df['amount'] = df['amount'].str.replace('+','')
df['amount'] = df['amount'].str.replace('undisclosed','0')
df['amount'] = df['amount'].str.replace('unknown','0')
df['amount'] = df['amount'].str.replace('Undisclosed','0')
df['amount'] = df['amount'].astype('float')
df['date'] = df['date'].str.replace('05/072018','05/07/2018')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
#print(df.info())
startup_list = df['startup'].unique().tolist()
investor_list = list(set(df['investors'].str.split(',').sum()))

def investor_detail(investor):
    df2 = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
    df1 = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    df3 = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
    df4 = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
    df5 = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
    df6 = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    print(df5)
    return(df1,df2,df3,df4,df5,df6)



    


#investor_detail(' IDG Ventures')