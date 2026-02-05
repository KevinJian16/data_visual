import pygal
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

my_style = LS("#336699", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

plot_dicts = [
    {"value": 16101, "label": "Description of the httpie"},
    {"value": 12345, "label": "Description of the flask"},
    {"value": 9876, "label": "Description of the django"},
]

chart.add("", plot_dicts)
chart.render_to_file("../../results/bar_descriptions.svg")
