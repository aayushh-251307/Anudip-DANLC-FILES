import numpy as np

# Input: list and tuple
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

# Convert list to array
array_from_list = np.array(my_list)

# Convert tuple to array
array_from_tuple = np.array(my_tuple)

# Print the arrays
print("List to Array :")
print(array_from_list)

print("\nTuple to array :")
print(array_from_tuple)
