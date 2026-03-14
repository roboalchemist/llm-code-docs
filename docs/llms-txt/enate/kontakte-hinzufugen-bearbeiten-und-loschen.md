# Source: https://docs.enate.net/enate-help/deutsch/kontakte/kontakte-hinzufugen-bearbeiten-und-loschen.md

# Kontakte hinzufügen, bearbeiten und löschen

## Kontakte hinzufügen

Externe Kontakte können in Enate auf verschiedene Arten erstellt werden.

### 1)  Automatisch aus einer eingehenden E-Mail

Das Enate-System kann so eingestellt werden, dass es automatisch neue externe Kontaktdatensätze erstellt, wenn E-Mails eingehen, die neue E-Mail-Adressen enthalten, wenn die Einstellung ["Automatische Kontakterstellung aktivieren" im Builder eingeschalten ist.](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)

Das System füllt den Vor- und Nachnamen des Kontakts automatisch auf der Grundlage des E-Mail-Anzeigenamens aus. Weitere Einzelheiten dazu:

* Wenn der E-Mail-Anzeigename ein Leerzeichen enthält, wird alles vor dem ersten Leerzeichen als Vorname des Kontakts und alles nach dem letzten Leerzeichen als Nachname verwendet. Wenn der E-Mail-Anzeigename zum Beispiel "John Smith" lautet, wird der Vorname des Kontakts automatisch als "John" und der Nachname als "Smith" ausgefüllt.
* Wenn der E-Mail-Anzeigename ein Komma enthält, wird alles vor dem ersten Komma als Nachname des Kontakts und alles nach dem letzten Komma als Vorname verwendet. Wenn der Name der E-Mail-Anzeige zum Beispiel "Smith, John" lautet, wird der Nachname des Kontakts automatisch mit "Smith" und der Vorname mit "John" ausgefüllt.
* Wenn das System den Vor- und Nachnamen nicht automatisch ausfüllen kann, wird der Kontakt automatisch ohne Vor- und Nachnamen erstellt und der Benutzer wird aufgefordert, diesen selbst auszufüllen, wenn er den Arbeitsauftrag einreicht.

