import requests

# Part 1: Initial API Call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # The url is split up into segments
# Segment one: The staple for any website --> https://api.github.com/
# Segment two: The specific function --> search/repositories
# Segment three: the query --> ?q=
# Segment four: specify the category --> language:python
# Segment five: more specific functions --> &sort=stars

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store the API Response into a variable
response_dict = r.json()

# Process the results
print(response_dict.keys())