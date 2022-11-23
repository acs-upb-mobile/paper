import matplotlib.pyplot as plt
import numpy as np

labels = [
    "B.Sc. I", 
    "B.Sc. II", 
    "B.Sc. III", 
    "B.Sc. IV",
    "M.Sc. I",
    "M.Sc. II",
]
sizes = [46, 16, 18, 28, 2, 2]
#colors
colors = ['#66b3ff','#ff9999','#ffcc99','#99ff99', '#f199ff', "#daff99"]
 
fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%')
for text in texts:
    text.set_size(16)
for autotext in autotexts:
    autotext.set_size(16)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()