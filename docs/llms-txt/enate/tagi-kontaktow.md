# Source: https://docs.enate.net/enate-help/polski/lacznosc/tagi-kontaktow.md

# Tagi kontaktów

Tagi kontaktów służą do łączenia kontaktów z elementami pracy.

## Systemowe tagi domyślne

Dostępne systemowe tagi domyślne dla kontaktu to:

* **Kontakt główny** – osoba, z którą należy się kontaktować w sprawie bieżącej czynności. Dla danego elementu pracy może być tylko jeden kontakt główny. Dla zapytań wskazanie tego kontaktu jest obowiązkowe. W zależności od ustawień w Builderze, wskazanie tego kontaktu może, ale nie musi być obowiązkowe dla spraw (a jeśli jest obowiązkowe dla spraw, to również dla należących do nich czynności).
* **Wnioskodawca pierwotny** – osoba, która złożyła początkowy wniosek. Dla danego elementu pracy może być tylko jeden wnioskodawca pierwotny, a wartość ta jest niezależna od tagu „Wnioskodawca”. Jako wnioskodawca pierwotny zostanie automatycznie ustawiony prawidłowy kontakt, którego wiadomość e-mail dała początek elementowi pracy, albo pierwsza osoba, która zostanie ręcznie ustawiona jako „Wnioskodawca”. Tagu „Wnioskodawca pierwotny” nie da się zmienić, a oznaczonego nim kontaktu nie można usunąć z elementu pracy.
* **Wnioskodawca** – osoba będąca autorem zgłoszenia. Dla danego elementu pracy może być tylko jeden wnioskodawca. Dla zapytań wskazanie tego kontaktu jest obowiązkowe. W zależności od ustawień w Builderze, wskazanie tego kontaktu może, ale nie musi być obowiązkowe dla spraw (a jeśli jest obowiązkowe dla spraw, to również dla należących do nich czynności).
* **Podmiot** – osoba, której dotyczy czynność (nie musi to być ani kontakt główny, ani wnioskodawca pierwotny, ani wnioskodawca). Dla danego elementu pracy może być tylko jeden podmiot.

Bardzo często we wszystkich powyższych przypadkach wskazana będzie ta sama osoba. W przypadku oznaczenia którymś z tych systemowych tagów domyślnych kolejnego kontaktu, zostanie on usunięty z poprzedniego, ponieważ tagi tego rodzaju może posiadać tylko jeden kontakt na każdy element pracy.

Pierwszy kontakt dodany ręcznie zostanie domyślnie ustawiony jako kontakt główny, wnioskodawca i podmiot, ale tagi te można później przypisać do innych kontaktów.

* DW – wszelkie inne osoby, które mogą być uwzględniane w korespondencji. Jeśli kontakt jest oznaczony tylko jako „DW”, będzie wyświetlany na osobnej liście (ukrytej do czasu wyboru dla danego elementu pracy kontaktu tego rodzaju).

## Przypisywanie do kontaktu dodatkowego tagu domyślnego

Oprócz systemowych tagów domyślnych (kontakt główny, podmiot, DW, wnioskodawca) do kontaktu można dodać kolejny tag domyślny, by ułatwić i przyspieszyć korzystanie z tej funkcjonalności podczas przetwarzania elementów pracy.

Przykład: wiedząc, że „Jane Smith” będzie brokerem dla każdego elementu pracy, do którego zostanie przypisana jako kontakt, można dodać do jej danych na liście kontaktów tag „broker”, który odtąd będzie podstawiany do elementu pracy przez system i użytkownik nie będzie musiał za każdym razem robić tego ręcznie.

Lista domyślnych tagów dostępnych do wyboru jest utrzymywana w Builderze w sekcji [„Ustawienia ogólne” >> „Tagi kontaktów”](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).

Tag domyślny można ustawić podczas dodawania nowego kontaktu do systemu,

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F5skmdjAzTzwy2F2dn0LH%2Fimage.png?alt=media&#x26;token=7d1f716c-2765-4037-9a0f-f08faf14a360" alt=""><figcaption></figcaption></figure>

Można to zrobić również przy okazji edycji istniejącego kontaktu na stronie „Kontakty”.

Atrybut „tag domyślny” można też edytować zbiorczo, to znaczy dla wielu kontaktów jednocześnie – wystarczy wybrać kontakty na siatce poświęconej im strony i kliknąć przycisk „Edytuj”, by otworzyć wyskakujące okienko „Edycja zbiorcza”.

<figure><img src="https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FrEP9U8qdxb8Jm5JZkT8T%2Fimage.png?alt=media&#x26;token=d5ed1266-6c00-4372-9d71-0a989d8432d6" alt=""><figcaption></figcaption></figure>

### Zachowanie domyślnego tagu kontaktu, gdy ustawienie „Dostępny dla wielu” jest wyłączone

Jeśli ustawienie „Dostępny dla wielu” jest w przypadku określonego tagu wyłączone, można go przypisać tylko do jednego kontaktu danego elementu pracy. Przykład: może się zdarzyć, że tylko jeden kontakt przypisany do danego zapytania może być oznaczony jako „broker”. Uderzy to w domyślne tagowanie, gdy dwa kontakty mające taki sam tag domyślny (który musi być unikalny) zostaną dodane do elementu pracy (zarówno ręcznie, jak i automatycznie). W takiej sytuacji system przypisze tag domyślny tylko jednemu kontaktowi i tym samym usunie go z pozostałych, którym przydzieli *inny* istniejący tag w następującej kolejności:

* kontakt główny;
* wnioskodawca;
* podmiot;
* DW;
* inny kontakt przypisany do danego elementu pracy.

