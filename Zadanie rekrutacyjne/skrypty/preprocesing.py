import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.preprocessing import LabelEncoder

# ZBIERAM INFORMACJE O ZBIORZE DANYCH
pd.set_option('display.width', None)
df = pd.read_json("data/raw_data_cocktail.json")

# ZAMIENIAM KOLUMNĘ SKŁADNIKÓW NA NAZWY UŻYWANYCH DO ZROBIENIA DANEGO KOKTAJLU
df["ingredients"] = df["ingredients"].apply(lambda x: [ingredient['name'] for ingredient in x])

# WYRZUCAM KOLUMNY KTÓRYCH NIE UŻYJĘ DO KLASTROWANIA
df = df.drop(
    columns=["id", "imageUrl", "createdAt", "updatedAt", "tags", "instructions", "alcoholic", "name", "category"])

# ZAMIENIAM GLASS NA DANE NUMERYCZNE ABY UŻYĆ ICH DO KLASTROWANIA
label_encoder = LabelEncoder()
df["glass_encoded"] = label_encoder.fit_transform(df["glass"])

# WYRZUCAM WERSJĘ KATEGORYCZNĄ KOLUMNY ABY ZMNIEJSZCZYĆ DATASET
df.drop(columns=["glass"], inplace=True)


# ZAMIENIAM KOLEJNĄ KOLUMNĘ NA DANE NUMERYCZNE ABY WYKORZYSTAĆ JA DO KLASTROWANIA
    unique = []
    for list in kolumna.values:
        for ing in list:
            if ing not in unique:
                unique.append(ing)
    return unique


# DODAJĘ CECHY 0/1 SKŁADNIKÓW
składniki = pd.DataFrame(0, index=df.index, columns=ekstrakcja(df.ingredients))
for index, składnik in df["ingredients"].items():
    składniki.loc[index, składnik] = 1
df = df.drop(columns="ingredients")
df = pd.concat([df, składniki], axis=1)

# NOWY PLIK JSON DO WYKORZYSTANIA PRZY KLASTROWANIA
df.to_json("data/cluster_data.json", indent=4)
