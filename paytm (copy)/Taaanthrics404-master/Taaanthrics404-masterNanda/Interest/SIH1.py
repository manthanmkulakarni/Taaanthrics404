#blocklist
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm

#importing dataset
dataset=pd.read_csv(r'crowddatasetforsihmodified.csv')

#adding column called interest and inserting values
wishlist=pd.DataFrame(dataset)
wishlist=wishlist.iloc[0:50]
wishlist=wishlist[['Catagory','Color','Discount']]
wishlist['Interest']=1
index=wishlist.index[wishlist['Catagory']=="Fashion"].tolist()
wishlist.loc[index,'Interest']=0
index=wishlist.index[wishlist['Color']=="Tomato"].tolist()
wishlist.loc[index,'Interest']=0
index=wishlist.index[wishlist['Discount']==5].tolist()
wishlist.loc[index,'Interest']=0

#categorising
x=wishlist.iloc[:,:-1].values
y=wishlist.iloc[:,3].values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder() 
x[:,0]=labelencoder.fit_transform(x[:,0])
x[:,1]=labelencoder.fit_transform(x[:,1])
onehotencoder= OneHotEncoder(categorical_features= [0,1])
x = onehotencoder.fit_transform(x).toarray()
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn import tree,metrics
dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
dtree.fit(xtrain, ytrain)
# use the model to make predictions with the test data
y_pred = dtree.predict(xtest)
# model performance
count_misclassified = (ytest != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(ytest, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))

"""from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=10)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(xtrain,ytrain)

# prediction on test set
y_pred=clf.predict(xtest)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(ytest, y_pred))"""
#0.80 accuracy
