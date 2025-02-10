import pandas as pd
import numpy as np

# Given data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Define index labels
labels = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

# Create a DataFrame
df = pd.DataFrame(exam_data, index=labels)

# Display the DataFrame
print(df)
