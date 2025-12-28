import pandas as pd
import matplotlib.pyplot as plt
file=pd.read_csv("D:\\excel\\project\\customer_shopping_behavior.csv")
#print(file.head())
#print(file.info())
#print(file.describe(include="all"))
#print(file.describe())
'''print(file.isnull().sum())
file['Review Rating']=file.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))
print(file.isnull().sum())
file.columns=file.columns.str.lower()
file.columns=file.columns.str.replace(' ','_')
print(file.columns)
file=file.rename(columns={'Purchase_Amount_(USD)':'Purchase_Amount'})
print(file.columns)'''


x=file["Category"]
y=file["Age"]
plt.title("category with age")
plt.xlabel("category")
plt.ylabel("age")
plt.bar(x.head(50),y.head(50),color="r")
plt.grid()
plt.show()
