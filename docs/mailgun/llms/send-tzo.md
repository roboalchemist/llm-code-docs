# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/send-tzo.md

## Sending a Message with TZO

Time Zone Optimization (TZO) allows senders to schedule messages to be delivered in a recipient's local time zone. TZO is like message scheduling, however, the focus is on passing the message on to the desired delivery time based on the recipient's local time zone.

Mailgun will convert the message to use the recipient's local time zone, when there is data present for the recipient. If Mailgun does not have data for that recipient, the message will be delivered immediately.

- Time zones are based on a recipient's IP address
  - Mailgun collects IP addresses on click events and uses a geo-location service to translate the IP address into a time zone for the user.
  - The time zone is hashed and stored in a database, which Mailgun will look up for that user when a TZO message is sent.


### Sending TZO message via API and SMTP

- Send a message via API by passing the parameter: **o:time-zone-localize**
- Send a message via SMTP using a MIME header: **X-Mailgun-Time-Zone-Localize**
  - The value (String) should be set to the preferred delivery time in HH:mm or hh:mmaa format, where HH:mm is used for 24 hours format without AM/PM and hh:mmaa is used for 12-hour format with AM/PM.