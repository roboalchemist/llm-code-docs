# Source: https://docs.enate.net/enate-help/deutsch/bearbeitung-einer-aktion/abbyy-flexicapture-aktionen.md

# ABBYY FlexiCapture-Aktionen

Enate bietet durch die Verwendung einer integrierten Aktion eine Anbindung an [ABBYY FlexiCapture](https://www.abbyy.com/flexicapture/) - ([hier ](https://docs.enate.net/enate-help/integrations/enate-integrations/ocr-integration/abbyy-integration)finden Sie eine Anleitung zur Erstellung und Konfiguration dieses neuen Aktionstyps).

Wenn eine ABBYY-Aktion für einen Fall ausgeführt wird, dann können die Dokumentanhänge des Falls an ABBY FlexiCapture übermittelt werden.

{% hint style="info" %}
Achtung: Es können nur Dateitypen verarbeitet werden, die von ABBYY ab Version 12 unterstützt werden. [Klicken Sie hier, um eine Liste der von ABBYY unterstützten Formate anzuzeigen](https://help.abbyy.com/en-us/flexicapture/12/standalone_operator/input_formats).&#x20;
{% endhint %}

Das System zeigt diese Nachricht an, während es darauf wartet, dass Sie Dokumente zur Verarbeitung an die ABBYY FlexiCapture-Engine senden:

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FU2TLZzxIthC8j345gUql%2Fimage.png?alt=media\&token=2594b408-9084-4b3a-bb1b-46c7e0114f1f)

Sie erhalten eine Bestätigung, wenn die Dokumente erfolgreich zur Verarbeitung an ABBYY übermittelt wurden:

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2F0a5lzVV7uRMxQjuMx1zT%2Fimage.png?alt=media\&token=6817681e-6010-4355-a364-8b208d57d899)

Der letzte Versuch ist der Zeitpunkt, zu dem das Dokument bzw. die Dokumente zur Verarbeitung an die ABBYY FlexiCapture-Engine gesendet wurden.&#x20;

Wenn die eingereichten Dokumente ein ungültiges Dateiformat hatten oder es Probleme mit der Formatierung des Dokuments selbst gab, gibt das System diese Meldung zurück:

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FqB00Yv09Olz9XJkHIsWz%2Fimage.png?alt=media\&token=89d62654-e905-4c87-9085-49f2b5aadb39)

## Automatische Wiederholungsversuche

Wenn ein Problem bei der Übermittlung von Dokumenten aufgetreten ist, wird das System automatisch eine bestimmte Anzahl von Übermittlungsversuchen, je nachdem, wie Ihr System in Builder konfiguriert wurde (weitere Informationen finden Sie [hier](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)), durchführen.

Wenn nach den automatischen Wiederholungsversuchen immer noch ein Problem mit der Übermittlung besteht (z. B. wenn die Einstellung für Wiederholungsversuche auf 5 gesetzt ist und das System nach 5 automatischen Wiederholungsversuchen keine Verbindung herstellen kann), wechselt die ABBYY-Aktion in den Status "Geschlossen".

{% hint style="info" %}
Wenn die Aktion keine Verbindung mit dem externen System herstellen kann, wird dies an den Fallbesitzer weitergeleitet, der im Abschnitt "Aktion" des Fallbildschirms darauf hingewiesen wird, dass die Aktion "Geschlossen - nicht erledigt" wurde.
{% endhint %}

## Validierung

Nachdem ein Dokument gescannt wurde, erstellt ABBYY eine Bewertung zur Einschätzung der Scanqualität. Wenn der Zuverlässigkeitswert über dem definierten Schwellenwert liegt, ist keine Überprüfung erforderlich, die Daten werden verarbeitet und die Aufgabe abgeschlossen. Wenn der Zuverlässigkeitswert unter einem bestimmten Schwellenwert liegt, ist eine menschliche Überprüfung erforderlich.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### Keine Verifizierung erforderlich <a href="#no-verification-required" id="no-verification-required"></a>

