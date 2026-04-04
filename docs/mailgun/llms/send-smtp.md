# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/send-smtp.md

## Send via SMTP

First you'll need to grab your SMTP credentials (user and password).

SMTP credentials are set and managed on a per-domain basis. You can view and modify them via our HTTP API or UI.
To access them in our UI, navigate on the sidebar to `Sending` -> `Domain Settings`, select your domain from the
dropdown, then select the `SMTP Credentials` tab. Go to the article  Can I Customize My SMTP Credentials? for more information.

To send an email via SMTP you can utilize Swaks via your command line.


```bash
# Swaks is the cURL equivalent for SMTP, install it first:
curl http://www.jetmore.org/john/code/swaks/files/swaks-20130209.0/swaks -o swaks
# Set the permissions for the script so you can run it
chmod +x swaks
# It's based on perl, so install perl
sudo apt-get -y install perl
# now send!
./swaks --auth \
       --server smtp.mailgun.org \
       --au YOUR-SMTP-USER \
       --ap YOUR-SMTP-PASSWORD \
       --to recipient@example.com \
       --h-Subject: "Hello" \
       --body 'Testing some Mailgun awesomness!'
```

Mailgun SMTP servers listen on ports `25`, `465`, `587`, and `2525`. Port 465 requires a TLS connection. Ports `25`, `587`, and `2525` require a non-TLS connection but may be upgraded to TLS using the STARTTLS command. We offer many different ports due
to some ISPs blocking / throttling certain SMTP ports.

Learn more about ports by reading our article,   Which SMTP Port Should I Use? Undertsanding Ports 25, 465,& 587.

| **Port** | **Requirements** |
|  --- | --- |
| `25` | Requires a non-TLS connection but may be upgraded to TLS using the STARTTLS command. |
| `465` | Requires a TLS connection |
| `587` | Requires a non-TLS connection but may be upgraded to TLS using the STARTTLS command. |
| `2525` | Requires a non-TLS connection but may be upgraded to TLS using the STARTTLS command. |


Info
* Some ISPs are blocking or throttling SMTP port 25. Using port 587 is recommended.
* Google Compute Engine allows port 2525 for SMTP submission.
* SMTP send will error with "Cannot parse to address" or "cannot parse from address" if the provided email address fails syntax checks in accordance with RFC5321, RFC5322, RFC6854


Warning!
IP addresses for HTTP and SMTP API endpoints will change frequently and be subjected to change without notice. Be sure there are no IP-based ACLs that would prevent communication to new IP addresses that may be added or removed at any time.

## Passing Sending Options

