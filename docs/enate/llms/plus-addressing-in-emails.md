# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic/plus-addressing-in-emails.md

# Plus Addressing in Emails

Plus Addressing is an industry-defined feature which allows the automatic addition of information *into* an email address when a mail is being composed. Systems can then subsequently use this additional information if they know to look for it within the email addresses, while still ensuring that the mail gets to its intended recipients.&#x20;

In Enate, we make use of Plus Addressing by automatically adding the reference number of a Case, Action or Ticket (e.g. '101203-T') into the email address of any emails that we know should be being subsequently shared with that work item.

Adding this extra information into the email addresses of mails relating to work items allows us to run an additional layer of processing logic for any response emails which come back *in* as responses from them. The logic is fairly simple: If a work item reference number is recognized as part of any of an email's target mail addresses, that mail is shared with that work item.

{% hint style="info" %}
Another way to think of this is that **with Plus Addressing addressing each work item gets its own email address.**
{% endhint %}

Doing this massively reduces the chances of creating unnecessary work items when sending emails back and forth - particularly useful when there are multiple separate work items being actioned across multiple separate teams in Enate to deal with larger queries.

**Example**

If an Agent is emailing out a reply to a query that has arrived into the mailbox **'*****<info@enate.io>*****'**, upon sending the email back out Enate will auto-populate the From email address with a plus sign (+) followed by the reference number of the work item as a tag, so the From email address coming out of Enate will look something like this: **'*****<info+101203-T@enate.io>'*****.**&#x20;

The underlying structure of this is: **\[email connector address]\[+EnateRef]@\[email domain].**

Similarly, if the person sending the email out from Enate includes other Enate email addresses (e.g. they're copying in other internal departments) where there might also be a linked work item the email could be shared to, the system will allow the sender to share their mail with these other departments - it does this by adding in further work item references to the other departments' email addresses.
