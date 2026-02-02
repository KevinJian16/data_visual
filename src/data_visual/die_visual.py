import pygal
from die import Die

# Create a D6 die.
die_1 = Die(6)
# Create a D10 die.
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for i in range(50000)]

# Analyze the results.
max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]


# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 dice 50000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D10", frequencies)
hist.render_to_file("die_visual.svg")