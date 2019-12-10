import requests

url = 'https://www.bbc.co.uk/news'

response = requests.get(url)

print(response.status_code)

# print(response.content)

print(response)

# packages allow us to do complex things but easier as its abstracted