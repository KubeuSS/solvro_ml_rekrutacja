import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

df = pd.read_json("data\\cluster_data.json")


# SZUKAM OPTYMALNEJ ILOŚCI KLASTRÓW METODĄ ŁOKCIA
potencjalne_klastry = range(2, 20)
łokieć = []
for k in potencjalne_klastry:
    kmeans = KMeans(n_clusters=k, random_state=1, n_init=50)
    kmeans.fit_predict(df)
    łokieć.append(kmeans.inertia_)

# WYKRES ABY ODCZYTAĆ WYNIK
plt.plot(potencjalne_klastry, łokieć, marker="*")
plt.xlabel("Liczba klastrów")
plt.title("Metoda łokcia")
plt.grid(True, axis="x")
plt.xticks(range(2, 20, 1))
plt.show()


# KLASTRACJA NA PODSTAWIE METODY ŁOKCIA
ilosc_klastow = 14
kmeans = KMeans(n_clusters=ilosc_klastow, random_state=1, n_init=50)
df["Klaster"] = kmeans.fit_predict(df)


# PCA ABY ZWIZUALIZOWAĆ WYNIK KLASTRACJI
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df.drop(columns="Klaster"))


# WIZUALIZACJA KLASTRÓW W DWÓCH WYMIARACH
plt.scatter(df_pca[:, 1], df_pca[:, 0], c=df["Klaster"], cmap="magma", marker="o")
plt.xticks([])
plt.yticks([])
plt.title("Wykres pokazujący poczczególne klastry")
plt.show()
score = silhouette_score(df.drop(columns="Klaster"), df["Klaster"])
print("Silhouette Score: ", score)
