import WishlistFiltering as wm
import UserBehaviourBasedPrediction as usbbpm
import AgeandRegionBasedPrediction as arbpm
import MarketbasketAnalysis as mbam
import UserBasedTimeSlotPrediction as ubtspm
import TimeSlotOnAge as tsam

#Users details

userUniqueId=2
age=20
regionid=2
Usergender=1 #male
g=['M','F']

print("User ID: "+str(userUniqueId)+"\nAge: "+str(age)+"\nRegion Id: "+str(regionid)+"\nUseragender: "+str(g[Usergender-1]))

iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']

arbpm.RegionAndAgeBasedGeneralPrediction(age,720,regionid) # parameters are age , usagetime , regionid
print('$')


top2UsersPrediction=usbbpm.IndivisualUserBasedProductPrediction(userUniqueId)
print('$')


mbam.MarketBasedPrediction(top2UsersPrediction)   #only users intrested products id are sent for basket analysis
print('$')
wm.PotentialIteamsInWishlist(3)
print('$')

tsam.TimeSlotBasedOnAge(age,Usergender)
print('$')
ubtspm.UserBasedTimeSlot(userUniqueId)

print('$')
