# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/schedule-delivery.md

# Scheduling Delivery

Mailgun allows you to request a specific time for delivering messages.

Use `o:deliverytime` parameter if sending via the API.
Use the MIME header `X-Mailgun-Deliver-By` when sending via SMTP.

Info
If your billing plan supports 7 or more days of storage capability, you can now schedule emails out up to 7 days.