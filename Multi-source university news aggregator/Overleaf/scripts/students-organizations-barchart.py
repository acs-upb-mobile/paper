import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()

counts = [62, 44, 5, 1, 1, 1, 1, 0]
total_count = 112
bars = [
    "No organization",
    "LSAC",
    "MLSA",
    "BEST Bucharest",
    "StudentHub",
    "AS Poli",
    "Hackademy",
    "EESTEC",
]
percentages = np.array([
    55.4,
    39.3,
    4.5,
    0.9,
    0.9,
    0.9,
    0.9,
    0
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

colors = ['#66b3ff']

# Create horizontal bars
bars_h = plt.barh(y=df.Group, width=df.Value, color=colors)

for idx, bar in enumerate(bars_h):
  width = bar.get_width() #Previously we got the height
  percentage = round((width * 100.0) / total_count, 1)
  label_y_pos = bar.get_y() + bar.get_height() / 2
  ax.text(width + 1, label_y_pos, s=f'{width} ({percentage}%)', va='center')

plt.xlim(0, 80)
plt.xlabel('Total responses')

# y_pos = np.arange(len(bars))

# # Create bars
# plt.barh(y_pos, counts)

# # Create names on the x-axis
# plt.yticks(y_pos, bars)

# # Show graphic
plt.show()