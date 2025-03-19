# Analiza danych z koktajlami

Projekt dotyczy analizy danych z koktajlami przy użyciu algorytmu klastrowania KMeans oraz innych technik analizy, takich jak PCA i Silhouette Score. Celem eksperymentów jest:

- **Analiza eksploracyjna zbioru danych**.
- **Przetwarzanie i przygotowanie danych do klastrowania**,
- **Znalezienie optymalnej liczby klastrów**,
- **Wyznaczenie klastrów**,



## Instrukcje instalacji

### Wymagania
Aby uruchomić skrypty w Pythonie, upewnij się, że masz zainstalowanego Pythona w wersji 3.x oraz **pip**.

### Instalacja zależności

Zainstaluj wymagane biblioteki uruchamiając poniższe polecenie:

pip install -r dependencies.txt

## Dane wejściowe

Dane wejściowe znajdują się w pliku formatu JSON:

- `data/raw_data_cocktail.json`

## Przygotowanie danych

1. Uruchom skrypt **preprocessing**. Ten skrypt przygotowuje dane do klastrowania i zapisuje je w pliku:

   - `data/cluster_data.json`

2. Skrypt wykonuje następujące operacje:
   - Wydobywa z kolumny `ingredients` nazwy poszczególnych składników koktajli.
   - Dodaje kolumny 0/1 informujące o obecności składników w koktajlu.
   - Usuwa dane kategoryczne z zestawu danych.

Po uruchomieniu skryptu **preprocessing**, dane będą gotowe do klastrowania.

## Klastrowanie

1. Uruchom skrypt **clustering**. Zawiera on metodę łokcia do wyboru optymalnej liczby klastrów oraz przeprowadza klastrowanie danych za pomocą algorytmu **KMeans**.

2. Po uruchomieniu skryptu **clustering**:
   - Zobaczysz wykres prezentujący **metodę łokcia**, który pomoże Ci wybrać odpowiednią liczbę klastrów.
   - Następnie zostanie przeprowadzona klastrowanie danych.
   - Zostanie wyświetlony wynik **Silhouette Score**, który oceni jakość klastracji.
   - Na końcu pojawi się wykres ilustrujący klasteryzację.

## Analiza eksploracyjna danych (EDA)

W projekcie znajduje się również **notatnik Jupyter** o nazwie **EDA**, który zawiera:
   - **Korelacje pomiędzy składnikami** koktajli,
   - **Wykresy częstości występowania poszczególnych składników** w danych,
   - **Analizę korelacji tagów**.

Notatnik ten pozwala na głębszą eksplorację danych, analizę wzorców i zależności pomiędzy składnikami.

## Przekształcenie danych

Do przeprowadzenia klasteryzacji, dane zostały przekształcone w następujący sposób:
   - Z kolumny **ingredients** wydobyto nazwy składników koktajli, a następnie dodano kolumny 0/1, które informują o obecności poszczególnych składników w koktajlu.
   - Usunięto dane kategoryczne, aby uprościć dane do formatu numerycznego.
   - Dla **tagów**: usunięto wiersze z brakującymi wartościami, a następnie wykonano identyczną operację jak w przypadku składników, tworząc kolumny 0/1.
