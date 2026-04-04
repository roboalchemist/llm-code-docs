# Source: https://docs.enate.net/enate-help/deutsch/kontakte/kontakt-tags.md

# Kontakt-Tags

Kontakt-Tags werden verwendet, um Kontakte mit Arbeitsaufträgen zu verknüpfen.

## System-Standard-Tags

Die folgenden Kontakt-Tags sind standardmäßig verfügbar:

* **Hauptkontakt** - die Hauptperson, an die Sie sich für diese Anfrage wenden. Es gibt jeweils immer nur einen Hauptkontakt für einen Arbeitsauftrag. Dies ist für Tickets obligatorisch. Abhängig von der Fallkonfiguration im Builder kann dies für den Fall obligatorisch sein oder nicht (wenn für den Falltyp als obligatorisch festgelegt, ist dies auch für die Aktionen dieses Falls obligatorisch).
* **Ursprüngliche/r Antragsteller/in** – die Person, die den ursprünglichen Antrag gestellt hat. Es gibt jeweils immer nur eine/n ursprüngliche/n Antragsteller/in für einen Arbeitsauftrag, unabhängig vom Tag „Antragsteller/in“. Die/der ursprüngliche Antragsteller/in wird entweder automatisch eingestellt, indem ein valider Kontakt aus der Ausgangs-E-Mail, mit der ein Arbeitsauftrag begonnen hat, oder die erste Person, die manuell als „Antragsteller:in“ eingetragen wird, zur/zum „ursprünglichen Antragsteller/in“ werden. Das Tag „ursprüngliche/r Antragsteller/in“ kann später nicht mehr geändert werden und man kann den verknüpften Kontakt nicht aus dieser Rolle im Arbeitsauftrag entfernen.
* **Antragsteller/in** - die Person, die den ursprünglichen Antrag gestellt hat. Es gibt jeweils immer nur eine/n Antragsteller/in für einen Arbeitsauftrag. Dies ist für Tickets obligatorisch. Abhängig von der Fallkonfiguration im Builder kann dies für den Fall obligatorisch sein oder nicht (wenn für den Falltyp als obligatorisch festgelegt, ist dies auch für die Aktionen dieses Falls obligatorisch).
* **Subjekt** - um wen es im Arbeitsauftrag geht (dies kann keines der beiden oben genannten Themen sein).  Es gibt jeweils immer nur ein Subjekt für einen Arbeitsauftrag.

Sehr oft werden alle drei die gleiche Person sein. Wenn Sie einen anderen Kontakt als einen dieser vom System vorgegebenen Beziehungstypen kennzeichnen, wird die Kennzeichnung vom vorherigen Kontakt entfernt, da es in einem Arbeitsauftrag nur einen Inhaber der vom System vorgegebenen Kontakte geben kann.

Wenn Sie einen Kontakt manuell hinzufügen, wird er standardmäßig als Hauptkontakt, Antragsteller/in und Subjekt festgelegt. Sie können diese Tags anschließend manuell anderen Nutzern neu zuweisen.

