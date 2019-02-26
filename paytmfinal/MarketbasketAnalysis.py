def MarketBasedPrediction(iteamId):
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt


	dataset=pd.read_csv('/home/manthan/Desktop/paytm/Taaanthrics404-master/Paytmmodel/crowddatasetforsihmodified.csv')

	dataset=np.array(dataset)
	x=[]
	for i in range(dataset.shape[0]):
		time=int(dataset[i][9][:2])*60+int(dataset[i][9][3:5])
		x.append([dataset[i][1],dataset[i][5],time,dataset[i][7]])
	x=np.array(x,dtype=object)

	def distance(p1,p2):
		t1=p1[0]-p2[0]
		t2=p1[1]-p2[1]
		t3=p1[2]-p2[2]
		return ((t1*t1+t2*t2+t3*t3))

	iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']
	iteams=np.array(iteams)
	pname=['ElectronicsAppliances','Fashion','ComputerAndMobile','Grossaries']
	pname=np.array(pname)


	centroid=np.zeros((iteams.shape[0],3))
	count=np.zeros((iteams.shape[0]))
	for i in range(x.shape[0]):
		t=int(np.where(iteams==x[i][3])[0])
		centroid[t][0]=centroid[t][0]+x[i][0]
		centroid[t][1]=centroid[t][0]+x[i][1]
		centroid[t][2]=centroid[t][0]+x[i][2]
		count[t]=count[t]+1
	   

	for i in range(iteams.shape[0]):
		centroid[i]=centroid[i]/count[i]


	distancetable=np.zeros((iteams.shape[0],iteams.shape[0]))
	for i in range(iteams.shape[0]):
		for j in range(iteams.shape[0]):
		    distancetable[i][j]=distance(centroid[i],centroid[j])


	distancetable=np.array(distancetable,dtype=int)
	#print distancetable

	#predicting the associated products
	"""for i in range(iteams.shape[0]):
		median=np.median(distancetable[i])/2
		print "If product "+str(iteams[i])+ "is choosen then other similar products which might be choosen are"
"""
	string=""
	for l in range(iteamId.shape[0]):
		median=np.median(distancetable[l])*2
		for j in range(iteams.shape[0]):
		    if(distancetable[iteamId[l]][j]>median):
		        string=string+str(" ")+str(iteams[j])
		print ("Based On users market basket analysis "+string+"\n")
		        
	#if response id negative decrease the value by .15 time else increase the value by .15 times




