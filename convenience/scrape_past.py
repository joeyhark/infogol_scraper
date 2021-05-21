from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from convenience.results_convenience import bet_outcome, profit
import selenium.common.exceptions as exc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import sys

url = 'https://www.infogol.net/en/matches/2021-05-13'


def scrape_day(URL):
    # Setup - change url for a different page (different date)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='/Users/joeharkness/Documents/Python_projects/infogol_scaper/convenience/chromedriver',
                              options=chrome_options)
    driver.get(URL)

    # Blue value ball png codes
    # noinspection SpellCheckingInspection
    blues = [
        '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']

    # Obtain date
    date = datetime.datetime.strptime(URL.split('/')[-1], '%Y-%m-%d').date()
    print('\n[INFO] Finding games on {}...'.format(date))

    # Empty dataframe
    df = pd.DataFrame(columns=['Date', 'League', 'Home', 'Away', 'Bet', 'Value', 'Odds', 'Result', 'W/L', 'Profit'])

    # Iterate over number of all possible leagues
    for i in range(1, 27):
        # Reset game number
        game_num = 1

        # Increase game number by one until error is thrown
        while type(game_num) == int:
            try:
                # Click into game
                gamex = '/html/body/div/main/section/tf-match-list/div/ul/li[{}]/ul/li[{}]/match-header/div/table/tbody/tr/td[7]/span'.format(i, game_num)
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, gamex)))

                game = driver.find_element_by_xpath(gamex)
                driver.execute_script("arguments[0].click();", game)

                # Extract info
                league = driver.find_element_by_xpath(
                    '/html/body/div/main/tf-match-details/div/tf-competition-header/h3/a/span[2]')
                league = league.text

                score = driver.find_element_by_xpath(
                    '/html/body/div/main/tf-match-details/div/match-shirts/div/div[1]/div[2]')
                score = score.text

                home = driver.find_element_by_xpath(
                    '/html/body/div/main/tf-match-details/div/match-shirts/div/div[1]/div[1]/a')
                home = home.text

                away = driver.find_element_by_xpath(
                    '/html/body/div/main/tf-match-details/div/match-shirts/div/div[1]/div[3]/a')
                away = away.text

                predx = '/html/body/div/main/tf-match-details/div/tf-match-summary/div/tf-match-verdict/div/tf-match-analyst-verdict/div/div/div[1]/span'
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, predx)))

                pred = driver.find_element_by_xpath(predx)
                pred = pred.text

                odds = driver.find_element_by_xpath('/html/body/div/main/tf-match-details/div/tf-match-summary/div/tf'
                                                    '-match-verdict/div/tf-match-analyst-verdict/div/div/div['
                                                    '2]/tf-odds/div/span[2]')
                odds = odds.text

                # Look at value balls and count how many are blue
                value = 1
                ball1 = driver.find_element_by_xpath('/html/body/div/main/tf-match-details/div/tf-match-summary/div/'
                                                     'tf-match-verdict/div/tf-match-analyst-verdict/div/div/div[1]/div/'
                                                     'span[2]/tf-ball-rating/div/span[1]')
                blue = sys.getsizeof(ball1.screenshot_as_png)
                for j in range(2, 6):
                    ball_curr = driver.find_element_by_xpath('/html/body/div/main/tf-match-details/div/tf-match-summary/div/'
                                                             'tf-match-verdict/div/tf-match-analyst-verdict/div/div/div[1]/div/'
                                                             'span[2]/tf-ball-rating/div/span[{}]'.format(j))
                    ball_curr = sys.getsizeof(ball_curr.screenshot_as_png)
                    if ball_curr == blue:
                        value += 1

                outcome = bet_outcome(home, away, pred, score)

                Profit = profit(outcome, odds, value)

                # Append game info into empty dataframe
                df = df.append(
                    {'Date': date, 'League': league, 'Home': home, 'Away': away, 'Bet': pred, 'Value': value,
                     'Odds': odds, 'Result': score, 'W/L': outcome, 'Profit': Profit}, ignore_index=True)

                # Go back to all games and increase game count
                driver.back()
                game_num += 1

            # Break if: games in league are complete or game does not have betting info
            except (exc.NoSuchElementException, exc.TimeoutException):
                if game_num > 1:
                    print('[INFO] Found {} {} games'.format(game_num-1, league))
                break
    driver.quit()
    return df


if __name__ == '__main__':
    DF = scrape_day(url)
    DF.to_pickle('sample.pickle')
