import matplotlib.pyplot as plt

# Given data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set figure size
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange', 'red', 'purple'])

# Add a title
plt.title('Distribution of Monthly Income by Source')

# Show plot
plt.show()
