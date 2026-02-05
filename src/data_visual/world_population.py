import json

import pygal_maps_world.maps as maps
from country_codes import get_country_code, is_region
from pygal.style import LightColorizedStyle as LCS
from pygal.style import RotateStyle as RS

# Load population data
filename = "../../data/population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of country codes and populations
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        country_code = get_country_code(country_name)
        if country_code:
            cc_populations[country_code] = population
        elif not is_region(country_name):
            print(f"Warning: No country code found for {country_name}")

# Group countries by population size
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


# Create a world map visualization
wm = maps.World()
wm_style = RS(
    "#336699", base_style=LCS
)  # Rotate the color style, 3 numbers meaning red, green, blue
wm = maps.World(style=wm_style)
wm.title = "World Population in 2010"
wm.add("0-10m", cc_pops_1)
wm.add("10m-1bn", cc_pops_2)
wm.add(">1bn", cc_pops_3)
wm.render_to_file("../../results/world_population.svg")
