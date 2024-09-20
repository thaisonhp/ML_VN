import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("ex2/diabetes.csv")
data.hist() 
plt.show()