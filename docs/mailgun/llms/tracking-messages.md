# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/tracking-messages.md

# Introduction to Email Events

Mailgun provides comprehensive email tracking tools that offer insights through **Events**, **Stats**, and **Tagging** in order to help you optimize your email strategy by providing detailed insights into the performance and engagement of your emails.
You can monitor various aspects of your emails, including:

- Tagging: Categorize and filter your emails for better management.
- Tracking Open Messages: See when recipients open your emails.
- Tracking Clicks: Monitor links clicked within your emails.
- Tracking Unsubscribes: Track when recipients opt-out from your mailing list.
- Tracking Spam Complaints: Identify when your emails are marked as spam.
- Tracking Failures: Understand when and why email deliveries fail.
- Tracking Deliveries: Confirm successful delivery of your emails.


Mailgun provides a variety of methods to access this data:

- To see every event that happened to every message, view and search Events through the **Logs** tab in the Control Panel. You can search by fields, like recipient, subject line, and even fields that don't use up in the Logs, such as message-id. Data is stored for at least 30 days for paid accounts, and at least 2 days for free accounts.
- Access data on Events programmability through the Events API. Data is stored for at least 30 days for paid accounts and at least 2 days for free accounts.
- View, search, and edit tables for Bounces, Unsubscribes, and Spam Complaints in the **Suppressions** table of the Control Panel of their retrospective APIs (Bounces API, Unsubscribes API, Complaints API). Data is stored indefinitely.
- Access statistics aggregated by tags in the **Analytics** tab of the Control Panel or the Stats API. Data is stored for at least six months.
- Receive notifications of events through he Webhook each time an Event happens and store the data on your side.


In addition to tracking messages, Mailgun permanently stores them when they cannot be delivered due to a hard bounce (permanent failure), or when a recipient unsubscribes or marks the message as spam. In these cases, Mailgun will not attempt to deliver messages to those recipients in the future. This is to protect your sending reputation.

### Enable Tracking

Event tracking is automatically enabled, with the exception for **Unsubscribes** , **Opens** , and **Clicks**. You can enable these for your domain's via the **Domains** tab of the **Control Panel**.

Opens and Clicks tracking can be enabled on two levels â per sending domain (as mentioned above) and per message. Please see [Open Tracking](#tracking-open-messages) and [Click Tracking](#tracking-clicks) for more details

There are two critical components to get tracking working properly

- You will need to point CNAME records to mailgun.org for Mailgun to rewrite links and track opens. These records can be found in your domains DNS records `Tracking records` section.
- There needs to be an HTML part of the message for Mailgun to track opens. (See Tracking Opens and Tracking Clicks for more details.)


#### Tracking Protocol (HTTP vs HTTPS)

By default, all tracking is performed over HTTP. If you want secure links to be used, you can set the `tracking protocol` to HTTPS via our control panel under your domains settings.
When set to HTTPS Mailgun will generate a Let's Encrypt TLS certificate for your tracking domain and use the HTTPS protocol for all tracking links.