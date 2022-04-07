

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset
#some time below path will give you problem ,again and again i was tring below syntex but it was giving me error , i got soluntion of this problem in stack over flow , this is bug in pandas ,
#you error may be like this OSError: [Errno 22] Invalid argument: 'E:\\pvg college study\x06th sem\x07iml\\practical\\practical 2.csv'

#temp = pd.read_csv("E:\\pvg college study\6th sem\aiml\practical\practical 2.csv")
#solution of this error try another way to give path 
temp = pd.read_csv("E:\\pvg college study\\6th sem\\aiml\\practical\\sales.csv")
print(temp)

sns.countplot(data = temp )
#you also can use plt.table either xlable 
plt.xlabel('X-axis')
plt.show()


a = temp.loc[:,"Sales"]
month = ['1','2','3','4','5','6','7','8','9']
fig = plt.figure(figsize=(10,10))
plt.pie(a[1:10] ,labels = month)
plt.show()

x = list(temp['Sales'])
y = list(temp['Profit'])
plt.scatter(x,y)
plt.show()


a = temp.loc[:, "Sales"]
x = list(a[:25])
Y = range (25)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend('temp')
plt.title("the sales for first 25 years")
plt.plot(Y, x)
plt.show()