Eine Statusmeldung bestätigt, dass eine menschliche Validierung nicht erforderlich ist:

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2F4GtbXVr2J5AwQ1kqhWgv%2Fimage.png?alt=media\&token=39652d31-ebdb-443d-be80-aaa7d586f835)

Sobald die Verarbeitung abgeschlossen ist, wird die ABBYY-Aktion geschlossen. Exportierte Dateien werden an den Fall angehängt und sind in "Dateien" sichtbar.

{% hint style="info" %}
Hinweis: Wenn "Ausgabedatei-Tags" festgelegt wurden, wendet ABBYY das Ausgabetag auf alle verarbeiteten Dateien an, damit sie für nachfolgende Aktivitäten verwendet werden können.
{% endhint %}

### Menschliche Verifizierung erforderlich <a href="#human-verification-required" id="human-verification-required"></a>

Das System warnt Sie, wenn eine menschliche Überprüfung erforderlich ist:

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsusO6eKdgoonewdT2%2Fimage.png?alt=media\&token=92610229-5480-4882-896c-4bda4b286600)

Zusätzlich wird neben dem Aktionsstatus ein Hinweis angezeigt, dass in ABBYY eine manuelle Verifizierung durchgeführt werden muss, bevor Sie fortfahren:

Wenn Sie auf die Schaltfläche „Verifizieren" klicken, gelangen Sie zur von ABBYY-Überprüfungsfunktion, wo Sie die gescannten Dokumente überprüfen und die Informationen bei Bedarf anpassen können.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsuykc2DFaOX6-GsPY%2Fimage.png?alt=media\&token=27953730-e342-4885-9206-fae88572b769)

{% hint style="info" %}
Achtung: Für den Vollzugriff auf die Funktion ist ein gültiges ABBYY FlexiCapture-Konto mit Berechtigungen zur Durchführung der Verifizierung im gewählten Projekt erforderlich.
{% endhint %}

Sobald Sie eingeloggt sind, wird Ihnen das Verifizierungs-Fenstervon ABBY FlexiCapture angezeigt, in dem Sie die Informationen überprüfen und bei Bedarf anpassen können.

Die Verifizierungsfunktion besteht aus drei Abschnitten:

1. Seitenansicht des zu scannenden Dokuments.
2. Vergrößerung des zu scannenden Originaldokuments.
3. Ausgabedatei - also die gescannte Version des Originaldokuments.

Der gelb markierte Text in der Registerkarte des Originaldokuments sind die Daten, die ABBYY nicht lesen kann. Die Ausgabedatei zeigt dies in rot an.

Bestimmte Zeichen wie 'i' können auch im Abschnitt Ausgabedatei hervorgehoben werden, wenn ABBYY sich bei der gescannten Version unsicher ist.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx6MLiLXtXFAmC00W%2Fimage.png?alt=media\&token=adebd784-bdf7-4f4c-b696-4832e40c4ec2)

Wenn Sie die manuelle Überprüfung abgeschlossen haben, wird auf dem Bildschirm eine Bestätigung angezeigt. Es erfolgt aber auch der Hinweis, dass die Annahme für die Notwendigkeit eines manuellen Eingriffs bestand:

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FTSVxjbe3pwjTMYwwmOiZ%2Fimage.png?alt=media\&token=86f1f3d4-df37-4a4d-8d4a-d0f69fb3cc6d)

‌Sobald die Verarbeitung abgeschlossen ist, werden die exportierten Dateien an den Fall angehängt und sind in „Dateien“sichtbar.

Sie können die Aktion dann als abgeschlossen markieren.

{% hint style="info" %}
Hinweis: Wenn "Ausgabedatei-Tags" festgelegt wurden, wendet ABBYY das Ausgabetag auf alle verarbeiteten Dateien an, damit sie für nachfolgende Aktivitäten verwendet werden können.
{% endhint %}
