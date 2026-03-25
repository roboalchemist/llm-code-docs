# Source: https://docs.iredmail.org/allow.insecure.pop3.imap.smtp.connections.html

Title: Allow insecure POP3/IMAP/SMTP connections without STARTTLS

URL Source: https://docs.iredmail.org/allow.insecure.pop3.imap.smtp.connections.html

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

*   [Allow insecure POP3/IMAP/SMTP connections without STARTTLS](https://docs.iredmail.org/allow.insecure.pop3.imap.smtp.connections.html#allow-insecure-pop3imapsmtp-connections-without-starttls)
    *   [Allow insecure POP3/IMAP connections](https://docs.iredmail.org/allow.insecure.pop3.imap.smtp.connections.html#allow-insecure-pop3imap-connections)
    *   [Allow insecure SMTP connection on port 25](https://docs.iredmail.org/allow.insecure.pop3.imap.smtp.connections.html#allow-insecure-smtp-connection-on-port-25)

With default iRedMail setting, all clients are forced to use POP3/IMAP/SMTP services over STARTTLS for secure connections. If your mail clients try to access mailbox via protocol POP3/IMAP without TLS support, you will get error message like below:

```
Plaintext authentication disallowed on non-secure (SSL/TLS) connections
```

This tutorial describes how to allow insecure connection for daily use.

Allow insecure POP3/IMAP connections
------------------------------------

If you want to enable POP3/IMAP services without STARTTLS for some reason (again, not recommended), please update below two parameters in Dovecot config file `/etc/dovecot/dovecot.conf` and restart Dovecot service:

*   on Linux and OpenBSD, it's `/etc/dovecot/dovecot.conf`
*   on FreeBSD, it's `/usr/local/etc/dovecot/dovecot.conf`

```
disable_plaintext_auth=no
ssl=yes
```

Again, it's strongly recommended to use only POP3S/IMAPS for better security.

Default and recommended setting configured by iRedMail is:

```
disable_plaintext_auth=yes
ssl=required
```

Allow insecure SMTP connection on port 25
-----------------------------------------

Please comment out lines below in Postfix config file `/etc/postfix/main.cf` and reload or restart Postfix service:

```
smtpd_sasl_auth_enable = yes
smtpd_sasl_security_options = noanonymous

# force all clients to use secure connection through port 25
#smtpd_tls_auth_only=yes
```