* CCs - alle weiteren Kontakte, die auf jede Korrespondenz kopiert werden können. Wenn ein Kontakt nur als 'Cc' markiert ist, wird er im separaten Ccs-Abschnitt angezeigt (ausgeblendet, bis irgendwelche Nur-Cc-Kontakte auf dem Arbeitsauftrag vorhanden sind.

## Festlegen zusätzlicher Standard-Tags für einen Kontaktdatensatz

Zusätzlich zu den vom System voreingestellten Kontakt-Tags (Hauptkontakt, Betreff, CC, Antragsteller) können Sie einem Kontaktdatensatz ein weiteres Standard-Kontakt-Tag hinzufügen, um die Verwendung von Kontakt-Tags für Arbeitsaufträge schneller und einfacher zu gestalten.

Beispiel: Wenn Sie wissen, dass "Jane Smith" bei jedem Arbeitsauftrag, zu dem sie als Kontakt hinzugefügt wird, immer der Makler sein wird, können Sie dem Kontaktdatensatz von Jane den Standard-Tag "Makler" zuweisen, so dass er für sie im Arbeitsauftrag automatisch ausgefüllt wird - anstatt dass Sie diesen Tag-Wert jedes Mal manuell festlegen müssen.

Die Liste der verfügbaren Optionen für Standard-Tags wird in Builder im Abschnitt [Allgemeine Einstellungen >> Kontakt-Tags](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags) gepflegt. &#x20;

Sie können diese Standardmarkierung setzen, wenn Sie einen neuen Kontakt zum System hinzufügen.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FOMHG01b5ufgZ5OwImhWf%2Fimage.png?alt=media&#x26;token=bef77781-8508-4ed1-8472-db343b91f96d" alt=""><figcaption></figcaption></figure>

Über die Kontakte-Seite können Sie diese Markierung auch zu bestehenden Kontakten hinzufügen und die Standardmarkierung bearbeiten.

Das Attribut Standard-Tag ist auch für die Massenbearbeitung verfügbar, d. h. Sie können es für mehrere Kontakte gleichzeitig festlegen. Wählen Sie einfach eine Anzahl von Kontaktdatensätzen im Raster aus und klicken Sie auf die Schaltfläche "Bearbeiten", um das Popup-Menü "Massenbearbeitung" aufzurufen.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FejO571MnCCEXjMJswnrd%2Fimage.png?alt=media&#x26;token=70a2b2ed-9bb8-4d97-9d52-6d6d30c3d6f8" alt=""><figcaption></figcaption></figure>

### Verhalten des Standard-Kontakt-Tags, wenn "Mehrere zulassen" nicht eingestellt ist

Wenn ein bestimmter Tag-Wert nicht auf "Mehrere zulassen" gesetzt wurde, darf nur ein Kontakt in einem Arbeitsauftrag diesen Wert haben. Beispiel: Es kann sein, dass es nur einen einzigen Kontakt der Kategorie "Makler:in" für ein Ticket geben kann. Dies wirkt sich natürlich auf die Standardkennzeichnung aus, wenn einem Arbeitsauftrag zwei Kontakte mit der gleichen Standardkennzeichnung "Muss eindeutig sein" hinzugefügt werden, entweder manuell oder automatisch. In diesem Fall ordnet das System das Standard-Tag nur einem Kontakt zu (und entfernt daher das Standard-Tag für die anderen Kontakte). Das System weist dem Kontakt, der bereits mit einem *anderen* Tag-Wert versehen ist, den nächsten Tag aus folgender Reihung zu:

* Hauptkontakt
* Antragsteller/in
* Betreff
* CC
* Ein anderer Kontakt im Arbeitsauftrag

### Zusätzliche Hinweise zur Nichtübereinstimmung zwischen Lieferantenunternehmen und Kontakt-Tags:

* Sie können einem Kontakt kein Standard-Tag hinzufügen, wenn das Unternehmen, dem er zugewiesen ist, ein anderes Lieferantenunternehmen hat als das Standard-Tag.
* Es ist nicht möglich, einen Arbeitsauftrag mit einem Kontakt einzureichen, dessen Standard-Tag auf ein anderes Lieferantenunternehmen als der Arbeitsauftrag gesetzt ist.

## Auto-Tagging von Kontakten in Arbeitsaufträgen

### Kontakte aus der ursprünglichen E-Mail

**Bekannte Kontakte**

Wenn eine E-Mail von einer Adresse eintrifft, die mit einem Kontakt verbunden ist, der bereits im System vorhanden ist, und der Kontakt:

* die Einstellung Globaler Bereich hat, oder
* einen lokalen Geltungsbereich hat, aber zu demselben Unternehmen gehört, zu dem der Arbeitsauftrag gemäß den Regeln für die Weiterleitung von E-Mails gehören wird

dann werden dessen Details automatisch in die Kontaktkarte eingetragen, wenn der Arbeitsauftrag vom System erstellt wird, und er wird automatisch als Hauptkontakt, ursprüngliche/r Antragsteller/in und Antragsteller/in des Arbeitsauftrags gekennzeichnet. Wenn dem Auftrag ein Standard-Tag zugewiesen wurde, wird der Kontakt außerdem mit diesem Tag versehen. Beachten Sie jedoch, dass Sie die Tags nach der Erstellung des Arbeitsauftrags jederzeit selbst manuell bearbeiten können.

Wenn eine E-Mail von einer Adresse eintrifft, die mit einem Kontakt verbunden ist, der bereits im System vorhanden ist, aber einen lokalen Geltungsbereich hat und zu einem *anderen* Unternehmen gehört als dem, zu dem der Arbeitsauftrag aufgrund der E-Mail-Routing-Regeln gehören wird, werden die Details NICHT automatisch in die Kontaktkarte eingetragen, wenn der Arbeitsauftrag vom System erstellt wird (und können daher nicht automatisch dem Arbeitsauftrag zugeordnet werden). Beachten Sie, dass Sie den Kontakt und die Markierungen nach der Erstellung des Arbeitsauftrags jederzeit selbst manuell bearbeiten können.

**Unbekannte Kontakte**

*Standardmäßig 'Globaler' oder 'Globaler & Lokaler' Bereich*

Wenn eine E-Mail von einer unbekannten Adresse eingeht und:

* [die Einstellung "Automatische Kontakterstellung aktivieren" im Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) auf EIN gesetzt ist und
* Ihr System so konfiguriert wurde, dass der Geltungsbereich Ihrer externen Kontakte auf "Global" oder "Global und lokal" eingestellt ist,

dann wird der Kontakt automatisch erstellt, hat einen globalen Geltungsbereich (d. h. er ist nicht mit einem bestimmten Unternehmen verknüpft) und seine Kontaktdaten werden automatisch in die Kontaktkarte eingefügt, wenn der Arbeitsauftrag vom System erstellt wird. Außerdem wird der Kontakt automatisch als Hauptkontakt, ursprüngliche/r Antragsteller/in und Antragsteller/in des Arbeitsauftrags gekennzeichnet. Da sie dem System vorher nicht bekannt waren, wird für sie kein Standard-Tag gesetzt. Beachten Sie, dass Sie die Tags nach der Erstellung des Arbeitsauftrags jederzeit selbst manuell bearbeiten können.

*Standardmäßig 'Lokaler' Bereich*

Wenn eine E-Mail von einer unbekannten Adresse eingeht und

* [die Einstellung "Automatische Kontakterstellung aktivieren" im Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) auf EIN gesetzt ist und
* Ihr System so konfiguriert wurde, dass der Geltungsbereich Ihrer externen Kontakte auf "Lokal" festgelegt ist,

dann wird der Kontakt automatisch erstellt, hat einen lokalen Geltungsbereich (d. h. er wird mit einem bestimmten Unternehmen verknüpft) und wird unter dem Unternehmen erstellt, unter dem der Arbeitsauftrag existiert. Die Kontaktdaten werden automatisch in die Kontaktkarte eingetragen, wenn der Arbeitsauftrag vom System erstellt wird, und sie werden automatisch als Hauptkontakt, ursprüngliche/r Antragsteller/in und Antragsteller/in des Arbeitsauftrags gekennzeichnet. Da sie dem System vorher nicht bekannt waren, wird für sie kein Standard-Tag gesetzt. Beachten Sie, dass Sie die Tags nach der Erstellung des Arbeitsauftrags jederzeit selbst manuell bearbeiten können.

*Automatische Kontakterstellung AUS*

Wenn eine E-Mail von einer unbekannten Adresse eingeht und

* [die Einstellung "Automatische Kontakterstellung aktivieren" im Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) AUSgeschaltet ist,

dann wird der Arbeitsauftrag auf der Grundlage der E-Mail-Weiterleitungsregeln erstellt, aber die Kontaktdaten der/s E-Mail-Absender/in werden NICHT automatisch in die Kontaktkarte eingetragen, wenn der Arbeitsauftrag vom System erstellt wird (und können daher nicht automatisch mit dem Arbeitsauftrag verknüpft werden). Beachten Sie, dass Sie den Kontakt und die Markierungen nach der Erstellung des Arbeitsauftrags jederzeit selbst manuell bearbeiten können.

### **Kontakt-Tags, die von der Kontaktaktivitätsseite aus eingegeben werden**

Wenn ein Arbeitsauftrag über den „Arbeitsauftrag starten“-Button auf der [Kontakte-Aktivitätenseite ](https://docs.enate.net/enate-help/deutsch/kontakte/die-aktivitaetsseite-kontakt)eines Kontakts erstellt wird, wird dieser Kontakt automatisch als ursprüngliche/r Antragsteller/in, Antragsteller/in, Betreff und Hauptkontakt des Arbeitsauftrags markiert, und sein Standard-Tag wird ebenfalls hinzugefügt (sofern er einen hat).
