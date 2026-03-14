# Source: https://docs.enate.net/enate-help/deutsch/bildschirme-alle-arbeitsauftrags-typen/smart-card.md

# Smart Card

Benutzerdefinierte Daten können zu Tickets, Fällen und Aktionen hinzugefügt werden, um maßgeschneiderte Informationen zu diesen Arbeitsaufträgen zu erfassen, während sie den Prozess durchlaufen. Die Informationen sind über Smart Cards anzeigbar. Bereiche können so eingestellt werden, dass sie im Hauptteil des Arbeitsauftrags angezeigt werden, aber auch als Teil der Seitenkonsole auf der rechten Seite der Bildschirme.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FabNeZ7uBzwEwM49IMlFN%2FsmartCaed.PNG?alt=media\&token=78483c14-62ab-4473-8ad0-ba5977ce1469)

Diese Bereiche können so gestaltet werden (mit HTML, Typescript und CSS), dass sie nahezu jeden Inhalt, z.B. Inhalte aus anderen Systemen, anzeigen.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1666082760%2Fuploads%2FM0Oq1EokDG3YFQYi4zLd%2Fimage.png?alt=media\&token=540f7923-64de-4d36-ac09-67acbec11176)

## Validierung in Smart Cards <a href="#a-validierung-in-smart-cards" id="a-validierung-in-smart-cards"></a>

Smart Cards können mit der Standard-Systemvalidierung verknüpft werden, um z.B. das Ausfüllen bestimmter Daten auf einem Bereich zur Voraussetzung für den Fortschritt eines Arbeitsauftrags zu machen.

## Warnung vor benutzerdefinierter Datenüberschreibung <a href="#b-warnung-vor-benutzerdefinierter-datenueberschreibung" id="b-warnung-vor-benutzerdefinierter-datenueberschreibung"></a>

Wenn Sie einen Arbeitsauftrag geöffnet haben und benutzerdefinierte Daten modifizieren, wird Enate auf Datenkonflikte prüfen, wenn Sie den Arbeitsauftrag aktualisieren. Insbesondere wird geprüft, ob ein anderer Nutzer auf den Arbeitsauftrag zugegriffen und seine benutzerdefinierten Daten geändert hat, seit Sie es geöffnet haben. Wenn dies der Fall ist, wird Ihnen ein Bestätigungsfeld angezeigt, in dem Sie gefragt werden, ob Sie mit der Aktualisierung fortfahren möchten (wodurch ihre Änderungen überschrieben werden) oder ob Sie stattdessen den Bildschirm abbrechen und aktualisieren möchten, um diese letzten Änderungen zu sehen (und beizubehalten).

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_yPpj2Ni3J3Es_sX%2Fimage.png?alt=media\&token=3272e5ac-e7e6-4ecc-8da6-bb99b4bbd1b4)
