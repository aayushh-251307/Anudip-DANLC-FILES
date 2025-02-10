import pandas as pd

# Given data
score = {
    'Math': [78, 85, 96, 80, 86],
    'English': [84, 94, 89, 83, 86],
    'Hindi': [86, 97, 96, 72, 83]
}

# Create a DataFrame
df = pd.DataFrame(score)

# Display the DataFrame
print(df)
