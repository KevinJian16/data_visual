import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Reds, edgecolor='none')

plt.title("Cubic Growth: y = x^3", fontsize=24)
plt.xlabel("Value of x", fontsize=14)
plt.ylabel("Value of y", fontsize=14)
plt.axis([0, 5100, 0, 130000000000])

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()