# Source: https://docs.enate.net/enate-help/deutsch/neue-arbeit-erstellen.md

# Neue Arbeit erstellen

Arbeiten können von Benutzern aus dem Arbeitsmanager auf zwei Arten erstellt werden:

1. **Aus dem 'Neuen Arbeitsauftrag‘ erstellen'.** Dies ist eine Dropdown-Liste, die in der Symbolleiste verfügbar ist. Der Agent wählt einen Fall oder ein Ticket aus, um unter einem bestimmten Geschäftskontext zu beginnen
2. **Von der Seite 'Kontaktaktivität'**, oft auch als Anrufbearbeitungsseite bezeichnet. Von dieser Seite aus suchte und fand der Servicemitarbeiter zunächst eine Person (oft jemand, der das Servicezentrum anrief) und begann dann direkt für diese Person eine Arbeit, z.B. ein Ticket oder einen Fall.

## Die Dropdown-Liste 'Neuen Arbeitsauftrag erstellen' <a href="#a-die-dropdown-liste-neuen-arbeitsauftrag-erstellen" id="a-die-dropdown-liste-neuen-arbeitsauftrag-erstellen"></a>

Sie können Arbeitsaufträge erstellen, indem Sie in der Kopfzeile „Erstellen“ anklicken (Würfel-Icon). Nach diesem Klick erscheint ein Dropdown-Auswahlmenü, mit dem Sie einen neuen Arbeitsauftrag erstellen können. Die hier angezeigte Reihenfolge lautet: Unternehmen, Vertrag, Service, Prozessgruppe (falls konfiguriert), gefolgt von den Fallarten, die erstellt werden können.

Nutzer mit mehreren Kunden können oben im Abschnitt der Dropdown-Listen nach Kunden und Vertrag filtern. Eingabe-Links erscheinen hier automatisch für Tickets und Fälle, wenn Sie einen Ticket- oder Fallvorgang im Builder erstellt und auf Live gesetzt haben

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEhH-dnBbM95bUBf0z%2F-MYEk7maY3OWhZPPG154%2FCreate-Work-Item.gif?alt=media\&token=1d97d13f-88ec-4b2f-b505-dd88d3156538)

{% hint style="info" %}
Anmerkung: Wenn sie im Testmodus sind, werden Prozesse, die sich im Zustand 'validierter Entwurf' befinden, hier angezeigt
{% endhint %}

## Dropdown-Menü 'Neue Aktivität starten' auf der Seite Kontaktaktivität <a href="#b-dropdown-menue-neue-aktivitaet-starten-auf-der-seite-kontaktaktivitaet" id="b-dropdown-menue-neue-aktivitaet-starten-auf-der-seite-kontaktaktivitaet"></a>

Automatisch generierte Input-Links werden auf der [Seite der Kontaktaktivität](https://docs.enate.net/enate-help/deutsch/kontakte/die-aktivitaetsseite-kontakt) angezeigt.

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEkWZ6buBtuWBZ8N3r%2F-MYEmC7zXzcavCD1pAwt%2FCreate-work-from-contact-activit.gif?alt=media\&token=c4cd6836-a55a-47fb-b302-d94716f09670)

Wenn Sie sich auf einer Kontaktseite für jemanden befinden, der einem bekannten Unternehmen untersteht (d.h. auf Kundenebene angesiedelt ist), werden die Kundeninformationen nicht in diesem Linknamen angezeigt.

Administratoren können über die Einstellungen im Builder steuern, ob Sie den Eingabe-Link für einen bestimmten Ticket-/Fallprozess sehen möchten.

## 'Gestartet von' Methoden <a href="#gestartet-von-methoden" id="gestartet-von-methoden"></a>

Es gibt verschiedene Methoden, mit denen ein Arbeitsauftrag erstellt werden kann. Diese können auf den Arbeitsaufträgen angezeigt und für verschiedene Darstellungszwecke verwendet werden - z.B. zur Anzeige in Tabellenspalten oder zur Suche im Ansichtsbildschirm. Die möglichen 'Gestartet von'-Methoden sind folgende:

* Workflow - wird durch einen anderen Arbeitsauftrag als Teil eines Ablaufs gestartet, z.B. eine durch einen Fall gestartete Aktion.
* Manuell - gestartet von Kollegen im Arbeitsmanager
* Selbstbedienung - gestartet durch eingehende Selbstbedienungsanfrage
* Robotik - Begonnen von RPA-Roboter
* E-Mail - gestartet durch eingehende Post
* Ticket - gestartet von einem Ticket
* Massenerstellung - vi abulk geladen, Excel-Datei hochgeladen
* Zeitplan - wird durch einen Systemzeitplan automatisch an einem bestimmten Datum / zu einer bestimmten Zeit gestartet.
