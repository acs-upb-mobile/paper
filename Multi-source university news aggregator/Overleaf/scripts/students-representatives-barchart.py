import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()

counts = [96, 9, 6, 5, 2, 1]
total_count = 112
bars = [
    "No representative\nfunction",
    "Group leader",
    "Students\norganization\nrepresentative",
    "Students menthor",
    "Series leader",
    "Faculty Council\nrepresentative"
]
percentages = np.array([
    85.7,
    8,
    5.4,
    4.5,
    1.8,
    0.9,
])

# Create a data frame
df = pd.DataFrame ({
        'Group':  bars,
        'Value': counts,
        'Percentages': percentages,
})

# Sort the table
df = df.sort_values(by=['Value'])
# percentages = -np.sort(-percentages)
print(percentages)

print(df)

colors = ['#ff9999']

# Create horizontal bars
bars_h = plt.barh(y=df.Group, width=df.Value, color=colors)

for idx, bar in enumerate(bars_h):
  width = bar.get_width() #Previously we got the height
  percentage = round((width * 100.0) / total_count, 1)
  label_y_pos = bar.get_y() + bar.get_height() / 2
  ax.text(width + 1, label_y_pos, s=f'{width} ({percentage}%)', va='center')

plt.xlim(0, 110)
plt.xlabel('Total responses')

# y_pos = np.arange(len(bars))

# # Create bars
# plt.barh(y_pos, counts)

# # Create names on the x-axis
# plt.yticks(y_pos, bars)

# # Show graphic
plt.show()