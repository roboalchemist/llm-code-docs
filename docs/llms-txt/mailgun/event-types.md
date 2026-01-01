# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/events/event-types.md

# Event Types

Mailgun tracks all of the events that occur throughout the system. Below are listed the events that you can retrieve using this API.

| Event Type | Description |
|  --- | --- |
| accepted | Mailgun accepted the request to send/forward the email and the message has been placed in queue. |
| rejected | Mailgun rejected the request to send/forward the email. |
| delivered | Mailgun sent the email and it was accepted by the recipient email server. |
| failed | Mailgun could not deliver the email to the recipient email server. severity=permanent when a message is not delivered. There are several reasons why Mailgun stops attempting to deliver messages and drops them including: hard bounces, messages that reached their retry limit, previously unsubscribed/bounced/complained addresses, or addresses rejected by an ESP. severity=temporary when a message is temporary rejected by an ESP. |
| opened | The email recipient opened the email and enabled image viewing. Open tracking must be enabled in the Mailgun control panel, and the CNAME record must be pointing to mailgun.org. |
| clicked | The email recipient clicked on a link in the email. Click tracking must be enabled in the Mailgun control panel, and the CNAME record must be pointing to mailgun.org. |
| unsubscribed | The email recipient clicked on the unsubscribe link. Unsubscribe tracking must be enabled in the Mailgun control panel. |
| complained | The email recipient clicked on the spam complaint button within their email client. Feedback loops enable the notification to be received by Mailgun. |
| stored | Mailgun has stored an incoming message |