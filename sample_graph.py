import matplotlib.pyplot as plt

# Data with values between 30,000 and 35,000, with increasing year-over-year growth
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
data1 = [31428, 32109, 33017, 33542, 35718, 36829, 38017, 39682, 41524, 43491, 45683]
data2 = [32871, 33542, 34328, 35229, 36347, 37632, 39248, 41023, 42879, 45012, 47238]

# Create line graph with adjusted data
plt.figure(figsize=(10, 6))  # Set the figure size

# Plot data source 1 (without legend)
plt.plot(years, data1, marker='o')  # Remove legend

# Plot data source 2 (without legend)
plt.plot(years, data2, marker='s')  # Remove legend

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Values')

# Set y-axis limits from 0 to 50,000
plt.ylim(25000, 50000)

# Add grid and tight layout
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()