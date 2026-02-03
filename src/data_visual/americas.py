from pygal_maps_world.maps import World

wm = World()
wm.title = "Population of the Americas in 2010"
wm.add("North America", {"ca": 34000000, "mx": 113000000, "us": 309000000})
wm.add(
    "South America",
    {
        "ar": 40300000,
        "br": 201000000,
        "cl": 16700000,
        "co": 44700000,
        "ec": 14600000,
        "pe": 29300000,
        "ve": 28500000,
    },
)
wm.render_to_file("../../data/americas_population.svg")
