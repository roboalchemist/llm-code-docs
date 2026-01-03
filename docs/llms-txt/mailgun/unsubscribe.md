# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/unsubscribe.md

# Unsubscribe Handling

It is important to give your recipients the ability to unsubscribe from emails. First, it is required by the [CAN-Spam Act](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business). Second, if you don't give them this option, they are more likely to click on the spam complaint button, which will cause more harm than allowing them to unsubscribe. Finally, many MBPs (Mailbox Providers) look for unsubscribe links and are more likely to filter your email if they don't have them.

Mailgun gives you the ability to include an unsubscribe link or email
automatically in your email. We give you the ability to link the
unsubscribe to a certain campaign, mailing list or make the request
global to your domain. You can access this data through the Control
Panel, API or via Webhooks. In addition, we will automatically stop
sending to email addresses that have unsubscribed. It is possible to
remove addresses from the flagged list in your Control Panel or through
the API.