# Source: https://docs.enate.net/enate-help/polski/lacznosc/dodawanie-edytowanie-i-usuwanie-kontaktow.md

# Dodawanie, edytowanie i usuwanie kontaktów

## Dodawanie kontaktów

Kontakty zewnętrzne są tworzone w Enate na kilka różnych sposobów:

### 1)  Automatycznie z przychodzącej wiadomości e-mail

System Enate można skonfigurować w taki sposób, by automatycznie tworzył nowe kontakty zewnętrzne po nadejściu wiadomości e-mail zawierającej nowe adresy e-mail – w tym celu należy aktywować w Builderze funkcję [„Włącz automatyczne tworzenie kontaktów”](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).

System automatycznie wstawi imię i nazwisko kontaktu na podstawie nazwy wyświetlanej w wiadomości e-mail. Dodatkowe informacje:

* Jeśli w nazwie wyświetlanej w wiadomości e-mail znajduje się spacja, wówczas wszystko, co znajduje się przed pierwszą spacją, zostanie użyte jako imię kontaktu, a to, co znajduje się po ostatniej spacji – jako jego nazwisko. Przykład: jeśli nazwa wyświetlana w wiadomości e-mail to „John Smith”, to imię kontaktu zostanie automatycznie wypełnione jako „John”, a nazwisko jako „Smith”.
* Jeśli w nazwie wyświetlanej w wiadomości e-mail znajduje się przecinek, wówczas wszystko, co znajduje się przed pierwszym przecinkiem, zostanie użyte jako nazwisko kontaktu, a to, co znajduje się po przecinku – jako jego imię. Przykład: jeśli nazwa wyświetlana w wiadomości e-mail to „Smith, John”, to nazwisko kontaktu zostanie automatycznie wypełnione jako „Smith”, a imię jako „John”.
* Jeśli system nie jest w stanie automatycznie wypełnić imienia i nazwiska, kontakt zostanie utworzony bez nich, a użytkownik zostanie poproszony o samodzielne dopisanie tych danych podczas przesyłania elementu pracy.

