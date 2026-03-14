# Source: https://docs.enate.net/enate-help/deutsch/bildschirme-alle-arbeitsauftrags-typen/prognosen-fur-falle.md

# Prognosen für Fälle

## Überblick <a href="#overview" id="overview"></a>

Nutzer:innen der v2024.1 können die Funktion „Aufwandsschätzung“ verwenden, um präzisere Aufwandsschätzungen für Arbeitsaufträge zu erhalten, was effektiveres Ressourcenmanagement möglich macht.

Langfristig gesehen können diese Daten gesammelt und an Administrator:innen zurückgemeldet werden, damit sie Zeiteinschätzungen anpassen und zukünftig präzisere Arbeitsaufwandsprognosen abgeben können.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2Fb8NiA8wmifLDaNmbcQSF%2Fimage.png?alt=media&#x26;token=5dfa334e-6cdb-4222-b1cb-a606805ba36a" alt=""><figcaption></figcaption></figure>

### Wie man „Prognosen“ verwendet

Sobald die Prognose-Funktion aktiviert wurde, erscheint in Fällen im Arbeitsmanager eine neue Registerkarte namens „Aufwandsschätzung“.

Dort sehen Sie eine Zusammenfassung des geschätzten Aufwands für den gesamten Fall, eine Aufschlüsselung der Aktionen und Unterfälle, aus denen der Fall besteht, und eine Aufschlüsselung des geschätzten Aufwands für noch nicht erstellte Arbeitsaufträge.

#### Zusammenfassung des Fallaufwands

Im Abschnitt „Zusammenfassung des Fallaufwands“ können Nutzer:innen den geschätzten Aufwand eines Falls ändern. Dort finden Sie auch andere nützliche Metriken des Falls.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2Fw1p1OQUxMKPXCWjVAuKR%2Fimage.png?alt=media&#x26;token=6179ff11-4158-4aa5-9cbd-00b16d592c76" alt=""><figcaption></figcaption></figure>

* Der „geschätzte“ Aufwand zeigt, wie viel Gesamtaufwand vermutlich für die Erledigung des Falls erforderlich sein wird. Nutzer:innen können diesen Wert mit einer genaueren Schätzung ersetzen.
  * Die Summe des „geschätzten“ Aufwands aller erstellten und noch zu erstellenden Aktionen (und Unterfallaktionen) für einen Fall ergibt den Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“.
  * In diesem Feld wird zunächst dieser Wert angezeigt, der sich mit der Anleitung [Anfänglich geschätzter Aufwand pro Datensatz](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) errechnen lässt und im Builder zu finden ist (falls es einen gibt), und mit der [Anzahl der Datensätze](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements) multipliziert.
    * Wird die „Anzahl der Datensätze“ aktualisiert, wird auch der „geschätzte Aufwand“ für den Fall aktualisiert, selbst wenn dieser noch nicht von einer/einem Arbeitsmanager-Nutzer:in aktualisiert wurde.
  * Sobald der Fall als „Erledigt“ oder „Geschlossen“ markiert wurde, kann der geschätzte Aufwand nicht mehr verändert werden.
  * Bitte beachten Sie, dass eine Erhöhung dieses Werts zu einer höheren Schätzung des „Aufwands für noch nicht erstellte Arbeitsaufträge“ führt und umgekehrt.
* Der „tatsächliche“ Aufwand gibt an, wie lange bereits an dem Fall gearbeitet wurde.
  * Dies ist die Summe des „tatsächlichen“ Aufwands für alle erstellten Aktionen und Unterfälle, aus denen dieser Fall besteht, entnommen aus den jeweiligen Zeittrackern.
* Der Wert „geschätzter verbleibender Aufwand“ zeigt an, wie lange vermutlich noch an diesem Fall gearbeitet werden muss.
  * Dies ist die Summe des „geschätzten verbleibenden“ Aufwands aller erstellten Aktionen und Unteraktionen, aus denen dieser Fall besteht, UND der geschätzten verbleibenden Zeit für die Arbeitsaufträge, die noch nicht erstellt wurden (daher kann dieser Wert von dem geschätzten Aufwand für den Fall minus dem tatsächlichen Aufwand abweichen).

