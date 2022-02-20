import pandas as pd
df=pd.read_csv('output.csv')
df = df.dropna()
import re
df["building"] = "hi"
for index, row in df.iterrows():
    result = ( re.search('bedroom (.*) for sale', row["type"]).group(1))
    df.loc[index,'building'] = result
for index, row in df.iterrows():
    if (row["building"])=="semi-detached house":
        df.loc[index,'building'] = 1
    elif (row["building"])=="terraced house":
        df.loc[index,'building'] = 2
    elif (row["building"])=="detached house":
        df.loc[index,'building'] = 3
    elif (row["building"])=="flat":
        df.loc[index,'building'] = 4
    elif (row["building"])=="apartment":
        df.loc[index,'building'] = 5
    elif (row["building"])=="bungalow":
        df.loc[index,'building'] = 6
    elif (row["building"])=="end of terrace house":
        df.loc[index,'building'] = 7
    elif (row["building"])=="detached bungalow":
        df.loc[index,'building'] = 8
    elif (row["building"])=="house":
        df.loc[index,'building'] = 9
    elif (row["building"])=="town house":
        df.loc[index,'building'] = 10
    elif (row["building"])=="character property":
        df.loc[index,'building'] = 11
    elif (row["building"])=="semi-detached bungalow":
        df.loc[index,'building'] = 12
    elif (row["building"])=="retirement property":
        df.loc[index,'building'] = 13
    elif (row["building"])=="ground floor flat":
        df.loc[index,'building'] = 14
    elif (row["building"])=="barn conversion":
        df.loc[index,'building'] = 15
for index, row in df.iterrows():
    if (row["postcode"])=="DH1":
        df.loc[index,'postcode'] = 1
    elif (row["postcode"])=="DH2":
        df.loc[index,'postcode'] = 2
    elif (row["postcode"])=="DH7":
        df.loc[index,'postcode'] = 7
    elif (row["postcode"])=="DH6":
        df.loc[index,'postcode'] = 6
    elif (row["postcode"])=="DH4":
        df.loc[index,'postcode'] = 4
#Model
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

linear_model =  LinearRegression(normalize=True)

def start_model():
    features = ['number_bedrooms','building']
    X = df[features]
    Y = df['price']

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=40)
    linear_model.fit(X,Y) 

    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=True)
    # coef = linear_model.coef_
    # intercept = linear_model.intercept_

    # linear_pred = linear_model.predict(X)

    # corr_matrix = np.corrcoef(Y, linear_pred)
    # corr = corr_matrix[0,1]
    # R_sq = corr**2

def run_model(num_bedroom, postcode):
    linear_pred = linear_model.predict([[num_bedroom, postcode]])
    #linear_pred = linear_model.predict([[5,2]])

    return linear_pred[0]