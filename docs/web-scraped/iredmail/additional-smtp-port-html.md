# Source: https://docs.iredmail.org/additional.smtp.port.html

Title: Allow internal network devices to send email with insecure connection

URL Source: https://docs.iredmail.org/additional.smtp.port.html

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

*   [Allow internal network devices to send email with insecure connection](https://docs.iredmail.org/additional.smtp.port.html#allow-internal-network-devices-to-send-email-with-insecure-connection)
    *   [Purpose](https://docs.iredmail.org/additional.smtp.port.html#purpose)
    *   [Open additional smtp port in Postfix](https://docs.iredmail.org/additional.smtp.port.html#open-additional-smtp-port-in-postfix)
    *   [Update firewall rules to deny access from external network](https://docs.iredmail.org/additional.smtp.port.html#update-firewall-rules-to-deny-access-from-external-network)

Purpose
-------

If you have some network devices like printer, firewall, and they need to send out notification or report email with insecure smtp connection, please try steps below to get it working without breaking default security settings.

Open additional smtp port in Postfix
------------------------------------

Since iRedMail-0.9.3, with default iRedMail settings, port 25 is used for postscreen service, all clients are forced to submit through port 587 with STARTTLS for secure connection.

To support network devices which doesn't support STARTTLS and SSL, we can ask Postfix to listen on additional port for smtp service by appending below line in `/etc/postfix/master.cf` (on Linux/OpenBSD) or `/usr/local/etc/postfix/master.cf` (on FreeBSD):

```
2525      inet  n       -       -       -       -       smtpd
  -o syslog_name=postfix/2525
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_sasl_security_options=noanonymous
  -o smtpd_tls_security_level=may
  -o smtpd_sender_restrictions=permit_mynetworks,permit_sasl_authenticated,reject
```

*   `2525` is the new port number for smtp service, you're free to change it to your favourite port number.
*   `smtpd_tls_security_level=may` allows both secure (TLS) and insecure connections.

Restarting Postfix service is required. After restarting, you can check whether it's listening on this new port:

```
netstat -ntlp | grep 2525
```

Now update your network devices to send email through this port number, without STARTTLS and SSL.

Note

SMTP authentication is still required to send email.

Update firewall rules to deny access from external network
----------------------------------------------------------

It's dangerous to expose this new port number to external network, so you must update your firewall rules to deny access from external network to this new port number.
