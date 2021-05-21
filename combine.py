import pandas as pd
from convenience.results_convenience import bet_outcome, profit

Date = 'Thursday 29 April'

# Read in data
notplayed = pd.read_pickle('{}_notplayed.pickle'.format(Date))
#df = pd.read_pickle('{}_results.pickle'.format(Date))
combine = notplayed.copy()

# Test df for 4/29/21
df = pd.DataFrame(columns=['League', 'Result'])
df = df.append({'League': 'UEFA Europa League', 'Result': '1 - 1'}, ignore_index=True)
df = df.append({'League': 'UEFA Europa League', 'Result': '1 - 1'}, ignore_index=True)
df = df.append({'League': 'Moot', 'Result': '3 - 4'}, ignore_index=True)
df = df.append({'League': 'Spanish La Liga', 'Result': '1 - 5'}, ignore_index=True)
df = df.append({'League': 'German Bundesliga Zwei', 'Result': '3 - 3'}, ignore_index=True)
df = df.append({'League': 'Portuguese Primeira Liga', 'Result': '3 - 7'}, ignore_index=True)
df = df.append({'League': 'Moot', 'Result': '2 - 1'}, ignore_index=True)
df = df.append({'League': 'Australian A-League', 'Result': '1 - 3'}, ignore_index=True)

# Establish counter for shorter not played df
index = 0

# Iterate over results df
for moot, row in df.iterrows():
    # Check if results row exists in not played, if not pass without moving to next row of not played
    if row[0] == notplayed.League[index]:

        # Add elements to combine df
        combine.Result[index] = row[1]
        # Check if W/L. Can also pass back 'push'
        outcome = bet_outcome(notplayed.Home[index], notplayed.Away[index], notplayed.Bet[index], row[1])
        combine['W/L'][index] = outcome

        combine.Profit[index] = profit(outcome, combine.Odds[index], combine.Value[index])
        index += 1
    else:
        pass

# Drop any rows containing postponed games
rows = combine[combine['Result'] == 'P'].index
combine.drop(rows, inplace=True)

# Pickle with date as title
combine.to_pickle('{}_combine.pickle'.format(Date))
