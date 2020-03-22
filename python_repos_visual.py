import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

# # Part 5: Visualizing repositories using plotly
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")
#
# # Process the results
# response_dict = r.json()
# repo_dicts = response_dict['items']
#
# repo_names, stars = [], []
# for repo_dict in repo_dicts:
#     repo_names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # Visualize the data
# data = [{
#     'type': 'bar',
#     'x': repo_names,
#     'y': stars,
# }]
#
# my_layout = {
#     'title': 'Most Starred Python Projects on GitHub',
#     'xaxis': {'title': 'Repository'},
#     'yaxis': {'title': 'Stars'},
# }
#
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename="plots/python_repos.html")



# # Part 6: Refining the plotly chart
# r = requests.get(url, headers=headers)
# print(f"Status Code: {r.status_code}")
#
# response_dict = r.json()
# repo_dicts = response_dict['items']
#
# repo_names, stars = [], []
# for repo_dict in repo_dicts:
#     repo_names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# data = [{
#     'type': 'bar',
#     'x': repo_names,
#     'y': stars,
#     'marker': {
#         'color': 'rgb(60, 100, 150)',
#         'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
#     },
#     'opacity': 0.6,
# }]
#
# my_layout = {
#     'title': 'Most Starred Python Projects on GitHub',
#     'titlefont': {'size': 28},
#     'xaxis': {
#         'title': 'Repository',
#         'titlefont': {'size': 24},
#         'tickfont': {'size': 14}
#     },
#     'yaxis': {
#         'title': 'Stars',
#         'titlefont': {'size': 24},
#         'tickfont': {'size': 14},
#     },
# }
#
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='plots/python_repos2.html')



# Part 7: Adding Custom Tooltips (the information shown after hovering)
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']

repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Below is how you pull together a couple values into one output key
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'RGB(179, 229, 255)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most Starred Python Project on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="plots/python_repos3.html")