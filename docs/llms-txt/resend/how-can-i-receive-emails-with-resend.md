# Source: https://resend.com/docs/knowledge-base/how-can-i-receive-emails-with-resend.md

# Can I receive emails with Resend?

> Receiving emails is in early access.

We're currently working on inbound email, [sign-up to join our early access waitlist](https://resend.com/inbound). The key components of this feature will include:

* Receive emails using webhooks. Get notified when emails are received.
* Parse content and attachments. Extract and process email data automatically.
* Reply to your users. Respond directly to incoming messages.

While this feature is in early access, you can still [set a Reply To Address](api-reference/emails/send-email) (`reply_to`) on your outbound emails to direct any responses to a different location like an existing inbox, slack channel, etc.

Here are a few current workarounds that could help:

* **Sending to existing inbox**: You could set the `reply_to` as your personal email address. If any recipient replies to your email, it will be sent to the `reply_to` address. This could be a different address on the same domain, or a different domain entirely.
* **Sending to Slack**: You could set the `reply_to` as a [channel email address in Slack](https://slack.com/help/articles/206819278-Send-emails-to-Slack). This will create a new message in slack with the contents of the reply.
