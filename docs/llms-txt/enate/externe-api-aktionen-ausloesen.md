# Source: https://docs.enate.net/enate-help/deutsch/bearbeitung-einer-aktion/externe-api-aktionen-ausloesen.md

# Externe API-Aktionen auslösen

Ähnlich wie andere Aktionsarchetypen können 'Trigger External API'-Aktionen in Case Prozessen verwendet werden und kommen zum Einsatz, wenn Sie automatisch ein anderes System aufrufen müssen, Daten übertragen und das externe System dazu zu bringen, aktualisierte benutzerdefinierte Daten zurück nach Enate zu übertragen.

Informationen zur Konfiguration von 'Trigger External API' Actions finden Sie in diesem [Builder ](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/info-section/external-api-action-info-tab)Abschnitt.

Manchmal kann es zu einer Verzögerung kommen, wenn man auf die Antwort des externen Systems wartet. Wenn dies der Fall ist, d. h. wenn die Aktion "Externe API auslösen" auf die Rückmeldung eines externen Systems wartet, wird auf der Infokarte der Aktion im Work Manager der Status "Warten" angezeigt

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Md2H6VBAXaSevf8ndNc%2F-Md2IBB9Srk02uF2L-yQ%2Fimage.png?alt=media\&token=f00b4b89-065b-4cc0-b13c-18c31a5ec0ed)

Wenn das externe System schließlich mit der Datenaktualisierung an Enate antwortet, wird dies mit einer Markierung versehen, die angibt, ob die Aktualisierung erfolgreich oder nicht erfolgreich war:

#### Antwort mit erfolgreicher Beendigung

Wenn das System antwortet, um mitzuteilen, dass es erfolgreich war, wird die Aktion automatisch in den Status "Abgeschlossen" mit der Lösungsmethode "Erfolgreich abgeschlossen" übergehen.&#x20;

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FJHmAc110jhkH2anxjQ3B%2Fimage.png?alt=media\&token=63c94b6c-5708-4e35-afca-7a8a9991dcdb)

#### Antwort bei nicht erfolgreicher Beendigung.

Wenn das System antwortet, dass die Aktion nicht erfolgreich abgeschlossen werden konnte, geht die Aktion in den den Status "Zu erledigen" mit dem Grund "Aktualisiert durch Integration". Die externe API kann auch mit zusätzlichen Informationen darüber antworten, warum die Aktion nicht erfolgreich war. Diese Informationen werden auf der Infokarte der Aktion im Abschnitt "Abgelehnter Grund" angezeigt.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2F9I4onlcXbFcM9J1dcEtv%2Fimage.png?alt=media\&token=5f8630d3-fb82-4330-8719-51356dc45ee3)

Wenn die Aktion nicht erfolgreich war, weil sie nicht innerhalb der für sie festgelegten Zeit abgeschlossen wurde ([im Builder konfiguriert](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/info-section/external-api-action-info-tab)), dann wird sie in den Status "Zu erledigen" mit dem Grund "Zeitüberschreitung" versetzt und wird einer Warteschlange/einem menschlichen Benutzer basierend auf den konfigurierten Zuweisungsregeln zugewiesen.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2F6RzzjEYKfnIitGL4aqjv%2Fimage.png?alt=media\&token=09d80fd7-46ee-496a-b9bc-2f5b18368f7f)

Solche erfolglosen Aktionen verhalten sich nun effektiv wie eine manuelle Standardaktion.&#x20;

{% hint style="info" %}
Bitte beachten Sie, dass der Fallinhaber in diesen Fällen NICHT benachrichtigt wird.
{% endhint %}

### Automatische Wiederholungsversuche

Wenn die Aktion nicht in der Lage ist, sich mit dem externen System zu verbinden, wird sie automatisch versuchen eine bestimmte Anzahl von Verbindungsversuchen, je nachdem, wie Ihr System in Builder Builder konfiguriert wurde ([siehe hier für weitere Informationen](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)). Es wird auch eine Fehlermeldung in der Aktionsleiste angezeigt:&#x20;

