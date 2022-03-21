import pandas as pd

data = pd.read_csv('life-expectancy.csv')

year = int(input('Enter the year of interest: '))

#Gives each country in the dataset with their respective minimun life expectancy values
df1 = data.groupby('Entity').Lifeexpectancy.min()

#Gives each country in the dataset with their respective maximum life expectancy values
df2 = data.groupby('Entity').Lifeexpectancy.max()

#Gives you the minimun life expectancy for the selected year
filtered = data[data.Year==year].Lifeexpectancy.min()




