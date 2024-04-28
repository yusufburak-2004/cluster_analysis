# Import Required Packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Loading and examining the dataset
penguins_df = pd.read_csv("data/penguins.csv")
penguins_df.head()
penguins_df.shape
penguins_df.isna().sum()
non_mis=penguins_df.dropna()
q1 = non_mis['flipper_length_mm'].quantile(0.25)
q3 = non_mis['flipper_length_mm'].quantile(0.75)

# IQR (interquartile range) hesaplama
iqr = q3 - q1

# Alt ve üst eşik değerlerini hesaplama
min_threshold = q1 - 1.5 * iqr
max_threshold = q3 + 1.5 * iqr

# Veriyi filtreleme işlemi
non_mis = non_mis[(non_mis['flipper_length_mm'] >= min_threshold) & (non_mis['flipper_length_mm'] <= max_threshold)]
penguins_clean=non_mis
penguins_clean=pd.get_dummies(penguins_clean)
penguins_clean.drop(['sex_FEMALE','sex_MALE'],axis=1,inplace=True)
penguins_clean.head()
scaler=StandardScaler()
penguins_preprocessed=scaler.fit_transform(penguins_clean)
pca=PCA(n_components=3)
pca.fit(penguins_preprocessed)
penguins_PCA=pca.transform(penguins_preprocessed)
list1=[]
for i in range(1,10):
    kmeans=KMeans(n_clusters=i,random_state=42)
    kmeans.fit(penguins_PCA)
    list1.append(kmeans.inertia_)
list1
plt.plot(range(1, 10), list1, marker='o')

kmeans=KMeans(n_clusters=4)
kmeans.fit(penguins_PCA)
labels=kmeans.predict(penguins_PCA)
pca=PCA(n_components=2)
array=pca.fit_transform(penguins_PCA)
xs=array[:,0]
ys=array[:,1]
plt.scatter(xs,ys,c=labels)
penguins_clean['label']=labels
stat_penguins=penguins_clean.groupby('label').mean()
stat_penguins
