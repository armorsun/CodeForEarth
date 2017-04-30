import pickle
import numpy as np
import itertools
import math
######################################
# Part1 : Read File
######################################
f = open('feature.p','rb')
data = pickle.load(f) 
f.close()

Feature = data[0]
Label = data[1]
print Feature.shape
print len(Label)

###########################################
#Training 
##########################################

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
# reg = linear_model.BayesianRidge()
# reg.fit(Feature, Label)
clf = LogisticRegression()
clf.fit(Feature, Label)
print 'score', clf.score(Feature, Label)	
###########################################
#Testing
##########################################
# simlat = np.random.uniform(-90,90,1).tolist()[0]
# simlog = np.random.uniform(0,360,1).tolist()[0]
output = []
simtesting = list(itertools.product(range(-90,91),range(1,361)))
simtesting = [[2018, e[0], e[1]] for e in simtesting]

#print reg.predict (simtesting)
print clf.predict(simtesting)
#t = 0
for i,test in enumerate(clf.predict_proba(simtesting).tolist()):
	if test[1] > 0.92: # 0.925
		print simtesting[i]
		output.append(simtesting[i])
		#t+=1
print len(output)
output = []
for y in [2018,2019,2020,2021,2022]:
	tmp = {}
	simtesting = list(itertools.product(range(-90,91),range(1,361)))
	simtesting = [[y, e[0], e[1]] for e in simtesting]

	#print reg.predict (simtesting)
	print clf.predict(simtesting)
	#t = 0
	for i,test in enumerate(clf.predict_proba(simtesting).tolist()):
		if test[1] > 0.98: # 0.925
			print simtesting[i]
			x = 0.16 * math.sin(math.radians(float(simtesting[i][1]))) * math.cos(math.radians(float(simtesting[i][2])))
			y = 0.16 * math.sin(math.radians(float(simtesting[i][1]))) * math.sin(math.radians(float(simtesting[i][2])))
			z = 0.16 * math.cos(math.radians(float(simtesting[i][1]))) 
			tmp['Date'] = '01 Oct ' + '%d' %(y)
			tmp['Time'] = '12:00:00'
			tmp['X'] = x
			tmp['Y'] = y
			tmp['Z'] = z
			output.append(simtesting[i])
			#t+=1
print len(output)

###########################################
#Writing JSON data
###########################################
import json

data = {
    'date': output
}

with open('data_predict.json', 'w') as f:
    json.dump(data, f)