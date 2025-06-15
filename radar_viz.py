import matplotlib.pyplot as plt
import numpy as np

# Define data
labels = ['Productivity', 'Quality', 'Communication', 'Teamwork', 'Leadership']
sales = [8, 7, 9, 6, 7]
marketing = [6, 8, 7, 9, 8]

# Prepare angles for the radar chart
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Prepare values by appending the first value to close the shape
values_sales = sales + [sales[0]]
values_marketing = marketing + [marketing[0]]

# Create the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot and fill data for Sales in green
ax.plot(angles, values_sales, color='green', linewidth=2, label='Sales')
ax.fill(angles, values_sales, color='green', alpha=0.25)

# Plot and fill data for Marketing in red
ax.plot(angles, values_marketing, color='red', linewidth=2, label='Marketing')
ax.fill(angles, values_marketing, color='red', alpha=0.25)

# Set the category labels on the axes
angles_deg = [a * 180 / np.pi for a in angles[:-1]]
ax.set_thetagrids(angles_deg, labels)

# Set the radial limits
ax.set_ylim(0, 10)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Display the plot
plt.show()
