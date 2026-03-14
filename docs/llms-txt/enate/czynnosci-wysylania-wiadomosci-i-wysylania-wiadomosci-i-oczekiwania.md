# Source: https://docs.enate.net/enate-help/polski/przetwarzanie-dzialania/czynnosci-wysylania-wiadomosci-i-wysylania-wiadomosci-i-oczekiwania.md

# Czynności „Wyślij wiadomość e-mail” oraz „Wyślij wiadomość e-mail i czekaj”

## Przegląd

Czynność „Wyślij wiadomość e-mail” obejmuje automatyczne wysłanie e-maila przez Enate i następujące od razu po tym zamknięcie czynności. Użytkownicy Work Managera nie powinni być w żaden sposób zaangażowani w przebieg tego rodzaju czynności.

Z kolei czynność „Wyślij wiadomość e-mail i czekaj” polega na automatycznym wysłaniu e-maila przez Enate, po którym status czynności zmienia się na „Oczekuje” do czasu otrzymania odpowiedzi. Po jej nadejściu czynność przechodzi do stanu „Do zrobienia” w celu dalszego przetwarzania.

Adres DO oraz wszelkie adresy DW i UDW użyte podczas wysyłania wiadomości dodawane są w Builderze – więcej na temat konfiguracji czynności „Wyślij wiadomość e-mail” w Builderze można znaleźć w tym artykule:

{% embed url="<https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab>" %}

Gdy wiadomość zostanie wysłana, na osi czasu pojawi się wpis zawierający następujące informacje: data wysłania, nadawca i adresat, adresy DW i UDW, temat e-maila oraz – po rozwinięciu – jego treść.

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC1k6yxkA8RGOKK0huxob%2Fimage.png?alt=media&#x26;token=c5378c66-4216-4eea-a1c3-35847b0aed54" alt=""><figcaption></figcaption></figure>

## Wyjątki

W przypadku błędnego adresu DO, DW lub UDW wiadomość dla czynności „Wyślij wiadomość e-mail” / „Wyślij wiadomość e-mail i czekaj” nie zostanie automatycznie wysłana, a sama czynność trafi z powrotem do swojej kolejki.

Na osi czasu pojawi się wówczas ostrzeżenie:

<figure><img src="https://2979960330-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ft9LYFTaD3Z1TU8mIKeU1%2Fimage.png?alt=media&#x26;token=412e9ad4-9b89-4196-9613-cb625e1e17d0" alt=""><figcaption></figcaption></figure>

Jeśli właściciel sprawy podejmie decyzję o ręcznym wysłaniu wiadomości, będzie musiał poprawić adres i dodać treść e-maila. Powinien również zawiadomić administratora systemu, by ten mógł poprawić błędny adres e-mail. Zapobiegnie to powtarzaniu się takiego problemu w przyszłości.
