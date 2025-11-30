import matplotlib.pyplot as plt
import os

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 4, 2, 5, 7, 6, 9]

plt.scatter(x, y)
# plt.scatter(x, y, s=80)

plt.title("Simple Scatter Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")

current_dir = os.path.dirname(__file__)
output_path = os.path.join(current_dir, "..", "outputs", "scatter_plot.png")

plt.show()

