# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/batch-sending.md

# Batch Sending

Mailgun supports the ability to send to a group of recipients through a single API call, or SMTP session.
This is achieved by:

- Using Batch Sending by specifying multiple recipient email addresses as `to` parameters and using Recipient Variables.
- Using Mailing Lists with the Template Variables


Warning!
When using Batch Sending, it is important to also use Recipient Variables. This will ensure that Mailgun will send an individual to each recipient in the **to** field. If this is not done, the email will show all recipients emails in the **to** field for all recipients

### Recipient Variables

**Recipient Variables** are custom variables that you define to allow the ability to send a custom message to each recipient while using a single API call (or SMTP session).

To access a Recipient Variable within your email, simply reference %recipient.yourkey%.
For example, consider the following JSON:


```JSON
{
  "user1@example.com" : {"unique_id": "ABC123456789"},
  "user2@example.com" : {"unique_id": "ZXY987654321"}
}
```

To reference the above variable within your email, use %recipient.unique_id%

Recipient Variables allow to:

- Submit a message template
- Include multiple recipients
- Include a set of key value pairs with unique data for each recipient



```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=alice@example.com \
    -F to=bob@example.com \
    -F subject="Hey %recipient.name%" \
    -F text='If you wish to unsubscribe, click <https://mailgun.com/unsubscribe/%recipient.id%>' \
    -F recipient-variables='{"alice@example.com": {"name":"Alice", "id":1}, "bob@example.com": {"name":"Bob", "id":2}}' \
```

The example above: Alice and Bob both will get personalized subject lines, "Hey, Alice", and "Hey, Bob", as well as unique unsubscribe links.

Info
- The maximum number of recipients allowed for batch is 1,000
- Recipient variables should be set as a valid JSON-encoded dictionary where key is a plain recipient address, and value is a dictionary with variables.


When sent via SMTP, recipient variables can be included by adding the following header to your email:

`X-Mailgun-Recipient-Variables: {"user1@example.com": {"unique\_id": "ABC123456789"}}`

Example:


```MIME
X-Mailgun-Recipient-Variables: {"bob@example.com": {"first":"Bob", "id":1}, "alice@example.com": {"first":"Alice", "id": 2}}
From: me@example.com
To: %recipient%
Date: 29 Mar 2016 00:23:35 -0700
Subject: Hello, %recipient.first%!
Message-Id: <20160329071939.35138.9413.6915422C@example.com>
Content-Type: text/plain; charset="us-ascii"
Content-Transfer-Encoding: quoted-printable

Hi, %recipient.first%,
=20
Please review your profile at example.com/orders/%recipient.id%.
=20
Thanks,
Example.com Team
```

Info
- The value of the "X-Mailgun-Recipient-Variables" header should be a valid JSON string, otherwise Mailgun won't be able to parse it.
- If your "X-Mailgun-Recipient-Variables" header exceeds 998 characters, you should use folding to spread the variables over multiple lines.


They can also be supplied through a special construct called a Variable Container.

To contain variables, create the following MIME construct:


```MIME
multipart/mailgun-variables
--application/json (base64 encoded)
--message/rfc822
----original-message
```

In this construct, JSON will be Base64 encoded, and will be stored inside the part of the body which will handle recipient variables containing special characters.

Example:


```JSON
Content-Type: multipart/mailgun-variables; boundary="8686cc907910484e9d21c54776cd791c"
Mime-Version: 1.0
From: me@example.com
Date: Thu, 26 Jul 2012 15:43:07 +0000
Message-Id: <20120726154307.29852.44460@definebox.com>
Sender: bob=bob-mg@definebox.com

--8686cc907910484e9d21c54776cd791c
Mime-Version: 1.0
Content-Type: application/json
Content-Transfer-Encoding: base64

eyJkZXNjcmlwdGlvbiI6ICJrbGl6aGVudGFzIn0=

--8686cc907910484e9d21c54776cd791c
Content-Type: message/rfc822
Mime-Version: 1.0

Date: Thu, 26 Jul 2012 19:42:55 +0400
To: %recipient.description% <support@mailgunhq.com>
From: me@example.com
Subject: (rackspace) Hello
 MSK 2012 support@mailgunhq.com %recipient.description%
Message-Id: <20120726154302.29322.40670@definebox.com>

support@mailgunhq.com %recipient.description%

--8686cc907910484e9d21c54776cd791c--
```

Info
Mailgun recommends only placing recipient variables in one of the supported locations described. If you feel you MUST use multiple locations, see the Recipient Variable Precedence section below to understand how we merge recipient variables together.

### Recipient Variable Precedence

If Recipient variables are found in multiple supported locations, they are merged together with the following precedence, in order of top-to-bottom, highest-to-lowest priority:

`multipart/mailgun-variables`: Variable Container mentioned above (highest priority)

`X-Mailgun-Recipient-Variables`: Headers within the main MIME `message/rfc822` body container

`recipient-variables API parameter`: API parameter (lowest-priority)