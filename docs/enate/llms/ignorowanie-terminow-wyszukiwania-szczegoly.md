# Source: https://docs.enate.net/enate-help/polski/dodatek/ignorowanie-terminow-wyszukiwania-szczegoly.md

# Ignorowanie terminów wyszukiwania - szczegóły

Jedną z wbudowanych w Enate funkcji służących do optymalizacji wyników wyszukiwania jest usuwanie z wyszukiwań powszechnie używanych terminów, jeśli zostały wprowadzone ręcznie przez użytkownika. Pozwala to zachować dużą szybkość wyszukiwania oraz uniknąć zwracania przez wyszukiwarkę ogromnych ilości wyników, które mogłyby przysłonić te, na których rzeczywiście zależy użytkownikom. Jedną z metod stosowanych w tym celu jest wykorzystanie stop-listy.

## Stop-lista

Stop-lista to spis powszechnie używanych słów, takich jak „i”, „ten”, „ja” itp., które są pomijane w wyszukiwaniach, ponieważ w przeciwnym razie zwróciłyby zbyt wiele wyników.

Poniżej znajduje się pełna stop-lista wyrazów, które będą pomijane we WSZYSTKICH wyszukiwaniach w Enate - dotyczy to nie tylko wyszukiwania poprzez szybkie wyszukiwanie, ale również wyszukiwania użytkowników, wiadomości e-mail, elementów pracy (np. zapytań podczas ich scalania) itp. Jeśli użytkownik wpisze którekolwiek z tych słów, zostanie ono automatycznie pominięte w wyszukiwaniu.

{% file src="<https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FRcoQNLmN7xBF09JA2Yga%2FEnate%20SQL%20Stop%20List.xlsx?alt=media&token=a9d36746-4614-4d7f-9a50-5f2bae5ba547>" %}

Obsługiwanych jest wiele stop-list dla różnych języków użytkownika.

{% hint style="info" %}
Uwaga: Przy wyszukiwaniu użytkowników oraz e-maili zawsze używana jest angielska (brytyjska) stop-lista. W przypadku elementów pracy (tytuł, nazwa klienta, nazwa kontraktu, nazwa usługi, nazwa sprawy/zapytania itd.) stop-lista zostanie wybrana na podstawie języka aktualnie zalogowanego użytkownika. Należy przy tym pamiętać, że język węgierski nie jest bezpośrednio wspierany w SQL, dlatego w wyszukiwaniach inicjowanych przez węgierskich użytkowników wykorzystana zostanie angielska stop-lista.
{% endhint %}

## Znaki pomijane w szybkim wyszukiwaniu

Podczas wyszukiwania w szybkim wyszukiwaniu pomijane będą również określone znaki, np. „\*”, „?”, „@”  itp. Oznacza to, że wpisując w polu szybkiego wyszukiwania customer.com, wyszukane zostaną słowa customer icom. Dlatego zaleca się umieszczanie takich kombinacji słów w cudzysłowie, aby wyszukać całą frazę - wyszukanie „customer.com” prawdopodobnie zwróci te wyniki, których potrzebujesz.

Poniżej znajduje się pełna lista znaków, które będą pomijane w szybkim wyszukiwaniu:

{% file src="<https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FgZAOwHFWUBvcjufxU09m%2FCharacters%20ignored%20in%20Quickfind.pdf?alt=media&token=793b17f0-3cef-46af-9bfb-a6bbc692b982>" %}
