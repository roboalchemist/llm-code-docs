# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/reputation.md

# Reputation

Reputation is one of the most important assets you have, even when sending email. If you do not have a good reputation tied to your domain and your IP address, your email will not reach your recipients' inboxes, as it may come across as spam. A good analogy for your email reputation is your personal credit score. Obviously, a bad reputation will hurt you. However, not having a reputation will also hurt you. If MBPs (Mailbox Provider) don't know you (or more specifically your IP and domain) they will assume the worst and filter you, at least initially. It's tough to blame them, given all the spam out there. Due to the importance of reputation, a significant portion of our discussion on best practices revolves around building and maintaining your email reputation.

Because of email's popularity and unique ability to push information to users, it has been overrun with spammers. According to [MAAWG](http://www.maawg.org/sites/maawg/files/news/MAAWG_2010_Q3Q4_Metrics_Report_14.pdf), approximately 90% of all email is spam. Due to this overabundance of spam activity, mailbox providers ("MBPs") like Gmail, AOL, Yahoo and Outlook/Hotmail have declared an all-out war on spammers, making our inboxes a more pleasant place. This emphasizes the importance of managing your email reputation; If it is not impeccable, you will get caught in the MBPs' spam filters.

Our goal with respect to your email reputation is to make sure that the infrastructure is optimized for emails reaching the inbox and doesn't get in your way. We test all of our IPs' reputation before we allocate them and we use the authentication methods that major MBPs require.

Beyond making sure that the infrastructure is properly set up, we also provide the tools to answer some important questions:

- Are emails being delivered and if not, why?
- Is a recipient MBP throttling your traffic and why?
- Are messages bouncing due to incorrect domains or stale addresses?
- Are recipients unsubscribing or complaining of spam?
- Are recipients engaging with your emails by opening them and/or
clicking on links?


You should use all of this data to make sure that you are complying with MBPs guidelines and adjust your email sending to stay in their good graces.

Although We give you all the tools for establishing a good sending reputation, it's ultimately up to you to send emails appropriately.

However, if you follow a couple rules (along with properly authenticating your email), you will most likely build up a great email sending reputation:

- Only send emails to people that have signed-up to receive them from
your website/application/service and always first send a
confirmation link to confirm their address is correct (aka, "double
opt-in")
- Track your email and adjust your sending based on feedback from MBPs
and recipients (eg., don't send additional emails to recipients that
have unsubscribed or complained of spam).