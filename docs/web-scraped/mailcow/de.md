# Source: https://docs.mailcow.email/de/

Title: Informationen & Support - mailcow: dockerized Dokumentation

URL Source: https://docs.mailcow.email/de/

Markdown Content:
[![Image 1: mailcow Logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/assets/images/logo.svg)

**Die Mailserver-Suite mit dem 'moo'**

Was ist mailcow: dockerized?[¶](https://docs.mailcow.email/de/#was-ist-mailcow-dockerized "Permanent link")
-----------------------------------------------------------------------------------------------------------

Frage

Mailcow, MailCow oder doch mailcow? Wie heißt das Projekt nun genau?

Richtig: **mailcow**, denn mailcow ist eine eingetragene Wortmarke mit kleinem m ![Image 2: 😁](https://docs.mailcow.email/assets/external/cdn.jsdelivr.net/gh/jdecked/twemoji@16.0.1/assets/svg/1f601.svg)

mailcow[1](https://docs.mailcow.email/de/#fn:1): dockerized ist eine Open-Source Groupware/E-Mail Suite auf Docker Basis.

Dabei setzt mailcow auf viele bekannte und seit Langem bewährte Komponenten, welche im Zusammenspiel einen rundum sorglosen E-Mail-Server ergeben.

Jeder Container repräsentiert eine einzelne Anwendung, die in einem überbrückten (Bridged) Netzwerk verbunden sind:

*   [**ACME**](https://letsencrypt.org/) Automatische Generation von Let's Encrypt Zertifikaten
*   [**ClamAV**](https://www.clamav.net/) Antiviren Scanner (optional)
*   [**Dovecot**](https://www.dovecot.org/) IMAP/POP Server zum Abrufen der E-Mails mit integrierter Full-Text Search Engine ["Flatcurve"](https://slusarz.github.io/dovecot-fts-flatcurve/)
*   [**MariaDB**](https://mariadb.org/) Datenbank zum Speichern der Nutzer Informationen u.w.
*   [**Memcached**](https://www.memcached.org/) Cache für den Webmailer SOGo
*   **Netfilter** Fail2ban-ähnliche Integration von [@mkuron](https://github.com/mkuron)
*   [**Nginx**](https://nginx.org/) Webserver für Komponenten des Stacks
*   [**Olefy**](https://github.com/HeinleinSupport/olefy) Analyse von Office Dokumenten nach Viren, Makros etc.
*   [**PHP**](https://php.net/) Programmiersprache der meisten webbasierten mailcow Applikationen
*   [**Postfix**](http://www.postfix.org/) MTA (Mail Transfer Agent) für den E-Mail-Verkehr im Internet
*   [**Postfix TLS-Pol**](https://github.com/Zuplu/postfix-tlspol) Leichter, performanter MTA‑STS- und DANE/TLSA‑Resolver sowie TLS‑Policy‑Socketmap für Postfix; standardkonform, DANE bevorzugt.
*   [**Redis**](https://redis.io/) Speicher für Spaminformationen, DKIM Schlüssel u.w.
*   [**Rspamd**](https://www.rspamd.com/) Spamfilter mit automatischem Lernen von Spammails
*   [**SOGo**](https://sogo.nu/) Integrierter Webmailer und Cal-/Carddav Schnittstelle
*   [**Unbound**](https://unbound.net/) Integrierter DNS-Server zum Verifizieren von DNSSEC u.w
*   **Watchdog** Für die grundlegende Überwachung der Containerstatus innerhalb von mailcow

Doch das Herzstück bzw. das, was mailcow besonders macht, ist die grafische Weboberfläche, die **mailcow UI**.

Diese bietet für so gut wie alle Einstellungen einen Platz und erlaubt das bequeme Anlegen von neuen Domains und E-Mail-Adressen mit wenigen Klicks.

Aber auch andere bzw. knifflige Themen können in ihr problemlos erledigt werden:

*   [DKIM](http://dkim.org/) und [ARC](http://arc-spec.org/) Unterstützung bzw. Generation.
*   Black- und Whitelists pro Domain und pro Benutzer
*   Spam-Score-Verwaltung pro Benutzer (Spam ablehnen, Spam markieren, Greylist)
*   Erlauben Sie Mailbox-Benutzern, temporäre Spam-Aliase zu erstellen
*   Voranstellen von E-Mail-Tags an den Betreff oder Verschieben von E-Mails im Unterordner (pro Benutzer)
*   Mailbox-Benutzer können die TLS-Durchsetzung für eingehende und ausgehende Nachrichten umschalten
*   Benutzer können die Caches von SOGo ActiveSync-Geräten zurücksetzen
*   imapsync, um entfernte Postfächer regelmäßig zu migrieren oder abzurufen
*   TFA: Yubikey OTP und WebAuthn USB (nur Google Chrome und Derivate), TOTP
*   Hinzufügen von Whitelist-Hosts zur Weiterleitung von Mails an mailcow
*   Fail2ban-ähnliche Integration
*   Quarantäne-System
*   Antivirus-Scanning inkl. Makro-Scanning in Office-Dokumenten
*   Integrierte Basisüberwachung
*   Und weitere...

Die mailcow Daten (wie bspw. E-Mails, Userdaten etc.) werden in **Docker-Volumes** aufbewahrt - geben Sie gut auf diese Volumes acht:

*   clamd-db-vol-1
*   crypt-vol-1
*   mysql-socket-vol-1
*   mysql-vol-1
*   postfix-vol-1
*   postfix-tlspol-vol-1
*   redis-vol-1
*   rspamd-vol-1
*   sogo-userdata-backup-vol-1
*   sogo-web-vol-1
*   vmail-index-vol-1
*   vmail-vol-1

Achtung

Die Mails werden komprimiert und verschlüsselt gespeichert. Das Schlüsselpaar ist in crypt-vol-1 zu finden. Bitte vergessen Sie nicht, dieses und andere Volumes zu sichern. #KeinBackupkeinMitleid

* * *

mailcow ausprobieren (Demos)[¶](https://docs.mailcow.email/de/#mailcow-ausprobieren-demos "Permanent link")
-----------------------------------------------------------------------------------------------------------

Haben wir Ihr Interesse geweckt? Verschaffen Sie sich in unseren offiziellen **mailcow Demos** einen ersten Überblick über die Funktionalitäten von mailcow und Ihrer mailcow UI!

Wir stellen zwei verschiedene Demos bereit:

*   **[demo.mailcow.email](https://demo.mailcow.email/)** ist die altbekannte Demo, welche sich am **Stabilen Stand** der mailcow orientiert (master Branch auf GitHub). 
*   **[nightly-demo.mailcow.email](https://nightly-demo.mailcow.email/)** ist die **Nightly Demo**, welche Testfunktionen beherbergt. (Also insbesondere für alle interessant, die keine Möglichkeit haben sich eine Testinstanz selbst zu erstellen.) (nightly Branch auf GitHub)

Nutzen Sie diese Anmeldedaten für die Demos

| Login Typ | Benutzername | Passwort | URL Endpunkt |
| --- | --- | --- | --- |
| **Administrator** | admin | moohoo | `/admin` |
| **Domänen-Administrator** | department | moohoo | `/domainadmin` |
| **Normaler Benutzer** | [demo@440044.xyz](mailto:demo@440044.xyz) | moohoo | `/` |

_Die Anmeldedaten für die Logins funktionieren bei beiden Varianten._

Immer auf dem neusten Stand

Die Demo Instanzen erhalten die neusten Updates direkt nach Release von GitHub. Vollautomatisch, ohne Downtime!

* * *

Unterstützen Sie das mailcow Projekt[¶](https://docs.mailcow.email/de/#unterstutzen-sie-das-mailcow-projekt "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------

Bitte erwägen Sie einen Supportvertrag gegen eine geringe monatliche Gebühr unter [Servercow](https://www.servercow.de/mailcow?#support)[1](https://docs.mailcow.email/de/#fn:1), um die weitere Entwicklung zu unterstützen. _Wir_ unterstützen _Sie_, während _Sie_ _uns_ unterstützen. :)

Wenn Sie super toll sind und uns ohne Vertrag unterstützen möchten, können Sie eine SAL (Stay-Awesome License) erhalten, die Ihre Unterstützung bestätigt (kaufbar als flexible Einmalzahlung) bei [Servercow](https://www.servercow.de/mailcow#sal).

* * *

Hilfe gefällig?[¶](https://docs.mailcow.email/de/#hilfe-gefallig "Permanent link")
----------------------------------------------------------------------------------

Es gibt zwei Möglichkeiten, Support für Ihre mailcow-Installation zu erhalten.

### Kommerzieller Support[¶](https://docs.mailcow.email/de/#kommerzieller-support "Permanent link")

Für professionellen und priorisierten kommerziellen Support können Sie ein Basis-Support-Abonnement unter [Servercow](https://www.servercow.de/mailcow#support) abschließen. Für kundenspezifische Anfragen oder Fragen, kontaktieren Sie uns stattdessen bitte unter [info@servercow.de](mailto:info@servercow.de).

Darüber hinaus bieten wir auch eine voll ausgestattete und verwaltete [managed mailcow](https://www.servercow.de/mailcow#managed) an. Auf diese Weise kümmern wir uns um alles technische und Sie können Ihr ganzes Mail-Erlebnis auf eine problemlose Weise genießen.

Die Alternative ist unser kostenloser Community-Support auf unseren verschiedenen Kanälen unten. Bitte beachten Sie, dass dieser Support von unserer großartigen Community rund um mailcow betrieben wird. Diese Art von Support ist best-effort, freiwillig und es gibt keine Garantie für irgendetwas.

*   [mailcow Community @ community.mailcow.email](https://community.mailcow.email/)

*   [Telegram (Support) @ t.me/mailcow](https://t.me/mailcow)

*   [Telegram (Off-Topic) @ t.me/mailcowOfftopic](https://t.me/mailcowOfftopic)

Telegram Desktop-Clients sind für [mehrere Plattformen](https://desktop.telegram.org/) verfügbar. Sie können den Gruppenverlauf nach Stichworten durchsuchen.

Nur für **Bug Tracking, Feature Requests und Codebeiträge**:

*   [mailcow/mailcow-dockerized @ GitHub](https://github.com/mailcow/mailcow-dockerized)

### Neuigkeiten und Release Informationen:[¶](https://docs.mailcow.email/de/#neuigkeiten-und-release-informationen "Permanent link")

Für Ankündigungen oder Release Informationen sind wir auf folgenden Plattformen vertreten:

*   [mailcow @ X/Twitter](https://twitter.com/mailcow_email)

*   [@doncow @ mailcow.social](https://mailcow.social/@doncow)

Oder alternativ auf unserem Blog:

*   [mailcow.email](https://mailcow.email/)

* * *

1.   mailcow und Servercow sind eingetragene Marken der The Infrastructure Company GmbH.[↩](https://docs.mailcow.email/de/#fnref:1 "Jump back to footnote 1 in the text")[↩](https://docs.mailcow.email/de/#fnref2:1 "Jump back to footnote 1 in the text")
