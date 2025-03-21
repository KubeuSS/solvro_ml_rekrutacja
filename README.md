# Klastrowanie zbioru danych zawierającego informacje o koktajlach

Mój projekt wykonuje klastrowanie oparte na nowym zbiorze danych, który jest wynikiem preprocessingu i augmentacji pierwotnego zbioru o których podjąłem decyzję na podstawie analizy oraz porównaniu klastrowań z użyciem innych zbiorów.

## Instrukcje instalacji

Aby uruchomić skrypty, zainstaluj Pythona i **pip**, następnie wymagane biblioteki uruchamiając poniższe polecenie w terminalu Pythona:
- `pip install -r dependencies.txt`

## Dane wejściowe

Dane wejściowe (pierwotna forma zbioru danych) znajduje się w pliku formatu JSON:

- `data/raw_data_cocktail.json`

## Wnioski z eksploracji

Dane wymagały obróbki przed klastrowaniem ze względu na format kategoryczny, zbędne kolumny oraz niepełne czy nieużyteczne wiersze. Po wstępnym obejrzeniu danych usunąłem kolumny createdat, updatedat, id, name (brak użytecznego związku z koktajlem), imageUrl (link do obrazu, samego obrazu też nie uwzględniałem), alcoholic (w każdym wierszu wartość 1), instructions (na pierwszy rzut oka niezwiązane z koktajlem). Założyłem, że dobre klastrowanie uda się osiągnąć z wykorzystaniem kolumn: **category**, **glass**, **ingredients** (zamieniłem na listę nazw składników), **tags**. Po zamianie ich na format binarny (dodałem do każdego wiersza kolumnę 0/1 z każdą z unikalnych cech kolumn używanych przy klastrowaniu z użyciem danej kombinacji), wielokrotnie przeprowadziłem klastrowanie wykorzystując rózne kombinacje wymienionych wcześniej kolumn, jeżeli korzystałem w danym momencie z **tags** usuwałem niepełne wiersze. Osiągnięte rezultaty nie były zbyt dobre, wartość silhouette była w granicach 0.15 - 0.31 z tego powodu po ponownym obejrzeniu wszystkich danych spróbowałem dodać nowe kolumny z informacjami wydobytymi z instrukcji, dodałem kolumny 0/1 informujące o czynnościach wykonywanych przy robienu danego koktajlu oraz ich łącznej ilość, klastrowanie z ich wykorzystanie dawało wyniki na poziomie 0.53, a wersja bez łącznej ilości czynności 0.55. Na podstawie tych obserwacji przeprowadziłem **preprocessing** przed **klastrowaniem**.

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

## Notatniki jupytera

Notatniki zawierają: 
   - **EDA** -
      przebrane obserwacje na podstawie, których dokonałem klastrowania,
   - **Preprocessing** -
      ramka danych, która trafia do klastrowania,
   - **Clustering** -
        ewaluację klastrwoania.
