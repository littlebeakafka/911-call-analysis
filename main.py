# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv('/Users/jixinlin/Desktop/911.csv')
# Check basic information about the dataset
df.info()
print(df.head())
# Top 5 most common zip codes for 911 calls
print(df['zip'].value_counts().head(5))
# Top 5 most common townships (twp)
print(df['twp'].value_counts().head(5))
# Count the number of unique titles
print(len(df['title'].unique()))
# Create a new column 'Reason' based on the 'title' column
df['Reason']=df['title'].apply(lambda title:title.split(':')[0])
# Display the most common reason for 911 calls
print(df['Reason'].value_counts().head(1))
# Visualize the distribution of reasons for 911 calls
sns.countplot(x='Reason',data=df)
plt.show()
# Convert the 'timeStamp' column to datetime format
df['timeStamp']=pd.to_datetime(df['timeStamp'])
time=df['timeStamp'].iloc[0]
print(time)
# Extract time attributes (Hour, Month, Day of Week) from 'timeStamp'
df['Hour']=df['timeStamp'].apply(lambda time:time.hour)
df['Month']=df['timeStamp'].apply(lambda time:time.month)
df['Day of Week']=df['timeStamp'].apply(lambda time:time.dayofweek)
# Preview the updated DataFrame
print(df.head())
# Map numeric days of the week to string names
dmap={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
# Preview the updated DataFrame
print(df.head())
# Visualize the number of 911 calls by day of the week and reason
sns.countplot(x='Day of Week',data=df,hue='Reason')
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
# Visualize the number of 911 calls by month and reason
sns.countplot(x='Month',data=df,hue='Reason')
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
# Group data by month and count the number of calls
byMonth = df.groupby('Month').count().reset_index()
# Visualize a linear regression plot of calls by month
sns.lmplot(x='Month', y='twp', data=byMonth)
plt.show()
# Add a new column 'Date' for grouping by date
t=df['timeStamp'].iloc[0]
df['Date']=df['timeStamp'].apply(lambda t:t.date())

#group by this date column with the count() aggregate and create a plot of counts of 911 calls.
df.groupby('Date').count()['lat'].plot()
plt.tight_layout()
# Visualize the number of calls by date for different reasons
df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.show()
# Create a matrix showing the number of calls by day of the week and hour
dayHour= df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
# Visualize the matrix as a heatmap
sns.heatmap(dayHour,cmap='YlGn')
plt.show()
#using the new DataFrame, show the month as the column
dayHour= df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
# Visualize the new matrix as a heatmap
sns.heatmap(dayHour,cmap='YlGn')
plt.show()
#conclusion:The above analysis of 911 call data provides the following insights:

#Most Common Reasons for 911 Calls:

#The most common reasons for 911 calls are categorized as "Traffic," "EMS," and "Fire."
#"Traffic" appears to be the top reason based on the data.
#Timing of 911 Calls:

#The majority of 911 calls occur during daytime hours, particularly around peak commuting times.
#Traffic-related incidents are more frequent during the weekdays.
#Patterns by Day and Month:

#There is a noticeable trend in the frequency of calls based on the day of the week. Weekdays generally have more calls compared to weekends.
#Monthly trends indicate fluctuations in call volume, which may be influenced by weather or seasonal factors.
#Heatmap Observations:

#The heatmap of calls by hour and day of the week shows a high concentration of calls during daytime hours on weekdays.
#Similarly, the heatmap of calls by day of the week and month highlights specific periods with higher call activity.
