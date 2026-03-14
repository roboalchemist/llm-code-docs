# Source: https://docs.enate.net/enate-help/deutsch/bearbeitung-einer-aktion/aktion-dokumentenextraktion.md

# Aktion „Dokumentenextraktion“

## Überblick

Mittels Dokumentenextraktion werden relevante Daten automatisch aus angehängten Dateien eingehender E-Mails extrahiert, damit diese Daten im Rahmen des Arbeitsauftrags weiter verarbeitet werden können, was Zeit und Arbeit erspart. Das bedeutet auch, dass Dokumente wie PDFs gescannt und zum Anlegen von Fällen in Enate sowie als Bestandteil laufender Prozesse verwendet werden können.

Wird eine Dokumentenextraktion für einen Fall durchgeführt, können Dateien, die an den Fall angehängt sind, von der gewünschten Technologie gescannt werden, und die ausgegebenen Dateien werden anschließend automatisch wieder an den Fall angehängt.

Falls sich die Technologie, die Sie benutzen, nicht zu einem ausreichend sicheren Ergebnis kommt, im Sinne des von Ihnen eingestellten Vertrauensniveaus, leitet Enate den Auftrag automatisch an eine:n Agent:in im Arbeitsmanager weiter, damit diese:r den Auftrag überprüft und verifiziert, und damit ein Mensch eingebunden wurde.

Ihr:e Administrator:in kann diese Option im [**Marketplace** ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)des Enate Builders (de)aktivieren.

Sehen Sie sich dieses Video an, um mehr zu erfahren:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

## Wie funktioniert das?

Wird der Fall im Arbeitsmanager bearbeitet, werden relevante Daten aus angehängten Dateien von eingehenden E-Mails automatisch analysiert und extrahiert.

Falls die Technologie, die Sie nutzen, sich bei den Ergebnissen ausreichend sicher ist, ist die Kontrolle durch eine:n Agent:in gar nicht nötig. Der Vorgang wird dann automatisch abgeschlossen und der Fall wird geht zur nächsten Aktion über. Sie können die abgeschlossene Datenextraktionsaktion trotzdem mittels Klick einsehen, aber sie wird nicht an eine:n Agent:in weitergeleitet.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2Fwvhcdeg8QVwzY5RrGwcg%2Fimage.png?alt=media&#x26;token=12d169ea-a6d5-4aab-ab68-8ab902a0d43b" alt=""><figcaption></figcaption></figure>

Sollte die Technologie sich bei den Datenextraktionsergebnissen nicht ausreichend sicher sein, wird die Aktion zur Durchsicht und Bearbeitung an ein:e Agent:in weitergeleitet, wenn jemand das nächste Mal auf der Homepage „aus der Warteschlange nehmen“ anklickt. Öffnet ein:e Agent:in die Aktion, werden Sie sehen, dass die Aufgabe weitergeleitet wurde, weil weitere Überprüfungen nötig sind.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FagyhnGz7GWJsv1vROTW4%2Fimage.png?alt=media&#x26;token=e5c75d91-b7cf-4436-b772-424dec04be8b" alt=""><figcaption></figcaption></figure>

Dafür müssen Sie lediglich „Jetzt verifizieren“ anklicken und zum Fenster „Validierungsfenster“ in der Aktion scrollen, in dem Sie das gescannte Dokument und die daraus extrahierten Daten in einer Tabelle sehen können. Hier sehen Sie, dass die Werte, bei denen sich die Technologie nicht sicher ist, hervorgehoben wurden und können diese überprüfen und allfällige Korrekturen vornehmen. Sie können dieses Fenster innerhalb der Seite ansehen oder als Pop-up-Fenster im Vollbildmodus öffnen.

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2Ff2N72FJ6WOtjbdgkemTI%2Fimage.png?alt=media&#x26;token=5088a3b8-f8ff-439e-a5ec-acd46cdebb6b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Notiz: Es kann jeweils nur ein Dokument angezeigt werden.
{% endhint %}

<figure><img src="https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2Fs8PdPK6smlSomuhz3Xcu%2Fimage.png?alt=media&#x26;token=c8e753be-7aec-457f-82b5-b195362ef12f" alt=""><figcaption></figcaption></figure>

Auf diesem Validierungsbildschirm kann der Agent eine gescannte Kopie der Datei sehen, die mehrere Seiten umfassen kann, sowie zwei Registerkarten mit den extrahierten Daten.

* Die Registerkarte „Extrahierte Daten“ zeigt die Agentenschlüssel-Wertpaare der extrahierten Daten zusammen mit dem von EnateAI zugewiesenen Konfidenzniveau an. Die Werte können bei Bedarf angepasst werden und werden gespeichert, sobald der Agent auf die Schaltfläche „Aktualisieren“ für den jeweiligen Wert klickt. Dadurch wird der Konfidenzwert für diesen Schlüssel auf 100 % gesetzt.
* Die Registerkarte „Tabellen“ zeigt alle sich wiederholenden Daten an, die als Tabelle ausgewählt wurden. Mit der Schaltfläche „Löschen“ können Sie nicht benötigte Zeilen löschen.

Wenn der Mitarbeiter den Bildschirm „Validierungsstation“ verlassen muss, kann er jederzeit auf „Als Entwurf speichern“ klicken, um seine Änderungen für ein bestimmtes Dokument zu speichern.

{% hint style="info" %}
Notiz: Wenn ein Agent den Validierungsbildschirm für eine Aktion aufruft, die ihm nicht zugewiesen ist, sind die Daten schreibgeschützt und können nicht bearbeitet werden. Um die Daten bearbeiten zu können, muss der Agent sich die Aktion zunächst selbst zuweisen.
{% endhint %}

Sobald ein Agent mit den Daten zufrieden ist, muss er nur noch auf die Schaltfläche „Senden” klicken, um die aktualisierten Daten zu übermitteln. EnateAI schließt die Verarbeitung im Hintergrund ab und aktualisiert den Aktionsbildschirm, um zu bestätigen, dass der Vorgang abgeschlossen ist. Dank der Hintergrundverarbeitung kann der Agent mit anderen Dokumenten fortfahren, die überprüft werden müssen.

Once 'Submit' has been clicked for the last document needing validation, the Action screen auto-closes. Again, EnateAI is finishing processing in the background and will mark the Action as Resolved after a short time, then moved to Closed.

*Notiz: Jedes Mal, wenn Sie Datenelemente überprüfen und aktualisieren, lernt EnateAI dazu und verbessert seine Vorschläge zur Datenextraktion ein wenig. Wenn Sie feststellen, dass die Technologie regelmäßig falsche Vorschläge macht, sprechen Sie mit Ihrem Admin-Team über eine Änderung des Konfidenzschwellenwerts.*
