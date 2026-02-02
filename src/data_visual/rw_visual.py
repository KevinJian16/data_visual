import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Create a random walk instance, generate points, and plot the walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(rw.x_values, rw.y_values, color='steelblue', linewidth=1.6)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)  # Starting point
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # Ending point
    
    # Remove the axes.
    plt.axis('off')
    
    plt.show()
    
    # Prompt the user to continue or exit.
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break

