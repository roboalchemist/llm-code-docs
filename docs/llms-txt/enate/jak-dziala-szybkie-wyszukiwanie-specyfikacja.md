# Source: https://docs.enate.net/enate-help/polski/szybkie-wyszukiwanie/jak-dziala-szybkie-wyszukiwanie-specyfikacja.md

# Jak działa szybkie wyszukiwanie - szczegóły

Kilka dalszych wyjaśnień na temat działania szybkiego wyszukiwania: istnieją trzy różne rodzaje wyszukiwania, które są przeprowadzane równolegle podczas wprowadzania danych w wyszukiwarce:

**1) Konkretne wyszukiwanie według numeru referencyjnego.** Polega to na rozpoznaniu znanego formatu numeru referencyjnego dla elementów pracy w systemie, a następnie zwróceniu wyników związanych z zapytaniami, sprawami i czynnościami, które mają takie odniesienie. Możesz po prostu wpisać numer odniesienia, np. „40308-T” i system rozpozna je jako odniesienie. Nie musisz wpisywać głównego krótkiego kodu.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FLOSmDK6ZbyBLPOgfbV9t%2Fimage.png?alt=media\&token=b070ac05-07ed-4681-99e6-88fecd7c869d)

**2) Wyszukiwanie danych niestandardowych**. Jak opisano powyżej. System przeprowadzi tego rodzaju wyszukiwanie po wprowadzeniu znanego krótkiego kodu, np. „FN:” . Wyszukiwanie będzie dotyczyło pola zawierającego określoną wprowadzoną wartość. Więcej informacji na temat symboli wieloznacznych znajduje się poniżej.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FkkXoAwBWWVDvyJ0JrEGU%2Fimage.png?alt=media\&token=17d00e4c-99f5-4e21-90cc-33f90918c77f)

**3) Swobodne wyszukiwanie tekstowe elementów roboczych, komunikacji i osób** we wszystkim, co wprowadza użytkownik, a co nie jest zgodne z pierwszymi dwoma typami rozpoznawanych danych. Poszczególne słowa przeszukiwane są pod kątem różnych atrybutów systemowych elementów pracy, komunikacji i osób, np. tytułu elementu pracy czy tematu i treści wiadomości e-mail.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FbSv7ldoegZUNg3G6l2mH%2Fimage.png?alt=media\&token=9e983b7f-fb0a-4be0-a722-3066e1532a18)

**4) Wyszukiwanie plików według zasady „zaczyna się od”** – podczas wyszukiwania plików system kieruje się zasadą „zaczyna się od”, dodając symbol wieloznaczny na KOŃCU wyszukiwanego tekstu. W praktyce oznacza to, że wyszukiwarka nie odnajdzie pliku o nazwie „Invoice Processing.docx” po słowie „processing”, za to wpisanie słowa „invoice” zwróci pożądane wyniki.

## Symbole wieloznaczne dla prostych wyszukiwań

Podczas wyszukiwania system doda symbol wieloznaczny na KOŃCU wpisanego tekstu, nie na początku.

W przypadku wyszukiwania niestandardowych danych wygląda to następująco: wpisanie „p:John Smi” zwróciłoby wyniki z wartością „John Smith” w polu „osoba” (*person*), ale wpisanie tylko „p:Smith” już NIE.

W skrócie: w przypadku wyszukiwania danych niestandardowych, szukamy dokładnej wartości pola lub początku wartości. Wyszukiwanie dowolnego tekstu nie jest *do* *końca* takie samo, ponieważ w tym przypadku wyszukiwarka będzie starała się szukać wyników dla pojedynczych słów, a nie dla wartości jako całości.

Symbole wieloznaczne są również dodawane na końcu wyszukiwania numerów referencyjnych.

### **Wykorzystywanie symboli wieloznacznych podczas pisania**

Podczas wpisywania w szybkim wyszukiwaniu, system będzie wyszukiwał wieloznacznie na podstawie ostatniego słowa. Przykładowo: jeśli wpisujesz „John return prio”, system doda symbole wieloznaczne do ostatniego słowa i zwróci wyniki także dla słowa „priority”.

