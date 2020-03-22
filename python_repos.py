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



# # Part 2: Working with the response dictionary
# r = requests.get(url, headers=headers)
# response_dict = r.json()
#
# print(f"Total repositories: {response_dict['total_count']}") # prints the total amount of repositories under 'total_count'
#
# # Explore the information about the repositories
# repo_dicts = response_dict['items'] # Takes all repositories from the dictionary titled 'items' and stores them in a variable
# print(f"Repositories returned: {len(repo_dicts)}")
#
# # Examine the first repository
# repo_dict = repo_dicts[0] # takes the first repository and prints out all the keys
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()): # for loop that returns the name of every key in the first repository
#     print(key)




# # Part 3: Start returning the values associated with some of the keys
# r = requests.get(url, headers=headers)
# response_dict = r.json()
#
# print(f"Status code: {r.status_code}")
# print(f"Total repositories: {response_dict['total_count']}")
#
# repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")
#
# repo_dict = repo_dicts[0]
#
# print("\nSelected information from the first repository: ")
#
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")



# Part 4: Summarizing the top repositories
r = requests.get(url, headers=headers)
response_dict = r.json()

print(f"Status Code: {r.status_code}")
print(f"Total Repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Returned Repositories: {len(repo_dicts)}")

print("\nSelected Information about each repository: ")
for repo_dict in repo_dicts: # For Loop that loops through all keys in the repository and returns specific information
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")


