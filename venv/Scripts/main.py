import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

pd.set_option('display.max_columns', None)

data = pd.read_csv("C:\\Users\\aksh0\\PycharmProjects\\data_analysis\\SAT__College_Board__2010_School_Level_Results.csv")

reading_mean = data["Critical Reading Mean"]
writing_mean = data["Writing Mean"]
math_mean = data["Mathematics Mean"]
total_mean = reading_mean + writing_mean + math_mean

print(math_mean.describe())

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

colors = ['blue', 'green', 'tan']
labels = ['Critical Reading', 'Writing', 'Mathematics']
ax0.hist([reading_mean, writing_mean, math_mean], alpha = 1, range = (0, 800), bins = 10, density = False,
         histtype = 'bar', color = colors, edgecolor = 'black', label = labels)
ax0.set_title("2010 SAT Section Averages")
ax0.legend(prop={'size': 7}, loc='upper right')
ax0.set_xlabel("Mean Section Score (Out of 800)")
ax0.set_ylabel("# Of Schools")

ax1.hist(total_mean, alpha = 1, range = (0, 2400), bins = 15, density = False, histtype = 'bar',
         color = '#ff124d', edgecolor = 'black')
ax1.set_title("2010 SAT Overall Averages")
ax1.set_xlabel("Mean Overall Score (Out of 2400)")
ax1.set_ylabel("# Of Schools")
ax1.set_xticks(np.arange(0, 2401, 600))

ax2.axis("equal")
ax2.axis("off")
ax2.grid(False)

ax3.axis("equal")
ax3.axis("off")
ax3.grid(False)

rows = [u'\u03BC', 'Median', u'\u03C3']
columns = ['Reading', 'Writing', 'Mathematics', 'Overall']
row_colors = ['#4287f5', '#f5e942', '#ff124d']
cell_text = [
    [str(math.floor(np.nanmean(reading_mean))), str(math.floor(np.nanmean(writing_mean))), str(math.floor(np.nanmean(math_mean))), str(math.floor(np.nanmean(total_mean)))],
    [str(np.nanmedian(reading_mean)), str(np.nanmedian(writing_mean)), str(np.nanmedian(math_mean)), str(np.nanmedian(total_mean))],
    ['%.02f' % np.nanstd(reading_mean), '%.02f' % np.nanstd(writing_mean), '%.02f' % np.nanstd(math_mean), '%.02f' % np.nanstd(total_mean)],
]
table = plt.table(cellText=cell_text, rowColours=row_colors, rowLabels=rows,
                  colWidths=[0.4, 0.4] * 4, colLabels=columns, loc="center", cellLoc='center', bbox=[-1, 0, 1.75, 1])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.5, 1.5)

fig.tight_layout()

plt.show()