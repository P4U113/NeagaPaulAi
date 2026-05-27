from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

print("Forma setului de date:", X.shape)
print("atribute", iris.feature_names)
print("clase", iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
Scaler=StandardScaler()
X_train_scaled=Scaler.fit_transform(X_train)
X_test_scaled=Scaler.transform(X_test)
print("Forma setului de antrenare:", X_train.shape)
print("Forma setului de test:", X_test.shape)
print("Clases antrenare:", y_train.shape)
print("Clases test:", y_test.shape)
print("Setul de date scalat (antrenare):", X_train_scaled)
print("Setul de date scalat (test):", X_test_scaled)
print("Setul de date original (antrenare):", X_train[:5])
print(X_train_scaled[:5])
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)
accuracy = knn.score(X_test_scaled, y_test)
print("Acuratețea modelului:", accuracy)
