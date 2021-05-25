# Infogol Scraper

Infogol claims to have analyzed millions of data points to form a betting model that provides undervalued betting picks for soccer matches. The goal of this scraper is to capture Infogol's betting picks alongside the match results, which they also provide, to analyze the strength of their predictions.

This scraper gathers the information on the 'Matches' section of https://www.infogol.net/en using Selenium browser automation and Python. Providing the main script with a date range will yield a pandas dataframe structured as shown below:

|Date|League|Home team|Away team|Infogol betting pick|Infogol pick value|Bookmaker pick odds|Match result|Bet result|Profit/Loss|
|----|------|---------|---------|--------------------|------------------|-------------------|------------|----------|-----------|
|    |      |         |         |                    |                  |                   |            |          |           |
|    |      |         |         |                    |                  |                   |            |          |           |

In sports betting, bookmakers use machine learning to predict game-level events, match results, and long term team and player success. Betting odds are quantitative interpretations of these predictions, allowing bettors to try their luck at making better predictions than the bookmaker. Infogol claims to have devloped an algorithm that is more accurate than the bookmaker, and provides a 'pick' for soccer matches. This pick is the bet where their model varies most from the bookmaker's, thereby giving bettors favorable odds. This project aims to capture the picks Infogol provides alongside the match results to analyze where the strengths and weaknesses lie in their algorithm.

The project is currently in the data collection stage. The scraper is functional and robust, allowing for automated collection of years worth of data. The next stage will be forming an analysis plan to capture insights from the data.

**Contents:**  
*Functional, In Use*  
convenience  
&ensp;&ensp;`chromedriver` - executable used by WebDriver to control Chrome  
&ensp;&ensp;`results_convenience.py` - functions for calculating bet result and profit/loss from scraped match information  
&ensp;&ensp;`scrape_past.py` - function for scraping one day worth of matches that have already occured  
`main.py` - takes a date range and optional existing dataframe and yeilds a new dataframe with match information from given days  

*Semi-Functional, Obsolete*   
`notplayed.py` - yeilds dataframe with tomorrow's match information, leaving empty columns for match result, bet result, and profit/loss  
`results.py` - yeilds dataframe with results from played matches  

*Non-Functional*  
`combine.py` - aims to combine dataframes from notplayed.py and results.py and calculate bet result and profit/loss  
`test.py` - test script with changing uses  

**Issues/Improvements:**  
- [ ] Warn user if given dates are out of range (ongoing games, future games). Maintain functionality for capturing past games in date range after warning.
- [ ] Reduce explicit wait times to minimum without yielding errors, requires testing.

  
