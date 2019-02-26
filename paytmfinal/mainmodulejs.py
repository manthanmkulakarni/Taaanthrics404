import WishlistFiltering as wm
import UserBehaviourBasedPrediction as usbbpm
import AgeandRegionBasedPrediction as arbpm
import MarketbasketAnalysis as mbam
import UserBasedTimeSlotPrediction as ubtspm
import TimeSlotOnAge as tsam
import  sys, json, numpy as np
import math


#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
	#Users details

	userUniqueId=1
	age=35
	regionid=1
	Usergender=1 #male
	g=['M','F']

	print("User ID: "+str(userUniqueId)+"\nAge: "+str(age)+"\nRegion Id: "+str(regionid)+"\nUseragender: "+str(g[Usergender-1]))

	iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']

	arbpm.RegionAndAgeBasedGeneralPrediction(age,720,regionid) # parameters are age , usagetime , regionid



	top2UsersPrediction=usbbpm.IndivisualUserBasedProductPrediction(userUniqueId)



	mbam.MarketBasedPrediction(top2UsersPrediction)   #only users intrested products id are sent for basket analysis

	wm.PotentialIteamsInWishlist(3)


	tsam.TimeSlotBasedOnAge(age,Usergender)

	ubtspm.UserBasedTimeSlot(userUniqueId)









#start process
if __name__ == '__main__':
    main()


