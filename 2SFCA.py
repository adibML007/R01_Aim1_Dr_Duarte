# Load data
# Use an origin-destination matrix with cut-off driving time (30 minutes)
import pandas as pd
import numpy as np
data = pd.read_csv(r'W:\od_matrix.csv')
data.head()
Origins = np.unique(data.ZCTA_Center)
Destinations = np.unique(data.Provider)
# print(Origins)
# print(Destinations)
# print(data[data.iloc[:, 0] == 1])
# Step 1
Y = []
for j in Destinations:
    X = data[data.iloc[:, 1] == j]
    D = 1/X.Distance.sum()
    Y.append(D)
B = pd.DataFrame([])
B['Destinations'] = Destinations
B['Pop_pro_ratio'] = Y
T = []
X = []
# Step 2
for i in Origins:
    P = data[data.iloc[:, 0] == i]
    for k in range(P.shape[0]):
        G = B[B.iloc[:, 0] == P.iloc[k, 1]]
        T.append(G.iloc[0, 1])
    X.append(sum(T))
    T = []
Geo = pd.DataFrame([])
Geo['ZCTA'] = Origins
Geo['Access_Score'] = X
Geo.to_csv('Access.csv')

