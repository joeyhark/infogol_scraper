from selenium import webdriver
import pandas as pd
import re

# Setup - change url for a different page (different date)
driver = webdriver.Chrome('convenience/chromedriver')
driver.get('https://www.infogol.net/en/matches/2021-04-25')

# Obtain date
date = driver.find_element_by_xpath('/html/body/div/main/section/div/date-bar/div/div/div/div/span[1]')
date = date.text

# Empty dataframe
df = pd.DataFrame(columns=['League', 'Result'])

# Total number of leagues
for i in range(1, 27):
    try:
        # All games element
        elem = driver.find_element_by_xpath('/html/body/div/main/section/tf-match-list/div/ul/li[{}]'.format(i))
    except:
        # Break when all leagues present on day have been scraped
        break

    # Split all games element into list
    elem = elem.text.split('\n')
    league = elem[0]

    # Find results and add to empty df
    for j in elem:
        if '-' in j and re.search(r'\d', j):
            df = df.append({'League': league, 'Result': j}, ignore_index=True)
        # Check if game is postponed
        if j == 'v':
            df = df.append({'League': league, 'Result': 'P'}, ignore_index=True)

# Pickle with date as title
df.to_pickle('{}_results.pickle'.format(date))
driver.close()
