import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

threshold=3.5

def outliers_modified_z_score(data):
    median_d = np.median(data)
    medianArray=[]
    for d in data:
        medianArray.append(np.abs(d - median_d))
    median_absolute_deviation_d = np.median(medianArray)
    modified_z_scores = [0.6745 * (d - median_d) / median_absolute_deviation_d
                         for d in data]
    return np.where(np.abs(modified_z_scores) > threshold)
    
# Importing the dataset    
data = pd.read_csv('C:\\Users\\himverma\\AnacondaProjects\\ZScore\\xclaraOriginal.csv')
print("Input Data and Shape")
print(data.shape)
data.head()
# Getting the values and plotting it
row1 = data['V1'].values
x = np.array(row1)

outlierLocationArray = outliers_modified_z_score(x)
outliersLocation=[]
for index, location in enumerate(outlierLocationArray[0]):
    outliersLocation.append(location+1)
    
print("OutLiner Index: ", outliersLocation)

#Writing to output CSV File
myFile = open('C:\\Users\\himverma\\AnacondaProjects\\ZScore\\outlierResult.csv', 'w')
myData=[["outliers"],[outliersLocation]]
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
print("Write to CSV completed")

# Plot the results
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.hist(x)
ax1.set_title('Original')
ax2.hist(outliersLocation)
ax2.set_title('Outliers Location')
plt.show()