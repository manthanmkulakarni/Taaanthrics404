def IndivisualUserBasedProductPrediction(userId):
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	from sklearn.svm import SVR
	from sklearn import linear_model
	from sklearn.linear_model import LogisticRegressionCV
	from sklearn.naive_bayes import GaussianNB

	

	data=pd.read_csv('/home/manthan/Desktop/paytm/Taaanthrics404-master/Paytmmodel/userdata/userresponse/userpersonalizeddata'+str(userId)+'.csv')



	iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']
	iteams=np.array(iteams)
	pname=['ElectronicsAppliances','Fashion','ComputerAndMobile','Grossaries']
	pname=np.array(pname)

	x=[]
	y=[]

	# users behaviour analysis

	temp=np.array(data)
	for i in range(temp.shape[0]):
		x.append([temp[i][1],temp[i][2],temp[i][4]])
		y.append(temp[i][0])
	x=np.array(x)
	y=np.array(y)

	gnb=GaussianNB()
	gnb.fit(x,y)

	treshold=[[5,90,700],[6,100,750]]




	recomendedproductid=np.array(gnb.predict(treshold))
	
	#only top two predction are considered	
	
	print("Suitable iteams for userID"+str(userId)+" based on his behaviour are "+str(iteams[recomendedproductid[0]])+" and "+str(iteams[recomendedproductid[1]]))

	return recomendedproductid




