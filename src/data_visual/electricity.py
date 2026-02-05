import json

import pygal_maps_world.maps as maps
from country_codes import get_country_code, is_region
from csv2json import csv_to_json
from pygal.style import LightColorizedStyle as LCS
from pygal.style import RotateStyle as RS

# Load electricity access data
csv_filename = "../../data/API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_63.csv"

# Convert CSV to JSON
json_filename = "../../data/electricity.json"
csv_to_json(
    csv_filename,
    json_filename,
    selected_headers=["Country Name", "2022", "2023", "2024"],
)

with open(json_filename) as f:
    pop_data = json.load(f)

# Build a dictionary of country codes and electricity access
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["2023"] != "":
        country_name = pop_dict["Country Name"]
        electricity = float(pop_dict["2023"])
        country_code = get_country_code(country_name)
        if country_code:
            cc_populations[country_code] = electricity
        elif not is_region(country_name):
            print(f"Warning: No country code found for {country_name}")

# Group countries by electricity access
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, electricity in cc_populations.items():
    if electricity < 90:
        cc_pops_1[cc] = electricity
    elif electricity < 99.9:
        cc_pops_2[cc] = electricity
    else:
        cc_pops_3[cc] = electricity

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


# Create a world map visualization
wm = maps.World()
wm_style = RS(
    "#336699", base_style=LCS
)  # Rotate the color style, 3 numbers meaning red, green, blue
wm = maps.World(style=wm_style)
wm.title = "World Electricity Access in 2023"
wm.add("0-90%", cc_pops_1)
wm.add("90-99.9%", cc_pops_2)
wm.add(">99.9%", cc_pops_3)
wm.render_to_file("../../results/world_electricity.svg")
