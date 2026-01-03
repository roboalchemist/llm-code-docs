# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tls-connection-settings/skip-verification.md

# Skip verification

The skip verification option in TLS sending connection settings allows you to bypass certificate validation during email transmission, which can be useful for testing but may reduce connection security.

If set to *True*, the certificate and hostname will not be verified when trying to set up a TLS connection, and Mailgun will accept any certificate during delivery. If set to *False*, Mailgun will verify the certificate and hostname. If either one cannot be verified, a TLS connection will not be set up. The default is False.

Look at the table below to help you better understand the configuration possibilities and potential issues.

Info
Consider the type of threat you are concerned with when deciding how to configure sending settings.
** By default, *require-tls* and *skip-verification* are *false.*

| **Require-tls** | **Skip-verification** | **TLS** | **TLS Active Attack (MITM)** | **TLS Passive Attack (Capture)** | **Passive Plaintext Capture** |
|  --- | --- | --- | --- | --- | --- |
| false | false | Attempt | Not Possible | Not Possible | Possible via downgrade |
| false | true | Attempt | Posible | Not Possible | If STARTTLS not offered |
| true | false | Required | Not Possible | Not Possible | Not Possible |
| true | true | Required | Possible | Not Possible | Not Possible |


Additionally, the following fields are available in your logs under *delivery-status* to indicate how the message was delivered:

| **Field** | **Description** |
|  --- | --- |
| `tls` | Indicates if a TLS connection was used or not when delivering the message |
| `Certificate-verified` | Indicates if Mailgun verified the certificate or not when delivering the message |
| `mx-host` | Tells you the MX server Mailgun connected to deliver the message |