# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/tracking-failures.md

# Tracking Failures

Mailgun tracks all delivery failures, which consists of both hard bounces (permanent failures), and soft bounces (temporary failures).

When an email message is said to "bounce", this means that it was rejected by the recipient SMTP server. Bounced addresses are found on the "Bounces" table, which is found on the **Suppressions** tab on the Control Panel. With respect to failure persistence, Mailgun classifies bounces into two categories:

- **Hard bounces** (permanent failure): This based on these criteria:
  - The recipient is not found
  - The recipient email server specifies that the recipient does not exist
- **Soft bounces** (temporary failure):
  - Email is not delivered because the mailbox is full or for other reasons.


**Permanent and Temporary Failure Webhooks**
There may be a few reasons why Mailgun needs to stop trying to deliver messages. The most common reason being that Mailgun has received a hard bounce or repeatedly received soft bounces. Continually attempting to deliver the message may affect the sender's reputation with the receiving ESP. When the address is on one of the 'Do Not Send" lists because the recipient has previously bounced, unsubscribed, or reported spam, Mailgun will drop the message and stop trying to send it. If one of these events occurs, Mailgun will POST the following webhooks payload to your permanent_fail URLs. You can specify webhook URLs programmatically using the Webhook API.

With respect to when the recipient SMTP server has rejected incoming messages, Mailgun will classify bounces into the following categories:

- **Immediate bounce** :
  - An email message is rejected by the recipient SMTP server during the SMTP session.
- **Delayed** (asynchronous) **bounce:**
  - The recipient SMTP server accepts an email message during the SMTP session. After some time, it will send a Non-Delivery Report email message to the message sender.


Note:
In case of a bounce, Mailgun will retry to deliver the message only if the bounce was both immediate and soft. After several unsuccessful attempts, Mailgun will quit trying to preserve your sending reputation.

Warning!
 Mailgun can track delayed bounces, but only if the domain that the email message was sent from has MX records pointing to Mailgun; Otherwise, NDR email messages will not reach Mailgun. Please refer to Verifying Your Domain for details on how to do that.e