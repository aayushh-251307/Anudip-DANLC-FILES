import numpy as np
import matplotlib.pyplot as plt

# Given data (example values)
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800,
3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

# Create scatter plot
plt.scatter(square_footage, selling_prices, color='blue', marker='o')

# Add labels and title
plt.xlabel('Square Footage')
plt.ylabel('Selling Price (in thousands)')
plt.title('House Size vs. Selling Price')

# Show plot
plt.show()
