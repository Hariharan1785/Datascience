import numpy as np
import pandas as pd
from pandas import DataFrame
#data_link = "https://github.com/Hariharan1785/Datascience/blob/main/onewayAnovadata.csv"
data_link = "C://Users//USER/Downloads//onewayAnovadata.csv"
data: DataFrame = pd.read_csv(data_link)
print(data)
col_names = ["A","B","C","D"]
df = pd.read_csv("C://Users//USER/Downloads//onewayAnovadata.csv", names=col_names)
print(data.shape)
print(data.dtypes)
data_numeric = data.select_dtypes(include=[np.number])
print("Numeric datatypes are: \n", data_numeric)
data_objects = data.select_dtypes(exclude=[np.number])
print("Object datatypes are: \n", data_objects)
print("Statistics Summary:\n",data_numeric.describe())
