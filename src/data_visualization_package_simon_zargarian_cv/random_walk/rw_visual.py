import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    # Plot the points, ans show the plot.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_valeus, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors="none", s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_valeus[-1], c="red", edgecolors="none",
                s=100)

    # Remove the axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

    """"This code will generate a random walk, display it in matplotlib’s viewer,
    and pause with the viewer open. When you close the viewer, you’ll be asked
    whether you want to generate another walk"""
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break