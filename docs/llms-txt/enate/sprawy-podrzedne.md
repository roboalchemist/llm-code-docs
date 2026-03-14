# Source: https://docs.enate.net/enate-help/polski/rozpatrywanie-procesu/sprawy-podrzedne.md

# Sprawy podrzędne

Sprawa podrzędna będzie działała zgodnie ze swoją własną konfiguracją, ale sprawa nadrzędna nie zostanie zakończona, dopóki nie zostaną ukończone wszystkie jej sprawy podrzędne.

Można zatem utworzyć sprawę podrzędną tylko z już istniejącej sprawy.

By utworzyć nową sprawę podrzędną, kliknij przycisk „+ Element pracy” znajdujący się obok sekcji kart danej sprawy, a następnie wybierz „Sprawa podrzędna” z rozwijanej listy.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2Fcgp4suqBbmBpOkHMwj95%2Fimage.png?alt=media\&token=d8ea56c2-552a-457c-b4a9-a5f33b3bcd14)

W rezultacie pojawi się okienko umożliwiające utworzenie nowego procesu sprawy podrzędnej na dwa sposoby:

* wyszukując według przekierowań wiadomości e-mail - możesz określić adres skrzynki pocztowej, na który ludzie będą wysyłać wiadomości e-mail w celu tworzenia elementów pracy. Często skrzynka mailowa reprezentuje pewną część zadania, w ramach którego chcesz utworzyć nowy element pracy. By skrócić ten proces, dodaliśmy tutaj użyteczną funkcję, która pozwala wyszukiwać według skrzynki pocztowej i od razu zawężać liczbę procesów sprawy podrzędnej do wyboru. Wybór skrzynki pocztowej spowoduje ograniczenie rozwijanej listy opcji tylko do procesów powiązanych z tą skrzynką.
* wybierając klienta, kontrakt, usługę oraz proces sprawy podrzędnej do uruchomienia (jeśli do wyboru jest tylko jedna opcja, wyświetlone zostaną wartości domyślne). Jako „Klient” sprawy podrzędnej automatycznie ustawiony zostanie klient sprawy, z której sprawa podrzędna jest tworzona (czyli nadrzędnej).

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FRM9Sa24n7cOGw8ywBoJZ%2Fimage.png?alt=media\&token=554421c3-4977-4b5a-bf01-b0b1ddfa522e)

{% hint style="info" %}
Należy pamiętać, że wybór dostępnych do uruchomienia spraw podrzędnych zależy od ustawień uprawnień w Builderze. Do tego można wybrać proces sprawy podrzędnej tylko z takiego przekierowania wiadomości e-mail, które zostało aktywowane w Builderze ([więcej informacji tutaj](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes-detail)). By wybrać proces sprawy podrzędnej w [trybie testowym](https://docs.enate.net/enate-help/polski/tryb-testowy), przekierowanie wiadomości e-mail dla tego procesu sprawy podrzędnej musi być skonfigurowane do uruchamiania w [tym trybie](https://docs.enate.net/enate-help/polski/tryb-testowy).
{% endhint %}

Następnie można dostosować następujące ustawienia sprawy podrzędnej:

| Zmiana terminu zakończenia | Jeśli ustawienia systemu tego wymagają ([więcej informacji tutaj](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours)), można zmienić termin zakończenia tworzonej sprawy podrzędnej. |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opis                       | Pozwala zmodyfikować tytuł tworzonej sprawy podrzędnej.                                                                                                                                                                                             |
| Harmonogram                | Jeśli ustawienia systemu tego wymagają ([więcej informacji tutaj](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules)), trzeba wybrać harmonogram dla tworzonej sprawy.          |
| Dodawanie kontaktów        | Do nowej sprawy można dodawać różne kontakty i rozdzielać między nie znaczniki.                                                                                                                                                                     |

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F0hrzQMYA8cVLLwKdYPu4%2Fimage.png?alt=media\&token=6ad8ce84-17f8-4ea2-8ed2-7d460926f55d)

{% hint style="info" %}
Istniejące błędy, pliki, odnośniki i dane niestandardowe ze sprawy macierzystej będą automatycznie współdzielone z nową sprawą podrzędną. Komunikacja sprawy macierzystej i powiązanych z nią elementów pracy (czyli czynności i spraw podrzędnych, jeśli je posiada) również będą automatycznie współdzielone z nową sprawą podrzędną. Uwaga: ze współdzielenia wykluczone są wiadomości e-mail, ale można je bez trudu podejrzeć, wybierając na osi czasu opcję [„Uwzględnij powiązane elementy pracy”](https://docs.enate.net/enate-help/polski/rodzaje-elementow-pracy-bilety-procesy-i-czynnosci/sekcja-glowna). Należy również pamiętać, że zmiany dokonane w błędach, plikach, odnośnikach, danych niestandardowych lub komunikacji nowej sprawy podrzędną sprawią, że zostaną one uaktualnione również w sprawie macierzystej.
{% endhint %}

Odnośnik do nowej sprawy podrzędnej pojawi się na [karcie „Sprawy podrzędne”](#karta-sprawy-podrzedne), a nie na [karcie „Odnośniki”](#lista-powiazanych-elementow-pracy-karta-odnosniki).

### **Karta „Sprawy podrzędne”**

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8o18I3JZ3nO3hyj0a%2FSub-Cases-Tab.gif?alt=media\&token=bd36ffad-fe23-4381-b5ff-2f74c03a9518)

Na karcie „Sprawy podrzędne” wyświetlone zostaną następujące informacje dotyczące każdej sprawy podrzędnej danej sprawy:

* Ikona aktualnego stanu
* Numer referencyjny sprawy podrzędnej i tytuł sprawy
* Liczba czynności - liczba czynności związanych z tą sprawą podrzędną Właściciel – właściciel sprawy *(jeśli została zdefiniowany)*
* Kolejka – kolejka sprawa *(jeśli została zdefiniowana)*
* Termin zakończenia – termin zakończenia sprawy
* Przycisk służący do rozwinięcia sprawy podrzędnej w celu wyświetlenia jej czynności

#### Opis numeru referencyjnego sprawy podrzędnej

Numery referencyjne spraw podrzędnych odczytuje się w następujący sposób:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FSHBRSSGTl9YfSLAUfqaY%2Fimage.png?alt=media\&token=a3b0b799-739b-4cde-970f-ef8a2523d51e)
