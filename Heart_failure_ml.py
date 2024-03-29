# -*- coding: utf-8 -*-
"""ROC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nNldA-f0mXsaH1JeWTLOws8f91aPgPLq
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
import torch

df=pd.read_csv('/content/heart_failure_clinical_records_dataset.csv')

x=df.drop(['DEATH_EVENT'],axis=1)
y=df['DEATH_EVENT']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
print('X training data size: {}'.format(x_train.shape))
print('y training data size: {}'.format(y_train.shape))
print('X testing data size: {}'.format(x_test.shape))
print('y testing data size: {}'.format(y_test.shape))
print("{0:0.2f}% of data is in training set".format((len(x_train)/len(df.index)) * 100))
print("{0:0.2f}% of data is in test set".format((len(x_test)/len(df.index)) * 100))

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=100)
rf.fit(x_train,y_train)
y_pred = rf.predict(x_test)
rf.score(x_test,y_test)
#confusion matrix

from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn import metrics
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

cm=metrics.confusion_matrix(y_test, y_pred, labels=[1, 0])
df_cm = pd.DataFrame(cm, index = [i for i in ["Actual 1","Actual 0"]],
columns = [i for i in ["Predict 1","Predict 0"]])
plt.title('Random Forest')
sns.heatmap(df_cm, annot=True, fmt='g');


TP = cm[0,0]
FP = cm[0,1]
FN = cm[1,0]
TN = cm[1,1]

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy: {0:0.4f}'.format(classification_accuracy))

from sklearn.naive_bayes import GaussianNB
rf1=GaussianNB()
rf1.fit(x_train,y_train)
gnb_pred = rf1.predict(x_test)
rf1.score(x_test,y_test)

cm=metrics.confusion_matrix(y_test, gnb_pred, labels=[1, 0])
df_cm = pd.DataFrame(cm, index = [i for i in ["Actual 1","Actual 0"]],
columns = [i for i in ["Predict 1","Predict 0"]])
plt.title('Naive Bayes')
sns.heatmap(df_cm, annot=True, fmt='g');


TP = cm[0,0]
FP = cm[0,1]
FN = cm[1,0]
TN = cm[1,1]

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy: {0:0.4f}'.format(classification_accuracy))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5,weights='uniform',metric='euclidean')
knn.fit(x_train,y_train)
knn_pred = knn.predict(x_test)
knn.score(x_test,y_test)
0.8648238665093545
#confusion matrix for KNN
cm=metrics.confusion_matrix(y_test, knn_pred, labels=[1, 0])
df_cm = pd.DataFrame(cm, index = [i for i in ["Actual 1","Actual 0"]],
columns = [i for i in ["Predict 1","Predict 0"]])
plt.title('KNN Confusion Matrix')
sns.heatmap(df_cm, annot=True, fmt='g');


TP = cm[0,0]
FP = cm[0,1]
FN = cm[1,0]
TN = cm[1,1]

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy: {0:0.4f}'.format(classification_accuracy))

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
lr_pred=lr.predict(x_test)
lr.score(x_test,y_test)

cm=metrics.confusion_matrix(y_test, lr_pred, labels=[1, 0])
df_cm = pd.DataFrame(cm, index = [i for i in ["Actual 1","Actual 0"]],
columns = [i for i in ["Predict 1","Predict 0"]])
plt.title('Logistic Regression')
sns.heatmap(df_cm, annot=True, fmt='g');


TP = cm[0,0]
FP = cm[0,1]
FN = cm[1,0]
TN = cm[1,1]

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy: {0:0.4f}'.format(classification_accuracy))

from sklearn import ensemble
gb=ensemble.GradientBoostingClassifier()
gb.fit(x_train,y_train)
gb_pred = gb.predict(x_test)
gb.score(x_test,y_test)

#confusion matrix for Gradient Boosting Classifer
cm=metrics.confusion_matrix(y_test, gb_pred, labels=[1, 0])
df_cm = pd.DataFrame(cm, index = [i for i in ["Actual 1","Actual 0"]],
columns = [i for i in ["Predict 1","Predict 0"]])
plt.title('Gradient Boosting Classifer')
sns.heatmap(df_cm, annot=True, fmt='g');


TP = cm[0,0]
FP = cm[0,1]
FN = cm[1,0]
TN = cm[1,1]

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy: {0:0.4f}'.format(classification_accuracy))

from sklearn.svm import SVC
sv=SVC(kernel='linear',probability=True)
sv.fit(x_train,y_train)
sv_pred = sv.predict(x_test)
sv.score(x_test,y_test)

#confusion matrix for Support Vector Machine
cm=metrics.confusion_matrix(y_test, sv_pred, labels=[1, 0])
df_cm = pd.DataFrame(cm, index = [i for i in ["Actual 1","Actual 0"]],
columns = [i for i in ["Predict 1","Predict 0"]])
plt.title('Support Vector Machine')
sns.heatmap(df_cm, annot=True, fmt='g');


TP = cm[0,0]
FP = cm[0,1]
FN = cm[1,0]
TN = cm[1,1]

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy: {0:0.4f}'.format(classification_accuracy))

from sklearn import tree
dt=tree.DecisionTreeClassifier()
dt.fit(x_train,y_train)
dy_pred=dt.predict(x_test)
dt.score(x_test,y_test)

#Decision Tree Plot
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
fn = list(x_train)
cn = ['0', '1']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4, 4), dpi=300)
plot_tree(dt, feature_names = fn, class_names=cn, filled=True)
fig.savefig('tree.png')

from sklearn import tree
dt1=tree.DecisionTreeClassifier(criterion='entropy',max_depth=3)
dt1.fit(x_train,y_train)
dy_pred1=dt.predict(x_test)
dt1.score(x_test,y_test)

#Decision Tree Plot
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
fn = list(x_train)
cn = ['0', '1']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4, 4), dpi=300)
plot_tree(dt1, feature_names = fn, class_names=cn, filled=True)
fig.savefig('tree.png')

from sklearn.ensemble import BaggingClassifier
from sklearn import model_selection
kfold = model_selection.KFold(n_splits = 3)
model = BaggingClassifier(base_estimator = dt,n_estimators = 500)
results = model_selection.cross_val_score(model, x, y, cv = kfold)
print("accuracy :")
print(results.mean())

from sklearn.ensemble import AdaBoostClassifier
abc = AdaBoostClassifier(n_estimators=50,learning_rate=1)
# Train Adaboost Classifer
model = abc.fit(x_train, y_train)

#Predict the response for test dataset
ay_pred = model.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, ay_pred))

#confusion matrix for Decision Tree Classifier for entropy
cm=metrics.confusion_matrix(y_test, ay_pred, labels=[1, 0])
df_cm = pd.DataFrame(cm, index = [i for i in ["Actual 1","Actual 0"]],
columns = [i for i in ["Predict 1","Predict 0"]])
plt.title('Decision Tree Classifer')
sns.heatmap(df_cm, annot=True, fmt='g');


TP = cm[0,0]
FP = cm[0,1]
FN = cm[1,0]
TN = cm[1,1]

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
print('Classification accuracy: {0:0.4f}'.format(classification_accuracy))

print(classification_report(y_test,ay_pred))

df1 = pd.DataFrame({'All Classifier': ['Random Forest', 'Naive Bayes', 'K_Nearest Classifier', 'Logistic Regression',
'Gradient Boosting','Support Vector Machine', 'Decision Tree gini','Decision Tree Entropy','Bagging Clasifier','Ada Boosting'], 'Accuracy': ['0.8785', '0.8000',
'0.8643', '0.8784', '0.8824', '0.8800','0.8284','0.8698','0.8774','0.8712']})

df1

r_probs=[0 for _ in range(len(y_test))]
rf_probs=rf.predict_proba(x_test)
rf1_probs=rf1.predict_proba(x_test)
knn_probs=knn.predict_proba(x_test)
lr_probs=lr.predict_proba(x_test)
gb_probs=gb.predict_proba(x_test)
sv_probs=sv.predict_proba(x_test)
dt_probs=dt.predict_proba(x_test)
dt1_probs=dt1.predict_proba(x_test)
model_probs=model.predict_proba(x_test)
abc_probs=abc.predict_proba(x_test)

rf_probs=rf_probs[:,1]
rf1_probs=rf1_probs[:,1]
knn_probs=knn_probs[:,1]
lr_probs=lr_probs[:,1]
gb_probs=gb_probs[:,1]
sv_probs=sv_probs[:,1]
dt_probs=dt_probs[:,1]
dt1_probs=dt1_probs[:,1]
model_probs=model_probs[:,1]
abc_probs=abc_probs[:,1]

from sklearn.metrics import roc_curve,roc_auc_score
r_auc=roc_auc_score(y_test,r_probs)
rf_auc=roc_auc_score(y_test,rf_probs)
rf1_auc=roc_auc_score(y_test,rf1_probs)
knn_auc=roc_auc_score(y_test,knn_probs)
lr_auc=roc_auc_score(y_test,lr_probs)
gb_auc=roc_auc_score(y_test,gb_probs)
sv_auc=roc_auc_score(y_test,sv_probs)
dt_auc=roc_auc_score(y_test,dt_probs)
dt1_auc=roc_auc_score(y_test,dt1_probs)
model_auc=roc_auc_score(y_test,model_probs)
abc_auc=roc_auc_score(y_test,abc_probs)

print("Random Predictions:AUROC = %.3f"%(r_auc))
print("Random Forest:AUROC = %.3f"%(rf_auc))
print("Naive Bayes:AUROC = %.3f"%(rf1_auc))
print("K-Nearest Neighbours:AUROC = %.3f"%(knn_auc))
print("Logistic Regression:AUROC = %.3f"%(lr_auc))
print("Gradient Boosting:AUROC = %.3f"%(gb_auc))
print("Support Vector Machine:AUROC = %.3f"%(sv_auc))
print("Decesion Tree Gini:AUROC = %.3f"%(dt_auc))
print("Decesion Tree Entropy:AUROC = %.3f"%(dt1_auc))
print("Bagging Clasifier:AUROC = %.3f"%(model_auc))
print("Ada Boosting:AUROC = %.3f"%(abc_auc))

r_fpr,r_tpr,_=roc_curve(y_test,r_probs)
rf_fpr,rf_tpr,_=roc_curve(y_test,rf_probs)
rf1_fpr,rf1_tpr,_=roc_curve(y_test,rf1_probs)
knn_fpr,knn_tpr,_=roc_curve(y_test,knn_probs)
lr_fpr,lr_tpr,_=roc_curve(y_test,lr_probs)
gb_fpr,gb_tpr,_=roc_curve(y_test,gb_probs)
sv_fpr,sv_tpr,_=roc_curve(y_test,sv_probs)
dt_fpr,dt_tpr,_=roc_curve(y_test,dt_probs)
dt1_fpr,dt1_tpr,_=roc_curve(y_test,dt1_probs)
model_fpr,model_tpr,_=roc_curve(y_test,model_probs)
abc_fpr,abc_tpr,_=roc_curve(y_test,abc_probs)

plt.figure(figsize=(7,5))
plt.plot(r_fpr,r_tpr,linestyle='--', label="Random Preddiction(AUROC=%0.3f)"%r_auc)
plt.plot(rf_fpr,rf_tpr,linestyle='--', label="Random Forest(AUROC=%0.3f)"%rf_auc)
plt.plot(rf1_fpr,rf1_tpr,linestyle='--', label="Naive Bayes(AUROC=%0.3f)"%rf1_auc)
plt.plot(knn_fpr,knn_tpr,linestyle='--', label="K-nearest neighbor(AUROC=%0.3f)"%knn_auc)
plt.plot(lr_fpr,lr_tpr,linestyle='--', label="Logistic Regression(AUROC=%0.3f)"%lr_auc)
plt.plot(gb_fpr,gb_tpr,linestyle='--', label="Gradient Boosting(AUROC=%0.3f)"%gb_auc)
plt.plot(sv_fpr,sv_tpr,linestyle='--', label="Support Vector Machine(AUROC=%0.3f)"%sv_auc)
plt.plot(dt1_fpr,dt1_tpr,linestyle='--', label="Decesion tree(AUROC=%0.3f)"%dt1_auc)
plt.plot(model_fpr,model_tpr,linestyle='--', label="Bagging Classifier(AUROC=%0.3f)"%model_auc)
plt.plot(abc_fpr,abc_tpr,linestyle='--', label="Ada Boosting(AUROC=%0.3f)"%abc_auc)
plt.legend()

