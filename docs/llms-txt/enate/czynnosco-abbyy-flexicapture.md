# Source: https://docs.enate.net/enate-help/polski/przetwarzanie-dzialania/czynnosco-abbyy-flexicapture.md

# Czynności „ABBYY FlexiCapture”

Enate jest w stanie zapewnić integrację z aplikacją [ABBYY FlexiCapture ](https://www.abbyy.com/flexicapture/)- jest to osiągane poprzez użycie zintegrowanej czynności ABBYY FlexiCapture (zobacz [tutaj](https://docs.enate.net/enate-help/integrations/enate-integrations/ocr-integration/abbyy-integration), aby uzyskać wskazówki dotyczące tworzenia  i konfigurowania tego nowego typu czynności).

Gdy czynność ABBYY zostanie uruchomiona dla sprawy, dokumenty dołączone do sprawy można przesłać do programu ABBYY FlexiCapture w celu skanowania OCR, a przetworzone pliki wyjściowe zostaną zwrócone i automatycznie dołączone do sprawy.

{% hint style="info" %}
Uwaga: można przesyłać tylko typy plików obsługiwane przez program ABBYY v12 i nowsze. Kliknij [tutaj](https://help.abbyy.com/en-us/flexicapture/12/standalone_operator/input_formats), aby zobaczyć poniższe łącze z listą formatów obsługiwanych przez ABBYY.
{% endhint %}

System wyświetli następującą wiadomość w oczekiwaniu na przesłanie dokumentu/dokumentów do programu ABBYY FlexiCapture:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F5xoNoe9x0j1F35RDMMUY%2Fimage.png?alt=media\&token=fe5a90b4-b8fd-4193-8633-22ff188f21f0)

Zobaczysz potwierdzenie, że dokumenty zostały pomyślnie przesłane do ABBYY w celu przetworzenia:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2Fcs57VdwXbkrH853iCg6o%2Fimage.png?alt=media\&token=fc97ede6-b3ae-4542-8fef-e33d9a995352)

Ostatnia próba to czas, w którym dokument(y) został(y) przesłany(e) do przetworzenia przez mechanizm ABBYY FlexiCapture.

Jeżeli przesłane dokumenty miały nieprawidłowy format pliku lub wystąpiły problemy z formatowaniem samego dokumentu, system zwróci następujący komunikat:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FFL30I1pDsTRN4fWinfMn%2Fimage.png?alt=media\&token=febdedfc-af82-4c78-a908-5f8e61e0a6df)

### Automatyczne ponawianie&#x20;

Jeśli wystąpił problem z przesłaniem dokumentu, system automatycznie ponowi próbę jego przesłania określoną liczbę razy, w zależności od tego, jak twój system został skonfigurowany w Builderze ([więcej informacji znajdziesz tutaj](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)).&#x20;

Jeśli po automatycznych ponownych próbach nadal występuje problem z przesłaniem danych (np. jeżeli ustawiono liczbę ponownych prób na 5 i system nie ustanowi połączenia po 5 automatycznych próbach), stan akcji ABBYY zmieni się na 'Zamknięte'.

{% hint style="info" %}
W sytuacji, gdy czynności nie uda się nawiązać połączenia z systemem zewnętrznym, element zostanie przekazany właścicielowi sprawy, a w sekcji czynności na ekranie sprawy zostanie zaznaczone, że czynność jest Zamknięta – Nie udało się zakończyć pomyślnie.
{% endhint %}

## Zatwierdzenie

Po zeskanowaniu dokumentu ABBYY tworzy ocenę w oparciu o stopień pewności co do jakości skanu. Jeśli wynik zaufania jest powyżej zdefiniowanego progu, wówczas weryfikacja nie jest wymagana, a dane zostaną przetworzone i zakończone. Jeśli wynik zaufania jest poniżej pewnego progu, wymagana jest weryfikacja przez człowieka.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### Weryfikacja niewymagana

Komunikat o stanie potwierdzi, że weryfikacja przez człowieka nie jest wymagana:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FffXtqswN7ktDQyV39Eta%2Fimage.png?alt=media\&token=ce0dea51-9a15-4811-a8c7-7157d7e189c9)

Po zakończeniu przetwarzania czynność ABBYY zostanie zamknięta. Wyeksportowane pliki zostaną dołączone do sprawy i będą widoczne na karcie Pliki.

{% hint style="info" %}
Uwaga: jeśli zostały ustawione znaczniki pliku wyjściowego, ABBYY zastosuje znacznik do wszystkich przetworzonych plików, tak aby były od razu gotowe do dalszego przetwarzania.
{% endhint %}

### Weryfikacja wymagana

System wyświetli ostrzeżenie, jeśli wymagana jest weryfikacja przez człowieka:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2Fc8bynidmY5wyQTVzAJdy%2Fimage.png?alt=media\&token=199fdb81-ea8e-4ab4-9aa4-a4f6fd7685e8)

Dodatkowo, obok statusu czynności zostanie wyświetlone przypomnienie, że przed  kontynuowaniem należy przeprowadzić ręczną weryfikację w programie ABBYY:

Kliknięcie przycisku „Weryfikuj” przeniesie cię do modułu ABBYY Verification Station, gdzie można zweryfikować  skany dokumentów i wprowadzić ewentualne poprawki.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsuykc2DFaOX6-GsPY%2Fimage.png?alt=media\&token=27953730-e342-4885-9206-fae88572b769)

{% hint style="info" %}
Uwaga: aby uzyskać pełny dostęp, wymagane będzie ważne konto ABBYY FlexiCapture z uprawnieniami do przeprowadzania weryfikacji w wybranym projekcie.
{% endhint %}

Po zalogowaniu się zostanie wyświetlony ekran modułu ABBYY FlexiCapture Verification Station, na którym możesz przejrzeć i odpowiednio dostosować informacje.

Moduł weryfikacyjny składa się z trzech części:

1. Poszczególne strony dokumentu do zeskanowania.
2. Powiększenie oryginalnego dokumentu do zeskanowania.
3. Wyodrębniony wynik - czyli zeskanowana wersja oryginalnego dokumentu.

Tekst wyróżniony na żółto w zakładce oryginalnego dokumentu to dane, których ABBYY nie może odczytać. Jest to zaznaczone na czerwono w Wyodrębnionym wyniku.

Niektóre znaki, takie jak „i”, mogą być również podświetlone w sekcji „Wyodrębniony wynik”, jeśli         ABBYY nie ma pewności co do zeskanowanej kopii.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx6MLiLXtXFAmC00W%2Fimage.png?alt=media\&token=adebd784-bdf7-4f4c-b696-4832e40c4ec2)

Po zakończeniu ręcznej weryfikacji na ekranie zostanie wyświetlone potwierdzenie, że została przeprowadzona, wraz z informacją, że wymagane było działanie użytkownika:

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F1UxWiE9OJDmbABoNPvPj%2Fimage.png?alt=media\&token=165bd9f9-4c11-4d18-ba3c-7cc41897b3d9)

‌Po zakończeniu przetwarzania, wyeksportowane pliki zostaną dołączone do sprawy i będą widoczne na [karcie „Pliki”](https://docs.enate.net/enate-help/polski/rodzaje-elementow-pracy-bilety-procesy-i-czynnosci/karta-katalogowa).

Następnie można oznaczyć czynność jako zakończoną.

{% hint style="info" %}
Uwaga: jeśli zostały ustawione znaczniki pliku wyjściowego, ABBYY zastosuje znacznik do wszystkich przetworzonych plików, tak aby były od razu gotowe do dalszego przetwarzania.
{% endhint %}
