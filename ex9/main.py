import pandas as pd 
from sklearn.model_selection import train_test_split
data = pd.read_excel("dataset/final_project.ods" , engine="odf")

target = "career_level"
x = data.drop(target,axis=1)
y = data[target]

x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.2 ,random_state=42 ,stratify=y)
print(y_train.value_counts())
print(y_test.value_counts())