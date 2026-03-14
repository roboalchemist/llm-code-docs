# Source: https://docs.enate.net/enate-help/polski/dodatek/systemowa-metoda-ustalania-osoby-przypisanej-wlasciciela-oraz-kolejki-danego-elementu-pracy.md

# Systemowa metoda ustalania osoby przypisanej, właściciela oraz kolejki danego elementu pracy

W ramach zarządzania zapytaniami, sprawami i czynnościami w Enate system będzie regularnie dokonywał ewaluacji, do kogo praca jest przypisana, z którą kolejką jest połączona i kto jest ustawiony jako właściciel. Informacje te są ustalane według szczegółowych zbiorów reguł i w odpowiednim porządku.

Ważne, by najpierw zrozumieć nadrzędny wzorzec decydujący o tym, jak i kiedy te przydziały są określane. Sposób działania jest następujący:

1. [Najpierw należy określić, KIEDY ma dojść do ponownej ewaluacji](#okreslenie-kiedy-ma-dojsc-do-ponownej-ewaluacji) - zasadniczo chodzi o wszelkie zmiany na karcie „Status” elementu pracy.
2. Gdy system wykryje, że konieczna jest ewaluacja, należy zacząć od określenia na podstawie statusu lub sytuacji elementu pracy, [które wartości (osoba przypisana, właściciel, kolejka) trzeba ustawić](#okreslenie-czy-wartosci-osoby-przypisanej-wlasciciela-lub-kolejki-maja-byc-ustawione-czy-wyczyszczon), a które całkowicie wyczyścić.
3. [Jeśli wymagane jest ustawienie:](#ustawianie-osoby-przypisanej-wlasciciela-lub-kolejki)

   a) w przypadku kolejki sprawa jest prosta – należy wybrać kolejkę, do której odwołuje się reguła przydziału (są tylko dwa typu reguł przydziału kolejki, które trzeba mieć na uwadze);

   b) w kwestii osoby przypisanej i właściciela kroków jest więcej – trzeba przejść przez szereg reguł w odpowiedniej kolejności, zatrzymując się w momencie, gdy któraś z nich została spełniona i wybrana jest poprawna\* wartość docelowa.

\*[Kontrola poprawności](#kontrola-poprawnosci) – w ramach testu reguły przydziału osoby przypisanej albo właściciela trzeba określić, czy wartość docelowa jest poprawna (musi pomyślnie przejść szereg testów kontroli poprawności). Jeśli nie jest, sprawdzanie reguł jest kontynuowane aż do chwili znalezienia poprawnej wartości docelowej.

Tak wygląda nadrzędny wzorzec, można zatem przyjrzeć się każdemu zbiorowi reguł stosowanych w powyższych punktach oraz kontroli poprawności wartości docelowych.

## Określenie, KIEDY ma dojść do ponownej ewaluacji

System sprawdzi osobę przypisaną, właściciela i kolejki za każdym razem, gdy zmienią się informacje na karcie „Status”. Chodzi przede wszystkim o:

* zmiany statusu;
* zmiany typu oczekiwania;
* zmiany daty zaplanowanego wznowienia;
* zmiany daty „Oczekuje na więcej informacji do”;
* zmiany opcji „Oczekuje na” (tylko dla spraw);
* zmiany kontekstu zapytania;
* zmiany kategorii zapytania;
* zmiany statusu „W trakcie wzajemnej oceny”;
* otrzymanie nowych informacji dotyczących danego elementu pracy;
* ewentualne problemy ze sprawą.

## Określenie, czy wartości osoby przypisanej, właściciela lub kolejki mają być ustawione, czy wyczyszczone

Po wykryciu, że należy dokonać ewaluacji, system wykorzysta status elementu pracy do określenia, które wartości (osoba przypisana, właściciel, kolejka) należy ustawić, a które całkowicie wyczyścić. Przedstawia to poniższa tabela:

| <p><strong>Status / sytuacja elementu pracy</strong></p><p> </p>  | <p><strong>Osoba przypisana</strong></p><p> </p> | <p><strong>Właściciel</strong></p><p> </p> | <p><strong>Kolejka</strong></p><p> </p> |
| ----------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------ | --------------------------------------- |
| <p>Zamknięte</p><p> </p>                                          | <p>Wyczyść wartość</p><p> </p>                   | <p>Wyczyść wartość</p><p> </p>             | <p>Wyczyść wartość</p><p> </p>          |
| <p>Wersja robocza</p><p> </p>                                     | <p>Ustaw wartość</p><p> </p>                     | <p>Wyczyść wartość</p><p> </p>             | <p>Wyczyść wartość</p><p> </p>          |
| <p>Otrzymano nowe informacje</p><p> </p>                          | <p>Ustaw wartość</p><p> </p>                     | <p>Wyczyść wartość</p><p> </p>             | <p>Ustaw wartość</p><p> </p>            |
| <p>Wymaga uwagi (tylko dla spraw)</p><p> </p>                     | <p>Ustaw wartość</p><p> </p>                     | <p>Wyczyść wartość</p><p> </p>             | <p>Ustaw wartość</p><p> </p>            |
| <p>Do zrobienia albo W toku (dla czynności i zapytań)</p><p> </p> | <p>Ustaw wartość</p><p> </p>                     | <p>Wyczyść wartość</p><p> </p>             | <p>Ustaw wartość</p><p> </p>            |
| <p>Do zrobienia albo W toku (dla spraw)</p><p> </p>               | <p>Wyczyść wartość</p><p> </p>                   | <p>Ustaw wartość</p><p> </p>               | <p>Wyczyść wartość</p><p> </p>          |
| <p>Rozwiązane albo Oczekuje</p><p> </p>                           | <p>Wyczyść wartość</p><p> </p>                   | <p>Ustaw wartość</p><p> </p>               | <p>Wyczyść wartość</p><p> </p>          |

## Ustawianie osoby przypisanej, właściciela lub kolejki

* **Kolejki** – jeśli trzeba ustawić kolejkę, sprawa jest prosta – uruchamiana jest uprzednio skonfigurowana [metoda przydziału kolejki](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method).
* **Osoba przypisana i właściciel** – jeśli trzeba ustawić osobę przypisaną i właściciela, kroków jest więcej. Trzeba przejść przez szereg reguł w odpowiedniej kolejności, zatrzymując się w momencie, gdy któraś z nich została spełniona i wybrana jest [poprawna wartość docelowa](#kontrola-poprawnosci).

Test do wykonania w pierwszej kolejności: jeśli osoba przypisana lub właściciel jest już ustawiony, **niczego w tym zakresie nie zmieniamy, chyba że zmianie ulegnie kategoria zapytania**.

W przeciwnym razie należy przejść przez poniższe reguły w podanej kolejności, zatrzymując się w momencie, gdy znajdzie się poprawna wartość docelowa:

1. Jeśli dany element pracy ma włączoną opcję „Zatrzymaj przy mnie”, jako osoba przypisana lub właściciel zostanie ustawiony ten użytkownik, który ją wybrał. Jeśli jest inaczej albo docelowy użytkownik nie jest odpowiedni, wtedy:
2. Jeśli ustawiony jest właściciel, należy tę samą wartość wybrać dla osoby przypisanej. Jeśli jest inaczej albo docelowy użytkownik nie jest odpowiedni, wtedy:
3. Jeśli element pracy nie jest zapytaniem ALBO jest zapytaniem (a kategoria zapytania się nie zmieniła I są więcej niż dwa wiersze historii statusów, czyli to nie jest pierwszy status inny niż wersja robocza), wtedy:
   1. Jako osobę przypisaną i właściciela należy ustawić ostatniego użytkownika lub robota, który zaktualizował dany element pracy. Jeśli takiego nie ma albo docelowy użytkownik nie jest odpowiedni, wtedy:
   2. Jako osobę przypisaną i właściciela należy ustawić dowolnego wcześniej przypisanego użytkownika lub robota (w kolejności malejącej od daty tego przypisania). Jeśli takiego nie ma albo docelowy użytkownik nie jest odpowiedni, wtedy:
   3. Jeśli czynność została uruchomiona w ramach przepływu pracy (czyli nie ręcznie i doraźnie), jako osobę przypisaną i właściciela należy ustawić ostatniego użytkownika lub robota, który pracował nad tą samą poprzednio zakończoną czynnością danej sprawy (albo dokonywał wzajemnej oceny czynności, jeśli chodzi o ten etap). Jeśli takiego nie ma albo docelowy użytkownik nie jest odpowiedni, wtedy:
4. Należy uruchomić [regułę przydziału](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) dla tego elementu pracy:
   1. Jeśli główny przydział automatyczny jest ustawiony na konkretnego użytkownika, jako osobę przypisaną i właściciela należy wybrać właśnie jego. Jeśli takiego nie ma albo docelowy użytkownik nie jest odpowiedni, wtedy:
   2. Jeśli poboczny przydział automatyczny jest ustawiony na konkretnego użytkownika, jako osobę przypisaną i właściciela należy wybrać właśnie jego. Jeśli takiego nie ma albo docelowy użytkownik nie jest odpowiedni, wtedy:
   3. Jeśli główny przydział automatyczny jest ustawiony na pozycję, jako osobę przypisaną i właściciela należy wybrać tego z użytkowników zajmujących daną pozycję, który ma w swojej skrzynce odbiorczej ma najmniej elementów pracy. Jeśli takiego nie ma albo docelowy użytkownik nie jest odpowiedni, wtedy:
   4. Jeśli poboczny przydział automatyczny jest ustawiony na pozycję, jako osobę przypisaną i właściciela należy wybrać tego z użytkowników zajmujących daną pozycję, który ma w swojej skrzynce odbiorczej ma najmniej elementów pracy. Jeśli takiego nie ma albo docelowy użytkownik nie jest odpowiedni, wtedy:
5. Jeśli element pracy jest sprawą, jako osobę przypisaną i właściciela należy wybrać użytkownika lub robota, który uruchomił tę sprawę.

## Kontrola poprawności

W ramach testu reguły przydziału osoby przypisanej albo właściciela trzeba określić, czy wartość docelowa jest poprawna (czyli musi pomyślnie przejść szereg testów kontroli poprawności). Jeśli nie jest, sprawdzanie reguł jest kontynuowane aż do chwili znalezienia poprawnej wartości docelowej. Testy poprawności są następujące:

* Jeśli użytkownik lub robot nie może zajmować się elementami pracy danego typu (czyli aktywnymi / testowanymi) – zablokuj;
* Jeśli użytkownik lub robot jest wycofany – zablokuj;
* Jeśli użytkownik nie posiada uprawnień – zablokuj (testy uprawnień nie dotyczą robotów);
* Jeśli robot jest zawieszony – zablokuj;
* Jeśli robot aktywował dla danego elementu pracy funkcję „Zdobądź więcej pracy” więcej niż trzy razy – zablokuj;
* Jeśli wybrany użytkownik jest robotem, a element pracy to czynność na etapie wzajemnej oceny – zablokuj (roboty nie mogą dokonywać wzajemnej oceny);
* Jeśli wybrany użytkownik jest robotem, element pracy to czynność, a żadna sieć robotów nie została skonfigurowana dla czynności – zablokuj;
* Jeśli wybrany użytkownik jest robotem, element pracy to czynność, a robot nie należy do sieci robotów skonfigurowanej dla czynności – zablokuj;
* Jeśli wybrany użytkownik jest robotem, a element pracy to sprawa – zablokuj (roboty nie mogą być przypisane do spraw);
* Jeśli element pracy to ręcznie uruchomiona czynność z wzajemną oceną, która znajduje się na etapie wzajemnej oceny, a użytkownik dokonał jednej lub więcej aktualizacji, gdy znajdowała się na etapie przetwarzania – zablokuj (użytkownicy nie mogą dokonywać wzajemnej oceny własnej pracy);
* Jeśli element pracy to ręcznie uruchomiona czynność z wzajemną oceną, która znajduje się na etapie przetwarzania, a użytkownik dokonał jednej lub więcej aktualizacji, gdy znajdowała się na etapie wzajemnej oceny – zablokuj (użytkownicy nie mogą mieć zlecanej pracy, którą wcześniej oceniali).
