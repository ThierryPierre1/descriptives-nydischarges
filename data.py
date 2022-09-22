import pandas as pd
from tableone import TableOne, load_dataset
import tabulate
import numpy as np
import scipy as sp
import matplotlib as mpl

#import dataset
data = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
data
data.columns
data.dtypes
data.head
print(data.keys())
print(list(data.columns))

data_columns = ['Length of Stay', 'Zip Code - 3 digits', 'Age Group']
data_categorical = ['Length of Stay','Gender']
data_groupby = ['Hospital County']
data
print(data[['Length of Stay', 'Zip Code - 3 digits', 'Age Group']].to_string(index=False))

data =TableOne(data, columns=data_columns, categorical=data_categorical, groupby=data_groupby, pval=False)

print(data.tabulate(tablefmt = "fancy_grid"))

data.to_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')


# Data visualization
#Pie Chart of the age groups

data['Age Group'].value_counts()
Ages = np.array([283, 223, 208, 169, 118])
labels = ["70+", "0-17", "50-69", "18-29", "30-49"]
mpl.pie(Ages, labels = labels)
mpl.legend(title = "The Age Groups")
mpl.show()