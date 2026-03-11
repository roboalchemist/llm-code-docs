# Source: https://docs.enate.net/enate-help/polski/e-maile/przychodzace-wiadomosci-e-mail-schemat-przetwarzania/postepowanie-z-przychodzacymi-wiadomosciami-ooo-out-of-office.md

# Postępowanie z przychodzącymi wiadomościami OOO (Out of Office)

## W jaki sposób Enate radzi sobie z e-mailami OOO?

Wiadomości o nieobecności (OOO) są przez Enate przetwarzane na dwa sposoby:

1. Jeśli wiadomość OOO jest generowana w odpowiedzi na e-mail wysłany przez użytkownika w Enate, system dołączy ją do elementu pracy z adnotacją „otrzymano nowe informacje”. Więcej szczegółów poniżej.
2. Jeśli wiadomość OOO jest wysyłana w odpowiedzi na automatycznie wygenerowaną wiadomość z Enate (np. potwierdzenie utworzenia zapytania), wówczas NIE zostanie dołączona do elementu pracy i nie otrzyma on adnotacji „otrzymano nowe informacje” – innymi słowy wiadomość taka zostanie zignorowana.

Więcej na temat sytuacji nr 1, gdy e-mail OOO jest generowany w odpowiedzi na wiadomość wysłaną przez użytkownika w Enate…

## Przychodzące wiadomości OOO dopasowane do istniejącego i aktywnego elementu pracy

Jeśli przychodząca wiadomość OOO zostanie dopasowana do już istniejącego elementu pracy (zapytania, sprawy lub czynności), którego status to WERSJA ROBOCZA, DO ZROBIENIA lub W TOKU, system podejmie następujące działania:

* dołączenie wiadomości e-mail do elementu pracy;
* oznaczenie elementu pracy znacznikiem „otrzymano nowe informacje”.

