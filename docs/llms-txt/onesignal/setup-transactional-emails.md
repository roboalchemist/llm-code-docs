# Source: https://documentation.onesignal.com/docs/en/setup-transactional-emails.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transactional emails

> Send transactional emails to users with OneSignal.

A great path to start using OneSignal Email Messaging is to begin delivering transactional emails like:

* Welcome emails,
* Purchase confirmations,
* Password resets, or
* any other service-related message.

By sending transactional messages on OneSignal. You can easily **track delivery, click, and open statistics** on your transactional emails from the OneSignal Dashboard, alongside your push notifications and marketing emails.

Keep all of your communications in one place. If you are just starting to send emails, setting up transactional messages in OneSignal means:

* you'll have fewer email products to manage,
* you can see all communications to your users in one place, and
* you can create visual automation with Journeys that can include marketing and transactional messaging.

# Transactional vs marketing

Transactional emails typically are emails as a result of an action that a user has taken. It is not necessary for transactional emails to contain an `unsubscribe link` because the message itself is considered necessary to the delivery of your organization's services.

Marketing messages are all other messages that are not required as part of the delivery of your services. You should make sure you have consent to send marketing messages and include an unsubscribe link in every email. Read more about [Email Regulatory Compliance](./email-compliance).

# Sending transactional emails

Enable sending to unsubscribed users if desired.

### Dashboard or templates

If using the dashboard or [Templates](./templates), toggle open **Advanced Settings** then check **Include sending to unsubscribed users**.

<Frame caption="Example shows a template's Advanced Settings.">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b5b5e821031cf258f0711edebcde18fc4df8632c32816a98c454e7ab00db2408-Screenshot_2024-12-02_at_3.13.48_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=e5bd655b38050ac581d4e66b7f6bf6e0" width="1700" height="662" data-path="images/docs/b5b5e821031cf258f0711edebcde18fc4df8632c32816a98c454e7ab00db2408-Screenshot_2024-12-02_at_3.13.48_PM.png" />
</Frame>

You can also remove the [unsubscribe links](./unsubscribe-links-email-subscriptions) because we will send this to every recipient in the segment regardless of their subscription status.

When sending from the dashboard, you can only target [Segments](./segmentation), so you may want to set [Tags](./add-user-data-tags) to create a list with the [Import](./import) functionality.

<Info>
  If you send via a third-party ESP like Mandrill, Mailgun, or SendGrid, you might need to clear unsubscribed emails from your suppression list to enable sending to those recipients and improve your deliverability.
</Info>

### API

The most common way to send transactional messages is through our [Create message](/reference/email) API.

To send to unsubscribed email subscriptions, set `include_unsubscribed` to `true`.

<CodeGroup>
  ```json json theme={null}
  {
    "app_id": "YOUR_ONESIGNAL_APP_ID",
    "include_email_tokens": ["[email protected]", "[email protected]"],
    "email_subject": "Your Email Subject",
    "template_id": "e59b3a5e-ccc4-44ff-b39e-aa4c668fe6c1",
    "include_unsubscribed": true
  }
  ```
</CodeGroup>

This example uses [Templates](./templates) which can exclude the unsubscribe link as described in [Email unsubscribe links & headers](./unsubscribe-links-email-subscriptions) but you can also remove it from your email HTML in this case.

See [Transactional Messages](./transactional-messages) for more details.

# Migrate your existing transactional emails

You can import your existing email templates using our [Email Template Forwarding](./email-template-forwarding) or [Create template](/reference/create-template) API. Otherwise, you can inject your HTML into the `email_body` on our [Create message](/reference/email) API.

***

Built with [Mintlify](https://mintlify.com).