To, [jaka firma zostanie](#nazwa-firmy-okreslanie-zakresu-kontaktow-zewnetrznych) przypisana do automatycznie tworzonego kontaktu, zależy od ustawionego w [Builderze zakresu kontaktu](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation). Jeśli jest on ustawiony na „Globalny” lub „Globalny i lokalny”, nowemu kontaktowi zostanie przypisany zakres globalny, tzn. nie będzie on powiązany z żadną konkretną firmą. Jeśli zaś zakres ustawiony jest na „Lokalny”, kontakt będzie podpięty do firmy, z którą połączony jest powiązany element pracy.

### 2)  Dodawanie pojedynczego kontaktu na stronie zarządzanie kontaktami

Aby dodać kontakt na [stronie „Zarządzanie kontaktami”](https://docs.enate.net/enate-help/polski/lacznosc/strona-zarzadzania-kontaktami), należy kliknąć ikonę „Utwórz kontakt” i uzupełnić dane w okienku, które zostanie wtedy wyświetlone.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2Fm669BBnVJmOsqjuadw5b%2F7A%20Adding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=ef4936b7-f2e7-4601-bbf6-30057ddeb065" alt=""><figcaption></figcaption></figure>

### 3) Importowanie kontaktów z szablonu Excel na stronę zarządzania kontaktami

Można także zaimportować listę kontaktów na [stronę zarządzania kontaktami](https://docs.enate.net/enate-help/polski/lacznosc/strona-zarzadzania-kontaktami) z arkusza kalkulacyjnego Excel. Służy do tego szablon, dostępny we wszystkich językach obsługiwanych przez Enate.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FkQSYq1TYpT4ctc3onmFC%2F7A%20Bulk-Adding-Contacts.gif?alt=media&#x26;token=f08887e9-37e0-4fde-b848-851275783506" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
W przypadku importowania kontaktów z szablonu programu Excel należy obowiązkowo wpisać adres e-mail. Jeśli użytkownik nie określi firmy, kontakt zostanie automatycznie ustawiony jako globalny. [Więcej informacji na temat określania zakresu firm można znaleźć tutaj](#nazwa-firmy-okreslanie-zakresu-kontaktow-zewnetrznych).
{% endhint %}

### 4) Dodawanie kontaktu z szybkiego wyszukiwania

Jeśli wyszukiwany kontakt nie istnieje jeszcze w bazie danych systemu, można go utworzyć z [poziomu samej wyszukiwarki](https://docs.enate.net/enate-help/polski/szybkie-wyszukiwanie). W tym celu należy przejść do funkcji wyszukiwania osób i kliknąć „Dodaj kontakt”.

W tym momencie system odczyta i wstawi w odpowiednie pola imię, nazwisko i adres e-mail kontaktu. Po uzupełnieniu wszystkich informacji i utworzeniu kontaktu, użytkownik zostanie przeniesiony na [stronę „Aktywność kontaktu”](https://docs.enate.net/enate-help/polski/lacznosc/strona-aktywnosc-kontaktowa).

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXb0zH-DMnI1hDDpqYh%2F-MXbLFVyVHS1XoH7OEUQ%2FAdd-External-Contact-from-Quickf.gif?alt=media\&token=670bf5e6-48a3-4e3f-89d5-69d370bc529c)

{% hint style="info" %}
Uwaga: Wprowadzany adres e-mail nie może być już obecny w systemie.
{% endhint %}

### 5) Dodawanie kontaktu z karty kontaktu danego elementu pracy.

Można również utworzyć nowy [kontakt z](https://docs.enate.net/enate-help/polski/lacznosc/karta-kontaktowa) karty kontaktów elementu pracy. Jeśli wyszukanie na karcie kontaktów nie przyniosło rezultatów, ponieważ użytkownika nie ma jeszcze w systemie, opcja „Utwórz kontakt” umożliwia dodanie go do bazy i uzupełnienie jego danych.

Po wpisaniu adresu e-mail system odczyta i wstawi w odpowiednie pola imię i nazwisko kontaktu. Po dodaniu wszystkich informacji i kliknięciu przycisku „Utwórz kontakt” nastąpi przekierowanie z powrotem do elementu pracy.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FUy5LukmkNnFCwluXa8Wm%2F7A-Create-Contact-from-Work-Item.gif?alt=media&#x26;token=64cc9883-31b1-4de6-b557-28c56599e89a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Należy pamiętać, że w przypadku utworzenia nowego kontaktu w trybie testowym, kontakt ten będzie można wykorzystać w systemie tylko do uruchamiania pakietów testowych.
{% endhint %}

## Automatyczne i ręczne tworzenie kontaktów

Znajdująca się na [stronie zarządzania kontaktami](https://docs.enate.net/enate-help/polski/lacznosc/strona-zarzadzania-kontaktami) kolumna „Utworzone automatycznie” wskazuje, czy dany kontakt zewnętrzny został dodany automatycznie przez system, czy ręcznie przez użytkownika.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F2BAFKrBXyjloUPhnAmMC%2Fimage.png?alt=media&#x26;token=6c343edb-2e82-4a82-9daa-3133c132d65f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Należy pamiętać, że po dokonaniu edycji kontaktu, który został utworzony automatycznie, nie będzie on już wyświetlany jako taki w kolumnie „Utworzone automatycznie” na stronie „Zarządzanie kontaktami”.
{% endhint %}

## Nazwa firmy - Określanie zakresu kontaktów zewnętrznych

W zależności od tego, jak zostało to skonfigurowane w Builderze, podczas przypisywania firmy do kontaktu zewnętrznego dostępne będą różne opcje:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FEZzcqWQUfoSM3vbPv9qK%2F7-Company-Scope.gif?alt=media\&token=7ce7ebed-f55c-467b-8632-535d9b08b4b4)

* Wszystkie firmy/Globalnie
  * Ustawienie firmy w ten sposób oznacza, że kontakt zewnętrzny może tworzyć elementy pracy i uzyskiwać do nich dostęp dla wszystkich firm.
  * Oznacza to również, że użytkownicy Work Managera mogą wyszukiwać wszystkie inne zewnętrzne kontakty danego elementu pracy.

{% hint style="info" %}
Należy pamiętać, że to ustawienie jest dostępne tylko wtedy, gdy zakres kontaktu zewnętrznego został ustawiony na „Globalny” lub „Globalny i lokalny” w narzędziu Builder. Zobacz [tutaj](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#external-contact-scoping), aby uzyskać więcej informacji.
{% endhint %}

* Konkretna firma (lokalna)
  * Ustawienie zakresu kontaktów na określoną firmę oznacza, że kontakt zewnętrzny będzie mógł tworzyć elementy pracy i uzyskiwać do nich dostęp tylko dla tej konkretnej firmy, z którą został powiązany.
  * Użytkownicy będą również mogli dodać kontakt do interfejsu API pakietu tylko wtedy, gdy kontakt znajduje się w tej samej firmie (lub w firmie parasolowej).

{% hint style="info" %}
Uwaga:

1. Zmiana firmy powiązanej z kontaktem zewnętrznym z „Wszystkie firmy/Globalne” na konkretną firmę (lokalną) jest możliwa tylko wtedy, gdy kontakt ten nie jest powiązany z elementami pracy z wielu różnych firm. Można to zmienić poprzez zmianę przypisania kontaktu do elementu pracy.
2. Aby ograniczyć zakres kontaktów zewnętrznych do „Wszystkie firmy/Globalne”, kolumna „Firma” w pliku przesyłania zbiorczego powinna być pusta – dzięki temu zakres zostanie domyślnie ustawiony na „Globalny”.
3. To, jaka firma zostanie przypisana do automatycznie tworzonego kontaktu, zależy od ustawionego w Builderze zakresu kontaktu. Jeśli jest on ustawiony na „Globalny” lub „Globalny i lokalny”, nowemu kontaktowi zostanie przypisany zakres globalny, tzn. nie będzie on powiązany z żadną konkretną firmą. Jeśli zaś zakres ustawiony jest na „Lokalny”, kontakt będzie podpięty do firmy, z którą połączony jest powiązany element pracy.
   {% endhint %}

**Wpływ globalnego i lokalnego zakresu na podłączanie kontaktów do elementu pracy**

{% hint style="warning" %}
Należy pamiętać, że jeśli zakres kontaktu zewnętrznego został ustawiony na lokalny (czyli jest on połączony z określoną firmą), dodanie go do elementu pracy należącego do innej firmy nie będzie możliwe. Zasada ta obowiązuje również w przypadku kont agentów, które zawsze muszą być przypisane do konkretnej firmy. TYLKO konta zewnętrzne o zakresie globalnym mogą być łączone jako kontakty z elementami pracy należącymi do dowolnego klienta.
{% endhint %}

## Edycja kontaktu

Dwukrotnie kliknięcie kontaktu na [stronie „Zarządzanie kontaktami”](https://docs.enate.net/enate-help/polski/lacznosc/strona-zarzadzania-kontaktami) otworzy okienko edycji.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FMhn7WpJy3kYUB4VKZbDL%2F7-Editing-a-Conact-in-Contact-Ma.gif?alt=media&#x26;token=d244c9c0-b0cc-49e8-9375-1b1f21714a02" alt=""><figcaption></figcaption></figure>

Można również zbiorczo edytować firmę, strefę czasową, lokalizację biura, preferowany język i tag domyślny kontaktów, zaznaczając wybrane pozycje na liście i klikając przycisk edycji, który się po tym pojawi – spowoduje to wyświetlenie wyskakującego okienka edycji zbiorczej. Należy ustawić szczegóły zgodnie z wymaganiami i kliknąć przycisk „Potwierdź”, aby zapisać zmiany.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FGq0ekkSfMwZtccBWcjqQ%2F7%20Bulk-Editing-Contacts-in-Conta.gif?alt=media&#x26;token=4f6aba53-19e2-42b5-92fc-c72e9e525fa3" alt=""><figcaption></figcaption></figure>

## Usuwanie kontaktu

Aby usunąć kontakt, należy zaznaczyć pole wyboru kontaktu na [stronie zarządzania kontaktami](https://docs.enate.net/enate-help/polski/lacznosc/strona-zarzadzania-kontaktami), a następnie kliknąć przycisk usuwania, który się po tym pojawi. Można usuwać wiele kontaktów jednocześnie.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FOH5bQG2M25PRyRFLxfZ5%2F7-Deleting-Conacts-from-Contact.gif?alt=media&#x26;token=90a02faf-db1d-4171-9474-7a9f3cdc39e0" alt=""><figcaption></figcaption></figure>
