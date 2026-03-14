# Source: https://docs.enate.net/enate-help/deutsch/schnellsuche/wie-die-schnellsuche-funktioniert-besonderheiten.md

# Wie die Schnellsuche funktioniert - Im Detail

Einige weitere Erläuterungen zur Funktionsweise von der Schnellsuche: Bei der Eingabe von Daten in der Schnellsuche laufen drei verschiedene Arten von Suchvorgängen parallel ab:

**1) Spezifische Suche nach Referenznummer**. Diese basiert auf der Erkennung eines bekannten Formats der Referenznummer des Systems für Arbeitsaufträge und der anschließenden Ausgabe von Ergebnissen in Bezug auf Tickets, Fälle, Aktionen, die diese Referenz haben. Sie können einfach die Referenz eingeben, z.B. '17117-T', und das System wird sie als Referenz erkennen. Sie brauchen keinen  Kurzcode davor einzugeben.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2F5EAF5GpUoq1qdNfO2Heh%2Fimage.png?alt=media\&token=618857c6-17aa-406c-b9fb-e42ab44704c8)

**2) Benutzerdefinierte Datenfeld-Suche**. Wie oben beschrieben. Das System erkennt diese Art der Suche, wenn Sie einen bekannten Kurzcode eingeben, z.B. 'p:'. Es wird nach einem Feld gesucht, das den von Ihnen eingegebenen spezifischen Wert enthält. Siehe weitere Anmerkung unten zu den Platzerhalterzeichen.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FegYNg02nHx05M1JyH4t2%2Fimage.png?alt=media\&token=dfbb7a64-233e-40ed-913f-f7396da224ab)

**3) Freitextsuche nach Arbeitsaufträgen und Kommunikationen und nach allem anderen**, was Sie eingeben und das nicht mit den ersten beiden Arten von erkannten Daten übereinstimmt. Die Freitextsuche durchsucht die einzelnen Wörter nach verschiedenen Systemattributen von Arbeitsaufträgen, Kommunikation und Personen, z.B. Arbeitsauftrag-Titel, E-Mail-Betreff und -Text.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FTb5BlgcIfaP1A2JM1BcL%2Fimage.png?alt=media\&token=2ea81e41-f20a-416d-b7ed-9ea263dc18f8)

**4)** Beachten Sie auch, dass das System bei der **Suche nach Dateien eine "Start mit"-Logik** verwendet, bei der es einen Platzhalter an das ENDE von Suchtexten anhängt. Das heißt, wenn Sie nach einer Datei mit dem Namen „Rechnungsbearbeitung.docx" suchen, wird die Datei bei der Suche nach „Bearbeitung“ nicht gefunden, bei der Suche nach „Rechnung" aber schon.

## Platzerhalterzeichen für die offene Suche <a href="#a-platzerhalterzeichen-fuer-die-offene-suche" id="a-platzerhalterzeichen-fuer-die-offene-suche"></a>

Bei der Suche fügt das System am Ende von Suchtexten einen Platzhalter ein, nicht aber am Anfang.

Speziell für benutzerdefinierte Datensuchen wäre ein Verhaltensbeispiel: Die Suche nach z.B. ‘p:John Smi’ würde Elemente mit dem Wert ‘John Smith’ in einem Feld ‘‘Person’’ finden, aber die Suche nur nach ‘p:Smith’ würde diese NICHT finden.

Kurz gesagt: Bei der Suche nach benutzerdefinierten Datenfeldern suchen wir nach dem genauen Wert des Feldes oder dem Anfang des Wertes.

Freitextsuchen sind nicht *ganz* dasselbe wie diese, da bei einer Freitextsuche versucht wird, jedes einzelne Wort innerhalb eines Textwertes zu finden, um eine Übereinstimmung zu erhalten, und nicht den Wert als Ganzes.

Platzhalter werden auch am Ende von Referenznummernsuchen hinzugefügt.

### **Ausführen von Platzhaltern beim Tippen** <a href="#ausfuehren-von-platzhaltern-beim-tippen" id="ausfuehren-von-platzhaltern-beim-tippen"></a>

Während Sie in der Schnellsuche tippen, sucht das System mit Platzhaltern nach dem allerletzten Wort, z.B. wenn Sie eine Freitextsuche eingeben: "John return prio".

