# Source: https://documentation.onesignal.com/docs/en/unsubscribe-links-email-subscriptions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email unsubscribe links & headers

> Learn how to manage email unsubscribe behavior in OneSignal, including unsubscribe links, List-Unsubscribe headers, suppression rules, and resubscription workflows.

Managing how users unsubscribe from your emails is critical to complying with email standards (like CAN-SPAM), ensuring strong deliverability with providers like Gmail and Yahoo, and building trust with your audience.

OneSignal supports both visible unsubscribe links and List-Unsubscribe headers, ensuring your emails are fully compliant while giving you control over when and how users can opt out.

## Subscription states and suppression logic

Email [Subscriptions](./subscriptions) are either:

* **Subscribed** – eligible to receive email messages.
* **Unsubscribed** – excluded from most email sends unless explicitly overridden.

To include unsubscribed Subscriptions in your email (e.g., for transactional messages):

* In the dashboard: Enable **Advanced Settings > Include sending to unsubscribed users** when sending an email.
* In the API: Use the `include_unsubscribed` property in the [create email notification API](/reference/email).

<Frame caption="Enable sending to unsubscribed users">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/72d0ed1-f246c05-Screenshot_2023-01-18_at_10.06.54_AM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=5bddf440aae0717dc518b8a43789d3da" width="906" height="616" data-path="images/docs/72d0ed1-f246c05-Screenshot_2023-01-18_at_10.06.54_AM.png" />
</Frame>

***

## How users get unsubscribed

Email subscription status is updated via:

* The user clicking an unsubscribe link or List-Unsubscribe header
* You [importing a CSV of email addresses](./import) and setting `subscribed` to `no`.
* You setting `enabled : false` via the [Create user](/reference/create-user), [Update user](/reference/update-user), or [Update subscription](/reference/update-subscription) APIs.
* You manually unsubscribing from **Audience > Subscriptions > Options > Unsubscribe from Email**

***

## Unsubscribe header vs unsubscribe link

* **List-Unsubscribe header**: A hidden email header used by inbox providers to display native “Unsubscribe” buttons (e.g., Gmail, Yahoo).
* **Unsubscribe link**: A visible clickable URL placed in your email content using the `[unsubscribe_url]` token.

### List-Unsubscribe header behavior

OneSignal includes a `List-Unsubscribe` header in all emails **except when you enable “Include sending to unsubscribed users.”** This helps:

* Prevent your emails from being marked as spam
* Comply with [Gmail/Yahoo 2024 rules](https://onesignal.com/blog/guide-to-2024-gmail-and-yahoo-requirements-for-email-senders/).

<Warning>
  The List-Unsubscribe header is **not included** if you enable "Include sending to unsubscribed users."

  Some inbox providers may hide this header from display unless you meet certain sending volume thresholds. See [Gmail's](https://support.google.com/a/answer/81126?visit_id=638683263663552218-2680312485\&rd=1#requirements-5k\&zippy=%2Crequirements-for-sending-or-more-messages-per-day) and [Yahoo's](https://senders.yahooinc.com/best-practices/) requirements.
</Warning>

If a user clicks this, their email Subscription will be marked as unsubscribed in your OneSignal app.

### Adding unsubscribe links in emails

OneSignal provides the `[unsubscribe_url]` token, which inserts a visible unsubscribe link into your email content.

You can also create a branded experience with your own unsubscribe page. See [Create a custom unsubscribe page](./create-custom-unsubscribe-page).

#### HTML editor

If using our HTML editor, the default template includes an unsubscribe link automatically:

<Frame caption="HTML editor with default unsubscribe link">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8b10e10-default_code.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=0c996973cd6335a81dd8854c8e0e355d" width="1309" height="562" data-path="images/docs/8b10e10-default_code.png" />
</Frame>

To add it manually (e.g. via API with `email_body`):

```html HTML theme={null}
<a href="[unsubscribe_url]">Unsubscribe</a>
```

#### Drag & drop editor

In a text block:

1. Click **Special Links > Suppression > Unsubscribe**
2. The `[unsubscribe_url]` placeholder is inserted
3. You can highlight text before inserting to turn it into a link

<Frame caption="Unsubscribe link in Drag & Drop editor">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7f78d2e-Screenshot_2023-01-18_at_9.59.12_AM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=46180061304abd272dbcef4c85b3b710" width="1114" height="230" data-path="images/docs/7f78d2e-Screenshot_2023-01-18_at_9.59.12_AM.png" />
</Frame>

<Info> Always make unsubscribe links **highly visible** with readable font sizes (at least 12px) and strong contrast. Hidden or hard-to-find links can lead users to mark your messages as spam, harming future deliverability. </Info>

***

## Custom unsubscribe link destinations

You may replace `[unsubscribe_url]` with your own unsubscribe landing page.

To do this:

* Follow the steps in [Create a Custom Unsubscribe Page](./create-custom-unsubscribe-page).
* Replace `[unsubscribe_url]` in your email with the URL of your custom unsubscribe page.

<Warning>
  If using a custom link, OneSignal will not automatically mark the user as unsubscribed. You must handle that through the API or page behavior.
</Warning>

***

## FAQ

### Why isn’t the unsubscribe link working in my test email?

If your OneSignal email sending domain is not yet verified, unsubscribe links in test emails won’t be functional. You’ll see placeholder text, but no real link.

Once your domain is verified, unsubscribe links will render and function properly.

### How do I resubscribe an email address?

Users can be resubscribed in three ways:

1. Dashboard: Go to **Audience > Subscriptions > Options > Resubscribe to Email**
2. API: Set `enabled: true` in the [Create User](/reference/create-user) or [Update subscription](/reference/update-subscription) APIs
3. CSV Import: Set `subscribed = yes` when importing email addresses

<Warning> If you use a third-party email provider (ESP), check their suppression list and remove the address there too. </Warning>

### Why are there two unsubscribe links in my email?

If you're using ESPs like Mailgun or SendGrid, they may insert their own unsubscribe link. You can disable this in your ESP's settings to avoid duplication.

### Do unsubscribe clicks count toward analytics?

* Clicking the OneSignal custom `[unsubscribe_url]` does not count towards click analytics.
* Clicking a custom unsubscribe URL will be counted as a click. See [URLs, Links, and Deep Links](./links) for more details.

***

## Related articles

* [Create a Custom Unsubscribe Page](./create-custom-unsubscribe-page)
* [Email Messaging](./email-messaging)
* [Email API](/reference/email)
* [URLs, Links, and Deep Links](./links)

***

Built with [Mintlify](https://mintlify.com).
