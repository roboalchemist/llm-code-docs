# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/email_content.md

# Email Content

There are a few tricks to remember about content besides the mantra of
'sending something people want'. As mentioned above, you can set up a
test mailbox at Mailgun and enable our spam filters to receive a
"spamicity" score to test how your content is being judged by spam
filters.

- Personalize your emails to each recipient. Ideally, the content
should reflect recipient's specific interests or usage patterns in
your application. At least address them by their name. Mailgun has recipient variables that you can define and use
with your email templates to achieve detailed levels of
personalization.
- It is best to send multi-part emails using both text and HTML or text only. Sending HTML only email is not well received by MBPs (Mailbox Providers). Also, remember that some MBPs block images by default so HTML only will not look very good unless users are proactive about enabling images. We recommend [Mailgun Optimize email previews](https://app.mailgun.com/app/email-preview) and [Email on Acid](https://www.emailonacid.com/) for testing how your emails render across MBPs, browsers, and email clients.
- The higher the text to link and text to image ratios, the better.
Too many links and images trigger spam flags at MBPs.
- Misspellings, spammy words (buy now!, Free!) are big spam flags, as
are ALL CAPS AND EXCLAMATION MARKS!!!!!!!!!!!!!
- The domains in the from field, return-path and message-id should
match the domain you are sending from.
- Make sure you are using unsubscribe links and headers in your
emails. Many MBPs (particularly Hotmail) pay attention to this and
if they are not there, you are likely to get filtered. You can
always use Mailgun's auto unsubscribe handling if you don't want
to deal with this on your end.
- Gmail pays particularly close attention to Message ID and Received
headers. Message IDs that are formed incorrectly (without brackets
<> and with wrong domain after @) can make Gmail think you are a
spammer. The simplest way to create the right Message ID with
Mailgun is to not include one. Then Mailgun will create a perfect
Message ID for you.
- Links should include the domain that is sending the email. Also,
popular url shorteners can be a bad idea because they are frequently
used by spammers.
- A/B test your emails to optimize recipient engagement. Subject lines
are particularly important. You can use Mailgun's tagging and
tracking statistics in order to measure A/B testing and improve your
content.