Eine Änderung des Wertes „geschätzter“ Aufwand bei einem Fall hat folgende Auswirkungen:

* Der Wert [„Aufwand für noch nicht erstellte Arbeitsaufträge“](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases#effort-for-work-not-yet-created) wird automatisch aktualisiert. Das liegt daran, dass der „geschätzte Aufwand“ für den Fall sich aus der Summe des „geschätzten“ Aufwands aller erstellten Arbeitsaufträge und der Aktionen (und Unterfallaktionen), aus denen der Fall besteht, sowie dem „Aufwand für noch nicht erstellte Arbeitsaufträge“ zusammensetzt.&#x20;
  * Steigt der „geschätzte“ Aufwand eines Falls, steigt der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ um ebenso viel.
  * Sinkt der „geschätzte“ Aufwand eines Falls, sinkt der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ um ebenso viel.

#### Aufwandsaufschlüsselung für erstellte Arbeitsaufträge

Im Abschnitt „Aufwandsaufschlüsselung für erstellte Arbeitsaufträge“ können Nutzer:innen den geschätzten Zeitaufwand für einzelne Aktionen (und Unterfälle), aus denen der Fall besteht, anpassen. Hier werden auch andere nützliche Metriken für alle Aktionen (und Unterfälle) angezeigt, die zum Fall gehören.

Bitte beachten Sie, dass der geschätzte Aufwand nicht mehr verändert werden kann, sobald eine Aktion als „Erledigt“ oder „Geschlossen“ markiert wurde.

Beim Erstellen von Aktionen (und Unterfällen) wird der geschätzte Aufwand jeweils dem Wert „geschätzter Aufwand“ aus dem Abschnitt „Aufwand für noch nicht erstellte Arbeitsaufträge“ entnommen.

#### Aktionsaufschlüsselung

Bei jeder Aktion sehen Sie:

* Einen Link zu jeder Aktion.
* Den „geschätzten“ Aufwand, der anzeigt, wie viel Zeit insgesamt für die Aktion vorgesehen wird. Nutzer:innen können diesen Wert mit einer genaueren Schätzung ersetzen.&#x20;
  * In diesem Feld wird zunächst dieser Wert angezeigt, der sich mit der Anleitung [Anfänglich geschätzter Aufwand pro Datensatz](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) errechnen lässt und im Builder zu finden ist, und mit der [Anzahl der Datensätze](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements) multipliziert.&#x20;
    * Wird die „Anzahl der Datensätze“ aktualisiert, wird auch der „geschätzte Aufwand“ für alle Aktionen, die noch nicht von einer/einem Arbeitsmanager:in aktualisiert wurden, aktualisiert, um die veränderte Anzahl der Datensätze wiederzugeben.&#x20;
  * Steigt dieser Wert, sinkt der geschätzte Aufwand für „Noch nicht erstellte Arbeitsaufträge“ und umgekehrt, weshalb dies auch den Gesamtaufwand „geschätzter Fallaufwand“ beeinflussen könnte.
  * Bitte beachten Sie, dass der geschätzte Aufwand nicht mehr verändert werden kann, sobald eine Aktion als „Erledigt“ oder „Geschlossen“ markiert wurde.
* Der Wert „tatsächlicher“ Aufwand gibt an, wie lange bisher an einer Aktion gearbeitet wurde.&#x20;
  * Dieser Wert wird dem Zeittracker der Aktion entnommen.&#x20;
* Der Wert „geschätzter verbleibender Aufwand“ zeigt an, wie lange vermutlich noch an der Aktion gearbeitet werden muss.&#x20;
  * Dieser Wert ergibt sich, indem man den „tatsächlichen“ Aufwand der Aktion vom „geschätzten“ Aufwand subtrahiert.&#x20;
* Das Fälligkeitsdatum der Aktion
  * Falls der „tatsächliche“ Aufwand null ist, sehen Sie daneben die Information „Beginnen bis“. Dieser Wert zeigt Ihnen an, bis wann Sie spätestens mit der Arbeit an einer Aktion beginnen müssen, um das Fälligkeitsdatum einhalten zu können.
* Der Status der Aktion

Eine Änderung des Wertes „geschätzter“ Aufwand bei einer Aktion hat folgende Auswirkungen:

* Der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ für den Fall wird automatisch aktualisiert.
* Möglicherweise wird der „geschätzte“ Aufwand für den gesamten Fall automatisch aktualisiert.

Details:

* Sinkt der „geschätzte“ Aufwand einer Aktion, steigt der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Falls um ebenso viel (wobei der „geschätzte“ Aufwand für den gesamten Fall gleichbleibt).
* Steigt der „geschätzte“ Aufwand einer Aktion, sinkt der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Falls um ebenso viel. Dies könnte den „geschätzten“ Gesamtaufwand des Falls beeinflussen, aber nicht zwingend.
  * Sofern der „geschätzte Aufwand“ einer Aktion nicht ausreichend ansteigt, um den Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ für den Fall auf unter 0 zu senken, bleibt der „geschätzte“ Aufwand für den Fall unverändert.
    * Beispiel: Angenommen, der „geschätzte“ Aufwand einer Aktion 1 beträgt zwei Stunden, der „Aufwand für noch nicht erstellte Arbeitsaufträge“ beträgt eine Stunde und der „geschätzte Aufwand“ des Falls beträgt drei Stunden. Ein:e Nutzer:in entscheidet, dass Aktion 1 eine weitere Stunde in Anspruch nehmen wird und aktualisiert den „geschätzten“ Aufwand der Aktion 1 von zwei auf drei Stunden. Dann sinkt der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ von einer auf null Stunden, und der „geschätzte“ Aufwand des Falls bleibt unverändert bei drei Stunden.
  * Sofern der aktualisierte „geschätzte Aufwand“ einer Aktion ausreichend ansteigt, um den Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ für den Fall auf unter 0 zu senken, wird die Differenz zum „geschätzten Gesamtaufwand“ des Falls dazu addiert.&#x20;
    * Beispiel 1: Angenommen, ein Fall besteht aus nur einer Aktion namens Aktion 1. Betragen der „geschätzte“ Aufwand für Aktion 1 zwei Stunden und der „Aufwand für noch nicht erstellte Arbeitsaufträge“ null Stunden, dann beträgt der „geschätzte Aufwand“ für den Fall insgesamt zwei Stunden. Ein:e Nutzer:in entscheidet, dass Aktion 1 eine weitere Stunde in Anspruch nehmen wird und aktualisiert daher den „geschätzten“ Aufwand für Aktion 1 von zwei auf drei Stunden. Da der „Aufwand für noch nicht erstellte Arbeitsaufträge“ null ist, steigt der „geschätzte“ Gesamtaufwand für den Fall um eine Stunde, von zwei auf drei Stunden.
    * Beispiel 2: Angenommen, ein Fall besteht aus nur einer Aktion namens Aktion 1. Betragen der „geschätzte“ Aufwand für Aktion 1 zwei Stunden und der „Aufwand für noch nicht erstellte Arbeitsaufträge“ eine Stunde, dann beträgt der „geschätzte Aufwand“ für den Fall insgesamt drei Stunden. Ein:e Nutzer:in entscheidet, dass Aktion 1 zwei weitere Stunden in Anspruch nehmen wird und aktualisiert daher den „geschätzten“ Aufwand für Aktion 1 von zwei auf vier Stunden, wodurch der „Aufwand für noch nicht erstellte Arbeitsaufträge“ um eine Stunde, von einer auf null sinkt (so weit wie möglich). Die „verbleibende“ eine Stunde wird effektiv zum „geschätzten“ Gesamtaufwand des Falls addiert, der um eine Stunde von drei auf vier steigt.

#### Unterfall-Aufschlüsselung

Wird ein Unterfall erstellt, sehen Sie:

* Einen Link zu dem Unterfall, sofern Sie die Zugangsberechtigung dazu haben (sonst sehen Sie nur den Namen und die Referenznummer des Unterfalls ohne Link).
* Eine Reihe „gesamt“ zum Unterfall mit den folgenden Informationen:
  * Der „geschätzte“ Aufwand zeigt, wie viel Gesamtaufwand vermutlich für die Erledigung des Unterfalls erforderlich sein wird. Nutzer:innen können diesen Wert mit einer genaueren Schätzung ersetzen.&#x20;
    * Dies ist die Summe des „geschätzten“ Aufwands aller erstellten und noch zu erstellenden Aktionen, aus denen der Unterfall besteht.
    * In diesem Feld wird zunächst dieser Wert angezeigt, der sich mit der Anleitung [Anfänglich geschätzter Aufwand pro Datensatz](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) errechnen lässt und im Builder zu finden ist, und mit der [Anzahl der Datensätze](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements) multipliziert.
      * Wird die „Anzahl der Datensätze“ aktualisiert, wird auch der „geschätzte Aufwand“ für den Unterfall, der noch nicht von einer/einem Arbeitsmanager:in aktualisiert wurde, aktualisiert, um die veränderte Anzahl der Datensätze wiederzugeben.&#x20;
    * Sobald ein Unterfall als „Erledigt“ oder „Geschlossen“ markiert wurde, kann der geschätzte Aufwand nicht mehr geändert werden.
    * Bitte beachten Sie, dass eine Erhöhung dieses Werts zu einer höheren Schätzung des „Aufwands für noch nicht erstellte Arbeitsaufträge“ innerhalb eines Unterfalls führt und umgekehrt.&#x20;
  * Der Wert „tatsächlicher“ Aufwand gibt an, wie lange bisher an einem Unterfall gearbeitet wurde.&#x20;
    * Dies ist die Summe des „tatsächlichen“ Aufwands aller erstellten und noch zu erstellenden Aktionen, aus denen der Unterfall besteht, entnommen aus den jeweiligen Zeittrackern.&#x20;
  * Der „geschätzte“ Aufwand, zeigt an, wie viel Zeit insgesamt für den Unterfall vorgesehen wird.&#x20;
    * Dies ist die Summe des „geschätzten verbleibenden“ Aufwands aller erstellten Aktionen, aus denen dieser Unterfall besteht, UND der geschätzten verbleibenden Zeit für die Arbeitsaufträge, die noch nicht für den Unterfall erstellt wurden (daher kann dieser Wert von dem geschätzten Aufwand für den Unterfall minus dem tatsächlichen Aufwand des Unterfalls abweichen).
    * Das Fälligkeitsdatum des Unterfalls
    * Der Status des Unterfalls
* Eine Reihe für jede Unterfall-Aktion mit den folgenden Informationen:
  * Der „geschätzte“ Aufwand zeigt an, wie viel Zeit insgesamt für die Unterfall-Aktion vorgesehen wird. Nutzer:innen können diesen Wert mit einer genaueren Schätzung ersetzen.
    * In diesem Feld wird zunächst dieser Wert angezeigt, der sich mit der Anleitung [Anfänglich geschätzter Aufwand pro Datensatz](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements) errechnen lässt und im Builder zu finden ist, und mit der [Anzahl der Datensätze](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements) multipliziert.&#x20;
      * Wird die „Anzahl der Datensätze“ aktualisiert, wird auch der „geschätzte Aufwand“ für alle Unterfall-Aktionen, die noch nicht von einer/einem Arbeitsmanager:in aktualisiert wurden, aktualisiert, um die veränderte Anzahl der Datensätze wiederzugeben.&#x20;
    * Steigt dieser Wert, sinkt der geschätzte Aufwand für „noch nicht erstellte Arbeitsaufträge“ und umgekehrt, weshalb dies auch den Gesamtaufwand „geschätzter Unterfallaufwand“ beeinflussen könnte.&#x20;
    * Sobald eine Aktion als „Erledigt“ oder „Geschlossen“ markiert wurde, kann der geschätzte Aufwand nicht mehr geändert werden.
  * Der Wert „tatsächlicher“ Aufwand gibt an, wie lange bisher an einer Unterfallaktion gearbeitet wurde.&#x20;
    * Dieser Wert wird dem Zeittracker der Unterfallaktion entnommen.&#x20;
  * Der Wert „geschätzter verbleibender Aufwand“ zeigt an, wie lange vermutlich noch an der Unterfallaktion gearbeitet werden muss.&#x20;
    * Er wird berechnet, indem man den „tatsächlichen“ Aufwand der Unterfallaktion vom „geschätzten“ Aufwand subtrahiert.
  * Das Fälligkeitsdatum der Unterfallaktion&#x20;
    * Falls der „tatsächliche“ Aufwand null ist, sehen Sie daneben die Information „Beginnen bis“. Dieser Wert zeigt Ihnen an, bis wann Sie spätestens mit der Arbeit an einer Unterfallaktion beginnen müssen, um das Fälligkeitsdatum einhalten zu können.
  * Der Status der Unterfallaktion
* Eine Reihe für „noch nicht erstellte Unterfall-Arbeitsaufträge“ mit den folgenden Informationen:
  * Der „geschätzte“ Aufwand zeigt, wie viel geschätzter Aufwand für die Erledigung der Unterfallaktionen, die noch nicht für den Unterfall erstellt wurden, insgesamt erforderlich sein wird. Nutzer:innen können diesen Wert mit einer genaueren Schätzung ersetzen.&#x20;
    * Eine Änderung dieser Schätzung beeinflusst den Gesamtaufwand „geschätzter Unterfallaufwand“ und kann die Aufwandseinschätzung für den gesamten Fall beeinflussen.

Eine Änderung des Wertes „geschätzter“ Aufwand bei einer Unterfallaktion hat folgende Auswirkungen:

* Der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ für den Unterfall wird automatisch aktualisiert.
* Möglicherweise wird der „geschätzte“ Aufwand für den gesamten Unterfall automatisch aktualisiert.
* Möglicherweise wird der „geschätzte“ Aufwand für den gesamten Elternfall automatisch aktualisiert.

Details:

* Sinkt der „geschätzte“ Aufwand einer Unterfallaktion, steigt der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls um ebenso viel (wobei der „geschätzte“ Aufwand für den gesamten Unterfall gleichbleibt, weshalb die Änderung keinen Einfluss auf den „geschätzten“ Aufwand des gesamten Elternfalls hat).
* Steigt der „geschätzte“ Aufwand einer Unterfallaktion, sinkt der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls um ebenso viel. Dies könnte den „geschätzten“ Gesamtaufwand des Falls beeinflussen, aber nicht zwingend.
  * Sofern der aktualisierte „geschätzte Aufwand“ einer Aktion nicht ausreichend ansteigt, um den Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ für den Unterfall auf unter null zu senken, wird der „geschätzte“ Aufwand des Unterfalls nicht beeinflusst (weshalb der „geschätzte“ Aufwand für den gesamten Elternfall nicht beeinflusst wird).
    * Beispiel: Angenommen, ein Unterfall besteht aus nur einer Aktion, die Unterfallaktion 1 heißt. Der „geschätzte“ Aufwand einer Unterfallaktion 1 beträgt zwei Stunden und der geschätzte „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls beträgt eine Stunde, beträgt der „geschätzte Aufwand“ des Unterfalls drei Stunden. Ein:e Nutzer:in entscheidet, dass Unterfallaktion 1 eine weitere Stunde in Anspruch nehmen wird und aktualisiert daher den „geschätzten“ Aufwand für Unterfallaktion 1 von zwei auf drei Stunden. Dadurch sinkt der „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls von einer Stunde auf null. Der „geschätzte“ Aufwand für den Unterfall bleibt unverändert bei drei Stunden (daher wird der „geschätzte“ Aufwand für den gesamten Elternfall nicht beeinflusst).
  * Sofern der aktualisierte „geschätzte Aufwand“ einer Unterfallaktion ausreichend ansteigt, um den Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ für den Unterfall auf unter null zu senken, wird die Differenz zum „geschätzten Gesamtaufwand“ des Unterfalls dazu addiert (weshalb dies auch den „geschätzten“ Gesamtaufwand für den ganzen Elternfall beeinflussen könnte).
    * Beispiel 1: Angenommen, ein Unterfall besteht aus nur einer Aktion, die Unterfallaktion 1 heißt. Der „geschätzte“ Aufwand für Unterfallaktion 1 beträgt zwei Stunden und der geschätzte „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls beträgt null Stunden, weshalb der „geschätzte“ Gesamtaufwand“ für den Unterfall zwei Stunden beträgt. Ein:e Nutzer:in entscheidet, dass Unterfallaktion 1 eine weitere Stunde in Anspruch nehmen wird und aktualisiert daher den „geschätzten“ Aufwand für Unterfallaktion 1 von zwei auf drei Stunden. Weil der „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls dadurch auf null sinkt, steigt der „geschätzte“ Aufwand für den Unterfall um eine Stunde, von zwei auf drei.
      * Wenn der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Elternfalls ausreichend hoch ist, könnte diese eine Stunde dort abgezogen werden, weshalb der „geschätzte“ Aufwand des gesamten Elternfalls unverändert bleibt.
      * Wenn der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Elternfalls nicht ausreichend hoch ist, wird durch diese Erhöhung um eine Stunde auch der „geschätzte“ Aufwand des gesamten Elternfalls ansteigen.
    * Beispiel 2: Angenommen, der Unterfall besteht nur aus einer Aktion, die Unterfallaktion 1 heißt. Der „geschätzte“ Aufwand für Unterfallaktion 1 beträgt zwei Stunden und der geschätzte „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls beträgt eine Stunde, weshalb der „geschätzte“ Gesamtaufwand des Elternfalls drei Stunden beträgt. Ein:e Nutzer:in entscheidet, dass Unterfallaktion 1 zwei weitere Stunden in Anspruch nehmen wird und aktualisiert daher den „geschätzten“ Aufwand für Unterfallaktion 1 von zwei auf vier Stunden. Dadurch sinkt der „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Unterfalls um so viel wie möglich – in diesem Fall um eine Stunde, von einer auf null. Die „verbleibende“ eine Stunde wird effektiv zum „geschätzten“ Gesamtaufwand des Unterfalls addiert, der um eine Stunde von drei auf viert steigt.
      * Wenn der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Elternfalls ausreichend hoch ist, könnte diese eine Stunde dort abgezogen werden, weshalb der „geschätzte“ Aufwand des gesamten Elternfalls unverändert bleibt.
      * Wenn der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ des Elternfalls nicht ausreichend hoch ist, wird durch diese Erhöhung um eine Stunde auch der „geschätzte“ Aufwand des gesamten Elternfalls ansteigen.

#### Aufwand für noch nicht erstellte Arbeitsaufträge

Im Abschnitt „Aufwand für noch nicht erstellte Arbeitsaufträge“ wird angezeigt, wie viel geschätzter Aufwand für die Erledigung der Aktionen (und Unterfallaktionen), die noch nicht für den Fall erstellt wurden, erforderlich sein wird.

Der Wert wird berechnet, indem der „geschätzte“ Aufwand für erstellte Arbeitsaufträge vom „geschätzten“ Aufwand für den Fall subtrahiert wird. Daher steigt die Aufwandsschätzung des gesamten Falls, wenn der Wert „Aufwand für noch nicht erstellte Arbeitsaufträge“ erhöht wird und umgekehrt.

Beim Erstellen von Aktionen (und Unterfällen) wird der geschätzte Aufwand jeweils dem Wert „geschätzter Aufwand“ aus dem Abschnitt „noch nicht erstellte Arbeitsaufträge“ entnommen.

Sobald ein Fall als „Erledigt“ oder „Geschlossen“ markiert wurde, kann der „Aufwand für noch nicht erstellte Arbeitsaufträge“ nicht mehr geändert werden.
