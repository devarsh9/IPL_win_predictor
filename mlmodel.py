import pandas as pd
import pandas as pd
from sklearn import tree
import pickle
# from IPython.display import Image  
# # from sklearn.externals.six import StringIO  
# from six import StringIO
# import pydot


df=pd.read_excel("IPLData.xlsx")


features = list(df.columns[:5])



y = df["Winner"]
X = df[features]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X,y)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=0)

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=300)
clf = clf.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,recall_score,confusion_matrix

y_pred = clf.predict(X_test)
print(len(X_test))
print("\nAccuracy")
print(accuracy_score(y_test,y_pred))
print("\nRecall_Score")
print(recall_score(y_test,y_pred))
print("\nConfusion Matrix")
print(confusion_matrix(y_test,y_pred))

# Accuracy for the Random Forest Model is 88.6%.
print("\n\nresult:")
print (clf.predict([[1,84,146,1,0]]))

pickle.dump(clf, open('model.pkl','wb'))


#Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1,84,146,1,0]]))