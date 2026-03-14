# Source: https://docs.enate.net/enate-help/polski/rodzaje-elementow-pracy-bilety-procesy-i-czynnosci/prognozowanie-dla-spraw.md

# Prognozowanie dla spraw

Użytkownicy wersji 2024.1 będę mogli korzystać z funkcji prognozowania, która zapewni bardziej precyzyjne szacunki nakładu pracy dla poszczególnych elementów pracy, pozwalając tym samym efektywniej planować zapotrzebowanie na zasoby.

Na dłuższą metę dane te mogą być gromadzone i przekazywane administratorom w celu dostosowywania śledzenia przewidywanego nakładu pracy oraz dostarczania dokładniejszych prognoz dla przyszłych zadań.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FtEf2jG3t2MaBDECOHZ60%252Fimage.png%3Falt%3Dmedia%26token%3Dc3a4c0c4-6ba2-49a2-aa8b-40f898c36109&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=d319d500&#x26;sv=1" alt=""><figcaption></figcaption></figure>

## Jak korzystać z prognozowania

Po włączeniu funkcji „Prognozowanie” w sekcji spraw w Work Managerze pojawi się nowa zakładka – „Szacowanie nakładu pracy”.

Znajdziesz tutaj podsumowanie przewidywanego nakładu pracy dla całej sprawy oraz dla czynności i spraw podrzędnych składających się na tę sprawę, a także analizę przewidywanego nakładu pracy dla czynności i spraw podrzędnych, które jeszcze nie zostały utworzone.

### Podsumowanie nakładu pracy dla sprawy

Sekcja „Podsumowanie nakładu pracy dla sprawy” to miejsce, w którym użytkownik może zmienić szacowany czas przewidziany dla załatwienia danej sprawy oraz znaleźć inne przydatne wskaźniki, które jej dotyczą.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252Fo9LyQZvnukScleAisS5b%252Fimage.png%3Falt%3Dmedia%26token%3Dbc93c65d-63c0-40e4-9eb2-9dd27deab3f3&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=d1ca627b&#x26;sv=1" alt=""><figcaption></figcaption></figure>

* „Całkowity szacunkowy nakład pracy” wskazuje całkowity przewidywany czas, jaki zajmie sprawa. Użytkownik może zastąpić tę wartość bardziej dokładnym oszacowaniem.
  * Jest to suma „Szacunkowego” nakładu pracy dla wszystkich utworzonych zadań i czynności (razem z czynnościami spraw podrzędnych), które składają się na sprawę, oraz wartości „Nakładu pracy dla elementów do utworzenia”.
  * W polu tym początkowo wyświetlana będzie ręcznie ustalana wartość [Początkowy szacunkowy nakład pracy na wpis](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) z Buildera (jeśli istnieje) pomnożona przez [liczbę wpisów](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements).
    * Jeśli „Liczba wpisów” zostanie zaktualizowana, zmiana ta zostanie automatycznie odzwierciedlona w „Szacunkowym nakładzie pracy” dla sprawy, jeśli nie zrobi tego użytkownik Work Managera.
  * Gdy status sprawy to „Rozwiązane” lub „Zamknięte”, jej szacunkowego nakładu pracy nie można już zmienić.
  * Trzeba przy tym pamiętać, że zwiększenie tej wartości zwiększy też wartość „Nakładu pracy dla elementów do utworzenia” i odwrotnie.
* „Całkowity rzeczywisty nakład pracy” pokazuje ilość czasu poświęconego na przetwarzanie jeszcze nieutworzonej sprawy.
  * Jest to suma „Rzeczywistego” nakładu pracy dla wszystkich utworzonych spraw i ich spraw podrzędnych, zaczerpniętych z poszczególnych modułów śledzenia czasu.
* „Całkowity szacunkowy pozostały” to przewidywany czas, jaki pozostał do załatwienia sprawy.
  * Jest to suma „Szacunkowego pozostałego” nakładu pracy dla wszystkich utworzonych czynności i spraw podrzędnych, które składają się na sprawę, ORAZ szacowanego pozostałego czasu pracy nad elementami, które nie zostały jeszcze utworzone (dlatego wartość to może być inna niż wynik odejmowania rzeczywistego nakładu pracy dla sprawy od nakładu szacowanego).

