import pandas as pd

#load dataset
file = pd.read_csv('adult.csv')

# 1. How many people of each race are represented in this dataset

count_race = file['race'].value_counts()

# 2. What is the average age of men?
average_age_men = file[file['sex'] == 'Male']['age'].mean()

# 3. What is the percentage of people who have a Bachelor's degree?

bachelor_percentage = (file[file['education'] == 'Bachelors'].shape[0]/file.shape[0])*100

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

higher_education = file['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
higher_education_percentage = file[higher_education & (file['income'] == '>50K')].shape[0] / file[higher_education].shape[0]*100

# 5  What percentage of people without advanced education make more than 50K?

lower_education = ~higher_education
lower_education_percentage = file[lower_education & (file['income'] == '>50K')].shape[0] / file[lower_education].shape[0]*100

# 6. What is the minimum number of hours a person works per week?
min_works_hr = file['hours.per.week'].min()

# 7 What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_workers = file[file['hours.per.week'] == min_works_hr].shape[0]
min_works_percentage = file[min_workers & (file['income'] == '>50K')].shape[0] / min_workers*100

# 8 What country has the highest percentage of people that earn >50K and what is that percentage?

country_earning = (file[file['income'] == '>50K']['native.country'].value_counts() / file['native.country'].value_counts()) * 100
high_earning_country = country_earning.idxmax()
high_earning_percentage = country_earning.max()

# 9 Identify the most popular occupation for those who earn >50K in India.

top_occupation = file[(file['native.country'] == 'India') & (file['income']== '>50K')]['occupation'].value_counts().idxmax()

results = {
    'race_count': count_race,
    'average_age_men': average_age_men,
    'percentage_bachelors': bachelor_percentage,
    'higher_education_rich': higher_education_percentage,
    'lower_education_rich': lower_education_percentage,
    'min_work_hours': min_works_hr,
    'rich_percentage_min_workers': min_works_percentage,
    'highest_earning_country': high_earning_country,
    'highest_earning_country_percentage': high_earning_percentage,
    'top_IN_occupation': top_occupation
}