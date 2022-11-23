import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define Data

totally_annoyed_factor = -3
annoyed_factor = -1
neutral_factor = 1
relatively_indiferent_factor = 1.5
indiferent_factor = 3

labels = [
    "Spam generated\nby users",
    "Missing important\nposts",
    "Lack of notifications\nvisibility",
    "Lack of search\nor filtering\nmechanism",
    "Finding an\nold post",
    "Unable to save\nimportant posts",
    "Lack of a precise\nposting chronology",
    "Need to repost\nthe same content\non multiple groups"
]

artists = [
    "Totally annoyed (-3)",
    "Annoyed (-1)",
    "Neutral (+1)",
    "Relatively indifferent (+1.5)",
    "Indifferent (+3)"
]

indiferent_counts = np.array([4, 6, 13, 4, 9, 15, 9, 29]) * indiferent_factor
relatively_indiferent_counts = np.array([19, 22, 17, 10, 24, 25, 23, 23]) * relatively_indiferent_factor
neutral_counts = np.array([37, 32, 28, 30, 29, 25, 27, 20]) * neutral_factor
annoyed_counts = np.array([23, 28, 34, 40, 30, 25, 25, 14]) * annoyed_factor
totally_annoyed_counts = np.array([29, 24, 20, 28, 20, 22, 28, 26]) * totally_annoyed_factor

colors = ['#ff9999','#ffcc99', '#f199ff', '#66b3ff', '#99ff99']

position = np.arange(8)

h = 0.4

plt.yticks(fontsize=10)

for x, ha, hb, hc, hd, he in zip (labels, totally_annoyed_counts, annoyed_counts, neutral_counts, relatively_indiferent_counts, indiferent_counts):
    for idx, (h, c) in enumerate(sorted(zip([ha, hb, hc, hd, he], colors))):
        if h < 0:
            plt.barh(x, h, color=c, zorder=idx)
        else:
            plt.barh(x, h, color=c, zorder=-idx)

plt.legend(artists, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fancybox=True, prop={'size': 10})
plt.show()