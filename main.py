from convenience.scrape_past import scrape_day
import argparse
import datetime
import pandas as pd

# Start date, end date, existing dataframe
ap = argparse.ArgumentParser()
ap.add_argument('-sd', '--start_date', required=True, help='[Str]: YYYY-MM-DD. If only one day, only pass this argument')
ap.add_argument('-ed', '--end_date', required=False, help='[Str]: YYYY-MM-DD')
ap.add_argument('-df', '--existing_df', required=False, help='[pickle path]: existing df to concatenate to')
args = vars(ap.parse_args())

# Convert start and end date strings to dates
start_date = datetime.datetime.strptime(args['start_date'], '%Y-%m-%d').date()
if args['end_date'] is None:
    end_date = start_date
    filename = '{}.pickle'.format(args['start_date'])
    print('[INFO] Scraping single day ({})...'.format(args['start_date']))
else:
    end_date = datetime.datetime.strptime(args['end_date'], '%Y-%m-%d').date()
    filename = '{}_to_{}.pickle'.format(args['start_date'], args['end_date'])
delta = datetime.timedelta(days=1)

# Unpickle existing dataframe
if args['existing_df'] is None:
    df = pd.DataFrame(columns=['Date', 'League', 'Home', 'Away', 'Bet', 'Value', 'Odds', 'Result', 'W/L', 'Profit'])
    print('[INFO] Starting with empty dataframe...')
else:
    df = pd.read_pickle(args['existing_df'])
    filename = '{}_to_{}.pickle'.format(args['existing_df'][:10], args['end_date'])
    print('[INFO] Starting with {}'.format(args['existing_df']))


while start_date <= end_date:
    current = start_date.strftime('%Y-%m-%d')
    url = 'https://www.infogol.net/en/matches/{}'.format(current)
    current_df = scrape_day(url)
    df = pd.concat([df, current_df])
    start_date += delta

df.to_pickle(filename)
print('\n[INFO] Dataframe saved ({}).'.format(filename))
