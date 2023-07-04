import requests
import datetime

# Specify your API key and other parameters
api_key = '1BxuT8kRkzP)G4lwrNBWLw(('
site = 'stackoverflow'
page_size = 10  # Number of results to retrieve

# Calculate the Unix timestamps for the current month
current_month = datetime.datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
from_date = int(current_month.timestamp())
to_date = int(datetime.datetime.now().timestamp())

# Construct the API request URL
url = f'https://api.stackexchange.com/2.3/questions?site={site}&fromdate={from_date}&todate={to_date}&order=desc&sort=votes&pagesize={page_size}'

# Add the API key as a header
headers = {'Accept-Encoding': 'gzip', 'User-Agent': 'My Stack Overflow API Client'}
params = {'key': api_key}

# Send the API request and fetch the data
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Extract the trending tags from the response
trending_tags = [item['tags'] for item in data['items']]

# Print the trending tags
print('Top Trending Tags:')
for tags in trending_tags:
    print(', '.join(tags))