Zmiana wartości „Szacunkowego” nakładu pracy dla sprawy ma następujące skutki:

* Automatyczna aktualizacja wartości „[Nakładu pracy dla elementów do utworzenia](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases#nak%C5%82ad-pracy-dla-jeszcze-nieutworzonych-element%C3%B3w)”. Wynika to z faktu, że „Szacunkowy nakład pracy” jest sumą „Szacunkowego” nakładu dla wszystkich utworzonych zadań i czynności (razem z czynnościami spraw podrzędnych), które składają się na sprawę, oraz wartości „Nakładu pracy dla elementów do utworzenia”.
  * Zwiększenie „Szacunkowego” nakładu pracy dla sprawy zwiększa „Nakład pracy dla elementów do utworzenia” o taką samą wartość.
  * Zmniejszenie „Szacunkowego” nakładu pracy dla sprawy zmniejsza „Nakład pracy dla elementów do utworzenia” o taką samą wartość.

### Analiza nakładu pracy dla utworzonych elementów

W sekcji „Analiza nakładu pracy dla utworzonych elementów” użytkownik może zmienić szacowany czas dla poszczególnych utworzonych czynności (i spraw podrzędnych) składających się na sprawę. Znajdziemy tu również inne przydatne wskaźniki dla każdej z utworzonych czynności (i spraw podrzędnych), które składają się na sprawę.

Gdy status czynności to „Rozwiązane” lub „Zamknięte”, jej szacunkowego nakładu pracy nie można już zmienić.

Szacunkowy nakład pracy dla tworzonych czynności będzie pobierany z „Szacunkowego” nakładu w sekcji „Elementów do utworzenia” poniżej.

### Analiza czynności

Dla każdej czynności użytkownik zobaczy:

* Odnośnik do każdej czynności.
* „Szacunkowy” nakład pracy wskazujący całkowity przewidywany czas, jaki zajmie czynność. Użytkownik może zastąpić tę wartość bardziej dokładnym oszacowaniem.
  * W polu tym początkowo wyświetlana będzie ręcznie ustalana wartość [Początkowy szacunkowy nakład pracy na wpis](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) z Buildera pomnożona przez [liczbę wpisów](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements).
    * Jeśli „Liczba wpisów” zostanie zaktualizowana, zmiana ta zostanie automatycznie odzwierciedlona w „Szacunkowym nakładzie pracy” dla każdej uruchomionej czynności, jeśli nie zrobi tego użytkownik Work Managera.
  * Zwiększenie tej wartości zmniejszy szacunkową wartość „Nakładu pracy dla elementów do utworzenia” i odwrotnie, co może wpłynąć na całkowity „Szacunkowy nakład pracy dla sprawy”.
  * Gdy status czynności to „Rozwiązane” lub „Zamknięte”, jej szacunkowego nakładu pracy nie można już zmienić.
* „Rzeczywisty" nakład pracy pokazuje ilość czasu poświęconego dotychczas na przetwarzanie czynności.
  * Wartość jest pobierana z modułu śledzenia czasu danej czynności.
* „Szacunkowy pozostały” to przewidywany czas, jaki pozostał do załatwienia czynności.
  * Oblicza się go poprzez odjęcie „Rzeczywistego” nakładu pracy dla czynności od nakładu „Szacunkowego”.
* Termin wykonania czynności.
  * Jeśli „Rzeczywisty” nakład aktualnie wynosi zero, zobaczymy tu wartość „Rozpocznij do”. Wskazuje ona najpóźniejszy moment na rozpoczęcie czynności, jeśli chcemy dotrzymać terminu.
* Status czynności.

Zmiana wartości „Szacunkowego” nakładu pracy dla czynności ma następujące skutki:

* Automatyczna aktualizacja wartości „Nakładu pracy dla elementów do utworzenia” dla danej sprawy.
* Możliwa automatyczna aktualizacja „Szacunkowego” nakładu pracy dla całej sprawy.

Szczegóły:

* Zmniejszenie „Szacunkowego” nakładu pracy dla czynności zwiększa „Nakład pracy dla elementów do utworzenia” dla sprawy o taką samą wartość (pozostawiając „Szacunkowy” nakład pracy dla całej sprawy bez zmian).
* Zwiększenie „Szacunkowego” nakładu pracy dla czynności zmniejsza „Nakład pracy dla elementów do utworzenia” dla sprawy o taką samą wartość. To może, ale nie musi, wpłynąć na „Szacunkowy” nakład pracy dla całej sprawy.
  * Jeśli zaktualizowany „Szacunkowy nakład pracy” czynności nie zwiększy się na tyle, aby wartość „Nakładu pracy dla elementów do utworzenia” dla sprawy spadła poniżej zera, wówczas „Szacunkowy” nakład pracy dla sprawy nie ulegnie zmianie.
    * Przykład: załóżmy, że „Szacunkowy” nakład pracy dla czynności nr 1 wynosi 2 godziny, szacowany „Nakład pracy dla elementów do utworzenia” to 1 godzina, a „Szacunkowy nakład pracy” dla sprawy – 3 godziny. Użytkownik postanawia, że czynność nr 1 zajmie godzinę dłużej i aktualizuje „Szacunkowy” nakład pracy dla tego elementu z 2 na 3 godziny. „Nakład pracy dla elementów do utworzenia” zmniejszy się z 1 godziny do zera, a „Szacunkowy” nakład pracy dla sprawy nie ulegnie zmianie – pozostanie na poziomie 3 godzin.
  * Jeśli zaktualizowany „Szacunkowy nakład pracy” czynności zwiększy się na tyle, aby wartość „Nakładu pracy dla elementów do utworzenia” dla sprawy spadła poniżej zera, wówczas różnicę należy dodać do „Szacunkowego nakładu pracy” dla całej sprawy.
    * Przykład: załóżmy, że dla sprawy utworzono tylko jedną czynność – to czynność nr 1. „Szacunkowy” nakład pracy dla czynności nr 1 wynosi 2 godziny, szacowany „Nakład pracy dla elementów do utworzenia” wynosi zero, a tym samym „Szacunkowy nakład pracy” dla całej sprawy to 2 godziny. Użytkownik postanawia, że czynność nr 1 zajmie godzinę dłużej i aktualizuje „Szacunkowy” nakład pracy dla tego elementu z 2 na 3 godziny. „Nakład pracy dla elementów do utworzenia” wynosi zero, zatem „Szacunkowy nakład pracy” dla całej sprawy zwiększy się o 1 godzinę – z 2 na 3 godziny.
    * Przykład 2: załóżmy, że dla sprawy utworzono tylko jedną czynność – to czynność nr 1. „Szacunkowy nakład pracy” dla czynności nr 1 wynosi 2 godziny, szacowany „Nakład pracy dla elementów do utworzenia” wynosi 1 godzinę, a tym samym „Szacunkowy nakład pracy” dla całej sprawy to 3 godziny. Użytkownik postanawia, że czynność nr 1 zajmie dodatkowe 2 godziny, więc aktualizuje „Szacunkowy” nakład pracy dla tego elementu z 2 do 4 godzin, powodując zmniejszenie „Nakładu pracy dla elementów do utworzenia” o 1 godzinę – z 1 do zera (czyli maksymalnie). „Pozostała” 1 godzina zostanie dodana do całkowitego „Szacunkowego” nakładu pracy dla sprawy, który wzrośnie o 1 godzinę – z 3 do 4 godzin.

### Analiza sprawy podrzędnej

Dla każdej utworzonej sprawy podrzędnej użytkownik zobaczy:

* Odnośnik do sprawy podrzędnej, jeśli ma uprawnienia do uzyskania do niej dostępu (w przeciwnym razie zobaczy tylko nazwę i numer referencyjny sprawy podrzędnej, bez odnośnika).
* Wiersz z podsumowaniem sprawy podrzędnej, w którym znajdą się następujące informacje:
  * „Szacunkowy” nakład pracy wskazuje całkowity przewidywany czas, jaki zajmie sprawa podrzędna. Użytkownik może zastąpić tę wartość bardziej dokładnym oszacowaniem.
    * Jest to suma „Szacunkowego” nakładu pracy dla wszystkich już utworzonych i przyszłych czynności, które składają się na sprawę podrzędną.
    * W polu tym początkowo wyświetlana będzie ręcznie ustalana wartość [Początkowy szacunkowy nakład pracy na wpis](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) z Buildera pomnożona przez [liczbę wpisów](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements).
      * Jeśli „Liczba wpisów” zostanie zaktualizowana, zmiana ta zostanie automatycznie odzwierciedlona w „Szacunkowym nakładzie pracy” dla sprawy podrzędnej, jeśli nie zrobi tego użytkownik Work Managera.
    * Gdy status sprawy podrzędnej to „Rozwiązane” lub „Zamknięte”, jej szacunkowego nakładu pracy nie można już zmienić.
    * Trzeba przy tym pamiętać, że zwiększenie tej wartości zwiększy też wartość „Nakładu pracy dla elementów do utworzenia” dla sprawy podrzędnej i odwrotnie.
  * „Rzeczywisty" nakład pracy pokazuje ilość czasu poświęconego dotychczas na przetwarzanie tej sprawy podrzędnej.
    * Jest to suma rzeczywistych nakładów pracy dla wszystkich utworzonych czynności, które składają się na sprawę podrzędna, zaczerpniętych z poszczególnych modułów śledzenia czasu.
  * „Szacunkowy pozostały” to przewidywany czas, jaki pozostał do załatwienia sprawy podrzędnej.
    * Jest to suma „Szacunkowego pozostałego” nakładu pracy dla wszystkich utworzonych czynności tworzących sprawę podrzędną ORAZ szacowanego pozostałego czasu pracy nad elementami, które dla tej sprawy podrzędnej nie zostały jeszcze utworzone (dlatego wartość to może być inna niż wynik odejmowania rzeczywistego nakładu pracy dla sprawy podrzędnej od nakładu szacowanego).
    * Termin wykonania sprawy podrzędnej.
    * Status sprawy podrzędnej.
* Wiersz dla każdej czynności sprawy podrzędnej, w którym znajdą się następujące informacje:
  * „Szacunkowy” nakład pracy wskazuje całkowity przewidywany czas, jaki zajmie czynność sprawy podrzędnej. Użytkownik może zastąpić tę wartość bardziej dokładnym oszacowaniem.
    * W polu tym początkowo wyświetlana będzie ręcznie ustalana wartość [Początkowy szacunkowy nakład pracy na wpis](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) z Buildera pomnożona przez [liczbę wpisów](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements).
      * Jeśli „Liczba wpisów” zostanie zaktualizowana, zmiana ta zostanie automatycznie odzwierciedlona w „Szacunkowym nakładzie pracy” dla każdej uruchomionej czynności sprawy podrzędnej, jeśli nie zrobi tego użytkownik Work Managera.
    * Zwiększenie tej wartości zmniejszy szacunkową wartość „Nakładu pracy dla elementów do utworzenia i odwrotnie, co może wpłynąć na całkowity „Szacunkowy nakład pracy dla sprawy”.
    * Gdy status czynności to „Rozwiązane” lub „Zamknięte”, jej szacunkowego nakładu pracy nie można już zmienić.
  * „Rzeczywisty" nakład pracy pokazuje ilość czasu poświęconego dotychczas na przetwarzanie czynności tej sprawy podrzędnej.
    * Wartość jest pobierana z modułu śledzenia czasu danej czynności sprawy podrzędnej.
  * „Szacunkowy pozostały” to przewidywany czas, jaki pozostał do załatwienia czynności sprawy podrzędnej.
    * Oblicza się go poprzez odjęcie „Rzeczywistego” nakładu pracy dla czynności sprawy podrzędnej od nakładu „Szacunkowego”.
  * Termin wykonania czynności sprawy podrzędnej.
    * Jeśli „Rzeczywisty” nakład aktualnie wynosi zero, zobaczymy tu wartość „Rozpocznij do”. Wskazuje ona najpóźniejszy moment na rozpoczęcie czynności sprawy podrzędnej, jeśli chcemy dotrzymać terminu.
  * Status czynności sprawy podrzędnej.
* Wiersz dla „Nakładu pracy dla elementów do utworzenia” sprawy podrzędnej, w którym znajdą się następujące informacje:
  * „Szacunkowy” nakład pokazuje, ile przewidywanej pracy trzeba będzie włożyć w zakończenie czynności sprawy podrzędnej, które nie zostały jeszcze dla niej utworzone. Użytkownik może zastąpić tę wartość bardziej dokładnym oszacowaniem.
    * Zmiana w zakresie tego oszacowania będzie miała wpływ na całkowity „Szacunkowy nakład pracy dla sprawy podrzędnej” i może rzutować na szacunkowy nakład pracy dla całej sprawy.

Zmiana wartości „Szacunkowego” nakładu pracy dla czynności sprawy podrzędnej ma następujące skutki:

* Automatyczna aktualizacja wartości „Nakładu pracy dla elementów do utworzenia” dla danej sprawy podrzędnej.
* Możliwa automatyczna aktualizacja „Szacunkowego” nakładu pracy dla całej sprawy podrzędnej.
* Możliwa automatyczna aktualizacja „Szacunkowego” nakładu pracy dla całej sprawy macierzystej.

Szczegóły:

* Zmniejszenie „Szacunkowego” nakładu pracy dla czynności sprawy podrzędnej zwiększa „Nakład pracy dla elementów do utworzenia” dla sprawy podrzędnej o taką samą wartość (pozostawiając „Szacunkowy” nakład pracy dla całej sprawy podrzędnej bez zmian, a tym samym nie wpływając na „Szacunkowy” nakład pracy dla całej sprawy macierzystej).
* Zwiększenie „Szacunkowego” nakładu pracy dla czynności sprawy podrzędnej zmniejsza „Nakład pracy dla elementów do utworzenia” dla sprawy podrzędnej o taką samą wartość. To może, ale nie musi, wpłynąć na „Szacunkowy” nakład pracy dla całej sprawy.
  * Jeśli zaktualizowany „Szacunkowy nakład pracy” czynności sprawy podrzędnej nie zwiększy się na tyle, aby wartość „Nakładu pracy dla elementów do utworzenia” dla sprawy podrzędnej spadła poniżej zera, wówczas „Szacunkowy” nakład pracy dla sprawy podrzędnej nie ulegnie zmianie (tym samym nie wpływając na „Szacunkowy” nakład pracy dla całej sprawy macierzystej).
    * Przykład: załóżmy, że dla sprawy podrzędnej utworzono tylko jedną czynność – to czynność sprawy podrzędnej nr 1. „Szacunkowy” nakład pracy dla czynności sprawy podrzędnej nr 1 wynosi 2 godziny, szacowany „Nakład pracy dla elementów do utworzenia” wynosi 1 godzinę, a tym samym „Szacunkowy nakład pracy” dla całej sprawy to 2 godziny. Użytkownik postanawia, że czynność nr 1 zajmie dodatkową godzinę, więc aktualizuje „Szacunkowy” nakład pracy dla tego elementu z 2 do 3 godzin, powodując zmniejszenie „Nakładu pracy dla elementów do utworzenia” z 1 godziny do zera. „Szacunkowy” nakład pracy dla sprawy podrzędnej nie ulegnie zmianie - pozostanie na poziomie 3 godzin (tym samym nie wpływając na „Szacunkowy” nakład pracy dla całej sprawy macierzystej).
  * Jeśli zaktualizowany „Szacunkowy nakład pracy” czynności sprawy podrzędnej zwiększy się na tyle, aby wartość „Nakładu pracy dla elementów do utworzenia” dla sprawy podrzędnej spadła poniżej zera, wówczas różnicę należy dodać do „Szacunkowego nakładu pracy” dla całej sprawy podrzędnej (co może mieć wpływ na „Szacunkowy” nakład pracy dla całej sprawy macierzystej).
    * Przykład: załóżmy, że dla sprawy podrzędnej utworzono tylko jedną czynność – to czynność sprawy podrzędnej nr 1. „Szacunkowy” nakład pracy dla czynności sprawy podrzędnej nr 1 wynosi 2 godziny, szacowany „Nakład pracy dla elementów do utworzenia” wynosi zero, a tym samym „Szacunkowy nakład pracy” dla całej sprawy podrzędnej to 2 godziny. Użytkownik postanawia, że czynność sprawy podrzędnej nr 1 zajmie godzinę dłużej i aktualizuje „Szacunkowy” nakład pracy dla tego elementu z 2 na 3 godziny. „Nakład pracy dla elementów do utworzenia” wynosi zero, zatem „Szacunkowy nakład pracy” dla sprawy podrzędnej zwiększy się o 1 godzinę – z 2 na 3 godziny.
      * Jeśli w „Nakładzie pracy dla elementów do utworzenia” sprawy macierzystej jest wystarczająco dużo czasu, tę dodatkową godzinę można pobrać z niego – wówczas „Szacunkowy” nakład pracy dla całej sprawy macierzystej nie ulegnie zmianie.
      * Jeśli w „Nakładzie pracy dla elementów do utworzenia” sprawy macierzystej nie ma wystarczająco dużo czasu, ta dodatkowa godzina zwiększy „Szacunkowy” nakład pracy dla całej sprawy macierzystej.
    * Przykład 2: załóżmy, że dla sprawy podrzędnej utworzono tylko jedną czynność – to czynność sprawy podrzędnej nr 1. „Szacunkowy” nakład pracy dla czynności sprawy podrzędnej nr 1 wynosi 2 godziny, szacowany „Nakład pracy dla elementów do utworzenia” wynosi 1 godzinę, a tym samym „Szacunkowy nakład pracy” dla całej sprawy to 3 godziny. Użytkownik postanawia, że czynność sprawy podrzędnej nr 1 zajmie 2 dodatkowe godziny, więc aktualizuje „Szacunkowy” nakład pracy dla tego elementu z 2 do 4 godzin, powodując zmniejszenie „Nakładu pracy dla elementów do utworzenia” z 1 godziny do zera (czyli maksymalnie). „Pozostała” 1 godzina zostanie dodana do całkowitego „Szacunkowego” nakładu pracy dla sprawy podrzędnej, który wzrośnie o 1 godzinę – z 3 do 4 godzin.
      * Jeśli w „Nakładzie pracy dla elementów do utworzenia” sprawy macierzystej jest wystarczająco dużo czasu, tę dodatkową godzinę można pobrać z niego – wówczas „Szacunkowy” nakład pracy dla całej sprawy macierzystej nie ulegnie zmianie.
      * Jeśli w „Nakładzie pracy dla elementów do utworzenia” sprawy macierzystej nie ma wystarczająco dużo czasu, ta dodatkowa godzina zwiększy „Szacunkowy” nakład pracy dla całej sprawy macierzystej.

### Nakład pracy dla elementów do utworzenia

„Nakład pracy dla elementów do utworzenia” pokazuje, ile przewidywanej pracy trzeba będzie włożyć w zakończenie czynności (i czynności sprawy podrzędnej), które nie zostały jeszcze utworzone dla tej sprawy.

Oblicza się go poprzez odjęcie sumy „Szacunkowego” nakładu pracy na utworzone elementy od „Szacunkowego” nakładu pracy dla sprawy. W związku z tym zwiększenie wartości „Nakładu pracy dla elementów do utworzenia” zwiększy oszacowany nakład dla całej sprawy i odwrotnie.

Szacunkowy nakład pracy dla tworzonych czynności (i spraw podrzędnych) będzie pobierany z szacunkowego „Nakładu pracy dla elementów do utworzenia”.

Gdy status sprawy to „Rozwiązane” lub „Zamknięte”, jej „Nakładu pracy dla elementów do utworzenia” nie można już zmienić.
