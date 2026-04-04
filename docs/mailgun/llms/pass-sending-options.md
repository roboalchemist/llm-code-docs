# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/pass-sending-options.md

## Passing Sending Options

When sending emails there are a variety of sending options to consider. See the table below:

- For HTTP please use the specified `o:` parameter, these are also found in our [API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages)
- For SMTP you must use the SMTP Headers below


| HTTP Option | SMTP Header | Description |
|  --- | --- | --- |
| `o:tag` | `X-Mailgun-Tag` | The Tag string is used for aggregating stats. You can make a message with several categories by setting multiple X-Mailgun-Tag headers. |
| `o:dkim` | `X-Mailgun-Dkim` | Enables/disables DKIM signatures on a per-message basis. Use `yes` or `no` |
| `o:testmode` | `X-Mailgun-Drop-Message` | Enables sending in test mode. Note: Sending in Test Mode will not actually deliver an email but will emit a `delivered` event with a 650 status code `Pass`, `yes`, or `no` if needed. |
| `o:tracking` | `X-Mailgun-Track` | Toggles tracking on a per-message basis. `Pass`, `yes` or `no`. |
| `o:tracking-clicks` | `X-Mailgun-Track-Clicks` | Toggles clicks tracking on a per-message basis. It has a higher priority than the domain-level setting. `Pass`, `yes`, `no`, or `htmlonly` |
| `o:tracking-opens` | `X-Mailgun-Track-Opens` | Toggles opens tracking on a per-message basis. It has a higher priority than the domain-level setting. `Pass`, `yes` or `no` |
| `o:sending-ip` | `X-Mailgun-Sending-Ip` | Used to specify an IP Address to send an email that is owned by your account |
| `o:sending-ip-pool` | `X-Mailgun-Sending-Ip-Pool` | If an IP Pool ID is provided, the email will be delivered with an IP that belongs in that pool |
| `o:require-tls` | `X-Mailgun-Require-TLS` | Use this header to control TLS connection settings. If set, Mailgun will only deliver the message over a secure TLS connection with the ESP. If TLS is not available, the delivery will fail |
| `o:skip-verification` | `X-Mailgun-Skip-Verification` | Use this header to control TLS (Transport Layer Security) connection settings. |
| `o:secondary-dkim` | `X-Mailgun-Secondary-DKIM` | Specify a second domain key to sign the email with. The value is formatted as `signing_domain,selector`, e.g. `example.com,s1`. This tells Mailgun to also sign the message with the signing domain `example.com` using the selector `s1`. Note: the domain key specified must have been created and activated. |
| `o:secondary-dkim-public` | `X-Mailgun-Secondary-DKIM-Public` | This header specifies an alias of the domain key specified in `X-Mailgun-Secondary-DKIM`. Also formatted as `public_signing_domain/selector`. The `X-Mailgun-Secondary-DKIM` header must also be provided if this header is used. Mailgun will sign the message with the provided key of the secondary DKIM, but use the public secondary DKIM name and selector. Note: We will perform a DNS check prior to singing the message to ensure the public keye matches the secondary DKIM |
| `o:deliverytime` | `X-Mailgun-Deliver-By` | Specifies the scheduled delivery time in [RFC-2822 format](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview#date-format). Depending on your billing plan, you can schedule messages up to 3 or 7 days in advance. If your domain has a custom message_ttl (time-to-live) setting, this value determines the maximum scheduling duration. Example: 'Fri, 14 Oct 2011 12:00:00 0000' |
| `o:deliverytime-optimize-period` | `X-Mailgun-Delivery-Time-Optimize-Period` | Toggles STO on a per-message basis. The string should be set to the number of hours in `[0-9]+h` format. |
| `o:deliver-within` | `X-Mailgun-Deliver-Within` | Specifies the maximum time window for delivering the message. Accepts values in format `[0-9]h[0-9]m` (e.g., `1h30m`, `30m`, `24h`), with a minimum of `5m` and maximum of `24h`. For scheduled messages, the delivery window starts from the scheduled time. The standard retry schedule applies within this window, so shorter timeframes may result in fewer delivery attempts. |
| `o:time-zone-localize` | `X-Mailgun-Time-Zone-Localize` | Toggles TZO on a per-message basis. The string should be set to the preferred delivery time in `HH:mm` or `hh:mmaa` format, where `HH:mm` is used for a 24-hour format without AM/PM, and `hh:mmaa` is used for 12-hour format with AM/PM. |
| `recipient-variables` | `X-Mailgun-Recipient-Variables` | Use this header to provide a JSON dictionary of variables to substitute for Batch messages. |
| `template` | `X-Mailgun-Template-Name` | Name for the template to be rendered as the message body. |
| `t:version` | `X-Mailgun-Template-Version` | Optional: Version of the template to be used, if different from the current active template. |
| `v:key=value` | `X-Mailgun-Variables` | If sending with a Template, the provided data will be treated as the values to substitute with the templates variables. Note that `X-Mailgun-Template-Variables`/`t:variables` will override these if also provided. If a template is not used, the provided data will be treated as metadata and appended to the user-variabled field in events / webhooks. NOTE: These variables are visible in the email MIME! |
| `t:variables` | `X-Mailgun-Template-Variables` | A valid JSON-encoded dictionary used as the input for template variable expansion. See Templates docs for more information. Note: These variables will be preferred over X-Mailgun-Variables, e.g. user variables |
| `o:tracking-pixel-location-top` | `X-Mailgun-Track-Pixel-Location-Top` | If you send long emails that experience truncation or other rendering issues at the recipient, you can ensure opens are being tracked accurately with placement of the tracking pixel at the top of your emails |


### A common gotcha with Templates

If you send an email with, only, a `text/plain body` *and* use the `X-Mailgun-Template-Name` header: this will *not* result in a template-rendered email. `text/plain` bodies are, typically, what you get when you send with Swaks!

To get around this issue, add the correct `Content-Type` header accordingly:


```
--add-header 'Content-Type: text/html; charset="utf-8"'
```

You do *not* have to add this header explicitly via the HTTP API!