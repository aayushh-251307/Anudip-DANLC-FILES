import numpy as np
import matplotlib.pyplot as plt

# Given data
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000,
                              36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000,
                           23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000,
                              25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000,
                                  19000, 20000, 21000, 22000, 23000])

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot sales data for each category
axes[0, 0].plot(months, electronics_sales, marker='o', color='blue', label='Electronics')
axes[0, 1].plot(months, clothing_sales, marker='s', color='green', label='Clothing')
axes[1, 0].plot(months, home_garden_sales, marker='^', color='orange', label='Home & Garden')
axes[1, 1].plot(months, sports_outdoors_sales, marker='d', color='red', label='Sports & Outdoors')

# Add titles and labels for each subplot
axes[0, 0].set_title('Electronics Sales')
axes[0, 1].set_title('Clothing Sales')
axes[1, 0].set_title('Home & Garden Sales')
axes[1, 1].set_title('Sports & Outdoors Sales')

# Add common labels
for ax in axes.flat:
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales ($)')
    ax.legend()
    ax.grid(True)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
