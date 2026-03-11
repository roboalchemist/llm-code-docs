# Source: https://docs.enate.net/enate-help/polski/rodzaje-elementow-pracy-bilety-procesy-i-czynnosci/karta-katalogowa.md

# Karta Pliki

## P**rzegląd**

Znacząco ulepszyliśmy sposób wyświetlania plików i odnośników oraz zarządzania nimi w przypadku zapytań, czynności i spraw. Karta „Pliki”, która wcześniej była wyświetlana na pasku bocznym, została teraz rozszerzona i przeniesiona na główną część ekranu elementu pracy obok osi czasu – teraz tam można dodawać pliki i odnośniki oraz przeglądać te, które wcześniej dodano do elementu pracy.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc5Nw==>" %}

Na karcie plików wyświetlane są wszystkie pliki i odnośniki, które zostały dodane do tego elementu pracy i elementów z nim powiązanych, a także załączniki do przychodzących i wychodzących wiadomości e-mail.

Wszelkie pliki i odnośniki dotyczące bieżącego, otwartego elementu pracy są wyświetlane w górnej części karty plików, a te dotyczące elementów z nim powiązanych znaleźć można w oddzielnej sekcji poniżej. Pozycje sortowane są według daty oraz godziny przesłania i wyświetlane od najnowszych.

Widoczne informacje o pliku obejmują jego nazwę, rodzaj, rozmiar, nadawcę i datę przesłania, a także numer referencyjny elemetu pracy, do którego został przesłany. Znajdziemy tam również [tagi ](#dodawanie-tagow-do-plikow-i-odnosnikow)i [uwagi ](#dodawanie-uwag-do-plikow)dodane do plików.

Kolejne informacje można odczytać z wyświetlanych ikon:

* standardowe załączniki są oznaczone ikoną spinacza do papieru: <img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FzVtpqZOLwtbtkxjya71O%2Fimage.png?alt=media&#x26;token=d1cd1f82-78ff-425f-8eea-e4ec2d80dfb7" alt="" data-size="line">
* odnośniki są oznaczone ikoną odnośnika: ![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FuouoGWzEfIRCMNQaFkfZ%2Fimage.png?alt=media\&token=e5a09f4a-b3ba-4017-b3a7-3377acb38b44)
* załączniki z przychodzących wiadomości e-mail są oznaczone zieloną ikoną e-maila: <img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FrhOO9NYraeno1aURRCW2%2Fimage.png?alt=media&#x26;token=21130ea4-0a1b-46db-a649-90132a5f02dd" alt="" data-size="line">
* załączniki z wychodzących wiadomości e-mail są oznaczone niebieską ikoną e-maila: <img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2Fi0JAgmcW4GVj5agS0wXz%2Fimage.png?alt=media&#x26;token=a246be93-9d3f-4ba1-b7e6-02bcab290b0e" alt="" data-size="line">

Wszystkie pliki wyszczególnione na karcie „Pliki” można dodawać jako załączniki do wychodzących wiadomości e-mail, z kolei odnośniki mogą być przesyłane w treści wiadomości.

{% hint style="info" %}
Uwaga: w przypadku aktualizacji z wersji starszych niż 2022.3 pliki dołączone bezpośrednio do elementu pracy będą widoczne w sekcji „Inne elementy robocze” bez numeru referencyjnego. Załączniki e-mail dla tego elementu pracy *znajdziemy jednak* w sekcji „Bieżące”.
{% endhint %}

## Dodawanie plików i odnośników do elementu pracy

Użytkownik, do którego przypisano dany element pracy, może dodawać do niego pliki i odnośniki na karcie Pliki. Można przesyłać wiele plików jednocześnie. Służą do tego przyciski w górnej części karty.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FN5ipeUnX7y7TIYgD4K7R%2Fimage.png?alt=media\&token=c449f006-b6d2-4d4d-a8d5-b80f483063a2)

Pliki można również przeciągnąć i upuścić na kartę Pliki.

{% hint style="info" %}
Uwaga: Maksymalny rozmiar pliku wynosi 100 MB.
{% endhint %}

### Ograniczenia dotyczące typu plików

