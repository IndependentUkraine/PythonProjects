import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

# Завантаження датасету
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Price'] = data.target  # Додаємо цільову змінну

df.head()

# Описова статистика для всіх ознак
print(df.describe())

# Перевірка наявності пропущених значень
print(df.isnull().sum())

# Типи даних кожної колонки
print(df.dtypes)

# Побудова гістограм для кожної ознаки
df.hist(figsize=(12, 10), bins=50)
plt.tight_layout()
plt.show()

# Boxplot для кожної ознаки для виявлення викидів
plt.figure(figsize=(12, 10))
sns.boxplot(data=df, orient="h")
plt.tight_layout()
plt.show()

# Кореляційна матриця
corr_matrix = df.corr()

# Теплова карта кореляційної матриці
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.tight_layout()
plt.show()

# Scatter plot між ціною та іншими ознаками
plt.figure(figsize=(12, 10))
sns.pairplot(df, vars=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude', 'Price'])
plt.tight_layout()
plt.show()

# Розділення даних на тренувальну та тестову вибірки
X = df.drop('Price', axis=1)
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабування даних
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Збереження скейлера для подальшого використання
import joblib
joblib.dump(scaler, 'scaler.pkl')

# Створення простого лінійного регресора
X_train_single = X_train[['MedInc']]
X_test_single = X_test[['MedInc']]

# Масштабування
X_train_single_scaled = scaler.fit_transform(X_train_single)
X_test_single_scaled = scaler.transform(X_test_single)

# Побудова та тренування моделі
model = LinearRegression()
model.fit(X_train_single_scaled, y_train)

# Прогнозування
y_pred_single = model.predict(X_test_single_scaled)

# Оцінка метрик
mse_single = mean_squared_error(y_test, y_pred_single)
rmse_single = np.sqrt(mse_single)
r2_single = r2_score(y_test, y_pred_single)

print(f'MSE: {mse_single}, RMSE: {rmse_single}, R²: {r2_single}')

# Графік передбачених vs реальних значень
plt.scatter(y_test, y_pred_single)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.xlabel('Real Prices')
plt.ylabel('Predicted Prices')
plt.title('Real vs Predicted Prices (Single Feature)')
plt.show()

# Графік залишків
residuals = y_test - y_pred_single
plt.scatter(y_pred_single, residuals)
plt.hlines(y=0, xmin=min(y_pred_single), xmax=max(y_pred_single), color='red')
plt.xlabel('Predicted Prices')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.show()

# Розподіл залишків
sns.histplot(residuals, kde=True)
plt.title('Distribution of Residuals')
plt.show()

# Створення множинної лінійної регресії
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_multi = LinearRegression()
model_multi.fit(X_train_scaled, y_train)

# Прогнозування
y_pred_multi = model_multi.predict(X_test_scaled)

# Оцінка метрик
mse_multi = mean_squared_error(y_test, y_pred_multi)
rmse_multi = np.sqrt(mse_multi)
r2_multi = r2_score(y_test, y_pred_multi)

print(f'MSE: {mse_multi}, RMSE: {rmse_multi}, R²: {r2_multi}')

from sklearn.linear_model import Lasso

# Створення Lasso моделі для регуляризації
lasso = Lasso(alpha=0.1)
lasso.fit(X_train_scaled, y_train)

# Прогнозування
y_pred_lasso = lasso.predict(X_test_scaled)

# Оцінка метрик
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
rmse_lasso = np.sqrt(mse_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)

print(f'MSE: {mse_lasso}, RMSE: {rmse_lasso}, R²: {r2_lasso}')

# Функція для прогнозування ціни на будинок
def predict_price(features):
    # Масштабуємо нові дані за допомогою збереженого скейлера
    features_scaled = scaler.transform([features])
    price = model_multi.predict(features_scaled)
    return price