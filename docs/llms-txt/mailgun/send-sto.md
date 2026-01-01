# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/send-sto.md

# Sending a Message with STO

Mailgun's **Send Time Optimization** (STO) feature uses machine learning to analyze engagement data (opens and clicks) for a recipient to determine when a user is most engaged with their messages. If there is enough engagement data to determine when the user is most engaged, Mailgun will hold onto the message and deliver it during that optimal period. The idea is to deliver the message to the recipient at a time when they are most likely to be engaged with their messages.

### Sending an STO message via API and SMTP

- Send a message via API by passing the parameter: ***o:deliverytime-optimize-period***
- Send an SMTP message using the MIME header: **X-Mailgun-Delivery-Time-Optimize-Period**
  - The value should be a string in the [0-9]+h format. This format defines the window in which Mailgun will run optimization algorithm against the data that has been delivered to the message.
  - Using a minimum value of 24h for best results, and the max value is 72h is highly recommended.
For more information on STO, see the article,  What is Send Time Optimization?.