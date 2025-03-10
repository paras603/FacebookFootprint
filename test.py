import matplotlib.pyplot as plt

# Set up the figure size
plt.figure(figsize=(8,5))

# Sample data
x = [1, 2, 3, 4, 5]  # Days
y = [10, 15, 30, 25, 40]  # Number of followers

# Plot the data
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add labels and title
plt.xlabel("Days")
plt.ylabel("Number of Followers")
plt.title("Follower Growth Over Time")

# Show the chart
plt.show()
