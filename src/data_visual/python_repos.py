import pygal
import requests
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS


# Get the most popular Python/C/Ruby/Java/Go repositories on GitHub
def fetch_python_repositories(url):
    r = requests.get(url)
    return r


url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = fetch_python_repositories(url)


# Store the response in a dictionary
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
# Analyze the repositories
repo_dicts = response_dict["items"]
# print(f"Repositories returned: {len(repo_dicts)}")

name, plot_dicts = [], []
for repo_dict in repo_dicts:
    name.append(repo_dict["name"])
    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"],
        "xlink": repo_dict["html_url"],
    }
    plot_dicts.append(plot_dict)


# Make visualization
my_style = LS("#336699", base_style=LCS)

# Config
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24  # Font size for the title
my_config.label_font_size = 14  # Font size for labels
my_config.major_label_font_size = 18  # Font size for major labels
my_config.truncate_label = 15  # Truncate long labels to 15 characters
my_config.show_y_guides = False
my_config.width = 1000  # Width of the chart

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = name

chart.add("", plot_dicts)
chart.render_to_file("../../results/python_repos.svg")

# print("Selected information about each repository:")
# for repo_dict in repo_dicts:
#     print(f"Name: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Description: {repo_dict['description']}")

# # Examine the first repository
# repo_dict = repo_dicts[0]
# print(f"Keys: {len(repo_dict.keys())}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("Selected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Forks: {repo_dict['forks_count']}")
# print(f"Description: {repo_dict['description']}")
