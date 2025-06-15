Below is a detailed explanation of each line of the provided Python script, formatted in Markdown for tutorial purposes. This explanation is designed to help anyone understand how the code works, especially those new to Python or data visualization with Matplotlib. You can add this file to your GitHub repository to make it easy for others to learn.

---

## Radar Chart Tutorial: Visualizing Department Performance

This Python script creates a radar chart (also known as a spider chart) to visualize performance metrics for two departments: Sales and Marketing. Each department is evaluated across five categories: Productivity, Quality, Communication, Teamwork, and Leadership. The chart uses green for Sales and red for Marketing, making it easy to compare their performance visually.

### Prerequisites

Before running this code, ensure you have the following Python libraries installed:
- **Matplotlib**: For creating the visualization.
- **NumPy**: For numerical operations, particularly handling angles in the radar chart.

You can install them using pip:
```bash
pip install matplotlib numpy
```

### Code Explanation

```python
import matplotlib.pyplot as plt
import numpy as np
```
- **Line 1-2**: We import the necessary libraries.
  - `matplotlib.pyplot` is commonly imported as `plt` and is used for plotting the radar chart.
  - `numpy`, imported as `np`, handles numerical operations, especially for calculating angles in the radar chart.

```python
labels = ['Productivity', 'Quality', 'Communication', 'Teamwork', 'Leadership']
sales = [8, 7, 9, 6, 7]
marketing = [6, 8, 7, 9, 8]
```
- **Line 4-6**: We define the data for the chart.
  - `labels`: A list of strings representing the five categories being evaluated.
  - `sales`: A list of integers representing the performance scores of the Sales department in each category (on a scale from 0 to 10).
  - `marketing`: A list of integers representing the performance scores of the Marketing department in each category.

```python
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop
```
- **Line 8-10**: We set up the angles for the radar chart.
  - `num_vars`: Stores the number of categories (5 in this case), calculated using `len(labels)`.
  - `angles`: Uses `np.linspace` to create evenly spaced angles around a circle, from 0 to 2π radians (a full circle). `num_vars` determines how many points are created, and `endpoint=False` excludes the endpoint to avoid overlap since we’ll close the loop manually. `.tolist()` converts the NumPy array to a Python list.
  - `angles += angles[:1]`: Appends the first angle to the end of the list to "close the loop." This ensures the radar chart forms a complete, connected shape.

```python
values_sales = sales + [sales[0]]
values_marketing = marketing + [marketing[0]]
```
- **Line 12-13**: We prepare the data points for plotting by closing the loop.
  - `values_sales`: Takes the `sales` list and appends its first value (`sales[0]`) to the end. This matches the closed-loop angles and ensures the chart connects back to the starting point.
  - `values_marketing`: Does the same for the `marketing` list, appending `marketing[0]` to the end.

```python
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
```
- **Line 15**: We create a figure and a set of axes for the plot.
  - `plt.subplots`: Returns a tuple containing a figure (`fig`) and axes (`ax`). `figsize=(6, 6)` sets the size of the figure to 6x6 inches.
  - `subplot_kw=dict(polar=True)`: Specifies that the axes should use polar coordinates, which is required for a radar chart.

```python
ax.plot(angles, values_sales, color='green', linewidth=2, label='Sales')
ax.fill(angles, values_sales, color='green', alpha=0.25)
```
- **Line 17-18**: We plot and fill the data for the Sales department.
  - `ax.plot`: Plots the Sales data as a line on the polar axes. `angles` provides the angular positions, and `values_sales` provides the radial distances. `color='green'` sets the line color, `linewidth=2` sets the thickness, and `label='Sales'` adds a label for the legend.
  - `ax.fill`: Fills the area inside the Sales data line with green color. `alpha=0.25` sets 25% transparency, making the fill slightly see-through for better visibility.

```python
ax.plot(angles, values_marketing, color='red', linewidth=2, label='Marketing')
ax.fill(angles, values_marketing, color='red', alpha=0.25)
```
- **Line 20-21**: We plot and fill the data for the Marketing department.
  - Similar to the Sales department, but uses `values_marketing` and red color (`color='red'`) to distinguish it from Sales.

```python
angles_deg = [a * 180 / np.pi for a in angles[:-1]]
ax.set_thetagrids(angles_deg, labels)
```
- **Line 23-24**: We set the category labels on the axes.
  - `angles_deg`: Converts the angles from radians to degrees using a list comprehension. `angles[:-1]` excludes the last angle (the repeated one for closing the loop) since we only need labels for the original categories. The conversion uses the formula: degrees = radians * 180 / π.
  - `ax.set_thetagrids`: Places the `labels` at the specified angles (in degrees) on the polar plot, labeling each axis of the radar chart.

```python
ax.set_ylim(0, 10)
```
- **Line 26**: We set the radial limits of the chart.
  - `ax.set_ylim(0, 10)`: Sets the radial axis range from 0 to 10, matching the scale of the performance scores in `sales` and `marketing`.

```python
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
```
- **Line 28**: We add a legend to the chart.
  - `ax.legend`: Displays the legend using the labels ('Sales' and 'Marketing') defined in the `ax.plot` calls.
  - `loc='upper right'`: Positions the legend in the upper right corner.
  - `bbox_to_anchor=(1.1, 1.1)`: Fine-tunes the legend’s position slightly outside the chart to avoid overlapping with the plot.

```python
plt.show()
```
- **Line 30**: We display the plot.
  - `plt.show()`: Renders the radar chart on the screen. This is the final step to visualize the result.

### Running the Code

To run this code:
1. Ensure you have Python installed on your system.
2. Install the required libraries if you haven’t already:
   ```bash
   pip install matplotlib numpy
   ```
3. Save the script as a `.py` file (e.g., `radar_chart.py`).
4. Run the script using Python:
   ```bash
   python radar_chart.py
   ```
5. A window will pop up displaying the radar chart.

### Summary

This script demonstrates how to create a radar chart using Matplotlib and NumPy in Python. It visualizes performance metrics for two departments across multiple categories, making it easy to compare their strengths and weaknesses. By following this tutorial, you can learn how to:
- Define and prepare data for a radar chart.
- Set up a polar plot with Matplotlib.
- Plot and fill data points with custom colors.
- Customize the chart with labels, limits, and a legend.

Feel free to modify the data (e.g., change scores or add more departments) to explore further! Happy coding!

--- 

This Markdown file is ready to be added to your repository. It’s beginner-friendly and provides a step-by-step breakdown of the code. Let me know if you’d like any adjustments!
