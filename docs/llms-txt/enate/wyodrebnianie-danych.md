# Source: https://docs.enate.net/enate-help/polski/przetwarzanie-dzialania/wyodrebnianie-danych.md

# Wyodrębnianie danych

## Przegląd

Komponent „Wyodrębnianie danych” automatycznie wyodrębnia odpowiednie dane z plików załączonych do przychodzących wiadomości e-mail, dzięki czemu dane te mogą być wykorzystane w dalszym przetwarzaniu elementu pracy, oszczędzając czas i wysiłek agentów. Oznacza to również, że dokumenty, takie jak np. pliki PDF, mogą być skanowane i wykorzystywane zarówno do rozpoczynania spraw w Enate, jak i do kontynuowania już trwających działań.

Gdy czynność wyodrębniania danych zostanie uruchomiona dla sprawy, dokumenty do niej dołączone można przesłać do wybranej aplikacji w celu zeskanowania, a przetworzone pliki wyjściowe zostaną odesłane i automatycznie dołączone do sprawy.

Jeśli na jakimkolwiek etapie wykorzystywana technologia, kierując się ustawianym przez użytkownika progiem pewności, nie będzie wystarczająco pewna otrzymanych wyników, Enate natychmiast przekaże pracę do sprawdzenia i weryfikacji agentowi w Work Managerze, zapewniając tym samym realizację podejścia „człowiek w pętli”.

Ten komponent może być włączony przez administratora w sekcji [Sklepu ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)w Builderze Enate.

Więcej na ten temat dowiesz się z poniższego filmu:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

## Jak to działa

Gdy sprawa zostanie uruchomiona w Work Managerze, odpowiednie dane z plików załączonych do jej przychodzących wiadomości e-mail zostaną automatycznie przeanalizowane i wyodrębnione.

Jeśli używana technologia jest wystarczająco pewna wyników wyodrębniania danych, użytkownik nawet nie zobaczy tej czynności – system zakończy ją automatycznie i sprawa przejdzie do następnej. Nadal można przeglądać szczegóły zakończonej czynności wyodrębniania danych, klikając wybrany element, ale sam proces odbędzie się bez udziału człowieka.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5x5hGES3lDv4IeonVeVS%2Fimage.png?alt=media&#x26;token=d780fad0-e13d-4f09-aab1-92d50045b3b3" alt=""><figcaption></figcaption></figure>

Jeśli jednak poziom pewności wykorzystywanej technologii jest niższy, czynność zostanie przekazana do przejrzenia użytkownikowi, który zobaczy ją na swojej stronie domowej, gdy naciśnie „Wybierz pracę z kolejek”. Po otworzeniu takiej czynności agent zobaczy informację, że została mu ona przekazana, ponieważ wymaga dalszej kontroli.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F4J9R530lDJ96RKIfArDq%2Fimage.png?alt=media&#x26;token=74beb37a-3b12-47b0-849c-6e93147390e9" alt=""><figcaption></figcaption></figure>

Należy wówczas kliknąć „Zweryfikuj teraz” i przewinąć do sekcji „punkt weryfikacji” w czynności, gdzie wyświetlony zostanie obraz zeskanowanego dokumentu wraz z wyodrębnionymi wartościami przedstawionymi w formie tabeli. Fragmenty z niskimi poziomami pewności zostaną podświetlone, aby łatwiej było je sprawdzić i ręcznie wprowadzić ewentualne poprawki. Można to zrobić na miejscu albo rozwinąć każdą pozycję do pełnoekranowego okna.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FuIqj8rVdYsjE3qvAQSFv%2Fimage.png?alt=media&#x26;token=f8241455-0c10-49de-a25e-1a1991584284" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Uwaga: Jednocześnie można wyświetlić tylko jeden dokument.
{% endhint %}

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FUnS7g9cfnGD4cFuBObFA%2Fimage.png?alt=media&#x26;token=4be1a149-b824-4c4d-b575-3436739b4770" alt=""><figcaption></figcaption></figure>

Na tym ekranie weryfikacji agent będzie mógł zobaczyć zeskanowaną kopię pliku, który może składać się z wielu stron, wraz z dwiema zakładkami zawierającymi wyodrębnione dane.

* Zakładka Wyodrębnione dane pokazuje pary wartości klucza agenta dla wyodrębnionych danych wraz z poziomem pewności nadanym im przez EnateAI. Wartości można w razie potrzeby dostosować i zapisać po kliknięciu przycisku aktualizacji dla danej wartości. Spowoduje to ustawienie wartości pewności dla danego klucza na 100%.
* Zakładka Tabele pokazuje wszystkie powtarzające się dane, które zostały wybrane jako tabela. Możesz użyć przycisku Usuń, żeby usunąć wszystkie wiersze, które nie są Ci potrzebne.

Jeśli agent musi opuścić ekran stacji walidacji w dowolnym momencie, może po prostu kliknąć „Zapisz jako wersję roboczą”, aby zapisać zmiany wprowadzone w danym dokumencie.

{% hint style="info" %}
Uwaga: Jeśli agent przejdzie do ekranu walidacji czynności, która nie została mu przypisana, dane będą dostępne tylko do odczytu i nie będzie można ich edytować. Aby móc edytować dane, agent musi najpierw przypisać sobie daną czynność.
{% endhint %}

Gdy agent jest zadowolony z danych, wystarczy kliknąć przycisk „Prześlij”, aby przesłać zaktualizowane dane. EnateAI zakończy przetwarzanie w tle i zaktualizuje ekran Czynność, aby potwierdzić zakończenie procesu. Przetwarzanie w tle pozwala agentowi przejść do innych dokumentów wymagających weryfikacji.

Po kliknięciu przycisku „Prześlij” dla ostatniego dokumentu wymagającego walidacji ekran Czynność zostanie automatycznie zamknięty. EnateAI ponownie zakończy przetwarzanie w tle i po krótkim czasie oznaczy czynność jako Rozwiązaną, a następnie przeniesie ją do sekcji Zamknięte.

*Uwaga: Za każdym razem, gdy przeglądasz i aktualizujesz elementy danych, EnateAI uczy się i nieco poprawia swoje sugestie dotyczące ekstrakcji danych. Jeśli zauważysz, że technologia regularnie podaje błędne sugestie, skontaktuj się z zespołem administratorów w celu zmodyfikowania progu pewności.*
