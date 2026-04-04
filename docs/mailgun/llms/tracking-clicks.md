# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/tracking-clicks.md

# Tracking Clicks

Mailgun can track every time a recipient clicks on a link included in your email. When you enable Click tracking, links will be overwritten and point to Mailgun's servers, giving us the ability to track.
These events can be viewed in the Control Panel in the **Logs** tab. You can also see counters of opens aggregated by tags by visiting the **Analytics** tab on the Control Panel. In addition, you can be notified through a webhook, or get the data programmatically through the Events API.

Click tracking can be enabled two ways

- on a per-domain basis: toggled in the **Tracking Settings** which can be found on your domain's settings page
- on a per-message basis using the parameters, `o:tracking`, or `o:tracking-clicks` when sending an email. This will override the domain setting. You can specify that you only want links rewritten in the HTML part of the message with the parameter `o:tracking-clicks` and passing `htmlonly`. See the [API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/messages/post-v3--domain-name--messages) for more details.


You can also disable click tracking for a specific link by including the HTML attribute `disable-tracking=true` in the HTML tag of the link. With this HTML attribute in the link's HTML tag, Mailgun will not rewrite the URL.
**Example** : `<a href="http://mailgun.com" disable-tracking=true\>Mailgun\</a\>`