Das System wird das letzte Wort mit einem Platzhalter versehen und würde auch Ergebnisse mit z.B. 'Priorität' zurückbringen

Sobald Sie die Leertaste gedrückt haben, schließt das System die Eingabe dieses Wortes ab und sucht ohne einen nachfolgenden Platzhalter nach diesem Wort.

## Andere Suchbegriffe ignorieren <a href="#b-andere-suchbegriffe-ignorieren" id="b-andere-suchbegriffe-ignorieren"></a>

Um die Systemleistung zu bewahren, werden die folgenden Elemente bei Suchanfragen ignoriert:

* Wörter, die aus 1 oder 2 Zeichen bestehen.
* Wörter, die in der „Stopp-Liste“ des Systems gelistet sind, etwa allgemeine Begriffe wie „und“, sowie Artikel und Pronomina, die sonst zu viele Ergebnisse generieren würden. Hier finden Sie die [detaillierte Stoppwortliste der Wörter, die bei Suchanfragen ignoriert werden](https://docs.enate.net/enate-help/deutsch/anhang/begriffe-die-beim-suchen-vom-system-ignoriert-werden-weitere-einzelheiten). Dies gilt für Schnellsuche und alle anderen Suchfunktionen im System.
* Zeichen, die bei der Schnellsuche ignoriert werden: „\*“, „?“, „@“ etc. Die [detaillierte Liste der Zeichen, die ignoriert werden,](https://docs.enate.net/enate-help/deutsch/anhang/begriffe-die-beim-suchen-vom-system-ignoriert-werden-weitere-einzelheiten#zeichen-die-bei-der-schnellsuche-ignoriert-werden) finden Sie hier. Das bedeutet, dass bei der Schnellsuche nach „Kunde.com“ beispielsweise nach „Kunde“ und „com“ gesucht würde. Um nach zusammengesetzten Begriffen als Einheit zu suchen, sollten sie die jeweiligen Begriffe in Anführungszeichen setzen.

## **Weitere Dinge, die bei der Schnellsuche zu beachten sind**

Die Schnellsuche ist eine textgesteuerte Suche. Die Eingabe von Daten in den Textstrings kann zu inkonsistente Ergebnisse liefern. Verwenden Sie möglichst „Anführungszeichen", wenn eine solche Suche notwendig ist, um die Suche nach ganzen Ketten von Daten von zu erleichtern.&#x20;

Verwenden Sie die Schieberegler für die Suche nach Ergebnissen in bestimmten Datumsbereichen.

Wenn Sie nach mehreren Wörtern suchen, verwendet die Suche eine "UND"-Logik und nicht eine ODER', d. h. es werden Elemente mit Apfel UND Banane UND Birne gefunden.

## **Besonderheiten der Suche nach Arbeitsaufträgen m Vergleich zu E-Mails**

Es ist wichtig zu beachten, dass die Schnellsuche drei unabhängige Suchen durchführt:

* eine für Arbeitsaufträge (Fälle, Aktionen, Tickets)
* eine für die E-Mails, die sich auf sie beziehen können
* und eine für Personen.

Wenn Sie z. B. nach einer Kombination von drei Wörtern suchen, z. B. Apfel, Banane und Birne, findet die Schnellsuche die Ergebnisse aller Arbeitsaufträge, in denen alle drei Wörter vorkommen, und separat alle E-Mails, in denen alle drei Wörter vorkommen. Situationen, in denen zwei der Wörter im Arbeitsauftrag und das dritte nur in einer zugehörigen E-Mail vorkommen, werden von keiner der beiden Suchen gefunden.

Die spezifischen Attribute, nach denen die Arbeitsauftrag-Suche durchgeführt wird, sind wie folgt:

* Arbeitsauftrag-Referenz
* Titel
* Name des Kunden
* Name des Lieferanten
* Name des Vertrags
* Name der Dienstleistung
* Name der Dienstleistungslinie
* Name der Prozessart

Die spezifischen Attribute, nach denen die Kommunikationssuche durchgeführt wird, sind wie folgt:

* E-Mail-Titel
* E-Mail-Text
* E-Mail-Adressen (Von, An, CC, BCC)
* Interner Notizentext (für in Enate / Self Service hinzugefügte Notizen).
