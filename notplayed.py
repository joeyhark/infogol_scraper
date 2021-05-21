from selenium import webdriver
import pandas as pd

# Setup - change url for a different page (different date)
driver = webdriver.Chrome('convenience/chromedriver')
driver.get('https://www.infogol.net/en/matches/tomorrow')

blues = ['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']


# Obtain date
date = driver.find_element_by_xpath('/html/body/div/main/section/div/date-bar/div/div/div/div/span[1]')
date = date.text

# Empty dataframe
df = pd.DataFrame(columns=['Date', 'League', 'Home', 'Away', 'Bet', 'Value', 'Odds', 'Result', 'W/L', 'Profit'])

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

    # If league does not contain betting information, skip loop iteration
    if (len(elem)-1) % 8 or 'Value' not in elem:
        continue

    game_num = 1
    # Break element into games
    for k in range(1, len(elem), 8):
        # Check for last game
        if k == len(elem):
            break
        # Establish game in element
        game = elem[k:k+8]

        value = 0
        if len(elem) == 9:
            for j in range(1, 6):
                ball = driver.find_element_by_xpath('/html/body/div/main/section/tf-match-list/div/ul/li[{}]/ul/li/match-header/div/tf-match-analyst-verdict/div/div/div[1]/div/span[2]/tf-ball-rating/div/span[{}]'.format(i, j))
                ball = ball.screenshot_as_base64
                if ball in blues:
                    value += 1
        else:
            for j in range(1, 6):
                ball = driver.find_element_by_xpath('/html/body/div/main/section/tf-match-list/div/ul/li[{}]/ul/li[{}]/match-header/div/tf-match-analyst-verdict/div/div/div[1]/div/span[2]/tf-ball-rating/div/span[{}]'.format(i, game_num, j))
                ball = ball.screenshot_as_base64
                if ball in blues:
                    value += 1

        # Add elements to empty df
        df = df.append({'Date': date, 'League': elem[0], 'Home': game[0], 'Away': game[2], 'Bet': game[4], 'Value': value, 'Odds': game[6]}, ignore_index=True)
        game_num += 1

# Pickle with date as title
df.to_pickle('{}_notplayed.pickle'.format(date))
driver.close()


