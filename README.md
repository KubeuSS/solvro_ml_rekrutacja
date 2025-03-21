# Klastrowanie zbioru danych zawierającego informacje o koktajlach

Mój projekt wykonuje klastrowanie oparte na nowym zbiorze danych, który jest wynikiem preprocessingu i augmentacji pierwotnego zbioru o których podjąłem decyzję na podstawie analizy oraz porównaniu klastrowań z użyciem innych zbiorów.

## Instrukcje instalacji

Aby uruchomić skrypty, zainstaluj Pythona i **pip**, następnie wymagane biblioteki uruchamiając poniższe polecenie w terminalu Pythona:
- `pip install -r dependencies.txt`

## Dane wejściowe

Dane wejściowe (pierwotna forma zbioru danych) znajduje się w pliku formatu JSON:

- `data/raw_data_cocktail.json`

## Przygotowanie danych

1. Uruchom skrypt **preprocessing**. Ten skrypt przygotowuje dane do klastrowania i zapisuje je w pliku:

- `data/cluster_data.json`

2. Skrypt wykonuje następujące operacje:
   - Dodaje kolumny 0/1, które przechowują informacje o czynności wykonywanych w celu przygotowania danego koktajlu,
   - Usuwa pozostałe kolumny.

Po uruchomieniu **preprocessing**, dane będą gotowe do klastrowania z użyciem **clustering**.

## Klastrowanie

1. Uruchom skrypt **clustering**. Zawiera on metody łokcia oraz silhouette score służące do wyboru optymalnej liczby klastrów i przeprowadza klastrowanie danych za pomocą algorytmu **KMeans**.

2. Po uruchomieniu skryptu **clustering**:
   - Zobaczysz wykres prezentujący **metodę łokcia**,
   - Zostanie przeprowadzona klastrowanie danych,
   - Zostanie wyświetlony wynik **Silhouette Score**, który oceni jakość klastrowania,
   - Pojawi się wykres ilustrujący klastrowanie.
