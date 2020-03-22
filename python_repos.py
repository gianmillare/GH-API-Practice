import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' # The url is split up into segments
# Segment one: The staple for any website --> https://api.github.com/
# Segment two: The specific function --> search/repositories
# Segment three: the query --> ?q=
# Segment four: specify the category --> language:python
# Segment five: more specific functions --> &sort=stars

headers = {'Accept': 'application/vnd.github.v3+json'} # Github is on the third version of API

# # Part 1: Initial API Call
# r = requests.get(url, headers=headers) # this is how we call the API, by using requests.get()
# print(f"Status code: {r.status_code}")
#
# # Store the API Response into a variable
# response_dict = r.json() # We reformat the data into something python can read using json() into a variable
#
# # Process the results
# print(response_dict.keys())
#
# # PLEASE NOTE: A status code of '200' means that API call was successfull



# Part 2: Working with the response dictionary
r = requests.get(url, headers=headers)
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

# Explore the information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
