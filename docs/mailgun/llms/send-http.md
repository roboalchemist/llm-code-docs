# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/send-http.md

# Send via HTTP

When sending an email via HTTP on our platform, Mailgun offers two options:

- You can [submit the individual parts](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages) (text, HTML, attachments, etc.) of your messages
- You can [send a pre-built MIME](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages-mime). This assumes you've built an RFC-compliant MIME in your choice of tooling


Some things to consider when sending emails:

- If your domain exists in our EU region, be sure to substitute âhttps://api.mailgun.netâ with âhttps://api.eu.mailgun.netâ
- The maximum message size Mailgun supports is 25MB
- An error will be returned with `"parameter is not a valid address"` if the provided email address fails syntax checks in accordance with RFC5321, RFC5322, RFC6854
- Mailgun *does* support receiving GZIP-compressed HTTP bodies if the `Content-Encoding: gzip` header is present
  - Bodies must be gzip-compressed as defined by [RFC1952](https://www.rfc-editor.org/rfc/rfc1952.html)
  - Compressing message bodies does *not* bypass the above limit. This limit is enforced on the *uncompressed* body
- Mailgun does have rate limits in place to protect our system. In the unlikely case you encounter them and need them raised, please reach out to our support team.


We understand email is complicated, and have provided many options to tailor your request to your personal needs. Please see all our [sending options](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages) here!

**Here are a few examples to get you familiar with interacting with the API (using cURL)**

### Sending Basic Text

Sending a simple text-based email using Mailgun's HTTP API requires a few parameters at minimum:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient-1@example.com \
    -F to=recipient-2@example.com \
    -F subject='Hello there!' \
    -F text='Testing some Mailgun awesomeness!'
```

What actually happened:

- Mailgun assembled a valid MIME message based on your input parameters
- Delivered the email to both recipients listed with the `to` parameters
- Added log entries to our full text index that we Accepted the email, and if delivered successfully, added a Delivered event. (See the Events API for more details)


### Send With Text and HTML Versions

By including both the 'text' and 'html' parameters, you can offer two different versions of your email to
the user:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject="Hello there!" \
    -F text='This will be the text-only version' \
    --form-string html='<html><body><p>This is the HTML version</p></body></html>'
```

info
A common gotcha: note the use of `--form-string` in this example for the HTML part. Without this, your
cURL command may fail to execute properly!

### Send a Single Message With Tracking

While tracking can be enabled for all messages in your Dashboard, you can also selectively enable tracking on
a per-message basis. To enable all tracking types you use the 'o:tracking="yes"' parameter. Otherwise, you
can enable only specific tracking for opens ('o:tracking-opens') or clicks ('o:tracking-clicks'):


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject="Hello there!" \
    -F text='Testing some Mailgun awesomeness!' \
    -F o:tracking-opens="yes"
```

### Send a Message using a Template with variable substitution

Not all templates use variables, but assuming it has variable called "name", here are two ways of going about the substitution. The first is recommended since it will hide the variables from the MIME and not show in events.


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from="Excited User <postmaster@YOUR_DOMAIN_NAME>" \
    -F to="recipient@example.com" \
    -F subject="Mailgun is awesome" \
    -F template="My Great Template Name" \
    -F t:variables="{\"name\":\"Foo Bar\"}"
```

Or, the old way, which will include the variables in the MIME under `X-Mailgun-Variables` and they will appear in the events / webhooks under `user-variables`


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from="Excited User <postmaster@YOUR_DOMAIN_NAME>" \
    -F to="recipient@example.com" \
    -F subject="Mailgun is awesome" \
    -F template="My Great Template Name" \
    -F v:name="Foo Bar"
```

### Send a Customized Batch Message

Batch messages are a great way to send emails to multiple people, while still being able to customize the content for each recipient.


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from="Excited User <postmaster@YOUR_DOMAIN_NAME>" \
    -F to="recipient@example.com, recipient-two@example.com" \
    -F subject="Mailgun is awesome" \
    -F text="Hello %recipient.fname% %recipient.lname%! Enjoy a free %recipient.gift%" \
    -F recipient-variables="{\"recipient@example.com\": {\"fname\":\"Bob\", \"lname\":\"Mailgun\", \"gift\":\"high five\"}, \"recipient-two@example.com\": {\"fname\":\"Foo\", \"lname\":\"Bar\", \"gift\":\"fist bump\"}}"
```

### Send a Message With Specified Delivery Time

The 'o:deliverytime' option allows you to specify when an email should be sent. It uses RFC822 date formatting
and can be no more than 3 days in the future:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject="Hello there!" \
    -F text='Testing some Mailgun awesomeness!' \
    -F o:deliverytime='Fri, 14 Oct 2011 23:10:10 -0000'
```

Info
If your billing plan supports 7 or more days of storage capability, you can schedule emails out up to 7 days.

### Send a Message using Tags

Mailgun allows you to Tag emails for further analytics within our platform:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject="Hello there!" \
    -F text='Testing some Mailgun awesomeness!' \
    -F o:tag='September newsletter' \
    -F o:tag='newsletters'
```

See [Tags](https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/track-tagging) for more information!

### Re-Delivering a Previously-Sent Email

By default: emails sent through our APIs are stored for 72 hours. If you navigate to your Dashboard, check the
Logs page and find a message sent within this time frame that you wish to resend, you should have a
'storage.url' field. Using that exact URL in your POST request, along with one or more 'to' parameters,
you can deliver that MIME to the provided recipients:


```bash
curl -s --user 'api:YOUR_API_KEY' {{STORAGE.URL}} \
    -F to='bob@example.com, john@example.com'
```