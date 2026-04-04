# Source: https://docs.enate.net/enate-help/deutsch/mehrsprachige-unterstuetzung.md

# Mehrsprachige Unterstützung

Enate unterstützt die folgenden Sprachen:

1. Englisch
2. Portugiesisch (Brasilien)
3. Spanisch
4. Rumänisch
5. Ungarisch
6. Polnisch
7. Russisch
8. Französisch
9. Deutsch

Die Betriebsumgebung für Endbenutzer zur Bereitstellung des Dienstes unterstützt diese Sprachen vollständig, und jeder Benutzer kann in seinen Benutzerprofileinstellungen seine bevorzugte Sprache zusammen mit dem Datums- und Zeitmuster auswählen.

Um eine bevorzugte Sprache einzustellen, wählen Sie eine Sprache aus der Dropdown-Liste Sprache in den Benutzereinstellungen.

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCCjQMZrIXW_c-JAut%2F-MZCWE2H20vuRKMcEY_D%2FChange-Language.gif?alt=media\&token=112e24b6-1177-4eba-8d46-043d1fae0317)

Die Anzeige der Labels erscheint in der bevorzugten Sprache des angemeldeten Benutzers - dies wird durch das Hinzufügen eines ‘Sprachpakets’ in **Enate** erreicht. Jedes Sprachpaket wird eine Zuordnung für benutzerspezifische Sprachen wie Portugiesisch haben, z.B. wird '**Warteschlange**' '**Fila'** und ‘**Aktion’** wird auf Portugiesisch ‘**Açao’** lauten.

Hier ist die Liste der UI-Elemente, die in der bevorzugten Sprache des angemeldeten Benutzers verfügbar sein werden.

| Auftrag               | Details                                                                                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Homepage              | <ol><li>RAG-Filter</li><li>Mein Team:</li><li>Bot Farm</li><li>Warteschlange</li><li>Diagramm</li><li>Tabellen und Spalteneinstellungen</li></ol><p>Auch die Seite Posteingang.</p> |
| Schnellsuche          | Personen-, Kommunikations- und Arbeitsauftrags-Suche                                                                                                                                |
| Warteschlangen-Seite  |                                                                                                                                                                                     |
| Links zur Navigation  | Link zum Builder, zur Warteschlangenseite oder zu zuletzt aufgerufenen Arbeitsauftrags usw.                                                                                         |
| Benutzerprofil-Seite  | Hier kann der Benutzer auch die bevorzugte Sprache zusammen mit dem Datum-Zeit-Muster ändern.                                                                                       |
| Seite Anrufabwicklung | Diese Seite zeigt alle Mitteilungen und Arbeitsaufgaben, die sich auf einzelne Benutzer beziehen                                                                                    |
| Arbeitsauftrags UI:   | Beschriftungen und Schaltflächen wie Kategorie-Picker, Zustand etc.                                                                                                                 |

{% hint style="info" %}
Hinweis - Echte Namen wie Kundennamen und Benutzernamen bleiben in der Originalsprache, wie sie von den Konfiguratoren im Builder eingegeben wurden.
{% endhint %}

## Vom Arbeitsmanager-Endbenutzern eingegebene Daten <a href="#vom-arbeitsmanager-endbenutzern-eingegebene-daten" id="vom-arbeitsmanager-endbenutzern-eingegebene-daten"></a>

Enate unterstützt die bevorzugte Sprache eines Nutzers bei der Anzeige des Arbeitsmanagers und in den UI-Elementen, einschließlich Beschriftungen, Links und Schaltflächen, jedoch bleibt alles, was von Ihnen hinzugefügt wird, in derselben Sprache, in der Sie es ursprünglich eingegeben haben, und wird nicht automatisch in eine andere Sprache übersetzt, wenn es von anderen Benutzern mit einer anderen bevorzugten Sprache angezeigt wird.

Wenn z.B. ein brasilianischer Benutzer einem Fall eine Notiz auf Portugiesisch hinzufügt, speichert Enate die Notiz auf Portugiesisch in der Datenbank und zeigt die Notiz immer nur auf Portugiesisch an.

Hier ist eine vollständige Liste der Artikel, die durch Benutzereingaben gesteuert werden und die **NICHT** automatisch vom Produkt übersetzt werden:

| Auftrag                      | Detail                                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fall                         | <p></p><ol><li>Notizen</li><li>E-mails</li><li>Fall - Kurzbeschreibung/Titel</li><li>Aktionsanweisung einer neuen, vom Endbenutzer gestarteten Aktion außer Kraft setzen</li></ol>                                                                                                                                                 |
| Aktion                       | <p></p><ol><li>Notizen</li><li>E-mails</li><li>Checklisten-Kommentare</li><li>Aktionsstatus - ‘Nicht im Stande, den Begründungstext zu vervollständigen’.</li><li>Aktionsanweisung einer neuen, vom Endbenutzer gestarteten Aktion außer Kraft setzen</li><li>Aktion Peer-Review-Notiz, die vom Nutzer eingegeben wurde.</li></ol> |
| Ticket                       | <p></p><ol><li>Titel und Beschreibung der neuen Untertickets</li><li>Name der neuen Aktion, die vom Nutzer gestartet wurde</li><li>Name des neuen Falls, der vom Nutzer gestartet wurde</li></ol>                                                                                                                                  |
| Kontakt                      | Details zur Kontaktaufnahme wie Adresse.                                                                                                                                                                                                                                                                                           |
| Dateien                      | Dateiname und Anmerkung zur Datei                                                                                                                                                                                                                                                                                                  |
| Probleme                     | Beschreibung der Probleme                                                                                                                                                                                                                                                                                                          |
| Anmerkungen zur Neuzuweisung | Text, der vom Nutzer eingegeben wird, während er eine Arbeit einem anderen Teamkollegen zuweist.                                                                                                                                                                                                                                   |

### Benutzerdefinierte Daten und Bereiche <a href="#benutzerdefinierte-daten-und-bereiche" id="benutzerdefinierte-daten-und-bereiche"></a>

Die ersten Versionen der mehrsprachigen Funktionalität werden Konfiguratoren, die bei der Erstellung von benutzerdefinierten Daten und Smartcards im Builder mehrere Sprachen definieren, nicht unterstützen. Dazu wären mehrere Bereiche und Datenelemente erforderlich.

### In App-Benachrichtigungen <a href="#in-app-benachrichtigungen" id="in-app-benachrichtigungen"></a>

Die ersten Versionen der mehrsprachigen Funktionalität unterstützen keine Benachrichtigung in Sprachen außer Englisch.&#x20;
