def UserBasedTimeSlot(userId):
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	import random
	from sklearn.svm import SVC

	timedata=pd.read_csv('/home/manthan/Desktop/paytm/Taaanthrics404-master/Paytmmodel/userdata/usertime/userstimebehaviour'+str(userId)+'.csv')


	timedata=np.array(timedata)

	xtime=[]
	ytime=[]
	t=0
	while (t<23*60+59):
		if (t not in (timedata.T[2]-timedata.T[2]%100)):
		    ytime.append(1)
		else:
		    ytime.append(0)
		xtime.append(t)
		t=t+100
		
	xtime=np.reshape(xtime,(len(xtime),1))
	ytime=np.reshape(ytime,(len(ytime),1))

	ytime

	xtime
	xprediction=[]
	t=120*4
	for m in range(50):
		xprediction.append(t)
		t=t+10
	
	xprediction=np.reshape(xprediction,(50,1))
	
	timemodel=SVC().fit(xtime,ytime)
	yprediction=timemodel.predict(xprediction)
	timeslot=[]
	for o in range(50):
		if(yprediction[o]!=0):
			timeslot.append(xprediction[o][0])
	print ("Time slot on user activity "+str(timeslot))
	return np.array(timeslot)


