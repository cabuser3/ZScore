import numpy as np
import pandas as pd
from copy import deepcopy
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
get_ipython().magic('matplotlib inline')
#%matplotlib inline
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing the dataset
data = pd.read_csv('C:\\Users\\himverma\\AnacondaProjects\\KMeans\\xclaraOriginal.csv')
print("Input Data and Shape")
print(data.shape)
data.head()

# Getting the values and plotting it
f1 = data['V1'].values
#f2 = data['V2'].values
#X = np.array(list(zip(f1, f2)))
X = np.array(f1)
stats.zscore(X)
fit = stats.norm.pdf(X, np.mean(X), np.std(X)) 
plt.plot(X,fit,'-o')
plt.hist(X, 30, normed=True)
plt.show()
print(X.mean())