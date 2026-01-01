# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/message-queue.md

# Message Queue

The queuing algorithms are one of the most important features of Mailgun. If you try sending bulk mailings all at once, most ISPs will block you. Mailgun will put your messages in a message queue when you submit them for delivery.

- A large number of messages can be submitted.
  - Mailgun will automatically queue for the delivery in compliance with the receiving domains' guidelines and maximum sending rate optimized for each ESP (email service provider), such as Yahoo, Gmail, etc.
- The messaging queue is dynamic.
  - Your messages may take longer at first, however, your sending rates will increase the more you send messages.
  - As your reputation grows, your sending rate will grow too.


Note:
Note: It is important to make sure you are sending quality traffic to ensure sending rates.

It is important to gradually increase your sending rates according to many factors, including:

- Consistency of traffic
- IP address sending history
- Domain reputation.