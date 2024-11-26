
# Імпортуємо необхідні бібліотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering

# Завантаження датасету
df = pd.read_csv('Mall_Customers.csv')

# Первинний аналіз даних
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Побудова гістограм
df[['Age', 'Annual_Income', 'Spending_Score']].hist(bins=20, figsize=(10, 6))
plt.show()

# Масштабування даних
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Age', 'Annual_Income', 'Spending_Score']])

# Метод ліктя для визначення оптимальної кількості кластерів
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker='o')
plt.title('Метод ліктя')
plt.xlabel('Кількість кластерів')
plt.ylabel('Інерція')
plt.show()

# Коефіцієнт силуету
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(scaled_data)
    silhouette_scores.append(silhouette_score(scaled_data, labels))

plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Коефіцієнт силуету')
plt.xlabel('Кількість кластерів')
plt.ylabel('Силует')
plt.show()

# Оптимальна кількість кластерів
optimal_k = 5  # Наприклад, на основі графіків

# Кластеризація методом K-means
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Візуалізація кластерів
plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=df['Cluster'], cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X')
plt.title('Кластери клієнтів')
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.show()

# Середні значення для кожного кластера
cluster_summary = df.groupby('Cluster').mean()
print(cluster_summary)

# Альтернативні методи кластеризації: DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
df['DBSCAN_Cluster'] = dbscan.fit_predict(scaled_data)

# Альтернативні методи кластеризації: Ієрархічна кластеризація
agg_clustering = AgglomerativeClustering(n_clusters=optimal_k)
df['Agglomerative_Cluster'] = agg_clustering.fit_predict(scaled_data)

# Збереження результатів у файл
df.to_csv('Clustered_Customers.csv', index=False)
