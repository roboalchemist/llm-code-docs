# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/smtp-protocol/smtp-relay.md

# SMTP Relay

You can configure your own mail server to relay mail via Mailgun (example below). To do so, you will need the following three variables on the Control Panel.

- Your SMTP username
- Your SMTP password
- SMTP host name mail server (these instructions will use smtp.mailgun.org as an example)


You have an SMTP username and password for each domain you have at Mailgun. To send mail from a particular domain, use the proper credentials.

## Postfix Instructions

You must configure a relay host with SASL authentication, as shown:


```JSON
# /etc/postfix/main.cf:

mydestination = localhost.localdomain, localhost
relayhost = [smtp.mailgun.org]:587
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = static:postmaster@mydomain.com:password
smtp_sasl_security_options = noanonymous

# TLS support
smtp_tls_security_level = may
smtpd_tls_security_level = may
smtp_tls_note_starttls_offer = yes
```

When using TLS encryption, make sure Postfix knows where to locate the CA database for your Linus distribution:


```JSON
smtpd_tls_key_file = /etc/ssl/private/smtpd.key
smtpd_tls_cert_file = /etc/ssl/certs/smtpd.crt
smtpd_tls_CApath = /etc/ssl/certs
```

Note:
You can use SMTP Credentials, but not your Control Panel password.

## Exim Instructions

For more information, see [Exim's documentation authenticated by outgoing SMTP](https://www.exim.org/exim-html-current/doc/html/spec_html/ch-smtp_authentication.html).
You will need to configure "smarthost" for your Exim setup.

Also make sure to configure login credentials (in your /etc/exim/passwd.clinet):


```JSON
# In your exim.conf:
# In routes configuration:
mailgun:
        driver = manualroute
        domains = ! +local_domains
        transport = mailgun_transport
        route_list = * smtp.mailgun.org byname

# In transports configuration:
mailgun_transport:
        driver=smtp
        hosts_require_auth = <; $host_address
        hosts_require_tls = <; $host_address
```

Also make sure to cinfigure login credentials (in your  /etc/exim/passwd.client):


```JSON
*.mailgun.org:username:password
```

## Sendmail Instructions

Define the smarthost in your sendmail.mc before mailer definitions:


```JSON
## Mailgun
define(`SMART_HOST', `smtp.mailgun.org')dnl
FEATURE(`authinfo', `hash /etc/mail/authinfo')dnl
# optional, see http://www.sendmail.org/m4/features.html before enabling:
# FEATURE(`accept_unresolvable_domains')dnl
# FEATURE(`accept_unqualified_senders')dnl
# execute: make -C /etc/mail
## Mailgun
```

Specify login credentials in your authinfo:


```JSON
AuthInfo:smtp.mailgun.org "U:<LOGIN>" "P:<PASSWORD>" "M:PLAIN"
```

Run the following command and then restart sendmail:


```JSON
make -C /etc/mail
```