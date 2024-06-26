# -*- coding: utf-8 -*-
"""rock vs mine prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U3fB55Qa5obBMdoEuhf0BLP40EKSzcaS
"""

import pandas as pd #for data processing steps asn for loading our data into tables.
import numpy as np # for array
from sklearn.model_selection import train_test_split # to split the data into 2 categories i.e 1 is to train the data and other is to test the trained the data

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score # to check the accuracy of the data

#loading the data set to pandas data frame

sonar_data = pd.read_csv('./Copy of sonar data.csv', header = None)

sonar_data.head()

#to check how many number of rows and columns are there

sonar_data.shape

#statistical mesures for the data

sonar_data.describe() #count mean,..... max

sonar_data[60].value_counts() # to see how many rock and mines are there. 60 is written, so as R amd M are present in the 60th column.

#grouping the data based on mine and rock

sonar_data.groupby(60).mean()

#separating the data and labels

x = sonar_data.drop(columns=60, axis=1) #as droping a column axis =1, if dropng a column asis =0;

y = sonar_data[60]

print(x)
print(y)

#spliting the data to train and test data


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1, stratify = y, random_state=1)
#0.1 means 10% of the data is to be the test data
#statify =y means we need to split the data based on y i.e based on rock and mine
# random_sate is just for fun

print(x.shape, x_train.shape, x_test.shape)

print(x_train,y_train)

"""Model Training --> Using Logistic regression model


"""

model = LogisticRegression()

#training the Logistic Regression model with training data

model.fit(x_train,y_train)

"""Acuurance of the Model

"""

#accuracy of the training data
x_train_prediction = model.predict(x_train)
trainning_data_accuracy = accuracy_score(x_train_prediction, y_train)
print('Accuracy on the training data : ',trainning_data_accuracy)

x_test_prediction = model.predict(x_test)
training_data_accuracy1 = accuracy_score(x_test_prediction, y_test)
print('Accuracy score on test data: ',training_data_accuracy1)

"""Making a predictive System"""

input_data = (0.0340,0.0625,0.0381,0.0257,0.0441,0.1027,0.1287,0.1850,0.2647,0.4117,0.5245,0.5341,0.5554,0.3915,0.2950,0.3075,0.3021,0.2719,0.5443,0.7932,0.8751,0.8667,0.7107,0.6911,0.7287,0.8792,1.0000,0.9816,0.8984,0.6048,0.4934,0.5371,0.4586,0.2908,0.0774,0.2249,0.1602,0.3958,0.6117,0.5196,0.2321,0.4370,0.3797,0.4322,0.4892,0.1901,0.0940,0.1364,0.0906,0.0144,0.0329,0.0141,0.0019,0.0067,0.0099,0.0042,0.0057,0.0051,0.0033,0.0058)
# changing the input data(list) to a numpy array

input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for 1 instance i.e R or M

input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshape)
print(prediction)

if (prediction =='R') :
  print('The object is a Rock')
else :
  print('The object is a Mine')

