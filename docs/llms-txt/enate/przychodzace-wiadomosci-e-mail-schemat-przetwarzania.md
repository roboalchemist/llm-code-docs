# Source: https://docs.enate.net/enate-help/polski/e-maile/przychodzace-wiadomosci-e-mail-schemat-przetwarzania.md

# Przychodzące wiadomości e-mail – schemat przetwarzania

## **W jaki sposób Enate dopasowuje przychodzącą wiadomość e-mail?**

Gdy w Enate pojawiają się nowe wiadomości e-mail, system analizuje je, aby określić, czy zgłoszenie jest zupełnie nowe, czy też powiązane z już istniejącym, a następnie wybiera sposób dalszego postępowania.

System sprawdzi wiele różnych kryteriów w określonym porządku, a jeśli znajdzie pasujące, zatrzyma wyszukiwanie (czyli pierwsze wygrywa). Kolejność wykonywania tych czynności jest następująca:

**1)  Wartość „in-reply-to” nagłówka** – wartość „in reply to” nagłówka wiadomości e-mail. Wartość ta ma następującą strukturę:

<‘GUID wiadomości e-mail’.’GUID elementu pracy’@‘serwer Enate, z którego wysłano wiadomość e-mail’.enate>

e.g. \<d23a9d57-6006-4ab7-a412-8ca8ece2f3aa.2b8586bb-ef95-4020-9cf8- <ed56a059b47e@SendingServerName.enate>>

**2)  Unikalny identyfikator w treści wiadomości e-mail –** jeśli przychodząca wiadomość e-mail została wysłana jako odpowiedź na wiadomość e-mail wysłaną z Enate, najprawdopodobniej zawierać będzie znacznik unikalnego identyfikatora jako część treści.

**3)  Odniesienie do elementu pracy w temacie wiadomości e-mail**

**4)  Odniesienie do elementu pracy w treści wiadomości e-mail**&#x20;

## Przesyłanie przychodzącej wiadomości e-mail do istniejącego, aktywnego elementu pracy

Jeśli system znajdzie dopasowanie do już istniejącego elementu pracy (zapytania, sprawy lub czynności), którego status to WERSJA ROBOCZA, DO ZROBIENIA lub W TOKU, wykonane zostaną następujące działania:

* dołączenie wiadomości e-mail do elementu pracy;
* oznaczenie elementu pracy znacznikiem „otrzymano nowe informacje”.

