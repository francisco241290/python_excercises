import pandas as pd

data = pd.read_csv('life-expectancy.csv')

year = int(input('Enter the year of interest: '))

#Gives you the overall max life expectancy
min_life = data['Lifeexpectancy'].min()
#Gives you the overall min life expectancy
max_life = data['Lifeexpectancy'].max()

#Gives you the country with the overall max an min life expectancy
max_country = data[data.Lifeexpectancy==max_life].Entity
min_country = data[data.Lifeexpectancy==min_life].Entity

#Gives you the year for the overall max and min life expectancy 
max_year = data[data.Lifeexpectancy==max_life].Year
min_year = data[data.Lifeexpectancy==min_life].Year

#Gives you the minimun life expectancy for the selected year
filteredMin = data[data.Year==year].Lifeexpectancy.min()
#Gives you the maximum life expectancy for the selected year
filteredMax = data[data.Year==year].Lifeexpectancy.max()
#Gives you the average life expectnacy for the selected year
filteredMean = data[data.Year==year].Lifeexpectancy.mean()

#Gives you the country for the selected minimun life expectancy / maximum
entity_min = data[data.Lifeexpectancy==filteredMin].Entity
entity_max = data[data.Lifeexpectancy==filteredMax].Entity



print(f'\nThe overall max life expectancy is: {max_life} from {max_country.to_string(index=False)} in {max_year.to_string(index=False)}')
print(f'The overall min life expectancy is: {min_life} from {min_country.to_string(index=False)} in {min_year.to_string(index=False)}')
print('')
print(f'For the year {year}:')
print(f'The average life expectancy across all countries was {filteredMean:.2f}')
print(f'The max life expectancy was in {entity_max.to_string(index=False)} with {filteredMax}')
print(f'The min life expectancy was in {entity_min.to_string(index=False)} with {filteredMin}')




