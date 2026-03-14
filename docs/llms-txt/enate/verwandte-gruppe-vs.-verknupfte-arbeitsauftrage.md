# Source: https://docs.enate.net/enate-help/deutsch/mit-verknuepften-arbeitsauftraegen-arbeiten/verwandte-gruppe-vs.-verknupfte-arbeitsauftrage.md

# Verwandte Gruppe vs. Verknüpfte Arbeitsaufträge

## Gruppe von verwandten Arbeitsaufträgen

Zusammenhängende Arbeitsaufträge sind eine eng miteinander verbundene Gruppe von Arbeitsaufträgen, die sich zwar gemäß ihrer eigenen Konfiguration verhalten, sich aber aktiv auf ihren "übergeordneten" Arbeitsauftrag auswirken - insbesondere wird der übergeordnete Arbeitsauftrag nicht abgeschlossen, bevor nicht alle seine "Kinder" abgeschlossen sind.

Kommunikationen werden automatisch zwischen Arbeitsaufträgen in der zugehörigen Gruppe ausgetauscht, so dass sie immer sichtbar sind, und wenn Sie auf eine E-Mail in einem Arbeitsauftrag antworten, ist die Antwort in allen anderen Arbeitsaufträgen zu sehen.

Außerdem werden Dateien, Links, Defekte, Smartcards und Kontakte automatisch zwischen allen Arbeitsaufträgen in der Gruppe ausgetauscht, so dass z. B. die Aktualisierung einer Datei in einem Arbeitsauftrag die Datei auch in allen anderen Arbeitsaufträgen in der verwandten Gruppe aktualisiert wird.

Gruppen von verwandten Arbeitsaufträgen umfassen:

* Ein Fall und seine Aktionen
* Ein Fall und sein(e) Unterfäll(e)
* Der verbleibende Vorgang und andere "gelöste" Vorgänge, wenn mehrere Vorgänge zusammengeführt wurden
* Ein 'untergeordneter' Fall und sein übergeordnetes Ticket, wenn ein Ticket in einen Fall umgewandelt wurde

{% hint style="info" %}
Beachten Sie, dass bei geteilten Tickets ein Schnappschuss der Dateien, Verknüpfungen, Fehler, Smartcards und Kontakte des übergeordneten Tickets auf die untergeordneten Tickets übertragen wird. Wenn Sie also beispielsweise eine Datei in einem Arbeitsauftrag aktualisieren, wird die Datei nicht in allen anderen Arbeitsaufträgen der entsprechenden Gruppe aktualisiert. Die übergeordnete Anfrage, die in den Zustand "Warten" versetzt wird, wird jedoch erst dann abgeschlossen, wenn alle ihre "untergeordneten" Anfragen abgeschlossen sind. Wenn die übergeordnete Anfrage eine eingehende E-Mail erhält, wird diese in die untergeordneten Anfragen kopiert und nicht geteilt.
{% endhint %}

## Verknüpfte Arbeitsaufträge

Wenn Arbeitsaufträge keine aktive Auswirkung aufeinander haben (d.h. sie sind nicht Teil einer Gruppe von verwandten Arbeitsaufträgen), aber dennoch eine lose Verbindung zwischen ihnen besteht und Sie in der Lage sein wollen, schnell von einem zum anderen zu springen, sollten Sie die Funktion "Verknüpfte Arbeitsaufträge" in Enate verwenden.

Arbeitsaufträge mit einer 'verknüpft'-Beziehung verhalten sich gemäß ihrer eigenen Konfiguration und müssen nicht auf die Fertigstellung des anderen warten, bevor sie selbst fertiggestellt werden können. Sie können jederzeit zwei oder mehr Arbeitsaufträge miteinander verknüpfen und es ist eine sehr nützliche, flexible Methode, um Arbeitsaufträge locker miteinander zu verbinden, so dass z.B. Mitarbeiter in verschiedenen Abteilungen leicht auf dem Laufenden bleiben können, wie andere Arbeiten im Zusammenhang mit dem Ticket/Fall, an dem sie gerade arbeiten, ablaufen.

Die Kommunikation wird auch nicht automatisch zwischen verknüpften Arbeitsaufträgen ausgetauscht, aber Sie können einen Schnappschuss der Kommunikation in einem Arbeitsauftrag in einen Arbeitsauftrag kopieren, mit dem er verknüpft ist.

Beachten Sie, dass Sie auch die Möglichkeit haben, E-Mails zwischen verknüpften Arbeitsaufträgen auszutauschen - [siehe hier für weitere Informationen zum Austausch von E-Mails zwischen verknüpften Arbeitsaufträgen](https://docs.enate.net/enate-help/deutsch/mit-verknuepften-arbeitsauftraegen-arbeiten/e-mails-zwischen-verknuepften-arbeitsauftraegen-teilen).

Außerdem werden die Dateien, Verknüpfungen, Defekte, benutzerdefinierten Daten und Kontakte nicht automatisch freigegeben, wenn Sie einen neuen verknüpften Arbeitsauftrag starten, aber Sie können wählen, ob Sie einen Schnappschuss von ihnen kopieren möchten. Alle Aktualisierungen, die an ihnen vorgenommen werden, werden in den anderen verknüpften Arbeitsaufträgen nicht berücksichtigt.

Arbeitsaufträge mit einer verknüpften Beziehung werden auf der Registerkarte "Verknüpfte Arbeitsaufträge" in Fällen und Tickets angezeigt.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FoUCIuiG6UgMz7gHVn3Uy%2F13%20Clicking-on-links-tab.gif?alt=media&#x26;token=52c86d94-413b-4c62-a7bf-9b5e8d3c60dd" alt=""><figcaption></figcaption></figure>

Diese Art der Verknüpfung ist nützlich, wenn z. B. das Fälligkeitsdatum eines Vorgangs nicht von der Fertigstellung einer anderen Arbeit (z. B. durch eine andere Abteilung) abhängt, aber es wird dennoch als nützlich angesehen, dass Personen, die an einem der beiden Vorgänge arbeiten, über die Aktivitäten des anderen informiert sind und, was wichtig ist, einen schnellen Zugriff auf den anderen Vorgang haben.

Arbeitsaufträge können auf folgende Weise miteinander verknüpft werden:

* Ein Fall oder ein Ticket wird direkt aus einem bestehenden Fall oder Ticket heraus gestartet.
* Manuelles Hinzufügen einer Verknüpfung von einem Fall/Ticket zu einem anderen bestehenden Fall oder Ticket.
