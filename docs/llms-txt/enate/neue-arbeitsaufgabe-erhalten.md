# Source: https://docs.enate.net/enate-help/deutsch/neue-arbeitsaufgabe-erhalten.md

# Neue Arbeitsaufgabe erhalten

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc3MQ==>" %}

Wenn Sie auf die Schaltfläche ‘Auftrag von Warteschlange bekommen’’ in der Tabelle ‘‘Posteingang’’ klicken, wird Ihnen eine neue Arbeit zugewiesen.

![](https://809551593-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWqMXrK_ZvY1cj8JBqs%2F-MWqRv4hiUBVt6rGJXr3%2Fimage.png?alt=media\&token=0ae54aa3-e15a-4bc0-afd5-26dc5ed9119f)

### Zuordnungsregeln aus Warteschlange übernehmen

**Wie ermittelt das System, welche Arbeitsaufgabe ein Benutzer erhalten soll, wenn er in seinem Posteingang auf die Schaltfläche "Aus Warteschlange übernehmen" klickt?**

Das System prüft alle nicht zugewiesenen Arbeitsaufgaben aus allen Warteschlangen, die mit einem Benutzer verknüpft sind und für die er Berechtigungen hat, und weist ihm eine neue Arbeitsaufgabe zu, wobei es die Aufgaben wie folgt priorisiert:

1. Jede momentan überfällige Arbeitsaufgabe (die am stärksten überfällige Aufgabe zuerst). Wenn keine vorhanden, dann
2. Jede momentan überfällige Arbeitsaufgabe (die am stärksten überfällige Aufgabe zuerst). Wenn keine vorhanden, dann
3. Beliebige Arbeitsaufgabe (die am frühesten fällige Aufgabe wird als erste gewählt).

{% hint style="info" %}
Achtung: Warteschlangen, die auf den "strikten Modus" eingestellt sind, dienen dazu, die Arbeit ausschließlich Robotern zuzuweisen. Alle menschlichen Benutzer, die mit solchen Warteschlangen verknüpft sind, dienen nur als Ausweichlösung für aussortierte Roboter-Arbeitsaufgaben. Wenn sie auf "Aus Warteschlange übernehmen" klicken, erhalten sie somit nicht automatisch normale, nicht aussortierte Arbeitsaufgaben aus diesen Warteschlangen zugewiesen.
{% endhint %}
