import matplotlib.pyplot as plt

# Given data
segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set figure size
colors = ['blue', 'green', 'orange', 'red']
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=140, colors=colors)

# Add a title
plt.title('Revenue Distribution Across Business Segments')

# Show plot
plt.show()
