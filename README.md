README - Instrukcja instalacji i powtórzenia eksperymentów
Projekt dotyczy analizy danych z koktajlami przy użyciu algorytmu klastrowania KMeans oraz innych technik analizy, takich jak PCA i Silhouette Score. Celem eksperymentów jest znalezienie optymalnej liczby klastrów, wyznaczenie ich a także przetwarzanie i przygotowanie danych do klastrowania oraz analiza eksploracyjna zbioru danych.

W celu uruchomienia skryptów w python: 
instalujemy biblioteki -> pip install -r dependencies.txt
dane znajdują się w pliku formatu JSON data/raw_data_cocktail.json

Eksperyment rozpoczynamy od uruchomienia skryptu preprocesing, przygotowuje on dane do klastracji i zapisuje ten plik jako "data/cluster_data.json".
Uruchamiając skrypt clustering zobaczymy wykres prezentujący metodę łokcia, która służy do wyboru liczby klastrów, po tym odbywa się klastracja,
widzimy wynik Silhouette Score i wykres, które służą do oceny klastracji.
Notatnik jupyter EDA, zawiera informacje o korelacjach pomiędzy składnikami, wykres częstości występowania danego składniki i korelację tagów.
To oraz klastracja jest możliwa dzięki przekształceniu danych w następujący sposób: 
wydobycie z kolumny indgredients nazw poszczególnych składników użytych do zrobienia danego koktajlu i dodanie kolumn 0/1 informujących o obecności składnika w koktajlu, 
wyrzucenie danych kategorycznych ze zbioru,
do wyznaczenie korelacji tagów usunięcie wierszy niepełnych, a następnie identyczna operacja jak "ingredients".
