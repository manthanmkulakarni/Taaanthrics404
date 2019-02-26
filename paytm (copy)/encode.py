from PIL import Image
import cv2
import  sys, json, numpy as np
import math

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
        #get our data as an array from read_in()
        lines = read_in()

	m=int(lines["first_num"])
	n=int(lines["last_num"])
	rows=n-m
	cols=n
	rwidth=50
	cwidth=50
	string=str(lines["path"])
	str1="/home/manthan/"
	
	path=str1+string
	
	image = cv2.imread(path)
	#image=image.convert('L')
	image=np.array(image)
	# resize image so it can be processed
	# choose optimal dimensions such that important content is not lost
	shape=image.shape
	image = cv2.resize(image, (800,800) )

	# creating copy of original image
	orig = image.copy()

	# convert to grayscale and blur to smooth
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(image, (3, 3), 0)

	edged = cv2.Canny(blurred, 0, 50)
	th2 = cv2.adaptiveThreshold(edged,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
		    cv2.THRESH_BINARY,11,5)
	th2 = cv2.GaussianBlur(th2, (11, 11), 0)
	th2 = cv2.adaptiveThreshold(th2,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
		    cv2.THRESH_BINARY,51,5)
	edges=Image.fromarray(th2)
	edges.save('/home/manthan/matrixr.jpg')
	edges.show()






	def rectify(h):
	    h = h.reshape((4,2))
	    hnew = np.zeros((4,2),dtype = np.float32)

	    add = h.sum(1)
	    hnew[0] = h[np.argmin(add)]
	    hnew[2] = h[np.argmax(add)]

	    diff = np.diff(h,axis = 1)
	    hnew[1] = h[np.argmin(diff)]
	    hnew[3] = h[np.argmax(diff)]

	    return hnew

	image = cv2.imread('/home/manthan/matrixr.jpg')
	#image=image.convert('L')
	image=np.array(image)
	# resize image so it can be processed
	# choose optimal dimensions such that important content is not lost
	shape=image.shape
	image = cv2.resize(image, (800,800) )

	# creating copy of original image
	orig = Image.open(path)
	orig=orig.resize((800,800))
	orig=np.array(orig)

	# convert to grayscale and blur to smooth
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(image, (3, 3), 0)
	#blurred = cv2.medianBlur(gray, 5)

	# apply Canny Edge Detection
	edged = cv2.Canny(blurred, 0, 50)
	orig_edged = edged.copy()

	# find the contours in the edged image, keeping only the
	# largest ones, and initialize the screen contour
	(o,contours, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]


	# get approximate contour
	for c in contours:
	    p = cv2.arcLength(c, True)
	    approx = cv2.approxPolyDP(c, 0.02 * p, True)

	    if len(approx) == 4:
		target = approx
		break


	# mapping target points to 800x800 quadrilateral
	approx = rectify(target)
	pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])

	M = cv2.getPerspectiveTransform(approx,pts2)
	dst = cv2.warpPerspective(orig,M,(800,800))
	outline=Image.fromarray(dst)
	outline=outline.resize((cols*50,rows*50))
	outline.show()
	outline.save("/home/manthan/cropped1.jpg")






	image=Image.open('/home/manthan/cropped1.jpg')
	image=image.convert('L')
	image=np.array(image)


	k=0
	image=Image.fromarray(image)
	for i in range(cols):
	    cropimg=image.crop((i*cwidth,0,(i+1)*cwidth,rows*50))
	    cropimg.save(('/home/manthan/subimages/cell'+str(k)+".jpg"))
	    k=k+1
	    
	#cropimg=image.crop((k*cwidth,0,(k+1)*cwidth,size[1]))
	#cropimg.save(('/home/manthan/subimages/day'+str(k)+".jpg"))





	for j in range(cols):
	    image=Image.open('/home/manthan/subimages/cell'+str(j)+'.jpg')
	    image=image.convert('L')
	    image=np.array(image)
	    size=image.shape
	    image=Image.fromarray(image)
	    for i in range(rows):
		cropimg=image.crop((0,i*rwidth,cwidth,(i+1)*rwidth))
		cropimg.save(('/home/manthan/subimages/subcells/cell'+str(j)+':'+str(i)+".jpg"))
    

	ar=np.zeros((rows,cols))
	for i in range(rows):
	    for j in range(cols):
		img = cv2.imread(('/home/manthan/subimages/subcells/cell'+str(j)+':'+str(i)+'.jpg'),0)
		img = cv2.medianBlur(img,5)
		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,95,param1=15,param2=23,minRadius=1,maxRadius=0)
		if circles is None:
		    ar[i][j]=1
	ar=ar.astype(int)
	for j in range(n-m):
	    for i in range(m,n):
		if((i-m)==j):
		    ar[j][i]=1
		else:
		    ar[j][i]=0

	print "The given Parity check matrix \nH= \n"+str(ar)



	A=ar.T[:m]
	two=np.full((1,n),2)


	#To get agumented matrix  [A|I]
	i=np.identity(m,dtype=int)
	#Generator matrix
	g=i
	g=np.concatenate((g,np.array(A)),axis=1)

	print "The generator matrix [A|I] is:"
	print "G= \n"+str(g)

	size=int(math.pow(2,m))
	M=np.full((size,m),0)
	C=np.full((size,n),0)

	#To generate all combinations for message word  

	for i in range(size):
	    binary=(np.binary_repr(i,width=m))
	    for j in range(m):
		M[i][j]=int(binary[j])
		
	print "\nThe code words for the given message words\n"
	for i in range(size):
	    C[i]=np.dot(M[i],g)    #generating the codewords
	    C[i]=np.remainder(C[i],two)
	    print ("E("+str(M[i])+")---->"+str(C[i]))


       
    
      

#start process
if __name__ == '__main__':
    main()



