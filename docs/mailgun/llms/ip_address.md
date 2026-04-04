# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/ip_address.md

# IP Addresses and Sending Volume

Mailgun offers both shared and dedicated IPs. We are constantly monitoring the traffic on these IPs, so even for shared IPs, you can feel comfortable knowing that your reputation is not being unduly influenced by others. We also offer pools of IPs for high volume senders. In addition, we have queuing algorithms that gradually warm up your IPs. Our sending rates automatically increase over time as your IP warms up. Finally, we separate our sending queues for each domain you set up at Mailgun, which mitigates the need for multiple IPs for different types of traffic.

If you are sending a lot of email (greater than 50K per week), it is best to isolate your reputation by having a dedicated IP address. When you use a shared IP, you are sharing your reputation with those other senders. In addition, MBPs (Mailbox Providers) rate limit your emails based on the IP. So if you are a high volume sender, you should consider getting a pool of IPs. However, your reputation can also be hurt if you are not sending enough volume consistently from an IP so it's a tricky balance.

If your email sending is volatile with large spikes of volume, MBPs may assume those large spikes are spam. Also, if you overall volume is too low, they won't acknowledge your reputation. Generally, if you are sending less than 5,000 emails per day, a shared IP may be the right solution.

The other thing to consider is using separate IPs for your bulk and transactional mail if you are sending high volumes of email. There are a couple reasons for this:

- Delivery of time-sensitive transactional emails may get queued
behind a large batch of bulk/marketing emails.
- Your transactional mail will be affected by the reputation created
by your bulk/marketing mail.


Even if you have a clean IP address, you need to warm up the IP gradually. This means sending emails at a low rate initially and then gradually increasing that rate, taking into account MBP feedback. If you send a ton of emails right away, they will get filtered or dropped by the MBPs. In some cases, they won't even tell you they are dropping them.