Uwaga: Powyższy schemat działania ma zastosowanie do wszystkich automatycznie wygenerowanych wiadomości przychodzących, które zostaną dopasowane do istniejącego elementu pracy mającego status WERSJA ROBOCZA, DO ZROBIENIA lub W TOKU (to oznacza, że przychodzące wiadomości OOO są traktowane dokładnie tak samo jak inne przychodzące wiadomości generowane automatycznie dla elementów o takim statusie). Więcej informacji na temat tego, jak system wykrywa automatycznie wygenerowane wiadomości e-mail, można znaleźć [w tej sekcji](https://docs.enate.net/enate-help/polski/e-maile/przychodzace-wiadomosci-e-mail-schemat-przetwarzania/..#schemat-wykrywania-automatycznie-generowanych-wiadomosci-e-mail).

## Przychodzące wiadomości OOO dopasowane do elementu pracy, którego status to OCZEKUJE

Jeśli przychodząca wiadomość e-mail zostanie dopasowana do istniejącego elementu pracy, którego status to OCZEKUJE, system wykona następujące działania:

* dołączenie wiadomości e-mail do elementu pracy;
* oznaczenie elementu pracy znacznikiem „otrzymano nowe informacje”.

Ponadto, jeśli typ oczekiwania to „Oczekiwanie na więcej informacji”, system wykona następujące działania:

* zmiana statusu elementu pracy z OCZEKUJE na DO ZROBIENIA;
* w wyniku zmiany statusu na DO ZROBIENIA element pracy zostanie przypisany do odpowiedniej kolejki i osoby oraz przeniesiony z powrotem do skrzynki odbiorczej Enate właściwego agenta z adnotacją „otrzymano nowe informacje”;
* jeśli elementem pracy jest czynność, a status zarówno czynności, jak i jej sprawy macierzystej to OCZEKUJE (a typ oczekiwania to „Oczekiwanie na więcej informacji”), wówczas stan sprawy macierzystej zmieni się na W TOKU.

Powyższy schemat działania ma zastosowanie do wszystkich automatycznie wygenerowanych wiadomości przychodzących, które zostaną dopasowane do istniejącego elementu pracy mającego status OCZEKUJE lub „Oczekiwanie na więcej informacji” (to oznacza, że przychodzące wiadomości OOO są traktowane dokładnie tak samo jak inne przychodzące wiadomości generowane automatycznie dla elementów o takim statusie). Więcej informacji na temat tego, jak system wykrywa automatycznie wygenerowane wiadomości e-mail, można znaleźć [w tej sekcji](https://docs.enate.net/enate-help/polski/e-maile/przychodzace-wiadomosci-e-mail-schemat-przetwarzania/..#schemat-wykrywania-automatycznie-generowanych-wiadomosci-e-mail).

## Przychodzące wiadomości OOO dopasowane do rozwiązanego elementu pracy (sprawa i zapytanie)

Jeśli przychodząca wiadomość e-mail zostanie dopasowana do istniejącego elementu pracy, którego status to ROZWIĄZANE (należy pamiętać, że tylko sprawy i zapytania mogą mieć taki status), system wykona następujące działania:

* dołączenie wiadomości e-mail do elementu pracy;
* ponowne otworzenie elementu pracy i ustawienie jego statusu z powrotem na DO ZROBIENIA;
* W wyniku zmiany statusu na DO ZROBIENIA element pracy zostanie przypisany do odpowiedniej kolejki i osoby oraz przeniesiony z powrotem do skrzynki odbiorczej Enate właściwego agenta z adnotacją „otrzymano nowe informacje”.

Powyższy schemat działania ma zastosowanie do wszystkich automatycznie wygenerowanych wiadomości przychodzących, które zostaną dopasowane do istniejącego elementu pracy mającego status ROZWIĄZANE (to oznacza, że przychodzące wiadomości OOO są traktowane dokładnie tak samo jak inne przychodzące wiadomości generowane automatycznie dla elementów o takim statusie). Więcej informacji na temat tego, jak system wykrywa automatycznie wygenerowane wiadomości e-mail, można znaleźć [w tej sekcji](https://docs.enate.net/enate-help/polski/e-maile/przychodzace-wiadomosci-e-mail-schemat-przetwarzania/..#schemat-wykrywania-automatycznie-generowanych-wiadomosci-e-mail).

## Przychodzące wiadomości OOO dopasowane do zamkniętego elementu pracy

Jeśli przychodząca wiadomość e-mail zostanie dopasowana do istniejącego elementu pracy, którego status to ZAMKNIĘTE, system wykona następujące działania w zależności od typu elementu pracy:

* Przejście w górę łańcucha elementów pracy w celu odnalezienia elementu macierzystego, np.:
  * jeśli wiadomość e-mail została dopasowana do czynności, której status to ZAMKNIĘTE, system sprawdzi, czy sprawa macierzysta danej czynności jest wciąż otwarta;
  * jeśli wiadomość e-mail została dopasowana do sprawy, której status to ZAMKNIĘTE, system sprawdzi, czy posiada ona sprawę macierzystą, która jest wciąż otwarta.
  * jeśli wiadomość e-mail została dopasowana do zapytania, którego status to ZAMKNIĘTE, system sprawdzi, czy posiada ono zapytanie macierzyste, które jest wciąż otwarte.
* Jeśli system znajdzie wciąż otwarty macierzysty element pracy, to zastosuje do niego resztę schematu przetwarzania wiadomości e-mail (tzn. cały schemat przedstawiony w powyższych punktach dotyczących aktywnych elementów pracy).
* Jeśli system nie może znaleźć wciąż otwartego macierzystego elementu pracy, wówczas przychodząca wiadomość e-mail NIE zostanie dołączona do już zamkniętego elementu pracy. Zamiast tego zostanie utworzony nowy element pracy zgodnie z [poniższymi zasadami](#system-nie-moze-dopasowac-przychodzacej-wiadomosci-ooo-do-juz-istniejacego-elementu-pracy) dotyczącymi postępowania w przypadku, gdy system nie może dopasować wiadomości e-mail do już istniejącego elementu pracy.

Ten sam schemat działania ma zastosowanie do wszystkich automatycznie wygenerowanych wiadomości przychodzących, które zostaną dopasowane do istniejącego elementu pracy mającego status ZAMKNIĘTE (to oznacza, że przychodzące wiadomości OOO są traktowane dokładnie tak samo jak inne przychodzące wiadomości generowane automatycznie dla elementów o takim statusie). Więcej informacji na temat tego, jak system wykrywa automatycznie wygenerowane wiadomości e-mail, można znaleźć [w tej sekcji](https://docs.enate.net/enate-help/polski/e-maile/przychodzace-wiadomosci-e-mail-schemat-przetwarzania/..#schemat-wykrywania-automatycznie-generowanych-wiadomosci-e-mail).

## System nie może dopasować przychodzącej wiadomości OOO do już istniejącego elementu pracy

Jeśli nie można zidentyfikować żadnych informacji, które pozwoliłyby powiązać wiadomość OOO z aktywnym elementem pracy, system wygeneruje zupełnie nowy element (zapytanie lub sprawę) na podstawie ustawionych reguł przekierowania wiadomości e-mail.

Gdy utworzonym elementem będzie zapytanie, to pomimo aktywnej opcji „Wyślij odpowiedź” w ustawieniach przekierowania w Builderze, system NIE wyśle automatycznego potwierdzenia na adres e-mail, z którego nadeszła wiadomość OOF, ponieważ w takiej sytuacji automatycznie włączona zostanie funkcja „Wyłącz automatyczne wiadomości e-mail”.
