# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/tracking-deliveries.md

# Tracking Deliveries

Mailgun tracks all successful deliveries that occur when the recipient email server responds that it has accepted the message.

You can see when a message has been successfully sent by clicking on the Logs tab found on the Control Panel. You can also be notified when a message has been delivered through a webhook or get the data programmatically through the Events API.

Do note that, for messages that get routed to an HTTP endpoint, we *do not* send a Delivered webhook to your configured URL(s). We *do* emit the delivered event for the message itself so that the Routed delivery shows up in the Events API.