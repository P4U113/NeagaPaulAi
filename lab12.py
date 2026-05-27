from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
diabetes=load_diabetes()
import pandas as pd
import numpy as np
x=np.array([[1],[2],[3],[4]])
y=np.array([5,6,7,8])
reg=LinearRegression()
reg.fit(x,y)
print(reg.predict([[5]]))
df=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
df['target']=diabetes.target
print(df.head())
print(df.describe())

import matplotlib.pyplot as plt

# Histograma bmi
plt.figure()
plt.hist(df['bmi'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma BMI')
plt.xlabel('BMI')
plt.ylabel('Frecvență')
plt.grid(axis='y', alpha=0.75)
plt.savefig('bmi_histograma.png')
print('Histograma BMI a fost salvată ca bmi_histograma.png')
plt.show()

# Grafic BMI și vârstă în funcție de target
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(df['target'], df['bmi'], c=df['target'], cmap='viridis', edgecolor='k')
plt.title('BMI în funcție de target')
plt.xlabel('Target')
plt.ylabel('BMI')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(df['target'], df['age'], c=df['target'], cmap='plasma', edgecolor='k')
plt.title('Vârstă în funcție de target')
plt.xlabel('Target')
plt.ylabel('Age')
plt.grid(True)

plt.tight_layout()
plt.savefig('bmi_age_target.png')
print('Graficul BMI și vârstă în funcție de target a fost salvat ca bmi_age_target.png')
plt.show()