To samo dotyczy automatycznie generowanych wiadomości e-mail, które zostały dopasowane do już istniejącego elementu pracy znajdującego się w stanie WERSJA ROBOCZA, DO ZROBIENIA lub W TOKU. Więcej informacji na temat tego, jak system wykrywa automatycznie wygenerowane wiadomości e-mail, można znaleźć [poniżej](#dalsze-szczegoly).

## Przesyłanie przychodzącej wiadomości e-mail do elementu pracy, którego status to „Oczekuje”

Jeśli przychodząca wiadomość e-mail zostanie dopasowana do istniejącego elementu pracy, którego status to OCZEKUJE, system wykona następujące działania:

* dołączenie wiadomości e-mail do elementu pracy;
* oznaczenie elementu pracy znacznikiem „otrzymano nowe informacje”.

Ponadto, jeśli typ oczekiwania to „Oczekiwanie na więcej informacji”, system wykona następujące działania:

* zmiana statusu elementu pracy z OCZEKUJE na DO ZROBIENIA;
* W wyniku zmiany statusu na DO ZROBIENIA element pracy zostanie przypisany do odpowiedniej kolejki i osoby oraz przeniesiony z powrotem do skrzynki odbiorczej Enate właściwego agenta z adnotacją „otrzymano nowe informacje”;
* jeśli elementem pracy jest czynność, a status zarówno czynności, jak i jej sprawy macierzystej to OCZEKUJE (a typ oczekiwania to „Oczekiwanie na więcej informacji”), wówczas stan sprawy macierzystej zmieni się na W TOKU.

To samo dotyczy automatycznie generowanych wiadomości e-mail, które zostały dopasowane do już istniejącego elementu pracy znajdującego się w stanie „Oczekuje” lub „Oczekiwanie na więcej informacji”. Więcej informacji na temat tego, jak system wykrywa automatycznie wygenerowane wiadomości e-mail, można znaleźć [poniżej](#dalsze-szczegoly).

## Przesyłanie przychodzącej wiadomości e-mail do rozwiązanego elementu pracy (sprawa i zapytanie)

Jeśli przychodząca wiadomość e-mail zostanie dopasowana do istniejącego elementu pracy, którego status to ROZWIĄZANE (należy pamiętać, że tylko sprawy i zapytania mogą mieć status ROZWIĄZANE), system wykona następujące działania:

* dołączenie wiadomości e-mail do elementu pracy;
* ponowne otworzenie elementu pracy i ustawienie jego statusu z powrotem na DO ZROBIENIA;
* w wyniku zmiany statusu na DO ZROBIENIA element pracy zostanie przypisany do odpowiedniej kolejki i osoby oraz przeniesiony z powrotem do skrzynki odbiorczej Enate właściwego agenta z adnotacją „otrzymano nowe informacje”.

To samo dotyczy automatycznie generowanych wiadomości e-mail, które zostały dopasowane do już istniejącego elementu pracy znajdującego się w stanie ROZWIĄZANE. Więcej informacji na temat tego, jak system wykrywa automatycznie wygenerowane wiadomości e-mail, można znaleźć [poniżej](#dalsze-szczegoly).

## Przesyłanie przychodzącej wiadomości e-mail do zamkniętego elementu pracy

Jeśli przychodząca wiadomość e-mail zostanie dopasowana do istniejącego elementu pracy, którego status to ZAMKNIĘTE, system wykona następujące działania w zależności od typu elementu pracy:

* Przejście w górę łańcucha elementów pracy w celu odnalezienia macierzystego elementu pracy, np.:
  * jeśli wiadomość e-mail została dopasowana do czynności, której status to ZAMKNIĘTE, system sprawdzi, czy sprawa macierzysta danej czynności jest wciąż otwarta;
  * jeśli wiadomość e-mail została dopasowana do sprawy, której status to ZAMKNIĘTE, system sprawdzi, czy dana sprawa posiada sprawę macierzystą albo zapytanie, które są wciąż otwarte;
  * jeśli wiadomość e-mail została dopasowana do zapytania, którego status to ZAMKNIĘTE, system sprawdzi, czy dane zapytanie posiada zapytanie macierzyste, które jest wciąż otwarte.
* Jeśli system znajdzie wciąż otwarty macierzysty element pracy, to zastosuje do niego resztę schematu przetwarzania wiadomości e-mail (tzn. cały schemat przedstawiony w powyższych punktach dotyczących aktywnych elementów roboczych).
* Jeśli system nie może znaleźć wciąż otwartego macierzystego elementu pracy, wówczas przychodząca wiadomość e-mail NIE zostanie dołączona do już zamkniętego elementu pracy. Zamiast tego zostanie utworzony nowy element pracy zgodnie z [poniższymi zasadami](#system-nie-moze-dopasowac-przychodzacej-wiadomosci-e-mail-do-juz-istniejacego-elementu-pracy) dotyczącymi postępowania, w przypadku gdy system nie może dopasować wiadomości e-mail do już istniejącego elementu pracy.

## System nie może dopasować przychodzącej wiadomości e-mail do już istniejącego elementu pracy

Jeśli nie można zidentyfikować żadnych informacji, które pozwoliłyby powiązać wiadomość e-mail z aktywnym elementem pracy, system wygeneruje zupełnie nowy element pracy (zapytanie lub sprawę) na podstawie ustawionych reguł przekazywania wiadomości e-mail. Na adres e-mail, z którego nadeszło zgłoszenie, zostanie automatycznie wysłana potwierdzająca wiadomość e-mail zawierająca numer referencyjny, jeśli w ustawieniach przekierowania poczty elektronicznej w Builderze opcja „wyślij odpowiedź” jest włączona.

## Dalsze szczegóły

* **Rozdzielone zapytanie** – jeśli przychodząca wiadomość e-mail zostanie dopasowana do rozdzielonego zapytania – albo do oryginalnego zapytania, które zostało rozdzielone, albo do jednego z zapytań podrzędnych, na które rozdzielono oryginalne zapytanie – wówczas zostanie też dołączona do każdego z zapytań PODRZĘDNYCH. Następnie system zastosuje resztę schematu przetwarzania wiadomości e-mail niezależnie do każdego zapytania podrzędnego.
* **Połączone zapytanie –** jeśli przychodząca wiadomość e-mail zostanie dopasowana do połączonego zapytania – albo jednego z oryginalnych zapytań, które zostały połączone, albo zapytania „docelowego”, które powstało po połączeniu oryginalnych – wówczas zostanie dołączona do zapytania „docelowego”. Następnie system zastosuje resztę schematu przetwarzania wiadomości e-mail do zapytania „docelowego”.
* **Zapytanie przekształcone w sprawę –** jeśli przychodząca wiadomość e-mail zostanie dopasowana do zapytania, które zostało rozwiązane poprzez przekształcenie w sprawę, wówczas zostanie dołączona do sprawy. Następnie system zastosuje resztę schematu przetwarzania wiadomości e-mail do sprawy.

## Schemat wykrywania automatycznie generowanych wiadomości e-mail

System wykrywa automatycznie generowane wiadomości e-mail na podstawie jednej lub więcej z poniższych informacji:

* nagłówek « x-autoreply » istnieje;
* nagłówek « x-autorespond» istnieje;
* nagłówek « auto-submitted » istnieje, a jego wartość to « auto-generated » albo « auto-replied »;&#x20;
* nagłówek « content-type » istnieje, a jego wartość to « multipart/report » albo « delivery-status »;&#x20;
* nagłówek « return-path » istnieje, a jego wartość to « <> » albo « <<>> ».
