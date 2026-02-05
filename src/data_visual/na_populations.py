from pygal_maps_world.maps import World

wm = World()
wm.title = "Population of North America in 2010"
wm.add("North America", {"ca": 34000000, "mx": 113000000, "us": 309000000})
wm.render_to_file("../../results/na_population.svg")
