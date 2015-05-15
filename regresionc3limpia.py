# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
import cymysql as MySQLdb
from patsy import dmatrices
from sklearn.cross_validation import cross_val_score, train_test_split
from sklearn import metrics
from scipy import interp
import matplotlib.pyplot as pl
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import StratifiedKFold

# con esto tengo una lista con todos los sellers
connection = MySQLdb.connect (host = "localhost", user = "", passwd = "", db = "iic1005", charset = 'utf8')

cursor = connection.cursor()
cursor.execute("SELECT name FROM sellers")
datasellers = cursor.fetchall()
sellers = datasellers[:]
cursor.close()
connection.close()


a= open("datosgeneradosc3.txt","r")
b=a.readlines()

listaf=[]
for line in b:
    lin=line.strip("\n")
    n=lin.split(";")
    new=n[1:]
    new2=';'.join(new)
    u = (str(n[0]),)
    if u in sellers:
        new2+=";1\n"
    else:
        new2+=";0\n"
    listaf.append(new2)
a.close()

c=open("txtfilegenc3.txt","w")

for lineas in listaf:
    c.write(lineas)
c.close()


data = np.loadtxt('txtfilegenc3.txt', delimiter = ';')

X = data[:, 0:2]
y = data[:, 2]

model = LogisticRegression()
model = model.fit(X, y)
print('precision de modelo:')
print(model.score(X, y))
print('porcentaje de sellers:')
print(y.mean())
print(model.get_params())
print(model.coef_)

#modelo para entrenar 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
modeln2 = LogisticRegression()
modeln2.fit(X_train, y_train)

print('prediccion y probabilidad:')
prediccion = modeln2.predict(X_test)
probabilidad = modeln2.predict_proba(X_test)
print (prediccion)
print (probabilidad)



print('cross validation:')
crossv = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=5)
print (crossv)
print('precision cross validation:')
print (crossv.mean())

print('precision de modelo con training set:')
print (metrics.accuracy_score(y_test, prediccion))
print('auc score:')
print (metrics.roc_auc_score(y_test, probabilidad[:, 1]))


print ('precision, recall y f1 score:')
print (metrics.classification_report(y_test, prediccion))

cv = StratifiedKFold(y, n_folds=5)

mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)
all_tpr = []
model = LogisticRegression()
for i, (train, test) in enumerate(cv):
    probas_ = model.fit(X[train], y[train]).predict_proba(X[test])
    # Compute ROC curve and area the curve
    fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
    mean_tpr += interp(mean_fpr, fpr, tpr)
    mean_tpr[0] = 0.0
    roc_auc = auc(fpr, tpr)
    pl.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))

pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

mean_tpr /= len(cv)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
pl.plot(mean_fpr, mean_tpr, 'k--',
        label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)

pl.xlim([-0.05, 1.05])
pl.ylim([-0.05, 1.05])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic example')
pl.legend(loc="lower right")
pl.savefig('roccurvec3')




#naivebayes

random_state = np.random.RandomState(0)
cv = StratifiedKFold(y, n_folds=5)

mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)
all_tpr = []
model = svm.SVC(kernel='linear', probability=True,
                     random_state=random_state)
for i, (train, test) in enumerate(cv):
    probas_ = model.fit(X[train], y[train]).predict_proba(X[test])
    # Compute ROC curve and area the curve
    fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
    mean_tpr += interp(mean_fpr, fpr, tpr)
    mean_tpr[0] = 0.0
    roc_auc = auc(fpr, tpr)
    pl.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))

pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

mean_tpr /= len(cv)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
pl.plot(mean_fpr, mean_tpr, 'k--',
        label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)

pl.xlim([-0.05, 1.05])
pl.ylim([-0.05, 1.05])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic example')
pl.legend(loc="lower right")
pl.savefig('roccurvec3svm')



