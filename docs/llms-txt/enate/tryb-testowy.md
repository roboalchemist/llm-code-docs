# Source: https://docs.enate.net/enate-help/polski/tryb-testowy.md

# Tryb testowy

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Przełączanie do trybu testowego <a href="#a-przelaczanie-do-trybu-testowego" id="a-przelaczanie-do-trybu-testowego"></a>

Jeśli twoje konto użytkownika jest ustawione tak, aby umożliwić Ci dostęp do danych testowych, możesz przełączyć środowisko Work Managera na 'Tryb testowy'. Ten link jest dostępny w rozwijanej liście użytkowników po prawej stronie paska nagłówka.

## Objaśnienie trybu testowego <a href="#b-objasnienie-trybu-testowego" id="b-objasnienie-trybu-testowego"></a>

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FIXp6H7skkMFeNUCuDAWC%2Fimage.png?alt=media\&token=81a3417c-d25e-4007-bf87-fd34a78f7643)

Po uruchomieniu w trybie testowym wyświetlane są tylko dane testowe; pozwala to na tworzenie i uruchamianie testowych elementów pracy poprzez testowe wersje procesów w celu ich weryfikacji przed ustawieniem na żywo, wszystko bez wpływu na dane produkcyjne na żywo.

Dla przypomnienia, pasek nagłówka jest ustawiony na kolor czerwony, gdy jesteś w trybie testowym.

## Kierownik testów i użytkownicy testowi kolejki <a href="#c-kierownik-testow-i-uzytkownicy-testowi-kolejki" id="c-kierownik-testow-i-uzytkownicy-testowi-kolejki"></a>

Funkcja trybu testowego pozwala teraz na ustawienie innego menedżera dla kolejki podczas pracy w trybie testowym vs. w trybie na żywo.

Przykład: Weź pod uwagę **Menedżera 1**, który ma dostęp do trybu na żywo i jest odpowiedzialny za zarządzanie dwiema kolejkami, **Finansową** i **Głównego procesu.**

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FwmrZWWCuQ10wIpJmrCde%2Fimage.png?alt=media\&token=9ae03bf9-492d-4fc1-b7bd-4469afeebbd0)

W trybie testowym te same dwie kolejki mogą być zarządzane przez innego użytkownika, który ma uprawnienia Leadera i Trybu testowego - patrz poniższy przykład, gdzie **Menadżer 2** jest odpowiedzialny za kolejki w trybie testowym.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FIPMsTKTrifr4MWRZSS9J%2Fimage.png?alt=media\&token=196a9ba4-57bc-4d4a-a263-64ae4d520625)

## Przełączanie robotów między pracą na żywo a testem <a href="#d-przelaczanie-robotow-miedzy-praca-na-zywo-a-testem" id="d-przelaczanie-robotow-miedzy-praca-na-zywo-a-testem"></a>

Teraz możliwe jest przełączenie robota tak, aby mógł pracować w trybie testowym lub w trybie na żywo. W szczególności, dwie nowe aktywności zostały dodane do bibliotek aktywności dla UiPath, Automation Anywhere i BluePrism (oraz standardowe API dostosowane tak, aby można je było nazwać ogólnymi) w następujący sposób:

* Ustaw tryb na żywo
* Ustaw tryb testowy

Te czynności umożliwiają przełączanie robota między stanem testowym a stanem rzeczywistym. Po przełączeniu robota w tryb testowy kolejne wywołania aktywności, które robot może wykonać, np. „Uzyskaj więcej pracy” i „Utwórz bilet / proces itp.” Odbywają się w tym kontekście trybu testowego, pobierając i tworząc tylko testowe elementy pracy. Robot powinien zostać przełączony z powrotem do trybu podglądu bieżącego po ustawieniu procesu na podgląd bieżący, więc należy upewnić się, że następnie tworzy on elementy pracy na żywo.

## Kontakty testowe Oddzielne kontakty testowe w systemie <a href="#e-kontakty-testowe-oddzielne-kontakty-testowe-w-systemie" id="e-kontakty-testowe-oddzielne-kontakty-testowe-w-systemie"></a>

Enate obsługuje teraz tworzenie osobnych rekordów kontaktów w trybie testowym, tj. Wszelkie rekordy kontaktów utworzone w trybie testowym będą dostępne tylko dla użytkowników w trybie testowym (a kontakty utworzone w trybie na żywo będą dostępne tylko dla użytkowników w trybie na żywo). Pomaga to zapewnić, że e-maile z pakietów testowych nie są przypadkowo wysyłane do użytkowników produkcyjnych i na odwrót.
