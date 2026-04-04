# Source: https://documentation.mailgun.com/docs/mailgun/faq/receiving.md

# FAQ: Receiving

### Do you provide spam filtering for incoming mail?

Yes. Click on your domain in the [Control
Panel](https://app.mailgun.com/app/domains) and enable our spam
filtering service.

### How do you handle quotations from replies and signatures when receiving mail?

We parse them and provide parameters for you to handle them as you wish.
Please take a look at our `user-manual`(https://documentation.mailgun.com/docs/mailgun/user-manual/get-started) or
`api-reference`(https://documentation.mailgun.com/docs/mailgun/api-reference/intro) to see more details on the
parameters we provide.

### Why am I not receiving an email when sending via the route with the sending address as a destination?

You're most likely using GMail for sending your message. From GMail's
documentation
([https://support.google.com/mail/troubleshooter/2935079?rd=1](https://support.google.com/mail/troubleshooter/2935079?rd=1)):

Finally, if you're sending mail to a mailing list that you subscribe
to, those messages will only appear in 'Sent Mail.' This behavior also
occurs when sending to an email address that automatically forwards mail
back to your Gmail address. To test forwarding addresses or mailing
lists, use a different email address to send your message.

When a message from, say, `bob@gmail.com` goes through a route:

test@mailgun-domain.com -> bob@gmail.com

When this message arrives to GMail, it will have `bob@gmail.com` as both
sender and recipient, therefore GMail will not show it.

In other words GMail does not show you messages you sent to yourself.

The other possibility is that the address had previously experienced a
Hard Bounce and is on the 'do not send' list. Check the `Suppressions`
tab of your Control Panel for a list of these addresses and remove the
address in question if it is there.

### How do I know if HTTP POST callbacks are coming from Mailgun, and not forged?

Mailgun allows you to check the authenticity of its requests by
providing three additional parameters in every HTTP POST request it
makes. Please take a look at our [webhooks
documentation](https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/#webhooks)
for more information.

### How do I know if the sender of an email is spoofed?

There is no 100% guarantee. However, there are some good clues. Mailgun
provides DKIM and SPF verification for incoming mail, which is shown in
the MIME headers once spam filtering is enabled in the [Control
Panel](https://login.mailgun.com/login). This way you can at least know if the message is coming from
an authenticated server.

### Can I use Mailgun for my personal email address?

It's not recommended. Honestly, there are plenty of hosted email
services better suited for this than Mailgun: Gmail, Google Apps,
Outlook, etc. Mailgun is meant to be a tool for developers and their
applications.