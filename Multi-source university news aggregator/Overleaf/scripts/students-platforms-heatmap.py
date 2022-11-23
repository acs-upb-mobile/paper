import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

items = [
    "None",
    "Official\ndecisions",
    "Events",
    "Timetable",
    "Course\nmaterials",
    "Assignments",
    "Notifications",
]

platforms = [
    "Facebook",
    "Whatsapp",
    "Teams",
    "Moodle",
    "Outlook",
    "Student\norganizations\nplaforms",
    "Faculty\nplatform",
    "University\nplatform",
]

data = np.array([
    [39, 20, 71, 1, 1, 2, 36],
    [2, 98, 88, 69, 57, 51, 94],
    [3, 77, 75, 21, 67, 61, 62],
    [1, 28, 29, 14, 92, 100, 22],
    [67, 13, 18, 2, 5, 7, 24],
    [63, 21, 36, 0, 0, 0, 31],
    [50, 22, 11, 43, 3, 3, 20],
    [84, 15, 8, 6, 1, 1, 5],
])

# print(np.random.rand(len(platforms), len(items)))

# sns.palplot(sns.color_palette("Greens"))

uniform_data = np.random.rand(len(platforms), len(items))
ax = sns.heatmap(data, linewidth=0.5, cmap = sns.color_palette("Reds", 20), cbar_kws={'label': 'Number of responses'})
sns.set(font_scale=2)
ax.set_yticklabels(platforms, rotation=0)
ax.set_xticklabels(items, rotation=0)
plt.show()