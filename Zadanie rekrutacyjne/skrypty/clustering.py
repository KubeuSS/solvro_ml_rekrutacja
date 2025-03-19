import pandas as pd
from scipy.cluster.vq import kmeans
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

df = pd.read_json("data\\cluster_data.json")

# SZUKAM OPTYMALNEJ ILOŚCI KLASTRÓW METODĄ ŁOKCIA
potencjalne_klastry = range(2, 20)
łokieć = []
for k in potencjalne_klastry:
    kmeans = KMeans(n_clusters=k, random_state=1, n_init=5)
    kmeans.fit(df)
    łokieć.append(kmeans.inertia_)
# WYKRES ABY ODCZYTAĆ WYNIK
plt.plot(potencjalne_klastry, łokieć, marker="*")
plt.xlabel("Liczba klastrów")
plt.title("Metoda łokcia")
plt.grid(True, axis="x")
plt.xticks(range(2, 20, 1))
plt.show()

# KLASTROWANIE NA PODSTAWIE METODY ŁOKCIA
ilosc_klastow = 3
kmeans = KMeans(n_clusters=ilosc_klastow, random_state=1, n_init=50)
df["Klaster"] = kmeans.fit_predict(df)

# SPOJRZENIE NA KLASTRY
liczebność_klastrów = df["Klaster"].value_counts()
print(liczebność_klastrów)

# PCA ABY ZWIZUALIZOWAĆ WYNIK KLASTROWANIA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df.drop("Klaster", axis=1))

# ROBIĘ WYKRES PO PCA
plt.scatter(df_pca[:, 1], df_pca[:, 0], c=df["Klaster"], cmap="inferno", marker="o")
plt.xticks([])
plt.yticks([])
plt.title("Wykres pokazujący poczczególne klastry")
plt.show()
score = silhouette_score(df, df["Klaster"])
print("Silhouette Score: ", score)
