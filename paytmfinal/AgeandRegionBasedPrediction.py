def RegionAndAgeBasedGeneralPrediction(userAge,userTime,regionId):


	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	import seaborn as sb
	import random
	from sklearn.svm import SVC

	dataset=pd.read_csv('/home/manthan/Desktop/paytm/Taaanthrics404-master/Paytmmodel/crowddatasetforsihmodified.csv')

	region1=[]
	region2=[]
	region3=[]
	region4=[]
	region5=[]
	dataset=np.array(dataset)
	for i in range(dataset.shape[0]):
		time=int(dataset[i][9][:2])*60+int(dataset[i][9][3:5])
		if(dataset[i][8]=='city1'):
		    region1.append([dataset[i][1],dataset[i][2],dataset[i][5],dataset[i][6],dataset[i][7],time])
		elif(dataset[i][8]=='city2'):
		    region2.append([dataset[i][1],dataset[i][2],dataset[i][5],dataset[i][6],dataset[i][7],time])
		elif(dataset[i][8]=='city3'):
		    region3.append([dataset[i][1],dataset[i][2],dataset[i][5],dataset[i][6],dataset[i][7],time])
		elif(dataset[i][8]=='city4'):
		    region4.append([dataset[i][1],dataset[i][2],dataset[i][5],dataset[i][6],dataset[i][7],time])
		else:
		    region5.append([dataset[i][1],dataset[i][2],dataset[i][5],dataset[i][6],dataset[i][7],time])
	region1=np.array(region1)
	region2=np.array(region2)
	region3=np.array(region3)
	region4=np.array(region4)
	region5=np.array(region5)

	
	collectionofregion=[]
	collectionofregion.append(region1)
	collectionofregion.append(region2)
	collectionofregion.append(region3)
	collectionofregion.append(region4)
	collectionofregion.append(region5)


	iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']
	iteams=np.array(iteams)
	pname=['ElectronicsAppliances','Fashion','ComputerAndMobile','Grossaries']
	pname=np.array(pname)

	#region wise analysis
	tempregion=np.array(collectionofregion[regionId-1])   # selecting the region required

	probabilityInTheRegion=np.zeros((pname.shape[0]))
	for i in range(tempregion.shape[0]):
		t=np.where(pname==tempregion[i][1])
		probabilityInTheRegion[t]=probabilityInTheRegion[t]+1
	probabilityInTheRegion=probabilityInTheRegion/tempregion.shape[0]
	probabilityInTheRegion=np.array(probabilityInTheRegion)

	#region based catagory prediction
	regionselected=[]
	for m in range(probabilityInTheRegion.shape[0]):
		if(probabilityInTheRegion[m] != 0):
			regionselected.append(pname[m])

	print("Probability of choosing the iteams in region "+str(regionId)+" are "+str(regionselected))


	#age based suggestion for users
	xage=[]
	yage=[]
	for i in range(dataset.shape[0]):
		time=int(dataset[i][9][:2])*60+int(dataset[i][9][3:5])
		xage.append([dataset[i][1],time])
		yage.append(np.where(pname==dataset[i][2]))
	xage=np.array(xage,dtype=object)
	yage=np.array(yage)
	yage=np.reshape(yage,yage.shape[0])



	svrmodel=SVC()
	svrmodel.fit(xage,yage)


	svrmodel.score(xage[50:75],yage[50:75])
	xpredict=[userAge,userTime]
	xpredict=np.array(xpredict)
	xpredict=np.reshape(xpredict,(1,2))
	#prediction based in age
	print ("Based on age is "+str(pname[svrmodel.predict(xpredict)]))






