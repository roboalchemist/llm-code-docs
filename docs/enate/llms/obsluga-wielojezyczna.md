# Source: https://docs.enate.net/enate-help/polski/obsluga-wielojezyczna.md

# Obsługa wielojęzyczna

Enate obsługuje następujące języki

* Angielski
* Portugalski (Brazylia)
* Hiszpański
* Rumuński
* Węgierski
* Polski
* Rosyjski
* Francuski
* Niemiecki

Środowisko operacyjne dla użytkowników końcowych w celu świadczenia usługi będzie w pełni obsługiwać wiele języków, a każdy użytkownik będzie mógł wybrać preferowany język wraz z wzorcem daty i godziny z ustawienia profilu użytkownika.

Aby ustawić preferowany język, wybierz język z listy rozwijanej Język w Ustawieniach użytkownika.

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCCjQMZrIXW_c-JAut%2F-MZCWE2H20vuRKMcEY_D%2FChange-Language.gif?alt=media\&token=112e24b6-1177-4eba-8d46-043d1fae0317)

Wyświetlanie etykiet pojawi się w preferowanym przez zalogowanego użytkownika języku - odbywa się to poprzez dodanie "pakietu językowego" do **Enate**. Każdy pakiet językowy będzie posiadał mapę dla konkretnego języka użytkownika, na przykład "**kolejka**" będzie "**Fila"** , a "**Czynność "** będzie "**Açao**" w języku portugalskim.

Poniżej znajduje się lista elementów UI, które będą dostępne w preferowanym przez zalogowanego użytkownika języku-

| **Pozycja**                          | **Detale**                                                                                                                                                                                               |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strona główna                        | <ol><li>Filtry RAG</li><li>Mój zespół</li><li>Sieć Botów</li><li>Kolejka</li><li>Wykres</li><li>Siatki i ustawienia kolumn</li></ol><p>Takie samo zachowanie również na stronie skrzynki odbiorczej.</p> |
| Szybkie wyszukiwanie                 | Wyszukiwanie ludzi, komunikatów i elementów pracy                                                                                                                                                        |
| Strona kolejki                       |                                                                                                                                                                                                          |
| Linki nawigacyjne                    | Link do Kreatora, strony z kolejką lub ostatnio otwieranych elementów pracy itp.                                                                                                                         |
| Strona profilu użytkownika           | Tutaj użytkownik może również zmienić preferowany język wraz z wzorcem daty i godziny.                                                                                                                   |
| Strona obsługi połączeń              | Ta strona pokazuje wszystkie elementy komunikacji i pracy związane z poszczególnymi użytkownikami                                                                                                        |
| Interfejs użytkownika elementu pracy | Etykiety i przyciski, jak zbieracz kategorii, stan itp.                                                                                                                                                  |

{% hint style="info" %}
Uwaga - Prawdziwe nazwy, takie jak nazwy klientów i użytkowników, pozostaną w oryginalnym języku, jak zostały wprowadzone przez konfiguratorów w Kreatorze.
{% endhint %}

## Dane wprowadzane przez użytkowników końcowych Work Managera <a href="#dane-wprowadzane-przez-uzytkownikow-koncowych-work-managera" id="dane-wprowadzane-przez-uzytkownikow-koncowych-work-managera"></a>

Enate w pełni obsługuje preferowany język użytkownika na ekranie Work Managera i elementy interfejsu użytkownika, w tym etykiety, łącza i przyciski, jednak wszystko, co doda użytkownik, pozostanie w tym samym języku, w którym użytkownik go pierwotnie wprowadził, i nie zostanie automatycznie przetłumaczone na żaden inny język podczas oglądania przez innych użytkowników w innym preferowanym języku.

Na przykład, jeśli brazylijski użytkownik doda notatkę do procesu w języku portugalskim, wówczas Enate zapisze notatkę w języku portugalskim w bazie danych i wyświetli notatkę tylko w języku portugalskim po wprowadzeniu przez użytkownika.

Poniżej znajduje się pełna lista elementów, które będą sterowane przez użytkownika i które **NIE** zostaną automatycznie przetłumaczone przez produkt.

| **Pozycja**                              | **Dane**                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Proces**                               | <ol><li>Notatki</li><li>E-mail</li><li>Proces - krótki opis/tytuł</li><li>Utrata ważności Instrukcja dotycząca nowych działań uruchamianych przez użytkownika końcowego</li></ol>                                                                                                                                           |
| **Czynność**                             | <ol><li>Notatki</li><li>E-mail</li><li>Uwagi do listy kontrolnej</li><li>Stan czynności - tekst przyczyny „Nie można uzupełnić”.</li><li>Utrata ważności Instrukcja dotycząca nowych działań uruchamianych przez użytkownika końcowego</li><li>Uwaga recenzenta dotycząca działania wprowadzona przez recenzenta.</li></ol> |
| **Bilet**                                | <ol><li>Tytuł i opis nowych biletów dla dzieci</li><li>Nazwa nowej akcji uruchomionej przez użytkownika</li><li>Nazwa nowego procesu uruchomionego przez użytkownika</li></ol>                                                                                                                                              |
| **Kontakt**                              | Szczegóły dotyczące kontaktu jak adres.                                                                                                                                                                                                                                                                                     |
| **Pliki**                                | Nazwa pliku i notatka o pliku                                                                                                                                                                                                                                                                                               |
| **Wady**                                 | Opis wady                                                                                                                                                                                                                                                                                                                   |
| **Uwagi dotyczące ponownego przydziału** | Tekst wprowadzany przez użytkownika podczas ponownego przypisywania pracy do innego członka zespołu.                                                                                                                                                                                                                        |

### Niestandardowe dane i karty <a href="#niestandardowe-dane-i-karty" id="niestandardowe-dane-i-karty"></a>

Pierwsza wersja funkcji wielojęzycznych nie będzie obsługiwać konfiguratorów definiujących wiele języków podczas tworzenia niestandardowych danych i kart inteligentnych w Kreatorze. W tym celu konieczne będzie użycie wielu kart i danych.

### W powiadomieniach o złożeniu wniosku <a href="#w-powiadomieniach-o-zlozeniu-wniosku" id="w-powiadomieniach-o-zlozeniu-wniosku"></a>

Początkowe wydanie funkcjonalności wielojęzycznej nie będzie obsługiwało zgłoszeń w językach innych niż angielski.
