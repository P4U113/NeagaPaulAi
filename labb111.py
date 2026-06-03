from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
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
# Ex 7

X = df[['bmi']]        # input  - coloana bmi (2D)
y = df['target']       # target - scorul diabetului

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Coeficient (panta m):   {model.coef_[0]:.2f}")
print(f"Intercept (n):            {model.intercept_:.2f}")
y_pred = model.predict(X_test)

plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color="steelblue", alpha=0.6, label="Date testare")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Linie regresie")
plt.xlabel("BMI")
plt.ylabel("Scor diabet")
plt.title("Regresie Liniara Simpla - BMI vs Scor Diabet")
plt.legend()
plt.show()

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"\nMSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")

# Ex 8

X2 = df[['bmi', 'bp']]
y = df['target']


X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X2_train, y2_train)


print("Coeficienti:")
for feature, coef in zip(X2.columns, model2.coef_):
    print(f"  {feature}: {coef:.2f}")
print(f"Intercept: {model2.intercept_:.2f}")


y2_pred = model2.predict(X2_test)
r2 = model2.score(X2_test, y2_test)
print(f"\nScorul R^2: {r2:.4f}")
