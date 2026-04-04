# Source: https://docs.enate.net/enate-help/polski/przetwarzanie-dzialania/poczekaj-na-zakonczenie-czynnosci-w-sprawach-podrzednych.md

# Czynności „Czekaj na zakończenie spraw podrzędnych”

Czynność „Czekaj na zakończenie spraw podrzędnych” będzie oczekiwać na zakończenie określonej sprawy podrzędnej. Dopiero po tym możliwe będzie przejście sprawy do następnej czynności.

Informację o tym, że dana czynność jest czynnością typu „Czekaj na zakończenie spraw podrzędnych” znaleźć można na karcie informacyjnej czynności – potwierdza to status „Czynność czeka na zakończenie sprawy podrzędnej”.

Gdy czynność „Czekaj na zakończenie spraw podrzędnych” została uruchomiona i sprawa podrzędna, na której ukończenie czynność ma czekać, również została uruchomiona, wówczas czynność ta przejdzie w stan „Oczekuje”.

Gdy sprawa podrzędna zostanie zakończona, czynność „Czekaj na zakończenie spraw podrzędnych” zamknie się automatycznie.

Zostanie to odnotowane na osi czasu.

Jeśli nie ma żadnej sprawy podrzędnej, na którą ma oczekiwać czynność „Czekaj na zakończenie spraw podrzędnych” – nie została utworzona albo została rozwiązana przed uruchomieniem tej czynności, czynność „Czekaj na zakończenie spraw podrzędnych” otrzyma status „Do zrobienia” i zostanie przypisana do kolejki, by to użytkownik podjął decyzję o dalszych krokach.

Jeśli użytkownik spróbuje ustawić status czynności „Czekaj na zakończenie spraw podrzędnych” na „Oczekuje”, czynność zostanie zamknięta, ponieważ nie uruchomiono sprawy podrzędnej, na której zakończenie miałaby czekać.

Jeśli status czynności jest inny niż „Czekaj na zakończenie spraw podrzędnych”, a sprawa podrzędna, na zakończenie której oczekuje, została zakończona, wówczas na karcie informacyjnej pojawi się komunikat „Sprawa podrzędna została zakończona”.

Jeśli użytkownik ręcznie rozwiąże czynność „Czekaj na zakończenie spraw podrzędnych”, czynność zostanie oznaczona jako „Rozwiązana” bez zakończenia sprawy podrzędnej.

{% hint style="info" %}
Należy pamiętać, że jeśli system został skonfigurowany do automatycznego zamykania czynności „Czekaj na zakończenie spraw podrzędnych” (więcej informacji na ten temat można znaleźć tutaj), a nie ma żadnej sprawy podrzędnej, na którą ma czekać ta czynność  (ponieważ sprawa ta nie została utworzona albo została rozwiązana przed uruchomieniem tej czynności), czynność „Czekaj na zakończenie spraw podrzędnych” automatycznie zostanie zamknięta. Zostanie to odnotowane na osi czasu.
{% endhint %}
