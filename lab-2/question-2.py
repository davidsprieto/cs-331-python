import random
import statistics

# Homework Solution:
# # Initialize a list to store the data read from the file
# data = []
#
# # Read data from the file and populate the list
# with open('data.txt', 'r') as file:
#     for line in file:
#         print(line, end='')  # Print each line as it's read
#         data.append(int(line))  # Convert line to int and add to the list
#
# # Calculate average and standard deviation using the statistics module
# average = statistics.mean(data)
# standard_dev = round(statistics.stdev(data), 1)
#
# # Print the calculated statistics
# print(f'Average: {average:.1f}')  # Format average to one decimal place
# print(f'Standard Deviation: {standard_dev}')
#
# # Append the calculated statistics to the end of the file
# with open('data.txt', 'a') as file:
#     file.write(f'Average: {average:.1f}\n')  # Format average to one decimal place
#     file.write(f'Standard Deviation: {standard_dev}')


# Solution that generates 10 random data points first when it's ran:
# Generate 10 random integers
random_integers = [random.randint(1, 100) for _ in range(10)]

# Calculate average and standard deviation directly from the list
average = sum(random_integers) / len(random_integers)
standard_dev = round(statistics.stdev(random_integers), 1)

# Convert integers to strings with newlines for file writing
random_integers_str = [str(num) + "\n" for num in random_integers]

# Write the integers and the calculated statistics to the file
with open('data.txt', 'w') as file:
    file.writelines(random_integers_str)
    file.write(f'Average: {average:.1f}\n')  # Format to one decimal place
    file.write(f'Standard Deviation: {standard_dev}')

# Print the lines to console
print(''.join(random_integers_str), end='')
print(f'Average: {average:.1f}')
print(f'Standard Deviation: {standard_dev}')