Domyślnie przesyłać można wszystkie pliki, jednak *istnieje możliwość* wykluczenia określonych typów poprzez wskazanie w [sekcji ustawień ogólnych Buildera ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#allowed-file-types)tych, które mają być dozwolone.

## Dodawanie tagów do plików i odnośników

Pomagają one usystematyzować dane i pozwalają skorzystać z funkcji takich jak automatyczne załączanie plików z określonymi tagami do wiadomości e-mail wysyłanych przez system lub do gotowych tekstów standardowych wstawianych do e-maili tworzonych przez użytkownika, a zewnętrznym procedurom automatyzacji wskazują, które konkretnie pliki pobrać z elementu pracy.

Oznaczanie plików tagami jest również istotne w przypadku procesów, w których wykorzystywana jest automatyzacja. Przykład: jeśli zautomatyzowana czynność na dalszych etapach prac musi wiedzieć, który z plików dołączonych do sprawy to „Potwierdzenie faktury”, można odpowiednio go oznaczyć – zautomatyzowany proces wybierze ten plik na podstawie jego tagów, bez względu na samą nazwę. Tego rodzaju zewnętrzna automatyzacja może być także źródłem tagów w ramach przesyłania dokumentów do elementów pracy w Enate w celu ich dalszego ręcznego lub automatycznego wykorzystania.

Tagi dostępne dla danego użytkownika są [określane w Builderze](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags). Jeśli często dochodzi do sytuacji, że dany tag nie jest dla nas dostępny, należy poprosić administratora o jego dodanie.

W celu dodania tagu do pliku wystarczy kliknąć ikonę „+”, a następnie wybrać właściwą pozycję z wyświetlonej listy.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVXReQz9C20sb4udydhJF%2Fimage.png?alt=media&#x26;token=602fe6a4-3867-4b26-b40b-61bb28b2f19a" alt=""><figcaption></figcaption></figure>

Można również dodawać tagi do wielu plików i odnośników jednocześnie, zaznaczając jeden lub więcej elementów i klikając ikonę znajdującą się na nagłówku karty „Pliki”.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F31DaG0W7U0ZJCX7Y8yLq%2Fimage.png?alt=media\&token=9984c5cf-21c6-446f-9b66-aefd2e6f0bf6)

W dostępnej w Buiderze sekcji [Sklep ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)dostępne są różne opcje, które pozwalają korzystać z komponentów (przygotowanych zarówno przez Enate, jak zewnętrznych) odpowiedzialnych za analizę treści przychodzących wiadomości i wskazywanie na jej podstawie najbardziej właściwych tagów dla załączników.

Jeśli administrator włączył dla nas komponent automatycznego tagowania, w sekcji tagów pliku zobaczymy dodatkowe informacje wynikające z systemowych podpowiedzi tagów dla załączników.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7DjliBUjGYgVVsFAlsVK%2Fimage.png?alt=media&#x26;token=50ad2fe4-77b6-496e-8cb4-4fe37f7fc0b8" alt=""><figcaption></figcaption></figure>

Jeśli używana technologia będzie wystarczająco pewna swojej podpowiedzi, tag zostanie wyświetlony na zielono. Nie musimy nic robić, jeśli sugerowany tag nam odpowiada – w przeciwnym wypadku wystarczy go kliknąć, by samodzielnie wybrać inny.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhrGM2KnQWOm6hWEOWvmT%2Fimage.png?alt=media&#x26;token=8ca78e18-5e32-46ef-aa4e-b11d0247b8c1" alt=""><figcaption></figcaption></figure>

Jeśli poziom pewności będzie niższy, tag zostanie wyróżniony kolorem pomarańczowym. Wówczas trzeba go potwierdzić, jeśli nam pasuje, albo zmienić na taki, który spełnia nasze wymagania. Przy każdej takiej sytuacji używana przez nas technologia będzie się uczyć i nabierać wprawy w podpowiadaniu tagów. Jeśli podpowiedzi wciąż są błędne, należy poprosić administratora o korektę progów pewności.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIMxyVCb2WYDXfK5CFCST%2Fimage.png?alt=media&#x26;token=b202cf44-61da-47bf-ae5c-989b964cedc1" alt=""><figcaption></figcaption></figure>

Po oznaczeniu tagami pliki i odnośniki będą mogły być automatycznie dodawane do wiadomości e-mail z pasującymi tagami, dzięki czemu użytkownik może mieć pewność, że wszystkie wymagane dokumenty zostaną dołączone do wiadomości e-mail o określonej treści.

