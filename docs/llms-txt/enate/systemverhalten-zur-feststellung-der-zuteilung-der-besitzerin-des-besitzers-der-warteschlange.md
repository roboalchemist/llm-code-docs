# Source: https://docs.enate.net/enate-help/deutsch/anhang/systemverhalten-zur-feststellung-der-zuteilung-der-besitzerin-des-besitzers-der-warteschlange.md

# Systemverhalten zur Feststellung, der Zuteilung, der Besitzerin/des Besitzers, der Warteschlange

Im Rahmen des Workflow-Managements von Tickets, Fällen und Aktionen evaluiert das Enate-System regelmäßig, wem ein Auftrag zugewiesen ist, wer ihn besitzt, und mit welcher Warteschlange der Arbeitsauftrag verknüpft ist. Es gibt detaillierte Regeln, die der Reihenfolge nach befolgt werden, um diese Dinge festzustellen.

Bevor Sie sich die Regeln ansehen, sollten Sie verstehen, wie und nach welchem übergeordneten Muster solche Arbeitsauftragszuweisungen evaluiert werden. Das funktioniert wie folgt:

1. Zuerst wird entschieden, [WANN evaluiert werden soll](#bestimmen-wann-eine-neu-evaluierung-stattfindet) – Im Prinzip passiert das immer dann, wenn der Status eines Arbeitsauftrages sich ändert.
2. Wenn das System entscheidet, dass es eine solche Auswertung vornehmen muss, wird zunächst [der Status/die Situation eines Arbeitsauftrages evaluiert, um zu bestimmen, welche der Zuweisungs-. Besitz- und Warteschlangen-Werte geändert und welche gelöscht werden müssen](#bestimmen-ob-zuweisungs-besitz-und-warteschlangen-werte-geaendert-oder-geloescht-werden-muessen).
3. [Wenn eine Umstellung nötig ist](#einstellen-wem-ein-arbeitsauftrag-zugewiesen-ist-wem-er-gehoert-und-mit-welcher-warteschlange-er-ver):
   1. Eine Warteschlange umzustellen, ist einfach – Wählen Sie einfach die betreffende Warteschlange aus der Zuweisungsregel aus (es gibt nur zwei verschiedene Warteschlangen-Zuweisungsregeln).
   2. Wenn es darum geht, wem ein Auftrag zugewiesen ist und wer diesen besitzt, gibt es mehr zu beachten. Einige Regeln müssen der Reihe nach abgearbeitet werden. Schluss ist, wenn die Anforderungen der Regeln erfüllt sind und das Ziel des Validitätschecks\* erreicht wird.

\*[Validitätscheck ](#validitaetschecks)– Bei Validitätschecks von Zuweisungen und Besitzer/innen müssen wir feststellen, ob das Ziel gültig ist (bei Validitätschecks müssen einige Regeln befolgt werden). Falls nicht, machen wir bei den Regeln in Teil 3 weiter, bis ein gültiges Ziel gefunden wird.

Da das geltende übergeordnete Muster nun beschrieben wurde, können wir uns die Regeln ansehen, die für die oben genannten Abschnitte 1-3 durchgegangen werden müssen, und jene für die Validitätschecks.

## Bestimmen, WANN eine Neu-Evaluierung stattfindet

Das System re-evaluiert bei jeder Statusänderung, wem ein Auftrag zugewiesen ist, wer ihn besitzt, und mit welcher Warteschlange der Arbeitsauftrag verknüpft ist. Es geht dabei folgende Eingaben durch:

* Statusänderungen
* Änderungen der Wartestellungsart
* Änderungen des geplanten Folgetermins
* Änderungen des „Warten bis“-Zeitpunkts
* Änderungen der „Warten auf“-Option (nur bei Fällen)
* Änderungen des Kontextes des Tickets
* Änderungen der Ticket-Kategorie
* Statusänderungen im „Peer Review“-Verfahren
* Neue Informationen zu einem Arbeitsauftrag erhalten
* Es gibt ein Problem bei einem Fall

## Bestimmen, ob Zuweisungs-, Besitz- und Warteschlangen-Werte geändert oder gelöscht werden müssen

Wenn das System entscheidet, dass es eine solche Auswertung vornehmen muss, wird zunächst der STATUS des Arbeitsauftrages evaluiert, um zu bestimmen, welche der Zuweisungs-. Besitz- und Warteschlangen-Werte geändert und welche gelöscht werden müssen. Sie finden diese Informationen in der folgenden Tabelle:

| <p><strong>Arbeitsauftrag/Situation</strong></p><p> </p>                          | <p><strong>Zugewiesene Person</strong></p><p> </p> | <p><strong>Besitzer</strong></p><p> </p> | <p><strong>Warteschlange</strong></p><p> </p> |
| --------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------- | --------------------------------------------- |
| <p>Geschlossen</p><p> </p>                                                        | <p>Wert löschen</p><p> </p>                        | <p>Wert löschen</p><p> </p>              | <p>Wert löschen</p><p> </p>                   |
| <p>Entwurf</p><p> </p>                                                            | <p>Wert festlegen</p><p> </p>                      | <p>Wert löschen</p><p> </p>              | <p>Wert löschen</p><p> </p>                   |
| <p>Neue Information erhalten</p><p> </p>                                          | <p>Wert festlegen</p><p> </p>                      | <p>Wert löschen</p><p> </p>              | <p>Wert festlegen</p><p> </p>                 |
| <p>Braucht Aufmerksamkeit</p><p> </p>                                             | <p>Wert festlegen</p><p> </p>                      | <p>Wert löschen</p><p> </p>              | <p>Wert festlegen</p><p> </p>                 |
| <p>„Zu erledigen“ oder „In Bearbeitung“ bei einer Aktion/einem Ticket</p><p> </p> | <p>Wert festlegen</p><p> </p>                      | <p>Wert löschen</p><p> </p>              | <p>Wert festlegen</p><p> </p>                 |
| <p>„Zu erledigen“ oder „In Bearbeitung“ bei einem Fall</p><p> </p>                | <p>Wert löschen</p><p> </p>                        | <p>Wert festlegen</p><p> </p>            | <p>Wert löschen</p><p> </p>                   |
| <p>„Erledigt“ oder „Warten“</p><p> </p>                                           | <p>Wert löschen</p><p> </p>                        | <p>Wert festlegen</p><p> </p>            | <p>Wert löschen</p><p> </p>                   |

&#x20;

## Einstellen, wem ein Arbeitsauftrag zugewiesen ist, wem er gehört und mit welcher Warteschlange er verknüpft ist

* **Warteschlangen** – Warteschlangen einstellen ist einfach. Sie müssen die konfigurierte [Warteschlangenzuweisungsmethode](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method) anwenden.
* **Zuweisung und Besitz** – Bei Zuweisungen und Besitz-Einstellungen gibt es mehr zu beachten. Einige Regeln müssen der Reihe nach abgearbeitet werden. Schluss ist, wenn die Anforderungen der Regel erfüllt sind und ein [gültiges Ziel](#validitaetschecks) erreicht wird.

Bevor Sie die Regeln durchgehen können, müssen Sie eine wichtigere Kontrolle durchführen: Falls der Auftrag bereits jemandem zugewiesen ist und jemandem gehört, **ändern Sie diese Einstellungen nicht, außer die Ticket-Kategorie wurde geändert**.

Sonst gehen Sie die folgenden Regeln der Reihenfolge nach durch. Schluss ist, wenn Sie ein gültiges Ziel erreichen:

1. Wenn die Option „Bei mir behalten“ bei einem Arbeitsauftrag angewählt wurde, muss entweder die Person, der der Auftrag zugewiesen ist oder der/die Besitzer/in die „Bei mir behalten“-Option angewählt haben. Wenn nicht, oder falls der/die Nutzer/in ungültig ist, dann...
2. Wenn es eine/n Besitzer/in gibt, dann muss der Auftrag auch jemandem zugewiesen sein. Wenn nicht, oder falls der/die Nutzer/in ungültig ist, dann...
3. Wenn der Arbeitsauftrag ein Ticket ist und sich die Ticket-Kategorie geändert hat und entweder die Art des Wartens oder der Status zu „Erledigt“ geändert wurden, dann wird der/die NutzerIn/BesitzerIn als die Person angegeben, die das Update durchführt. Wenn nicht, dann...
4. Wenn der Arbeitsauftrag kein Ticket ist ODER er ein Ticket ist (dessen Ticket-Kategorie nicht verändert wurde UND das mehr als 2 Reihen an Status-Verlaufsgeschichte hat – z. B. wenn es kein erster Entwurf ist), dann...
   1. Muss der/die Letztbearbeitende/der Roboter, der den Arbeitsauftrag aktualisiert hat, als Besitzer/in eingetragen werden, oder der Arbeitsauftrag muss ihm/ihr zugewiesen werden. Wenn es keine/n gibt, oder falls der/die Nutzer/in ungültig ist, dann...
   2. Werden diejenigen Nutzer/innen oder Roboter eingetragen, denen der Arbeitsauftrag einmal zugewiesen war (dem Datum nach). Wenn es keine/n gibt, oder falls der/die Nutzer/in ungültig ist, dann...
   3. Wenn eine Aktion automatisch gestartet wurde (d. h. nicht manuell als ad-hoc Aktion), dann wird der/die Letztbearbeitende/Roboter eingetragen, der/die die zuletzt abgeschlossene Aktion des Falls abgeschlossen hat (oder das „Peer Review“ der Aktion gemacht hat, falls eines vorgesehen ist). Wenn es keine/n gibt, oder falls der/die Nutzer/in ungültig ist, dann...
5. Gehen Sie die [Zuweisungsregel](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method) für diesen Arbeitsauftrag durch.
   1. Wenn die „Primary Push“-Zuweisung einem/r bestimmen Nutzer/in zugeteilt ist, machen Sie diese Person zum/r Besitzer/in und weisen Sie ihm/ihr den Auftrag zu. Wenn es keine/n gibt, oder falls der/die Nutzer/in ungültig ist, dann...
   2. Wenn die „Secondary Push“-Zuweisung einem/r bestimmten Nutzer/in zugeteilt ist, machen Sie diese Person zum/r Besitzer/in und weisen Sie ihm/ihr den Auftrag zu. Wenn es keine/n gibt, oder falls der/die Nutzer/in ungültig ist, dann...
   3. Wenn die „Primary Push“-Zuweisung einer bestimmten Position zugeteilt ist, machen Sie denjenigen/diejenige, der/die diese Position innehält und am wenigsten Arbeitsaufträge in seinem/ihren Posteingang hat, zum Besitzer und weisen der Person den Auftrag zu. Wenn es keine/n gibt, oder falls der/die Nutzer/in ungültig ist, dann...
   4. Wenn die „Secondary Push“-Zuweisung einer bestimmten Position zugeteilt ist, machen Sie denjenigen/diejenige, der/die diese Position innehält und am wenigsten Arbeitsaufträge in seinem/ihren Posteingang hat, zum Besitzer und weisen der Person den Auftrag zu. Wenn es keine/n gibt, oder falls der/die Nutzer/in ungültig ist, dann...
6. Wenn der Arbeitsauftrag ein Fall ist, weisen Sie ihn der Person zu, die ihn erstellt hat und machen Sie diese Person zum Besitzer.

## Validitätschecks

Im Rahmen der Zuweisungs- und Besitz-Regel-Kontrolle muss festgestellt werden, ob das Ziel gültig ist. Dazu muss das Ziel einige Validitätschecks bestehen. Falls nicht, machen wir bei den Zuweisungs- und Besitz-Regeln weiter, bis ein gültiges Ziel gefunden wird. Die Validitätschecks verlaufen folgendermaßen:

* Wenn der/die Nutzer/in/Roboter nicht an dieser Art von Arbeitsaufträgen arbeiten darf (z. B. Live/Test), dann blockieren Sie.
* Wenn der/die Nutzer/in/Roboter inaktiv ist, dann blockieren Sie.
* Wenn der/die Nutzer/in keine Befugnis hat, dann blockieren Sie (bei Robotern muss die Befugnis nicht überprüft werden).
* Wenn der Roboter suspendiert wurde, dann blockieren Sie.
* Wenn der Roboter bei diesem Arbeitsauftrag mehr als drei Mal mehr Arbeit angefordert hat, blockieren Sie.
* Wenn der/die ausgewählte Nutzer/in ein Roboter ist und der Arbeitsauftrag eine für ein „Peer Review“-Verfahren vorgesehene Aktion ist, dann blockieren Sie (Roboter können keine „Peer Reviews“ durchführen).
* Wenn der/die ausgewählte Nutzer/in ein Roboter ist und der Arbeitsauftrag eine Aktion ist, aber keine Roboterfarm für die Aktion konfiguriert ist, dann blockieren Sie.
* Wenn der/die ausgewählte Nutzer/in ein Roboter ist und der Arbeitsauftrag eine Aktion ist, aber der Roboter nicht zu der konfigurierten Roboterfarm gehört, dann blockieren Sie.
* Wenn der/die ausgewählte Nutzer/in ein Roboter ist und der Arbeitsauftrag ein Fall ist, dann blockieren Sie (Robotern können keine Fälle zugewiesen werden).
* Wenn der Arbeitsauftrag eine manuelle „Peer Review“-Aktion im „Peer Review“-Stadium ist und der/die Nutzer/in währenddessen 1 oder mehr Updates durchgeführt hat, dann blockieren Sie (Nutzer/innen dürfen nicht ihre eigene Arbeit überprüfen).
* Wenn der Arbeitsauftrag eine manuelle „Peer Review“-Aktion im Durchführungsstadium ist und der/die Nutzer/in während des „Peer Review“-Verfahrens 1 oder mehr Updates durchgeführt hat, dann blockieren Sie (Nutzer/innen dürfen nicht an Arbeitsaufträgen arbeiten, die sie zuvor überprüft haben).
