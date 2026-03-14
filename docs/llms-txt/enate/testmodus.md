# Source: https://docs.enate.net/enate-help/deutsch/testmodus.md

# Testmodus

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Umschalten in den Testmodus <a href="#a-umschalten-in-den-testmodus" id="a-umschalten-in-den-testmodus"></a>

Wenn Ihr Benutzerkonto so eingestellt ist, dass Sie auf Testdaten zugreifen können, können Sie Ihre Arbeitsmanager-Umgebung in den 'Testmodus' umschalten. Dieser Link ist in der Benutzer-Dropdown-Liste auf der rechten Seite der Kopfleiste verfügbar.

## Erläuterung zum Testmodus <a href="#b-erlaeuterung-zum-testmodus" id="b-erlaeuterung-zum-testmodus"></a>

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9UvXRgxVZmDdfoiC%2Fimage.png?alt=media\&token=551e6ab5-1c96-451d-880b-f7998fdbef21)

Sobald Sie sich im Testmodus befinden, sehen Sie nur noch Testdaten; dies ermöglicht es Ihnen, Test-Arbeitsaufträge zu erstellen und durch Testversionen von Prozessen laufen zu lassen, um diese vor der Produktivsetzung zu verifizieren, ohne die Live-Produktionsdaten zu beeinträchtigen.

Zur visuellen Erinnerung wird die Kopfzeile auf Rot gesetzt, wenn Sie sich im Testmodus befinden.

## Definieren Verschiedene Leiter und Mitglieder von Warteschlangen im Testmodus <a href="#c-definieren-verschiedene-leiter-und-mitglieder-von-warteschlangen-im-testmodus" id="c-definieren-verschiedene-leiter-und-mitglieder-von-warteschlangen-im-testmodus"></a>

Die Funktionalität des Testmodus ermöglicht es Ihnen, einen anderen Leiter für eine Warteschlange festzulegen, wenn sie im Testmodus gegenüber dem Live-Modus ausgeführt wird.

Beispiel: Denken Sie an **Teamleiter 1**, der Zugriff auf den Live-Modus hat und für die Verwaltung von zwei Warteschlangen verantwortlich ist, der **Finanzierungs-** und der **Master** **Fall** Warteschlange.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9gm1OMy6tLbgy9Dy%2Fimage.png?alt=media\&token=bf28b64a-3e8e-4c3d-b9a8-66472c51830b)

Im Testmodus können dieselben beiden Warteschlangen von einem anderen Nutzer verwaltet werden, der über die Berechtigung ‘Teamleiter’ und ‘Testmodus’ verfügt - siehe untenstehendes Beispiel, bei dem **Teamleiter 2** als Verantwortlicher für die Warteschlangen im Testmodus festgelegt wurde.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9kGgY1W_t3ul-aLF%2Fimage.png?alt=media\&token=7ec9b6f7-c3c3-4bc3-8eb7-3513f2308dea)

## Roboter zwischen Live und Test umschalten <a href="#d-roboter-zwischen-live-und-test-umschalten" id="d-roboter-zwischen-live-und-test-umschalten"></a>

Es ist möglich, einen Roboter so umzuschalten, dass er im Testmodus oder im Live-Modus verwendet werden kann. Konkret wurden den Aktivitätsbibliotheken für UiPath, Automation Anywhere und BluePrism zwei neue Aktivitäten hinzugefügt (und die Standard-APIs so angepasst, dass diese generisch genannt werden können), und zwar

* Live-Modus einstellen
* Testmodus einstellen

Mit diesen Aktionen können Sie einen Roboter zwischen Test- und Live-Zuständen umschalten. Sobald ein Roboter in den Testmodus geschaltet wurde, finden die nachfolgenden Aktivitätsaufrufe, die der Roboter möglicherweise macht, z.B. 'Mehr Arbeit holen' und 'Ticket/Fall erstellen usw.', in diesem Kontext des Testmodus statt, wobei nur Test-Arbeitsauftrag geholt und erstellt werden. Der Roboter sollte wieder in den Live-Modus geschaltet werden, sobald der Prozess in den Live-Modus geschaltet wird, stellen Sie also sicher, dass er dann Live-Arbeiten erstellt.

## Testkontakte - Separate Testkontakte im System <a href="#e-testkontakte-separate-testkontakte-im-system" id="e-testkontakte-separate-testkontakte-im-system"></a>

Enate unterstützt die Erstellung separater Kontaktdatensätze im Testmodus, d.h. alle Kontaktdatensätze, die Sie im Testmodus erstellen, sind nur für Benutzer im Testmodus zugänglich (und Kontakte, die im Live-Modus erstellt wurden, sind nur für Benutzer im Live-Modus zugänglich).  Dadurch wird sichergestellt, dass E-Mails von Test-Paketen nicht versehentlich an Produktionsbenutzer gesendet werden und umgekehrt.
