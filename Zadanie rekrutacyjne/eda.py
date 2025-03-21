import pandas as pd

df = pd.read_json("raw_data_cocktail.json")

# ZAMIENIAM KOLUMNĘ SKŁADNIKÓW NA NAZWY UŻYWANYCH DO ZROBIENIA DANEGO KOKTAJLU
df["ingredients"] = df["ingredients"].apply(lambda x: [ingredient['name'] for ingredient in x])


# ZAMIENIAM KOLEJNĄ KOLUMNĘ NA DANE BINARNE
def ekstrakcja(kolumna):
    unique = []
    for list in kolumna.values:
        for ing in list:
            if ing not in unique:
                unique.append(ing)
    return unique
# DODAJĘ KOLUMNY 0/1 SKŁADNIKÓW
składniki = pd.DataFrame(0, index=df.index, columns=ekstrakcja(df.ingredients))
for index, składnik in df["ingredients"].items():
    składniki.loc[index, składnik] = 1
df = df.drop(columns="ingredients")
df = pd.concat([df, składniki], axis=1)

