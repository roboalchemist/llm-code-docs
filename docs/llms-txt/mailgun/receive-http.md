# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/receive-forward-store/receive-http.md

## Receiving Messages via HTTP through a forward() action

When a URL is specified as a route destination through a forward() action, Mailgun will perform an HTTP POST request to the URL which contains
a parsed version of the received email. The POST will be, either, `Content-Type: application/x-www-form-urlencoded` or
`Content-Type: multipart/form-data`. We send `multipart/form-data` when the email has `attachments`.

The base set of fields we send include:

| **Parameter** | **Type** | **Description** |
|  --- | --- | --- |
| `signature` | string | A signed HMAC256 string (See [Securing Webhooks](https://documentation.mailgun.com/docs/mailgun/user-manual/events/webhooks#securing-webhooks)). |
| `timestamp` | int | The number of seconds passed since January 1, 1970 (See [Securing Webhooks](https://documentation.mailgun.com/docs/mailgun/user-manual/events/webhooks#securing-webhooks)) |
| `token` | string | A randomly generated string with a length of 50 (See [Securing Webhooks](https://documentation.mailgun.com/docs/mailgun/user-manual/events/webhooks#securing-webhooks)) |
| `subject` | string | Received email Subject |
| `sender` | string | The sender of the message as reported by MAIL FROM during SMTP chat. Note: this value *may differ* from From MIME header |
| `from` | string | The sender of the message as reported by from message header, for example "Bob <bob@example.com>" |
| `recipient` | string | The recipient of the message as reported by MAIL TO during SMTP chat |
| `message-headers` | string | A list of MIME headers dumped to a JSON string (*order of headers is preserved*) |
| `body-plain` | string | The text version of the email. This field is always present. If the incoming message only has HTML body, Mailgun will attempt to create a text representation for you. |
| `body-html` | array | An array of all `text/html` MIME parts, if any, encoded as UTF-8 |


### Stripped Message Body Fields

By default, Mailgun also attempts to provide a parsed version of each text body which, if successful, are present in
the `stripped-*` fields. There are many reasons why this process may fail due to poorly-constructed HTML documents but
we make our best effort.  If this process *does* fail: these fields are not present in the payload:

| **Parameter** | **Type** | **Description** |
|  --- | --- | --- |
| `stripped-text` | string | The text version of the message without quoted parts and signature block (if found) |
| `stripped-signature` | string | The signature block stripped from the plain text message (if found) |
| `stripped-html` | string | The HTML version of the message, without quoted parts. |


Info
*Consider using **http:/bin.mailgun.net** to debug and play with your routes. This tool allows you to forward incoming messages to a temporary URL and inspect the posted data.

Info
Not all web frameworks support multi-valued keys parameters, so the message-headers parameter was added.
**Note**: The `message-headers` field can contain duplicate values for mandatory payload fields like `subject` vs. `Subject`.

**Example:** Ruby on Rails requires a special syntax to post params like that: you need to add [] to a key to collect its values on the server side as an array.

### Attachments

As mentioned above, if the received email contains attachments AND the forward URL does not end in `mime`, we instead
POST with `Content-Type: multipart/form-data`. We add the following fields in addition to the ones listed above:

| **Parameter** | **Type** | **Description** |
|  --- | --- | --- |
| `attachment-count` | int | The number of attachments the message has. |
| `attachment-<number>` | string | A unique field name for each attachment received, suffixed with an incrementing-integer, starting at 1 |
| `content-id-map` | object | A JSON map which maps the `Content-ID` header to the correlated attachment name, if present in the MIME |


### Message Body Parsing

If your forward URL ends in `mime` or `raw-mime`: we include a `body-mime` field with the **raw** MIME content and **omit the `body-plain` and `body-html` fields**.
This allows you to have a raw copy of the MIME we received while still having the other base fields parsed out.

The payload would come as `application/x-www-form-urlencoded` with the above base fields.

Example: **http://myhost/post_mime** would receive the `body-mime` field *instead* of a `body-plain` or `body-html` field

### Response Codes for Retries

For Route POSTs, Mailgun listens to response codes from your server and reacts accordingly:

| **Received by Mailgun** | **Code description** |
|  --- | --- |
| `200 (Success)` | A HTTP 200 marks the webhook POST is successful and will not be retried. |
| `406 (Not Applicable)` | A HTTP 406 means the POST is rejected and it will not be retried. |
| `Any other code` | Mailgun will retry POST attempts according to the schedule below for webhooks other than the delivery notification. |


If a 406 error code is not returned and your application is unable to process the webhook request, Mailgun will attempt to retry (other than for delivery notification) in intervals for a total of 8 hours before stopping retries. The intervals are 10 minutes, 15 minutes, 30 minutes, 1 hour, 2 hours, and 4 hours.