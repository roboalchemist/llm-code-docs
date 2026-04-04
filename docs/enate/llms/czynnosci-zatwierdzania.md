# Source: https://docs.enate.net/enate-help/polski/przetwarzanie-dzialania/czynnosci-zatwierdzania.md

# Czynności zatwierdzania

## Czym są czynności zatwierdzania? Na czym to polega?

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==?utm_medium=iframely&utm_source=gitbook>" %}

Często w ramach przepływów spraw w procesach biznesowych tworzonych w Enate dochodzi do sytuacji, w których osoby z zewnątrz (tj. osoby pracujące poza systemem Enate, np. menedżerowie biznesowi w naszej firmie lub firmie klienta) muszą zatwierdzić działania, aby proces mógł być kontynuowany. Dobrym przykładem są procesy dotyczące wynagrodzeń, gdy osoby na kierowniczych stanowiskach po stronie klienta muszą zaakceptować zestawienia, zanim wypłaty będą mogły ruszyć.

Wbudowana w Enate czynność „Zatwierdzanie” umożliwia obsługę takich wniosków w bardziej zintegrowany sposób. Pozwala to zachować ścisłą kontrolę nad całym cyklem, a także łatwiej umiejscowić go w ramach przepływu podejmowanych działań.

## Jak to działa

Wnioski są wysyłane do agentów pracujących poza Enate w celu zatwierdzenia lub odrzucenia.

Rodzaj zatwierdzenia zależy od sposobu podejmowania decyzji:

* W scenariuszu wielopoziomowym wiadomość e-mail z wnioskiem jest wysyłana na kolejny poziom po uzyskaniu pomyślnej decyzji na poprzednim – maksymalnie do trzeciego poziomu. Jeśli na którymkolwiek z poziomów opinia będzie negatywna, cały wniosek zostanie odrzucony.
* W scenariuszu „dowolny równoległy” wiadomość e-mail z wnioskiem jest wysyłana do wszystkich osób zatwierdzających jednocześnie i decydujące znaczenie ma pierwsza odpowiedź.
* W scenariuszu „wszystkie równoległe” wiadomość e-mail z wnioskiem jest wysyłana do wszystkich osób zatwierdzających jednocześnie i WSZYSTKIE one muszą zatwierdzić wniosek. Jeśli opinia którejkolwiek z nich będzie negatywna, wniosek zostanie odrzucony.

Jeśli wniosek zostanie zatwierdzony przez wszystkie właściwe osoby, czynność zatwierdzania zostanie pomyślnie rozwiązana i automatycznie zamknięta, zatem żaden agent nie będzie musiał zajmować się nią w Work Managerze. Zamkniętą czynność można jednak w każdej chwili ręcznie otworzyć i przejrzeć.

## Wyjątki (rozpatrywane przez agenta w Work Managerze)

Może się zdarzyć, że do kontynuowania czynności zatwierdzania konieczne będzie zaangażowanie agenta w Work Managerze. Dochodzi do tego, gdy:

* zatwierdzenie zostało odrzucone;
* nie udało się automatycznie wskazać osób zatwierdzających (lub wskazano ich zbyt mało).

## Wniosek o zatwierdzenie został odrzucony

Gdyby wniosek o zatwierdzenie został **odrzucony**, czynność przejdzie w stan „Do zrobienia” i będzie musiała zostać rozpatrzona przez agenta w Work Managerze. Powinien on zapoznać się z powodem odrzucenia przez osobę zatwierdzającą i zdecydować, co dalej. Może wówczas wybrać jedną z poniższych możliwości:

1. **Zaktualizowanie zgodnie z uwagami i ponowne przesłanie wniosku poprzez ustawienie czynności statusu „Oczekuje”**. Spowoduje to ponowne automatyczne wysłanie wiadomości e-mail z wnioskiem o zatwierdzenie\*\* i ustawienie czynności statusu „Oczekuje na więcej informacji” – czekamy, aż do systemu wpłynie informacja z zewnątrz (odpowiedź w kwestii zatwierdzenia), zanim będzie można kontynuować przetwarzanie elementu pracy.
2. **Oznaczenie czynności jako „Nie można zakończyć”**. Właściciel sprawy zostanie wówczas powiadomiony o sytuacji i będzie musiał podjąć decyzję o dalszych krokach (np. czy trzeba przerobić sprawę, czy zupełnie ją zamknąć).
3. **Oznaczenie czynności jako „Rozwiązane”** – jest to ręczne zatwierdzenie wniosku. Sprawa przejdzie wówczas do następnej czynności.

{% hint style="info" %}
\*\* Uwaga: wysyłanie e-maili z wnioskiem rozpocznie się od początku – wszystkie osoby zatwierdzające otrzymają nowe wiadomości. Jeśli otworzą którąś z wcześniejszych wiadomości, zobaczą komunikat z informacją, że ten konkretny wniosek o zatwierdzenie jest już nieważny, ponieważ jego szczegóły mogły ulec zmianie.
{% endhint %}

## Niewystarczająca liczba osób zatwierdzających

W sytuacji, gdy agent musi dodać osoby zatwierdzające, ponieważ jedno lub więcej miejsc jest pustych (albo gdy dokona zmian, w wyniku których trzeba będzie ponownie wysłać wnioski o zatwierdzenie), zajmie się czynnością zatwierdzania w stanie „Do zrobienia”. Po dokonaniu wszystkich korekt lub uzupełnieniu brakujących osób zatwierdzających agent musi **ustawić czynności status „Oczekuje”**. Wiadomości z wnioskiem o zatwierdzenie zostaną wówczas ponownie automatycznie wysłane, a status czynności zmieni się na „Oczekuje na więcej informacji”, ponieważ do kontynuowania prac niezbędne będą informacje z zewnątrz (czyli zatwierdzenie wniosku).

{% hint style="info" %}
Uwaga: gdy status czynności zatwierdzania to „Do zrobienia” albo „W toku”, zewnętrzne strony, które otrzymały wiadomości z wnioskiem, NIE będą mogły go zatwierdzić ani odrzucić. Zamiast tego otrzymają informację, że dany element pracy jest aktualnie przetwarzany. Agenci obsługujący Work Managera muszę przenieść czynność z powrotem do stanu „Oczekuje na więcej informacji”, żeby czynność zatwierdzania mogła zostać wznowiona.
{% endhint %}

## Wygaśnięcie wniosku o zatwierdzenie

Może się też zdarzyć, że czynność zatwierdzania wygaśnie i zostanie automatycznie zamknięta – dzieje się tak, gdy nie otrzymano żadnych (lub otrzymano niewystarczającą liczbę) odpowiedzi na czas. W takiej sytuacji czynność automatycznie otrzyma status „Rozwiązane”, a sprawa będzie rozpatrywana dalej. Żaden agent nie będzie musiał zajmować się nią w Work Managerze, można ją jednak w każdej chwili ręcznie otworzyć i przejrzeć.
