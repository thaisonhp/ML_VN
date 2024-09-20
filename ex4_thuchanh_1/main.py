# lay dữ loiệu loiệu
 
import pandas as pd 

data = pd.read_csv("/Users/luongthaison/Documents/Third_years_student/ML_basic_VietNguyen/dataset/diabetes.csv")

# visualize dũ liệu 

from ydata_profiling import ProfileReport

# profile = ProfileReport(data, title = "Disabetes_report",explorative=True)
# profile.to_file("Disabetes_report.html")

# chia du lieu 

target = "Outcome"
x = data.drop(target,axis=1)
y = data[target]

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3 , random_state=42)

# tien xu ly du lieu 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit_transform(x_train)
scaler.fit(x_test)

# chon mo hinh va train 
# vi du lieu co do tuong quan thap nen chon mo hinh phi tuyen (Decision tree , randomforest )
from sklearn.metrics import classification_report 
from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
param = {
    "n_estimators" : [50,100,200,300],
    "criterion" : ["gini","entropy","log_loss"]
}
model = GridSearchCV(
    estimator = RandomForestClassifier(random_state=42),
    param_grid= param,
    scoring= "recall",
    verbose=1
)
model.fit(x_train,y_train)
score = model.scorer_
param_result = model.best_params_
y_pred = model.predict(x_test)
report = classification_report(y_pred=y_pred , y_true=y_test)
print("recall",model.best_score_)
print(model.best_params_)
print(report)