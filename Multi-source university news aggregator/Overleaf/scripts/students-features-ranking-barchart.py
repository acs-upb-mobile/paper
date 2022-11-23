import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

useless_factor = -3
not_so_useful_factor = -0.5
relatively_useful_factor = 0.5
useful_factor = 1.5
very_useful_factor = 3

labels = np.flip([
    "Subscription to\ndifferent information\nsources",
    "Having all news in\none centralized feed",
    "Ability to filter\nand sort posts",
    "Push notifications for\nthe most recent posts",
    "Students' ability to\ncontribute to the feed",
    "Ability to report\nor flag posts",
    "Ability to share\nexternally a post",
    "Ability to\nlike a post",
    "Ability to save\na post on device",
    "Option to preview\na post both in\nsummary and in detail"
])

artists = [
    "Useless (-3)",
    "Not so useful (-0.5)",
    "Relatively useful (+0.5)",
    "Useful (+1.5)",
    "Very useful (+3)"
]

useless_counts = np.flip(np.array([3, 2, 2, 6, 8, 8, 4, 19, 7, 6]) * useless_factor)
not_so_useful_counts = np.flip(np.array([15, 4, 8, 15, 26, 14, 13, 23, 11, 10]) * not_so_useful_factor)
relatively_useful_counts = np.flip(np.array([32, 18, 20, 32, 30, 28, 28, 23, 25, 29]) * relatively_useful_factor)
useful_counts = np.flip(np.array([34, 33, 35, 32, 24, 33, 32, 23, 33, 34]) * useful_factor)
very_useful_counts = np.flip(np.array([28, 55, 47, 27, 24, 29, 35, 24, 36, 33]) * very_useful_factor)

colors = ['#ff9999','#ffcc99', '#f199ff', '#66b3ff', '#99ff99']

position = np.arange(8)

h = 0.4

plt.yticks(fontsize=9)

for x, ha, hb, hc, hd, he in zip (labels, useless_counts, not_so_useful_counts, relatively_useful_counts, useful_counts, very_useful_counts):
    for idx, (h, c) in enumerate(sorted(zip([ha, hb, hc, hd, he], colors))):
        if h < 0:
            plt.barh(x, h, color=c, zorder=idx)
        else:
            plt.barh(x, h, color=c, zorder=-idx)

plt.legend(artists, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fancybox=True, prop={'size': 10})
plt.show()