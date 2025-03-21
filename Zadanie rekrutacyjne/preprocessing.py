import pandas as pd

df = pd.read_json("data/raw_data_cocktail.json")
# CZYNNOŚCI PRZY KOKTAJLU, KTÓRE POWTARZAJĄ SIĘ W INSTRUKCJACH
czynnosci = ["stir", "shake", "combine", "strain", "add", "garnish", "fill", "pour", "muddle"]
# DODAJĘ KOLUMNY Z INFORMACJĄ O CZYNNOŚCIACH W FORMACIE BINARNYM
for czynnosc in czynnosci:
    df[czynnosc] = df["instructions"].str.lower().str.contains(czynnosc).astype(int)
# DROPUJĘ KOLUMNY, KTÓRE NIE ZOSTANĄ UŻYTE PRZY KLASTROWANIU
df.drop(columns=["id", "imageUrl", "createdAt", "updatedAt", "tags", "instructions", "alcoholic",
                 "name", "glass", "category", "ingredients"], inplace=True)
# PLIK Z DANYMI DO KLASTROWANIA
df.to_json("data/cluster_data.json", indent=4)
