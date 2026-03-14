# Source: https://docs.enate.net/enate-help/polski/przetwarzanie-dzialania/czynnosci-trigger-external-api.md

# Czynność „Uruchomienie zewnętrznego API”

Podobnie jak w przypadku innych typowych czynności, uruchomienia zewnętrznego API można użyć w toku sprawy, gdy trzeba połączyć się z innym systemem, przekazać do niego dane i ewentualnie pobrać z zewnętrznego systemu zaktualizowane niestandardowe dane z powrotem do Enate.

Więcej informacji na temat konfiguracji czynności uruchomienia zewnętrznego API można znaleźć w tej sekcji poświęconej [Builderowi](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab).

Czasami odpowiedź z systemu zewnętrznego może nadejść z opóźnieniem. W takiej sytuacji, gdy czynność „Uruchomienie zewnętrznego API” oczekuje na informacje z zewnętrznego systemu, na karcie informacyjnej czynności w Work Managerze zostanie wyświetlony status „Oczekuje”.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdNTEzkqnqlLaT80_qu%2F-MdNThtZg4y1_1HCPb4o%2Fimage.png?alt=media\&token=77f09628-16d4-45de-abab-07833aed1b0b)

Gdy z zewnętrznego systemu do Enate nadejdzie wreszcie odpowiedź z aktualizacją danych, będzie ona opatrzona znacznikiem informującym użytkownika, czy aktualizacja się powiodła, czy nie.

#### **Odpowiedź „Zakończono pomyślnie”**

Jeśli system w odpowiedzi zgłasza, że operacja zakończyła się powodzeniem, status czynności automatycznie zmieni się na „Zamknięta” z metodą rozwiązania „Zakończono pomyślnie”.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F2YcgpiS0BQTrjQDgrv7p%2Fimage.png?alt=media\&token=6dfc2052-d9c8-4626-b34d-12bf5dcd255a)

#### **Odpowiedź „Nie udało się zakończyć pomyślnie”**

Jeśli system w odpowiedzi zgłasza, że operacja nie zakończyła się powodzeniem, status czynności zmieni się na „Do zrobienia” z podaną przyczyną „Zaktualizowano przez integrację”. Zewnętrzny API może również wraz z odpowiedzią dostarczyć dodatkowych informacji o przyczynach niepowodzenia. Ta informacja zostanie wyświetlona na karcie informacyjnej czynności w sekcji „Powód odrzucenia”.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FCO9OzHTaj0t7EpbiBtaU%2Fimage.png?alt=media\&token=9c4d807b-386a-4d33-8c8e-76dd9912af99)

Jeśli czynności nie udało zakończyć się pomyślnie z powodu przekroczenia ustawionego czasu ([w Builderze](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab)), wówczas otrzyma ona status „Do zrobienia” z przyczyną „Koniec czasu” i zostanie przeniesiona do kolejki lub przekazana innemu użytkownikowi, w zależności od ustawionych reguł przenoszenia.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FalYbjIOTTdZbByzNKQkd%2Fimage.png?alt=media\&token=6b5b50c6-3c2e-4c20-816e-6b512310dfc4)

Czynności zakończone niepowodzeniem będą się zachowywać jak standardowe czynności wykonywane ręcznie.

{% hint style="info" %}
Należy pamiętać, że właściciel sprawy NIE będzie powiadomiony o takich przypadkach.
{% endhint %}

### **Automatyczne powtórzenia**    &#x20;

Jeśli czynność nie może połączyć się z systemem zewnętrznym, wówczas automatycznie ponowi próbę określoną liczbę razy, zależnie od tego, jak twój system został skonfigurowany w Builderze (więcej informacji znajdziesz [tutaj](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)). Zostanie również wyświetlony komunikat o błędzie, informujący:

* kiedy wystąpił błąd
* kiedy system automatycznie spróbuje ponownie nawiązać połączenie
* ile razy system automatycznie ponowił próbę nawiązania połączenia
* ile razy system automatycznie spróbuje ponownie nawiązać połączenie.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2Fe6v399fHuRzYLddYcvzy%2Fimage.png?alt=media\&token=f6d24f31-e955-4945-9b4f-5419f51d1c21)

Można również z tego miejsca ręcznie ponowić próbę nawiązania połączenia, klikając w odnośnik „Ponów” w wiadomości o błędzie.

{% hint style="info" %}
Należy pamiętać, że ręczne ponowienie próby liczy się jako podjęta próba i tym samym będzie uwzględnione w liczbie wskazującej, ile razy system „automatycznie” próbował nawiązać połączenie.
{% endhint %}

Jeśli czynność nie nawiąże połączenia po automatycznych ponownych próbach (np. jeśli liczba prób jest ustawiona na 5, a system nie nawiąże połączenia po 5 automatycznych próbach), status czynności automatycznie zmieni się na „Zamknięta” z metodą rozwiązania „Nie udało się zakończyć pomyślnie”.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2F82EfaECsPQl3WFN6mDjg%2Fimage.png?alt=media\&token=e0aa2dd8-088f-482d-9396-3d618cfbedbc)

{% hint style="info" %}
W sytuacji, gdy czynności nie uda się nawiązać połączenia z systemem zewnętrznym, element zostanie przekazany właścicielowi sprawy, a w sekcji czynności na ekranie sprawy zostanie zaznaczone, że czynność jest Zamknięta – Nie udało się zakończyć pomyślnie.
{% endhint %}

Gdy czynność otrzyma wymagane informacje, zostanie automatycznie zamknięta.

![](https://3451550126-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1360089290%2Fuploads%2FC87cFnMSppZ5Ww3TQmey%2Fimage.png?alt=media\&token=e889409b-5a60-41d8-8d34-891ead03a5bd)

#### **Dostosowywanie ustawień ponawiania w Builderze podczas / po rozpoczęciu ponawiania**

Jeśli ustawienia automatycznego ponawiania w Builderze zostaną zmienione *już po* *tym,* jak system podjął automatyczne próby nawiązania połączenia z systemem zewnętrznym, sytuacja może rozwinąć się następująco.

Jeśli na przykład ustawienie ponawiania było pierwotnie ustawione na 5 i system automatycznie ponawiał próbę nawiązania połączenia 5 razy, ale bez powodzenia, wtedy status czynności zmieni się na „Zamknięte” z komunikatem o błędzie i wskazaną liczbą prób wynoszącą 5/5.

&#x20;Jeśli ustawienie ponownych prób zostanie zwiększone do wartości powyżej 5, na przykład 7, w komunikacie o błędzie zostanie wyświetlona liczba ponownych prób wynosząca 5/7, ale system NIE spróbuje automatycznie ponowić próby nawiązania połączenia po raz szósty i siódmy, ponieważ czynność zostanie już zamknięta.

Jeśli jednak czynność nie przeszła do stanu „Zamknięte”, ponieważ nie osiągnęła maksymalnej liczby automatycznych ponownych prób (na przykład próbowała nawiązać połączenie tylko 4 razy z 5), wówczas zwiększenie liczby ponownych prób do 7 oznacza, że czynność będzie automatycznie ponawiać próbę nawiązania połączenia, dopóki licznik nie osiągnie 7.

I odwrotnie, zmniejszenie liczby prób już po ich rozpoczęciu (np. przy próbie 4 z 10 zmniejszono maksymalną liczbę prób właśnie do 4) sprawi, że system będzie pokazywał próbę 4 z 10, ale czynność w rzeczywistości będzie już zamknięta.