Außerdem hängt das [Unternehmen, das einem automatisch erstellten Kontakt zugeordnet is](#firmenname-zweck-der-externen-kontakte)t, von der [Einstellung des Kontaktbereichs im Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope) ab. Wenn er auf "Global" oder "Global und Lokal" eingestellt ist, hat der automatisch erstellte Kontakt einen globalen Geltungsbereich, d.h. er ist nicht mit einem bestimmten Unternehmen verknüpft. Ist die Option auf "Lokal" eingestellt, wird der automatisch erstellte Kontakt unter dem Unternehmen erstellt, unter dem das zugehörige Arbeitsobjekt existiert.

### 2)  Hinzufügen eines einzelnen Kontakts über die Seite Kontaktverwaltung

Sie können Kontakte von der [Seite Kontaktverwaltung](https://docs.enate.net/enate-help/deutsch/kontakte/kontaktdaten-verwaltungsseite) aus hinzufügen, indem Sie auf das Symbol Kontakt erstellen klicken und die Details für den Kontakt im daraufhin angezeigten Popup ausfüllen.&#x20;

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FKoHVht680csIL2bmqThz%2F7%20Adding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=c6457eb1-79d3-46dd-b020-1e045d232e93" alt=""><figcaption></figcaption></figure>

### 3)  Importieren von Kontakten aus einer Excel-Vorlage in die Kontaktverwaltungsseite

Sie können eine Liste von Kontakten aus einer Excel-Tabelle in die [Seite Kontaktverwaltung](https://docs.enate.net/enate-help/deutsch/kontakte/kontaktdaten-verwaltungsseite) importieren. Es wird eine Vorlage bereitgestellt, die in allen von Enate angebotenen Sprachen unterstützt wird.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2F9uYYWmBJMP2ouiqcaGTJ%2F7A%20Bulk-Adding-Contacts.gif?alt=media&#x26;token=c6a6b538-a42f-4cdd-8f13-38d05ee58a29" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Wenn Sie Kontakte aus einer Excel-Vorlage importieren, müssen Sie die E-Mail-Adresse angeben. Wenn Sie kein Unternehmen angeben, wird der Kontakt automatisch auf global gesetzt. Weitere Informationen zum Firmenzweck finden Sie [hier](#firmenname-zweck-der-externen-kontakte).
{% endhint %}

### 4)  Einen Kontakt aus der Schnellsuche hinzufügen

Wenn Sie nach einem neuen Kontakt suchen, der derzeit nicht im System vorhanden ist, können Sie einen neuen Kontakt anlegen aus der [Schnellsuche](https://docs.enate.net/enate-help/deutsch/schnellsuche). Navigieren Sie zur Personensuche in der Schnellsuche und klicken Sie auf 'Kontakt hinzufügen'.

Wenn Sie auf 'Kontakt hinzufügen' klicken, entschlüsselt das System den Vornamen, Nachnamen und die E-Mail-Adresse und stellt sie automatisch ein. Nachdem Sie alle Informationen eingegeben und auf "Erstellen" geklickt haben, werden Sie zur [Kontaktaktivitätsseite ](https://docs.enate.net/enate-help/deutsch/kontakte/die-aktivitaetsseite-kontakt)des neuen Kontakts weitergeleitet.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MbH-BYuK4VLPdtNwqfT%2F-MbHBB9sVuyT_nCkaTfK%2FCreating-a-Contact-from-Quickfin.gif?alt=media\&token=fe49d4ff-b5be-4aee-bbd6-b5aeee0ff1f3)

{% hint style="info" %}
Anmerkung: Die Kontakt-E-Mail-Adresse muss im System eindeutig sein.
{% endhint %}

### 5)  Einen Kontakt aus der Kontaktkarte eines Arbeitsauftrags hinzufügen

Sie können auch aus einem Arbeitsauftrag - in der [Kontaktkarte](https://docs.enate.net/enate-help/deutsch/kontakte/kontakte)-  heraus einen neuen Kontakt anlegen. Wenn Sie in der Karteikarte Kontakte nach einem Benutzer suchen, der im System nicht vorhanden ist, können Sie einen neuen Kontakt anlegen, indem Sie auf die Option "Kontakt erstellen" klicken und die Angaben des Kontakts eingeben.

Wenn Sie die E-Mail-Adresse des Kontakts eingegeben haben, entschlüsselt das System den Vor- und Nachnamen des Kontakts und füllt ihn automatisch aus. Sobald Sie alle Informationen ausgefüllt und auf Kontakt anlegen geklickt haben, wird das System wieder auf den Arbeitsauftrag zurückleiten.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2Fd1ggtBXNf1X1eqoCBws9%2F7A-Create-Contact-from-Work-Item.gif?alt=media&#x26;token=2b69a6b8-8e8f-482e-a341-ae675adb7230" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Bitte beachten Sie, dass wenn Sie einen neuen Kontakt im Testmodus erstellen, dieser Kontakt nur für die Ausführung von Testpaketen im System verfügbar ist.
{% endhint %}

## Automatisch vs manuell einen Kontakt erstellen

Ob ein externer Kontakt automatisch vom System oder manuell von einem Benutzer erstellt wurde, erkennen Sie an der Spalte "Automatisch erstellt" auf der [Seite Kontaktverwaltung](https://docs.enate.net/enate-help/deutsch/kontakte/kontaktdaten-verwaltungsseite).

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FKckG4NCcdtHb8PDXmh9E%2Fimage.png?alt=media\&token=019b31de-5fef-4054-aa3a-433116d7fe20)

{% hint style="info" %}
Bitte beachten Sie, dass ein automatisch erstellter Kontakt nicht mehr als automatisch erstellter Kontakt in der Spalte "Automatisch erstellt" auf der Seite "Kontaktverwaltung" angezeigt wird, sobald er bearbeitet wurde.
{% endhint %}

## Firmenname – Externe Kontaktbegrenzung

Je nachdem, wie es im Builder konfiguriert wurde, haben Sie verschiedene Möglichkeiten, einem externen Kontakt ein Unternehmen zuzuordnen:

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FsFrTg5RvszrjvCqHUoCR%2F7A%20Company-Scope.gif?alt=media&#x26;token=e672fa15-aa24-4ce1-a958-7327fb5290f5" alt=""><figcaption></figcaption></figure>

* Alle Unternehmen/Global
  * Mit der Alle Unternehmen/Global-Einstellung können externe Kontakte Arbeitsaufträge für alle Unternehmen erstellen und auf diese zugreifen.
  * Dies bedeutet außerdem, dass Nutzers des Arbeitsmanagers in einem Arbeitsauftrag nach externen Kontakten suchen können.

{% hint style="info" %}
Bitte beachten Sie, dass diese Einstellung nur verfügbar ist, wenn der Umfang des externen Kontakts im Builder auf "Global" oder "Global und lokal" eingestellt wurde. Klicken Sie [hier](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#contact-scope) für mehr Informationen.&#x20;
{% endhint %}

* Ein bestimmtes Unternehmen (lokal)
  * Wenn Sie den Kontaktrahmen an ein bestimmtes Unternehmen anpassen, bedeutet dies, dass externe Kontakte nur Arbeitsaufträge für diese bestimmte Firma erstellen und bearbeiten können.
  * Benutzer können außerdem nur dann einen Kontakt zu einer Paket-API hinzufügen, wenn der Kontakt demselben Unternehmen (oder einem Dachunternehmen) angehört.

{% hint style="info" %}
Bitte beachten Sie:

1. dass Sie das mit einem externen Kontakt verbundene Unternehmen nur dann von „Alle Unternehmen/Global“ zu einem bestimmten Unternehmen ändern können, wenn der externe Kontakt nicht mit mehreren verschiedenen Arbeitsaufträgen für diverse Firmen in Verbindung steht. Sie können diese Änderung vornehmen, indem Sie dem Kontakt einen anderen Arbeitsauftrag zuordnen.
2. Um externe Kontakte zur Kategorie „Globale/Alle Unternehmen“ zu beschränken, sollte die Spalte Unternehmen in der Massen-Upload-Datei leer gelassen werden, damit die Kontakte standardmäßig auf „Global“ beschränkt werden.
3. Welche Firma einem automatisch generierten Kontakt zugewiesen wird, hängt von Ihren Kontaktbegrenzungseinstellungen ab. Ist „Global“ oder „Global und Lokal“ eingestellt, haben automatisch generierte Kontakte eine „Globale Kontaktauswahl“ und sind somit nicht mit einem spezifischen Unternehmen verknüpft. Ist „Lokal“ eingestellt, wird der Kontakt automatisch als Teil des Unternehmens erstellt, zu dem der zugehörige Arbeitsauftrag gehört.
   {% endhint %}

### **Auswirkung von globalen/lokalen Zwecken auf die Verknüpfung von Kontakten mit einem Arbeitsauftrag**

{% hint style="warning" %}
Bitte beachten Sie, dass Sie einen externen Kontakt, der lokal zugewiesen ist (d.h. mit einem bestimmten Unternehmen verknüpft ist), nicht als Kontakt für einen Arbeitsauftrag hinzufügen können, der in einem anderen Unternehmen existiert. Dies gilt auch für Kollegenkonten (die immer unter einem bestimmten Unternehmen existieren müssen). NUR global zugewiesene externe Konten haben die Möglichkeit, als Kontakt mit Arbeitsaufträgen in jedem Kunden verknüpft zu werden.
{% endhint %}

## Einen Kontakt bearbeiten

Um einen Kontakt zu bearbeiten, gehen Sie auf die [Seite Kontaktverwaltung](https://docs.enate.net/enate-help/deutsch/kontakte/kontaktdaten-verwaltungsseite) und doppelklicken Sie auf den Kontakt, um das Popup-Fenster Kontakt bearbeiten aufzurufen.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FSauUXiaR46P2Z6ldRxI9%2F7A%20Editing-a-Contact-in-Contact-Management%20Page.gif?alt=media&#x26;token=c73124cf-3431-4342-abd9-1f5360b341f2" alt=""><figcaption></figcaption></figure>

Sie können auch das Unternehmen, die Zeitzone, den Bürostandort, den Standard-Tag und die bevorzugte Sprache Ihrer Kontakte bearbeiten, indem Sie auf das Kontrollkästchen des Kontakts klicken, woraufhin die Schaltfläche Bearbeiten erscheint. Legen Sie die gewünschten Details fest und klicken Sie auf Bestätigen, um die Massenänderungen zu speichern.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FrXB90r7BVy00X20x7esK%2F7A%20Bulk-Editing-Contacts-in-Conta.gif?alt=media&#x26;token=0d9361bc-1f34-4d1d-9b60-078706bdf42c" alt=""><figcaption></figcaption></figure>

## Einen Kontakt löschen

Um einen Kontakt zu löschen, gehen Sie auf die [Seite Kontaktverwaltung](https://docs.enate.net/enate-help/deutsch/kontakte/kontaktdaten-verwaltungsseite) und klicken Sie auf das Kästchen des Kontakts, woraufhin die Schaltfläche Löschen erscheint. Sie können mehrere Kontakte gleichzeitig löschen.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FpUB5FknAmdaTww0emoMv%2F7A%20Deleting-Conacts-from-Contact.gif?alt=media&#x26;token=71515393-5a95-4bc5-b014-102dc8031a58" alt=""><figcaption></figcaption></figure>
