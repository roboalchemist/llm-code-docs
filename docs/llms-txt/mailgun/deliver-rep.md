# Source: https://documentation.mailgun.com/docs/mailgun/faq/deliver-rep.md

# FAQ: Deliverability / Reputation

### If I'm just starting to send mail, how do I build a good reputation?

The way to think about your email reputation is much like your credit
score. When you haven't sent any email, you don't have a bad
reputation but you don't have a good one, either. Also, no ESP is going
to allow you to send a million emails to their mailboxes, much like no
one is going to give you a credit card with a huge credit limit when you
graduate from college. There needs to be a history of performance for
you to create a reputation. We use algorithms for our new senders that
automatically queues your email and sends them at rates that makes the
ESPs happy, increasing those rates as your sending reputation grows.

Some of the factors that help you build a good reputation faster and
increase deliverability are:

- Limited spam complaints and bounces.
- Including the ability for recipients to unsubscribe.
- Recipients interacting with your emails in a good way: reading,
replying, forwarding and adding your addresses to their contacts.
- Following ESPs' guidelines on sending rates.
- Paying attention to ESPs' feedback to slow or stop sending for a
period of time.
- Having good content (see below for more guidance on content).


Also, consider letting your users to reply to your emails. Having a
meaningful email conversations with your audience will do wonders for
your reputation as a member of email community.

Finally, there are certification and white label services that can help
(although, you still need some history of sending). We have a
partnership with [Return Path](http://www.returnpath.com) and can help
get you signed up for their [Email Certification
Program](http://www.returnpath.com/solution-content/certification/).
They have already audited our infrastructure so we can get you a
discount off of their list pricing.

### Does the content of my email matter for deliverability?

Absolutely. Ideally, you send email that people want. That's over half
the battle. In addition, you should make your content interesting and
relevant to the recipient.

There are a few things to keep in mind about your email content. First,
we suggest setting up a test mailbox at [http://www.mail-tester.com](http://www.mail-tester.com).
Mail-Tester will provide you with a full analysis of your email for
free. Here are some other things to consider:

- Personalize your emails. Make sure to include the recipient's
address in the "To:" field and include his/her name in the
greeting.
- It is best to send multi-part emails using both text and HTML or
text only. Sending HTML only email is not well received by ESPs.
Also, remember that ESPs generally block images by default so HTML
only will not look very good unless users are proactive about
enabling images.
- Test how your html email looks across all email clients and
browsers. [Litmus](http://litmus.com/) and [Return
Path](http://www.returnpath.com) have tools to do this.
- Make your content relevant and targeted to the recipient. There are
even tools like [Movable Ink](http://movableink.com/) that let you
dynamically update your content after it is delivered.
- The higher the text to link and text to image ratios, the better.
Too many links and images trigger spam flags at ESPs.
- Misspellings, spammy words (buy now!, Free!) are big spam flags, as
are ALL CAPS AND EXCLAMATION MARKS!!!!!!!!!!!!!
- The from field in your emails should match the domain you are
sending from. Hotmail is particularly focused on this.
- Make sure you are using unsubscribe links and headers in your
emails. Many ESPs (particularly Hotmail) pay attention to this and
if they are not there, you are likely to get filtered. You can
always use Mailgun's auto unsubscribe handling if you don't want to
deal with this on your end.
- Include your physical mailing address. CAN-SPAM requires an
unsubscribe link and a physical mailing list. It is also a good idea
to provide a link to your privacy policy.
- Gmail pays particularly close attention to Message ID and Received
headers. Message IDs that are formed incorrectly (without brackets
<> and with wrong domain after @) can make Gmail think you are a
spammer. The simplest way to create the right Message ID is to not
set Message ID at all. Then Mailgun will create a perfect Message ID
for you. Also, if you use the HTTP API, Mailgun will deal with all
of this for you.
- Links should include the domain that is sending the email. Also,
popular url shorteners can be a bad idea because they are frequently
used by spammers.
- Long links may cause bounces. Some ESPs will block emails with links
(or any consecutive text) longer than 99 characters.
- A/B test your emails to optimize recipient engagement. Subject lines
are particularly important. You can use Mailgun's tagging and
tracking statistics in order to measure A/B testing and improve your
content.


### Should I use my primary corporate domain name to send email?

You can, but remember that your reputation is tied to your domain name
as well as the IP address. If you are in danger of being classified as a
'bad' sender of email, you will be affecting your domain reputation,
which is very hard to recover from. It may be safer to use a completely
separate domain (not a subdomain of your primary corporate domain) for
sending marketing or even transactional email if you are worried about
issues with domain reputation.

### Why does the amount of email I send matter?

Rate limiting allows ESPs proper time to process and filter spam and
ensure that transactional email doesn't get backed up. Without rate
limiting in place, ESPs would be even more overwhelmed than they already
are. The ESPs all have different sending limits on a per hour, per day
basis. Once you hit thresholds with the rate limits, send too much spam,
or have any number of other issues, the ISP may start returning error
messages. Some ESPs will want you to slow down the sending, stop sending
for a period of time, or change your habits (due to bad engagement, bad
reputation, etc). We automatically adjust your sending rates according
to the feedback from these ESPs to keep you in their good graces.

Generally, these rate limits are on a per IP address basis. [Contact our
Support Team](https://app.mailgun.com/app/support) if you wish to
purchase additional dedicated IP addresses for your account.

### Does the amount of email I send from my IP affect my deliverability?

Yes. Generally speaking, you don't want too few IPs, in case you
experience more volume than you expect and you don't want so many IPs
that you look suspicious or spread out your volume over too many IPs.
There has to be a balance of volume to IP/domain. Sending too much
volume from an IP, sending from too many IPs or sending too little from
a range of IPs can all lead to deliverability issues.

### Where can I learn more about Deliverability and Email?

One of the best resources is the blog [Word to the
Wise](http://blog.wordtothewise.com/). Also, [Return
Path](http://www.returnpath.com) is a service that enhances
deliverability and they publish a lot of great information through their
blog and white papers. Below is are some best practices from the major
ESPs.

- [Y Sender Hub/AOL Best Practices](https://postmaster.aol.com/best-practices)
- [Gmail Best
Practices](https://support.google.com/mail/answer/81126?hl=en)
- [Outlook Best Practices](http://mail.live.com/mail/policies.aspx)
- [Yahoo Best
Practices](https://help.yahoo.com/kb/postmaster/practices-senders-sln3435.html)