Po naciśnięciu klawisza spacji system stwierdzi, że dane słowo zostało wpisane i będzie wyszukiwał je bez końcowego symbolu wieloznacznego.

## Hasła pomijane w wyszukiwaniu

W celu zachowania wysokiej wydajności systemu, następujące elementy są ignorowane podczas wyszukiwania:

* Słowa o długości od 1 do 2 znaków.
* Słowa obecne na systemowej stop-liście. Są to często występujące słowa, takie jak „i”, „ja” itp., które zwróciłyby zbyt wiele wyników. Oto [pełna stop-lista wyrazów, które będą pomijane we wszystkich wyszukiwaniach w Enate](https://docs.enate.net/enate-help/polski/dodatek/ignorowanie-terminow-wyszukiwania-szczegoly#stop-lista) (zarówno w szybkim wyszukiwaniu, jak i w każdej innej systemowej wyszukiwarce).
* Określone znaki, takie jak „\*”, „?”, „@” itp. są ignorowane podczas korzystania z szybkiego wyszukiwania. Oto [pełna lista wszystkich pomijanych znaków](https://docs.enate.net/enate-help/polski/dodatek/ignorowanie-terminow-wyszukiwania-szczegoly#znaki-pomijane-w-szybkim-wyszukiwaniu). Oznacza to na przykład, że po wpisaniu w polu szybkiego wyszukiwania frazy „customer.com” wyszukiwane będą słowa „customer” i „com”. Z tego powodu zaleca się umieszczanie takich kombinacji słów w cudzysłowie – wyszukanie frazy „customer.com” prawdopodobnie zwróci te wyniki, które są potrzebne.

## Pozostałe wskazówki dotyczące szybkiego wyszukiwania

Szybkie wyszukiwanie jest wyszukiwaniem tekstowym. Wpisywanie dat w ciągach tekstowych może dawać niespójne wyniki. Należy używać cudzysłowów wszędzie tam, gdzie jest to możliwe, jeśli wyszukiwanie ma uwzględnić cały ciąg znaków, np. „szukaj miejsca, gdzie występuje cały ten ciąg”.

Do wyszukiwania w określonych zakresach dat służą suwaki.

W przypadku wyszukiwania wielu słów będzie się ono odbywać się przy użyciu operatora „AND”, a nie „OR”, tzn. wyniki będą zawierały I „jabłka”, I „banany”, I „gruszki”.

## Wyszukiwanie w elementach pracy a wyszukiwanie w wiadomościach e-mail – szczegóły

Należy pamiętać, że szybkie wyszukiwanie wykonuje trzy niezależne wyszukiwania:

* wyszukiwanie elementów pracy (spraw, czynności, zapytań),
* wyszukiwanie powiązanych z nimi wiadomości e-mail oraz
* wyszukiwanie osób.

W rezultacie dla wyszukiwania kombinacji trzech słów, np. „jabłka”, „banany” i „gruszki”, szybkie wyszukiwanie wyświetli wszystkie elementy pracy, w których wystąpiły wszystkie te trzy słowa oraz, osobno, wszystkie e-maile, w których wystąpiły wszystkie te trzy słowa. Jeśli dwa z tych słów pojawiają się w elementach pracy, a trzecie tylko w powiązanych e-mailach, wówczas taki wynik NIE zostanie wyświetlony.

Atrybuty elementów pracy, które są uwzględniane w trakcie wyszukiwania, to:

* Numer odniesienia elementu pracy;
* Tytuł;
* Nazwa klienta;
* Nazwa dostawcy;
* Nazwa kontraktu;
* Nazwa usługi;
* Nazwa działu usług;
* Nazwa typu procesu.

Atrybuty komunikacji, które są uwzględniane w trakcie wyszukiwania, to:

* Tytuł wiadomości e-mail;
* Treść wiadomości e-mail;
* Adresy (Od, Do, DW, UDW)
* Treść uwagi wewnętrznej (uwagi dodane w Enate / Samoobsługa).
