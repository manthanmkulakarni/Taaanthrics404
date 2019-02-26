def PotentialIteamsInWishlist(userId):
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	from sklearn.svm import SVR
	from sklearn import linear_model
	from sklearn.linear_model import LogisticRegressionCV as LR
	from sklearn.naive_bayes import GaussianNB


	data=pd.read_csv('/home/manthan/Desktop/paytm/Taaanthrics404-master/Paytmmodel/userdata/wishlist/wishlist'+str(userId)+'.csv')

	iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']
	iteams=np.array(iteams)
	pname=['ElectronicsAppliances','Fashion','ComputerAndMobile','Grossaries']
	pname=np.array(pname)

	temp=np.array(data)
	x=[]
	y=[]
	for i in range(temp.shape[0]):
		x.append([temp[i][1],temp[i][2]])
		y.append(temp[i][0])
	x=np.array(x)
	y=np.array(y)

	gnbmodel=GaussianNB()
	gnbmodel.fit(x,y)

	gnbmodel.score(x,y)

	treshold=[[350,5],[250,6]]
	output=gnbmodel.predict(treshold)
	print("Top two potential iteams in wishlist are "+str(iteams[output[0]])+" and "+str(iteams[output[1]]))



