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



# Exercitiul 5
import matplotlib.pyplot as plt

k_values = list(range(1, 16, 2))
accuracies = []
for k in k_values:
    knn_k = KNeighborsClassifier(n_neighbors=k)
    knn_k.fit(X_train_scaled, y_train)
    score = knn_k.score(X_test_scaled, y_test)
    accuracies.append(score)
    print(f"k={k} -> acuratete={score:.4f}")

plt.figure()
plt.plot(k_values, accuracies, marker='o')
plt.title('Acuratetea KNN în functie de valoarea lui k')
plt.xlabel('k (numar de vecini)')
plt.ylabel('Acuratete')
plt.xticks(k_values)
plt.grid(True)
plt.savefig('knn_accuracy.png')
print('Grafic salvat ca knn_accuracy.png în directorul proiectului.')
plt.show()

best_k = k_values[accuracies.index(max(accuracies))]
best_accuracy = max(accuracies)
print(f"Valoarea optima a lui k pare să fie {best_k} cu acuratetea {best_accuracy:.4f}.")
print("Comentariu: un k mic poate duce la supraspecializare, in timp ce un k prea mare poate subestima structura datelor.")

#ex 6
from sklearn.metrics import confusion_matrix, classification_report

y_pred = knn.predict(X_test_scaled)
cm = confusion_matrix(y_test, y_pred)
print("Matricea de confuzie:")
print(cm)
print("Raport de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Exercitiul 7
print("\nExercitiul 7: vizualizarea datelor cu 2 caracteristici")
feature_indices = [2, 3]  # petal length, petal width
feature_names = [iris.feature_names[i] for i in feature_indices]
X_plot = X[:, feature_indices]

plt.figure()
for class_label, class_name in enumerate(iris.target_names):
    mask = y == class_label
    plt.scatter(X_plot[mask, 0], X_plot[mask, 1], label=class_name, edgecolor='k')
plt.title('Scatter plot Iris: petal length vs petal width')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.legend()
plt.grid(True)
plt.savefig('iris_scatter.png')
print('Grafic de dispersie salvat ca iris_scatter.png in directorul proiectului.')
plt.show()

# Predict using a new sample entered by the user
print('\nIntrodu datele pentru o floare noua:')
print('Formateaza ca: lungime_petala,latime_petala (de exemplu 4.8,1.8)')
try:
    user_input = input('Valori: ')
    petal_length, petal_width = [float(v.strip()) for v in user_input.split(',')]
    mean_sepal = X_train[:, :2].mean(axis=0)
    new_sample_full = [[mean_sepal[0], mean_sepal[1], petal_length, petal_width]]
    new_sample_scaled = Scaler.transform(new_sample_full)
    prediction = knn.predict(new_sample_scaled)
    print(f'Predicția KNN pentru floarea nouă este: {iris.target_names[prediction[0]]}')
    print(f'(sepal length, sepal width folosite ca medie din datele de antrenament: {mean_sepal[0]:.2f}, {mean_sepal[1]:.2f})')
except Exception:
    print('Date invalide. Asigură-te că introduci două numere separate prin virgulă.')
