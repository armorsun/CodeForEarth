import pandas as pd
from collections import Counter
data = pd.read_csv('Meteorite_Landings.csv')
date = data['year'].tolist()
date.sort()

print date[0],type(date[0])
date = [info for info in date if type(info)!= float ]
L = Counter(date)
x = []
y = []
for key, value in L.items():
	if value >10:
		print key[6:10],value
		x.append(float(key[6:10]))
		y.append(value)

################################
# visualization 
################################
import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.show()