Gdy do tworzonej przez użytkownika wiadomości e-mail wstawiony zostanie tekst [gotowej odpowiedzi](https://docs.enate.net/enate-help/polski/e-maile/szablony-wiadomosci) lub gdy nowy e-mail zostanie automatycznie utworzony i wysłany w ramach przetwarzania danego elementu pracy, system zidentyfikuje wówczas wszystkie tagi powiązane z gotowym tekstem lub szablonem e-mail, a następnie automatycznie załączy do wiadomości wszystkie pliki z tego elementu pracy, które oznaczono tymi samymi tagami. Tagi są łączone z gotowymi odpowiedziami lub treścią wiadomości e-mail podczas tworzenia [szablonów e-mail](https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration) w Builderze przez administratorów systemu.

{% hint style="info" %}
Uwaga: Jeśli tagi dla plików nie zostały [skonfigurowane w systemie](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags), opcja „dodaj tag” nie będzie wyświetlana.
{% endhint %}

## Dodawanie uwag do plików

Do plików i odnośników można również dodawać uwagi zawierające krótki opis zawartości lub inne informacje, które mogą być przydatne.

Można dodawać uwagi do wielu plików i odnośników jednocześnie, zaznaczając jeden lub więcej elementów i klikając ikonę znajdującą się na nagłówku karty „Pliki”.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FImxnujeeYfEWicR46AR3%2Fimage.png?alt=media\&token=1916c161-f975-4baf-a8a6-b89e5f24eb9d)

## Podgląd plików

Menu z prawej strony ekranu umożliwia podgląd poszczególnych plików. Podgląd otworzy się w nowej karcie.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FUWawL5D5t3BPQNbG5OK1%2Fimage.png?alt=media\&token=dacc8658-5b10-4439-bf4e-dc5105f54f77)

{% hint style="info" %}
Jeśli zawartości danego pliku nie można podejrzeć, wyświetlone zostanie okienko ze stosowną informacją i możliwością pobrania pliku. Typy plików obsługiwane przez funkcję podglądu: **txt**, **pdf**, **jpg**, **jpeg**, **jpe**, **jif**, **jfif**, **jfi**, **png**, **gif**, **web**, **tiff**, **tif**, **heif**,**heic**, **svg**, **svgz**.
{% endhint %}

## Pobieranie plików

W celu pobrania poszczególnych plików należy wybrać odpowiednią opcję w menu po prawej stronie ekranu.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FqbpXzhVDIbLzeaIvWD6B%2Fimage.png?alt=media\&token=df58a1c7-e41f-4323-af6d-c127a28c4b20)

Można pobrać wiele plików jednocześnie, zaznaczając wybrane i klikając przycisk w górnej części ekranu. Zostaną one pobrane osobno lub razem w postaci pojedynczego skompresowanego archiwum ZIP – służy do tego przycisk znajdujący się tutaj.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F3tvc1axkblxQ4wdcmZ30%2Fimage.png?alt=media\&token=443c62cc-08ca-4217-9b04-05c1ac7cfeb1)

## Usuwanie plików i odnośników

W celu usunięcia poszczególnych plików lub odnośników należy wybrać odpowiednią opcję w menu po prawej stronie ekranu.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F4YgCm4eqpovVk9cpbp2G%2Fimage.png?alt=media\&token=6827c89e-1538-4d46-8595-7f83632c635c)

Można usunąć wiele plików lub odnośników jednocześnie, zaznaczając wybrane i klikając przycisk w górnej części ekranu.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FPh99qQZtJ5AYD7WA6dXk%2Fimage.png?alt=media\&token=2f37ebf9-cdc8-4b0f-a6ff-3e9de8d07e7e)

## Filtrowanie plików i odnośników

Pliki i odnośniki wyświetlane na karcie „Pliki” można filtrować, korzystając z odpowiedniej funkcji znajdującej się w górnej części ekranu. Pozycje można filtrować według: załączników, załączników wychodzącej poczty e-mail, załączników przychodzącej poczty e-mail i odnośników.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F8EWTiqtbpEHfsgq0Cezd%2Fimage.png?alt=media\&token=4213bce7-7145-403d-a024-25dfcf595522)

### Tekstowe wyszukiwanie plików

Funkcja wyszukiwania tekstowego ułatwia znajdowanie poszczególnych plików i odnośników. Obejmuje ona różne wyświetlane grupy informacji – nazwy pliku, informacje o tagach i dołączone uwagi.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FGZUdNMCQDmatyNXB15v8%2Fimage.png?alt=media\&token=63b6f020-717d-47d0-ae87-206112c0be3d)
