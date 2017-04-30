import pandas as pd
from collections import Counter
import numpy as np
###########################################
# For time 
###########################################
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_mapping = {}
for i,mon in enumerate(month):
    print mon
    if i <9:
        month_mapping['0%d'%(i+1)] = mon
    else:
        month_mapping['%d'%(i+1)] = mon
###########################################
# Read Data
###########################################        
data = pd.read_csv('Meteorite_Landings.csv')
data['meteorite'] = [1 for i in range(data.shape[0])]
data_no_missing = data.dropna()
#data = data[np.isfinite(data['reclat'])]
#print data[:3]
feature = []
label = []
for row in data_no_missing.values:
	if type(row[6])==str:
		if float(row[6][6:10]) > 1973 and float(row[6][6:10])!= 1998:
			tmp = {}
			if int(row[6][3:5]) >12:
				pass
			else:
				#print row[6][:10]
				date_list = [j if i!=1 else month_mapping[j]  for i,j in enumerate(row[6][:10].split('/')) ]
				print date_list[-1] # year
				#print ' '.join(date_list)
				#print row[6][11:-2]
				print row[7:9] # latitude, longitutude
				feature.append([int(date_list[-1])]+row[7:9].tolist() )
				label.append(row[-1])
print feature
print label,len(label)
###########################################
# Simulation Data
###########################################
simfeature = [] 
simlabel = [] 
for example in feature:
	simlat = np.random.uniform(-90,90,1).tolist()[0]
	simlog = np.random.uniform(0,360,1).tolist()[0]
	print [example[0],simlat,simlog]  # year, latitude, longitutude
	simfeature.append([example[0],simlat,simlog])
	simlabel.append(0)
feature = np.array(feature)
simfeature = np.array(simfeature)

Feature = np.concatenate((feature, simfeature), axis=0)
Label = label + simlabel

###########################################
#Saving Feature and Label for training (txt or feature.p)
###########################################
import pickle
f = open('feature.p','wb') 
pickle.dump((Feature,Label),f)
f.close()