* wann der Fehler aufgetreten ist
* wann das System erneut versucht
* automatisch eine Verbindung herzustellen wie oft das System automatisch versucht hat, eine Verbindung herzustellen
* und wie oft das System den Verbindungsaufbau automatisch wiederholen wird.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FbLq4fwohuJTxwcDfdvKw%2Fimage.png?alt=media\&token=5e5dbab7-2cb0-4f2c-b1ac-828b9dd26b19)

Sie können den Verbindungsaufbau auch von hier aus manuell wiederholen, indem Sie auf den Link 'Wiederholen' in der Fehlermeldung klicken.

{% hint style="info" %}
Bitte beachten Sie, dass ein manueller Wiederholungsversuch als ein Wiederholungsversuch gezählt wird und daher in der Zahl enthalten ist, die angibt, wie viele wie oft das System "automatisch" versucht hat, eine Verbindung herzustellen.
{% endhint %}

Wenn die Aktion nach den automatischen Wiederholungsversuchen keine Verbindung herstellen kann (z. B. wenn die Einstellung für Wiederholungen (z. B. wenn die Wiederholungen auf 5 eingestellt sind und das System nach 5 automatischen Versuchen keine Verbindung herstellt) Wiederholungsversuche), wird sie in den Zustand "Geschlossen" mit der Auflösungsmethode "Nicht erfolgreich abgeschlossen'.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Md2H6VBAXaSevf8ndNc%2F-Md2IFtN9PzOC77AnpuG%2Fimage.png?alt=media\&token=e799e470-9dd9-4e51-8162-b040df26ccb6)

{% hint style="info" %}
Wenn die Aktion nicht in der Lage ist, eine Verbindung mit dem externen System herzustellen, wird dies an den Fallverantwortlichen weitergeleitet, wobei im Abschnitt Aktion des Fallbildschirms hervorgehoben, dass diese Aktion abgeschlossen wurde - nicht erfolgreich.
{% endhint %}

Wenn die Aktion die erforderlichen Informationen erhält, wird sie automatisch geschlossen.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FwiJkEEYugrnixOG7sMy6%2Fimage.png?alt=media\&token=8cbf58be-0fc2-413b-a38a-3eb830eefbd6)

#### Anpassen der Wiederholungseinstellungen in Builder während/nach Beginn der Wiederholungen

Wenn die Einstellung für die automatische Wiederholung in Builder geändert wird, nachdem das System automatisch versucht hat versucht hat, eine Verbindung mit einem externen System herzustellen, geschieht Folgendes:

Wenn die Einstellung für die Wiederholungsversuche ursprünglich auf 5 eingestellt war und das System automatisch fünfmal versucht hat 5 Mal versucht hat, eine Verbindung herzustellen, dies aber fehlgeschlagen ist, geht die Aktion in den Zustand Geschlossen mit einer Fehlermeldung, die einen Wiederholungsversuch von 5/5 anzeigt.

Wird die Einstellung für die Wiederholungen anschließend auf einen Wert über 5, z. B. 7, erhöht, zeigt die Fehlermeldung eine Anzahl von Wiederholungsversuchen von 5/7 an, aber das System wird NICHT automatisch versuchen eine Verbindung zum 6. und 7. Mal herzustellen, da die Aktion bereits abgeschlossen ist.

Wenn die Aktion jedoch noch nicht in den Zustand "Abgeschlossen" übergegangen ist, weil sie noch nicht die maximale Anzahl automatischer Wiederholungsversuche erreicht hat (z. B. nur 4 von 5 Wiederholungsversuchen), dann bedeutet die Erhöhung der Einstellung für Wiederholungsversuche auf 7, dass die Aktion die Verbindung automatisch so lange wiederholt, bis die Zahl 7 erreicht ist.

Wenn Sie dagegen die Anzahl der Wiederholungen verringern, nachdem die Wiederholungen bereits begonnen haben, z. B. wenn Sie 4 von 10 eingestellt haben, dann aber die maximale Anzahl auf 4 verringern, zeigt das System immer noch 4 von 10 an, wird aber tatsächlich geschlossen.
