# Source: https://docs.enate.net/enate-help/deutsch/bearbeitung-einer-aktion/e-mail-senden-und-e-mail-senden-und-warten-aktionen.md

# „E-Mail senden“ und „E-Mail senden und Warten“-Aktionen

## Überblick

Bei "E-Mail senden"-Aktionen versendet Enate automatisch eine E-Mail und die Aktion wird dann automatisch geschlossen. Arbeitsmanager-NutzerInnen sollten bei diesem Aktionstyp nichts machen müssen.

Bei „E-Mail schicken und warten“-Aktionen verschickt Enate automatisch eine E-Mail und die Aktion wird dann in den „Warte“-Zustand versetzt, bis eine Antwort erhalten wird. Sobald eine Antwort einlangt, wird die Aktion zur weiteren Bearbeitung in den „Zu erledigen“-Status versetzt.

Die EmpfängerInnen-Adresse und jegliche CC- oder BCC-Adressen der E-Mail werden im Builder konfiguriert – im unten verlinkten Artikel erfahren Sie mehr über das Konfigurieren von „E-Mail schicken“-Aktionen im Builder:&#x20;

{% embed url="<https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab>" %}

Sobald eine E-Mail verschickt wurde, erscheint ein Eintrag im Verlauf, der angibt wann, von wem, an wen, an welche CC- oder BCC-Adressen, und mit welchem Betreff die E-Mail verschickt wurde. Wenn Sie diese Anzeige expandieren, können Sie auch den Inhalt der E-Mail lesen.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FeogUgPXHYQ65R9N1XEPk%2Fimage.png?alt=media&#x26;token=2437fee6-8745-4990-ba4b-c4213f5ae72e" alt=""><figcaption></figcaption></figure>

## Ausnahmen

Wird eine ungültige EmpfängerInnen-, CC- oder BCC-E-Mail-Adresse verwendet, wird die „E-Mail schicken“/„E-Mail schicken und warten“-Aktion keine automatische E-Mail schicken können und die Aktion wird wieder in die Warteschlange verschoben.

Im Verlauf wird dann eine Warnung angezeigt:&#x20;

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FHcis0xoiLZaBR2n0r8KG%2Fimage.png?alt=media&#x26;token=94b0c264-bb2f-41d0-b04c-b59ecfd5b29d" alt=""><figcaption></figcaption></figure>

Der/die BesitzerIn des Falls kann die E-Mail dann entscheiden, ob er/sie die E-Mail manuelle verschicken möchte. Dazu müssen die E-Mail-Adressen korrigiert und der Inhalt manuell eingefügt werden. In so einem Fall sollten Sie Ihre/n SystemadministratorIn benachrichtigen, damit die E-Mail-Adresse korrigiert und zukünftige Fehler vermieden werden können.