| SMTP Header | Description |
|  --- | --- |
| `X-Mailgun-Tag` | The Tag string is used for aggregating stats. You can make a message with several categories by setting multiple X-Mailgun-Tag headers. |
| `X-Mailgun-Dkim` | Enables/disables DKIM signatures on a per-message basis. UseÂ `yes`Â orÂ `no` |
| `X-Mailgun-Drop-Message` | Enables sending in test mode. Note: Sending in Test Mode will not actually deliver an email but will emit aÂ `delivered`Â event with a 650 status codeÂ `Pass`,Â `yes`, orÂ `no`Â if needed. |
| `X-Mailgun-Track` | Toggles tracking on a per-message basis.Â `Pass`,Â `yes`Â orÂ `no`. |
| `X-Mailgun-Track-Clicks` | Toggles clicks tracking on a per-message basis. It has a higher priority than the domain-level setting.Â Pass,Â yes,Â no |
| `X-Mailgun-Track-Opens` | Toggles opens tracking on a per-message basis. It has a higher priority than the domain-level setting.Â Pass,Â yesÂ orÂ no |
| `X-Mailgun-Sending-Ip` | Used to specify an IP Address to send an email that is owned by your account |
| `X-Mailgun-Sending-Ip-Pool` | If an IP Pool ID is provided, the email will be delivered with an IP that belongs in that pool |
| `X-Mailgun-Require-TLS` | Use this header to control TLS connection settings. If set, Mailgun will only deliver the message over a secure TLS connection with the ESP. If TLS is not available, the delivery will fail. |
| `X-Mailgun-Skip-Verification` | Use this header to control TLS (Transport Layer Security) connection settings. |
| `X-Mailgun-Secondary-DKIM` | Specify a second domain key to sign the email with. The value is formatted asÂ `signing_domain,selector`, e.g.Â `example.com,s1`. This tells Mailgun to also sign the message with the signing domainÂ `example.com`Â using the selectorÂ `s1`. Note: the domain key specified must have been created and activated. |
| `X-Mailgun-Secondary-DKIM-Public` | This header specifies an alias of the domain key specified inÂ `X-Mailgun-Secondary-DKIM`. Also formatted asÂ public_signing_domain/selector. TheÂ X-Mailgun-Secondary-DKIMÂ header must also be provided if this header is used. Mailgun will sign the message with the provided key of the secondary DKIM, but use the public secondary DKIM name and selector. Note: We will perform a DNS check prior to singing the message to ensure the public keye matches the secondary DKIM |
| `X-Mailgun-Deliver-By` | Specifies the scheduled delivery time in [RFC-2822 format](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview#date-format). Depending on your billing plan, you can schedule messages up to 3 or 7 days in advance. If your domain has a custom message_ttl (time-to-live) setting, this value determines the maximum scheduling duration. Example: 'Fri, 14 Oct 2011 12:00:00 0000' |
| `X-Mailgun-Deliver-Within` | Specifies the maximum time window for delivering the message. Accepts values in format `[0-9]h[0-9]m` (e.g., `1h30m`, `30m`, `24h`), with a minimum of `5m` and maximum of `24h`. For scheduled messages, the delivery window starts from the scheduled time. The standard retry schedule applies within this window, so shorter timeframes may result in fewer delivery attempts. |
| `X-Mailgun-Delivery-Time-Optimize-Period` | Toggles STO on a per-message basis. The string should be set to the number of hours inÂ `[0-9]+h`Â format. |
| `X-Mailgun-Time-Zone-Localize` | Toggles TZO on a per-message basis. The string should be set to the preferred delivery time inÂ `HH:mm`Â orÂ `hh:mmaa`Â format, whereÂ `HH:mm`Â is used for a 24-hour format without AM/PM, andÂ `hh:mmaa`Â is used for 12-hour format with AM/PM. |
| `X-Mailgun-Recipient-Variables` | Use this header to provide a JSON dictionary of variables to substitute for Batch messages. |
| `X-Mailgun-Template-Name` | Name for the template to be rendered as the message body. |
| `X-Mailgun-Template-Version` | Optional: Version of the template to be used, if different from the current active template. |
| `X-Mailgun-Variables` | If sending with a Template, the provided data will be treated as the values to substitute with the templates variables. Note thatÂ `X-Mailgun-Template-Variables/t:variables`Â will override these if also provided. If a template is not used, the provided data will be treated as metadata and appended to the user-variabled field in events / webhooks. NOTE: These variables are visible in the email MIME! |
| `X-Mailgun-Template-Variables` | A valid JSON-encoded dictionary used as the input for template variable expansion. See Templates docs for more information. Note: These variables will be preferred over X-Mailgun-Variables, e.g. user variables. |
| `X-Mailgun-Track-Pixel-Location-Top` | If you send long emails that experience truncation or other rendering issues at the recipient, you can ensure opens are being tracked accurately with placement of the tracking pixel at the top of your emails. |
| `X-Mailgun-Archive-To` | Sends a copy of successfully delivered messages to the specified URL via HTTP POST. The request uses Content-Type: application/mime and contains the exact message the recipient's SMTP server received. **NOTE: These are accounted for and billed as delivered messages** |
| `X-Mailgun-Suppress-Headers` | Removes the specified `X-Mailgun` header or all `X-Mailgun` headers if `all` is specified as the header value.  Can be specified multiple times. |


## SMTP Credentials

Mailgun gives you the ability to programmatically manage SMTP credentials which can be used to send mail.  Please see the [API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/credentials) for the complete API reference.