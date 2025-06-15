import matplotlib.pyplot as plt
import pandas as pd

# Create sample data
ages = [13, 14, 15, 16, 17, 18]
leadership = [60, 65, 70, 75, 78, 80]
ei = [55, 60, 65, 70, 72, 75]
introvert = [40, 35, 30, 28, 25, 25]
extrovert = [30, 35, 40, 45, 50, 50]
ambivert = [30, 30, 30, 27, 25, 25]

# Create a DataFrame
df = pd.DataFrame({
    'Age': ages,
    'Leadership': leadership,
    'EI': ei,
    'Introvert': introvert,
    'Extrovert': extrovert,
    'Ambivert': ambivert
})

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot line chart for leadership and emotional intelligence scores
ax1.plot(df['Age'], df['Leadership'], label='Leadership', color='blue', marker='o')
ax1.plot(df['Age'], df['EI'], label='Emotional Intelligence', color='orange', marker='o')
ax1.set_xlabel('Age')
ax1.set_ylabel('Score')
ax1.set_title('Leadership and Emotional Intelligence Scores')
ax1.legend()
ax1.grid(True)

# Plot stacked bar chart for personality types
ax2.bar(df['Age'], df['Introvert'], label='Introvert', color='purple')
ax2.bar(df['Age'], df['Extrovert'], bottom=df['Introvert'], label='Extrovert', color='green')
ax2.bar(df['Age'], df['Ambivert'], bottom=df['Introvert'] + df['Extrovert'], label='Ambivert', color='yellow')
ax2.set_xlabel('Age')
ax2.set_ylabel('Percentage')
ax2.set_title('Personality Type Distribution')
ax2.set_ylim(0, 100)
ax2.legend()

# Add a title to the entire figure
fig.suptitle('Leadership, Emotional Intelligence, and Personality Types in High School Students (Ages 13-18)', fontsize=16)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()
