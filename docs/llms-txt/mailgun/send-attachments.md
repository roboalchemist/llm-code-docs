# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/send-attachments.md

# Send with Attachments

Adding attachments uses the 'attachment' parameter. This example attaches 2 files to the email:

```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject="Hello there!" \
    -F text='Testing some Mailgun awesomeness!' \
    -F attachment=@tps-report.txt \
    -F attachment=@cover-letter.txt
```

You can also use the 'inline' parameter to include inline files that are intended to be displayed in the message itself (note the `cid:email.jpg` reference):

```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject="Hello there!" \
    -F inline=@email.jpg \
    --form-string html='<html><body><p>Hello from <img src="cid:email.jpg"/></p></body></html>'
```

## Attaching Metadata to Messages

When sending messages, you can attach data for later retrieval. For instance, you can attach campaign or recipient identifiers to messages to help relate webhook payloads or events retrieved from mailgun back to marketing campaigns or individual recipients in your system.

It's important to note that when using variables, the `X-Mailgun-Variables` header will be included in the MIME of the delivered email. This means that recipients who receive emails when variables are used will be able to see the variables if they view the MIME headers.

### Attaching Metadata to emails via SMTP

When sending messages via SMTP, you can attach data by providing a X-Mailgun-Variables header. You can provide multiple X-Mailgun-Variables headers, their map values will be combined. The header data must be in JSON map format, as shown in the example below.

```JSON
X-Mailgun-Variables: {"first_name": "John", "last_name": "Smith"}
X-Mailgun-Variables: {"my_message_id": 123}
```

The value of the "X-Mailgun-Variables" header must be a valid JSON string, otherwise Mailgun won't be able to parse it. If your "X-Mailgun-Variables" header exceeds 998 characters, you should use folding to spread the variables over multiple lines.

### Attaching Metadata to emails via API

If you are sending email via the HTTP API, you can attach data by providing a single or multiple form parameters via `v:` as shown in the example below.

```JSON
v:first_name=John
v:last_name=Smith
v:my_message_id=123
```

The data provided will be included in the recipient's email via a header called X-Mailgun-Variables. Additionally, the data will also be available via webhook payloads and events returned from the events API. The data will be attached to these payloads via the user-variables field as a JSON map. For example:

```JSON
{
    "event": "delivered",
    "user-variables": {
        "first_name": "John",
        "last_name": "Smith",
        "my_message_id": "123"
    }
}
```

### X-Mailgun-Variables substitutions with recipient-variables

When sending batches of emails, you can use values from recipient variables to provide a custom variable per recipient using templating.

For example, given a variable of `v:recipient-id=%recipient.id%` and a recipient variable of `{"user1@example.com":{"id":123}}`, events and webhooks associated with the recipient `user1@example.com` will contain a user-variable field with the content of `{"recipient-id":"123"}`