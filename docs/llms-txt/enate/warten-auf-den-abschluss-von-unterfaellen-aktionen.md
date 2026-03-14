# Source: https://docs.enate.net/enate-help/deutsch/bearbeitung-einer-aktion/warten-auf-den-abschluss-von-unterfaellen-aktionen.md

# Warten auf den Abschluss von Unterfällen' Aktionen

Eine Aktion "Warten auf den Abschluss von Unterfällen" wartet auf den Abschluss eines bestimmten Unterfalls, bevor der Fall zur nächsten Aktion übergehen kann.

Sie können eine Aktion mit der Bezeichnung "Warten auf den Abschluss von Unterfällen" daran erkennen, dass auf der Infokarte der Aktion "Aktion wartet auf den Abschluss eines Unterfalls" steht.

Sobald eine Aktion "Warten auf den Abschluss von Unterfällen" gestartet wurde UND der Unterfall, auf den sie warten soll, gestartet wurde (entweder manuell oder durch eine Aktion "Fall starten"), geht die Aktion "Warten auf den Abschluss von Unterfällen" in den Zustand "Warten" über.

Sobald der Unterfall abgeschlossen ist, wird die Aktion "Warten auf den Abschluss von Unterfällen" automatisch geschlossen.

Auch hierüber werden Sie in der Zeitleiste informiert.

Wenn der Unterfall, auf den die Aktion "Warten auf den Abschluss von Unterfall" warten soll, nicht verfügbar ist - entweder weil er nicht gestartet wurde oder weil er gelöst wurde, bevor die Aktion "Warten auf den Abschluss von Unterfall" gestartet wurde -, geht die Aktion "Warten auf den Abschluss von Unterfall" in den Status "Zu erledigen" über und wird einer Warteschlange zugewiesen, in der ein Nutzer sie aufgreift und entscheidet, wie es weitergeht.

Wenn Sie dann versuchen, die Aktion "Warten auf den Abschluss eines Unterfalls" auf "Warten" zu setzen, wird die Aktion geschlossen, da der Unterfall, auf den sie warten soll, noch nicht gestartet wurde.

Befindet sich die Aktion nicht im Zustand "Warten auf den Abschluss von Unterfällen" und wurde der Unterfall, auf den sie wartet, abgeschlossen, wird in der Infokarte die Meldung "Unterfall ist abgeschlossen" angezeigt.

Wenn Sie eine Aktion "Warten auf den Abschluss eines Unterfalls" manuell auflösen, wird die Aktion als gelöst markiert, ohne dass der Unterfall abgeschlossen wurde.

{% hint style="info" %}
Bitte beachten Sie, dass, wenn Ihr System so konfiguriert wurde, dass eine Aktion "Warten auf den Abschluss eines Unterfalls" automatisch geschlossen wird (weitere Informationen dazu finden Sie hier) und der Unterfall, auf den die Aktion "Warten auf den Abschluss von Unterfällen" warten soll, nicht verfügbar ist - entweder weil er nicht gestartet wurde oder weil er aufgelöst wurde, bevor die Aktion "Warten auf den Abschluss von Unterfällen" gestartet wurde -, die Aktion "Warten auf den Abschluss von Unterfällen" automatisch in den Status "abgeschlossen" übergeht. Dies wird Ihnen im Verlauf angezeigt. Auch hierüber werden Sie im Verlauf informiert.
{% endhint %}
