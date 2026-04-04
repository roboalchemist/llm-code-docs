# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/tracking-opens.md

# Tracking Opens

Mailgun uses tracking pixels and URL redirects to track every time a recipient opens a message. These events can be viewed in the Control Panel in the **Logs** tab. You can also see counters of opens aggregated by tags by visiting the **Analytics** tab on the Control Panel. In addition, you can be notified through a webhook, or get the data programmatically through the Events API.

Open tracking can be enabled two ways

- on a per-domain basis: toggled in the **Tracking Settings** which can be found on your domain's settings page
- on a per-message basis using the parameters, `o:tracking`, or `o:tracking-opens` when sending an email. This will override the domain setting. See the [API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages) for more details


By default, the open tracking pixel is added at the bottom of your email to mitigate possible impacts to email design. If you send long emails that experience truncation or other rendering issues at the recipient, you can ensure opens are being tracked accurately with placement of the tracking pixel at the top of your emails. This can be done on a domain level or a per-message level.

- on a per-domain basis: `Place open tracking pixel at top of message` can be toggled in the **Tracking Settings** which can be found on your domain's settings page (Same as where you enable open tracking)
- on a per-message basis using the parameters, `o:X-Mailgun-Track-Pixel-Location-Top`when sending an email. This will override the domain setting. See the [API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages) for more details


Info
Text only emails will not track opens. Opens are tracked by including a transparent `.png` file which will only work if there is an HTML component added to the email. It's also worth mentioning that many email service providers disable images by default, meaning this data will only show up if the recipient clicks on the display images button in the recipient's email.

As mentioned earlier on in this article, you will have to add the appropriate CNAME records to your DNS as specified in the **Domain Verification & DNS section** in order for this feature to work properly.

# Open Webhook

You can specify webhook URLs programmatically using the Webhooks API. When a user opens an email that you have sent, your **opened** URLs will be called with the following webhooks payload.