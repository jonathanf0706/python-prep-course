import matplotlib.pyplot as plt
import os

categories = ["A", "B", "C", "D"]
values = [10, 25, 5, 18]

plt.bar(categories, values, color="skyblue")

plt.title("Simple Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")


current_dir = os.path.dirname(__file__)
output_path = os.path.join(current_dir, "..", "outputs", "bar_chart.png")

plt.savefig(output_path)
plt.show()
