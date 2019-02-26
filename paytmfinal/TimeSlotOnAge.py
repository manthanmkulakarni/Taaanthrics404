def TimeSlotBasedOnAge(userAge,userGender):
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	import random
	from sklearn.linear_model import LinearRegression as lrg


	dataforagebasedtime=pd.read_csv('/home/manthan/Desktop/paytm/Taaanthrics404-master/Paytmmodel/AgeandGenderBaserBasedUagetime.csv')

	dataforagebasedtime=np.array(dataforagebasedtime)
	xagebasedtime=[]
	yagebasedtime=[]
	for o in range(dataforagebasedtime.shape[0]):
		xagebasedtime.append([dataforagebasedtime[o,2],dataforagebasedtime[o,3]])
		yagebasedtime.append(dataforagebasedtime[o,1])
	  

	#Svm could not give a good accurecy score
	  
	agegenderbasedtimemodel=lrg().fit(xagebasedtime,yagebasedtime)
	xprediction=[]
	xprediction.append([userAge,userGender])
	
	xprediction=np.array(xprediction)
	xprediction=np.reshape(xprediction,(1,2))
	print ("Best time based on age is "+str(int(agegenderbasedtimemodel.predict(xprediction))))
	return xprediction
