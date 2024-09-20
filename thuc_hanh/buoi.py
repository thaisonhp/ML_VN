import pandas as pd
# from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import  LogisticRegression
from sklearn.model_selection import GridSearchCV
from lazypredict.Supervised import LazyClassifier



data = pd.read_csv('/Users/luongthaison/Documents/Third_years_student/ML_basic_VietNguyen/dataset/diabetes.csv')

# start = data.describe()

# start = data.info()
# tao report de visualize duw lieu 
# profile = ProfileReport(data , title = "Diabetes Report", explorative= True)
# profile.to_file("Diabetes_Report.html")

# phan chia du lieu
target = "Outcome"
x = data.drop(target, axis=1)
y = data[target]


x_train ,x_test , y_train, y_test = train_test_split(x,y,test_size=0.2, random_state= 42)
# x_train ,x_val , y_train, y_val = train_test_split(x_train,y_train,test_size=0.25, random_state= 42)

print(x_train.shape)
# print(x_val.shape)
print(x_test.shape)

# tien xu ly du lieu

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test) # test vaf val ko duoc fit

params = {
    "n_estimators" : [50,100,200,300],
    "criterion" : ["gini" , "entropy" , "log_loss"]
}
# # chon mo hinh
model = GridSearchCV(
    estimator=  RandomForestClassifier(random_state=100) ,
    param_grid = params ,
    scoring= "f1" ,
    cv= 6 ,
    verbose= 1
    )

model.fit(x_train,y_train)
y_predict = model.predict(x_test)
for i , j in zip(y_predict,y_test):
    print(classification_report(y_test,y_predict))
# clf = LazyClassifier(verbose=0 , ignore_warnings=True , custom_metric=None)
# model , predictions = clf.fit(x_train,x_test,y_train=y_train,y_test=y_test)

# print(model)

# SVM
#               precision    recall  f1-score   support
#
#            0       0.75      0.83      0.79        99
#            1       0.62      0.51      0.56        55
#
#     accuracy                           0.71       154
#    macro avg       0.69      0.67      0.67       154
# weighted avg       0.71      0.71      0.71       154


# Randomforest

#               precision    recall  f1-score   support
#
#            0       0.81      0.80      0.81        99
#            1       0.65      0.67      0.66        55
#
#     accuracy                           0.75       154
#    macro avg       0.73      0.74      0.73       154
# weighted avg       0.76      0.75      0.75       154
