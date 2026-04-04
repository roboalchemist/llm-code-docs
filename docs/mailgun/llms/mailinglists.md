# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/mailinglists.md

# Mailing Lists

The number one reason we see people getting blocked is due to them having a bad mailing list. You should only send emails to people that have opted in to receiving
your emails on YOUR website. In addition, you should be sending a verification email with a link that confirms their subscription (double opt-in) to make sure their email address is correct and that they are the person that signed up.

You should have your Privacy Policy easily accessible on your website. In addition, you should have a place on your website where users can unsubscribe from your mailings, in addition to a link in every email you send.

While you are responsible for procuring your mailing list, Mailgun does track and give you data to easily see how your emails are being received. We also give you information for bounces, unsubscribes, complaints, opens and clicks so that you can modify your mailing lists appropriately. In addition, we automate a lot of the work by keeping track of recipients that have unsubscribed, bounced or complained and stopping future deliveries to those recipients. We give
you various levels of unsubscribe granularity so your recipients can unsubscribe to all emails from the domain, just that mailing list or just emails with that "tag" (which you define).

Tip:
**Do not purchase your list or scrape websites for
emails.** It's the easy way out, but you will pay the consequences. Most of these lists have bad email addresses and include spam traps. MBPs (Mailbox Providers) are
very good at recognizing bad mailing lists.