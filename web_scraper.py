from bs4 import BeautifulSoup
import requests
import pandas as pd


url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
page=requests.get(url)
soup=BeautifulSoup(page.text,features='html.parser')
# print(soup)
soup.find('table',class_="wikitable sortable ")
table=soup.find_all("table")[1]
# print (table)
titles=(table.find_all('th'))
table_titles=[title.text.strip() for title in titles ]
# print(table_titles)
df=pd.DataFrame(columns= table_titles)
# print(df)
column_data=table.find_all("tr")
for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data ]
    # print(individual_row_data)

    length=len(df)
    df.loc[length]=individual_row_data

# print(df)
df.to_csv(r'D:\Companies.csv', index=False)