### Dodatkowe uwagi dotyczące niedopasowania firmy dostawczej do tagów kontaktów:

* Nie da się dodać domyślnego tagu do kontaktu, jeśli firma, do której jest on przypisany, ma ustawioną inną firmę dostawczą niż tag domyślny.
* Nie da się przesłać elementu pracy z kontaktem, którego tag domyślny jest ustawiony na inną firmę dostawczą niż ta, która przypisana jest do elementu pracy.

## Automatyczne tagowanie kontaktów przypisanych do elementów pracy

### Kontakty podstawiane na podstawie pierwotnej wiadomości e-mail

**Znane kontakty**

Gdy wiadomość e-mail nadejdzie z adresu, który jest powiązany z już istniejącym w systemie kontaktem, a kontakt ten:

* ma ustawiony zakres globalny albo
* ma ustawiony zasięg lokalny, ale jest przypisany do tej samej firmy, do której należeć będzie element pracy (na podstawie ustawionych reguł przekierowania wiadomości e-mail),

wówczas jego dane są automatycznie wstawiane na karcie kontaktu podczas tworzenia elementu pracy przez system i jest on od razu tagowany jako kontakt główny, wnioskodawca pierwotny i wnioskodawca. Jeśli miał ustawiony tag domyślny, zostanie on również podstawiony. Warto jednak pamiętać, że po utworzeniu elementu pracy przypisane do niego tagi zawsze można edytować ręcznie.

Gdy wiadomość e-mail nadejdzie z adresu, który jest powiązany z już istniejącym w systemie kontaktem, ale kontakt ten ma ustawiony zakres lokalny i jest przypisany do *innej* firmy niż ta, do której należeć będzie dany element pracy (na podstawie ustawionych reguł przekierowania wiadomości e-mail), wówczas jego dane NIE BĘDĄ automatycznie wstawiane na karcie kontaktu podczas tworzenia elementu pracy przez system, a tym samym nie mogą być automatycznie oznaczone tagami. Trzeba jednak mieć na uwadze, że po utworzeniu elementu pracy przypisane do niego kontakty i tagi zawsze można edytować ręcznie.

**Nieznane kontakty**

*Domyślnie ustawiony zakres „Globalny” albo „Globalny i lokalny”*

Gdy nadejdzie wiadomość e-mail z adresu, którego nie ma w systemie, i:

* funkcja „[Włącz automatyczne tworzenie kontaktów](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)” jest włączona w Builderze i
* system został skonfigurowany w taki sposób, że zakres kontaktów zewnętrznych jest ustawiany na „**Globalny**” albo „**Globalny i lokalny**”,

wówczas kontakt zostanie utworzony automatycznie z zakresem globalnym (czyli nie będzie powiązany z żadną konkretną firmą), a jego dane zostaną automatycznie podstawione na karcie kontaktu podczas tworzenia elementu pracy przez system. Dodatkowo zostanie on oznaczony jako kontakt główny, wnioskodawca pierwotny oraz wnioskodawca tego elementu. Nie będzie posiadał tagu domyślnego, ponieważ do tej pory nie było go w systemie. Warto jednak pamiętać, że po utworzeniu elementu pracy przypisane do niego tagi zawsze można edytować ręcznie.

*Domyślnie ustawiony zakres lokalny*

Gdy nadejdzie wiadomość e-mail z adresu, którego nie ma w systemie, i:

* funkcja „[Włącz automatyczne tworzenie kontaktów](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)” jest włączona w Builderze i
* system został skonfigurowany w taki sposób, że zakres kontaktów zewnętrznych jest ustawiany na „**Lokalny**” ”,

wówczas kontakt zostanie utworzony automatycznie z zakresem lokalnym (czyli będzie powiązany z konkretną firmą) i przypisany zostanie do tej samej firmy, do której należy element pracy. Jego dane zostaną automatycznie podstawione na karcie kontaktu podczas tworzenia elementu pracy przez system, a on sam będzie od razu oznaczony jako kontakt główny, wnioskodawca pierwotny oraz wnioskodawca tego elementu. Nie będzie posiadał tagu domyślnego, ponieważ do tej pory nie było go w systemie. Warto jednak pamiętać, że po utworzeniu elementu pracy przypisane do niego tagi zawsze można edytować ręcznie.

*Wyłączenie automatycznego tworzenia kontaktów*

Gdy nadejdzie wiadomość e-mail z adresu, którego nie ma w systemie, i:

* funkcja „[Włącz automatyczne tworzenie kontaktów](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)” jest WYŁĄCZONA w Builderze,

wówczas element pracy zostanie utworzony zgodnie z ustawionymi regułami przekierowania wiadomości e-mail, ale dane nadawcy NIE zostaną automatycznie wstawione na karcie kontaktu podczas tworzenia elementu pracy przez system (a tym samym nie mogą być automatycznie oznaczone tagami). Trzeba jednak pamiętać, że po utworzeniu elementu pracy przypisane do niego kontakty i tagi zawsze można edytować ręcznie.

### **Tagi kontaktu podstawione ze strony „Aktywność kontaktu”**

Z kolei gdy element pracy został utworzony za pomocą przycisku „Rozpocznij element pracy” na stronie „[Aktywność kontaktu](https://docs.enate.net/enate-help/polski/lacznosc/strona-aktywnosc-kontaktowa)”, kontakt ten zostanie oznaczony jako wnioskodawca pierwotny, wnioskodawca, podmiot i kontakt główny tego elementu. Dodany zostanie również tag domyślny, o ile został wcześniej ustawiony.
