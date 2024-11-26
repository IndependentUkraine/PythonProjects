
# Імпортуємо необхідні бібліотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

# Завантаження датасету
df = pd.read_csv('Mall_Customers.csv')

# Попередній аналіз даних (EDA)
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Кодування категоріальної змінної 'Gender'
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])

# Масштабування даних
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Age', 'Annual_Income', 'Spending_Score']])

# Застосування PCA
pca = PCA()
pca_data = pca.fit_transform(scaled_data)

# Визначення оптимальної кількості головних компонент
explained_variance = np.cumsum(pca.explained_variance_ratio_)
plt.plot(range(1, len(explained_variance) + 1), explained_variance, marker='o')
plt.title('PCA: Кількість головних компонент')
plt.xlabel('Кількість компонент')
plt.ylabel('Кумулятивна пояснена дисперсія')
plt.show()

# Візуалізація PCA у 2D
pca_2d = PCA(n_components=2)
pca_2d_data = pca_2d.fit_transform(scaled_data)
plt.scatter(pca_2d_data[:, 0], pca_2d_data[:, 1], alpha=0.7, c='blue')
plt.title('PCA: 2D візуалізація')
plt.xlabel('Головна компонента 1')
plt.ylabel('Головна компонента 2')
plt.show()

# Візуалізація PCA у 3D
from mpl_toolkits.mplot3d import Axes3D
pca_3d = PCA(n_components=3)
pca_3d_data = pca_3d.fit_transform(scaled_data)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pca_3d_data[:, 0], pca_3d_data[:, 1], pca_3d_data[:, 2], alpha=0.7, c='green')
ax.set_title('PCA: 3D візуалізація')
ax.set_xlabel('Головна компонента 1')
ax.set_ylabel('Головна компонента 2')
ax.set_zlabel('Головна компонента 3')
plt.show()

# Застосування t-SNE
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, random_state=42)
tsne_data = tsne.fit_transform(scaled_data)

# Візуалізація t-SNE
plt.scatter(tsne_data[:, 0], tsne_data[:, 1], alpha=0.7, c='orange')
plt.title('t-SNE: 2D візуалізація')
plt.xlabel('t-SNE компонента 1')
plt.ylabel('t-SNE компонента 2')
plt.show()

# Експерименти з параметрами t-SNE
tsne_alt = TSNE(n_components=2, perplexity=50, learning_rate=300, random_state=42)
tsne_alt_data = tsne_alt.fit_transform(scaled_data)
plt.scatter(tsne_alt_data[:, 0], tsne_alt_data[:, 1], alpha=0.7, c='purple')
plt.title('t-SNE: Альтернативні параметри')
plt.xlabel('t-SNE компонента 1')
plt.ylabel('t-SNE компонента 2')
plt.show()

# Кластеризація на зменшених даних (PCA)
kmeans_pca = KMeans(n_clusters=5, random_state=42)
df['Cluster_PCA'] = kmeans_pca.fit_predict(pca_2d_data)

# Кластеризація на зменшених даних (t-SNE)
kmeans_tsne = KMeans(n_clusters=5, random_state=42)
df['Cluster_tSNE'] = kmeans_tsne.fit_predict(tsne_data)

# Кластеризація на оригінальних даних
kmeans_original = KMeans(n_clusters=5, random_state=42)
df['Cluster_Original'] = kmeans_original.fit_predict(scaled_data)

# Порівняння результатів кластеризації
print(df.groupby('Cluster_PCA').mean())
print(df.groupby('Cluster_tSNE').mean())
print(df.groupby('Cluster_Original').mean())

# Збереження результатів у файл
df.to_csv('Reduced_Clustered_Customers.csv', index=False)
