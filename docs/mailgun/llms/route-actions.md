# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/receive-forward-store/route-actions.md

# Route Actions

If a route expression is evaluated to *true,* Mailgun executes the corresponding action. Currently you can use the following three actions in your routes: forward(), store() and stop().

### Forward(destination)

Forwards the message to a specified destination, which can be another email address or a URL. A few examples:


```JSON
forward("mailbox@myapp.com")
forward("http://myapp.com/messages")
```

You can combine multiple destinations by separating them with a comma.


```JSON
forward("http://myapp.com/messages, mailbox@myapp.com")
```

Info
When forwarding messages to another email address, you should disable click tracking, and open tracking and unsubscribes, by editing your domain settings in the Control Panel. If these features are enabled, the content of each message is modified by Mailgun before forwarding, which invalidates the DKIM signature. If the message comes from a domain publishing a DMARC policy (like Yahoo! Mail), the message will be rejected as spam by the forwarding destination.

### Store(notification endpoint)

This temporarily stores the message (for up to 3 days) on Mailgun's servers so that you can retrieve it later. This is helpful for large attachments that may cause time-outs, or if you want to retrieve them later to reduce the frequency of hits on your server.

When you specify a URL, Mailgun will notify you when the email arrives along with a URL which you can use to retrieve the message:


```JSON
store(notify="http://mydomain.com/callback")
```

If you don't specify a URL with the notify parameter, the message will still be stored and you can get the message later through the [Messages API](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages). You can see a full list of parameters we will post/return to you below.

### Stop()

Without a stop() action executed, all lower priority Routes will also be evaluated. This simply stops the priority waterfall so the subsequent routes won't be evaluated.