# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-receipt-and-deduplication.md

# Email Receipt & Deduplication

As part of day-to-day processing in Email systems and integration with other systems, it is possible for errors to result in duplicate emails. To combat this Enate provides built-in capabilities to deduplicate received emails. Let’s take a look at the details for this.

### Enate Email Deduplication Logic

As a core principle, Enate will generate or update 1 work item per recipient per received Email after deduplication. A recipient is either an existing work item or an address defined by an email route.

To guard against accidental creation of multiple work items caused by duplicate incoming emails, Enate checks for such duplicates and deduplicates them so that only one work item is created.

### Further Details – What is considered a duplicate?

Enate looks for duplicates in 3 ways:

* The first method considers the entire content of the email, including not just the user-visible content such as Subject, Body, Senders, Recipient, Attachments, etc but also the underlying email information such as the email headers.
  * (Use case: We have requested IMAP server to delete email, but the server implements delayed delete. Next time we check for emails we receive the email that we asked it to delete again.)
* The second method considers a subset of the user visible content, but does not consider most of the underlying email headers.
  * (Use case: The same email was sent to a mailbox and one of its aliases, OR addressed to multiple work items on the same connector)
* The third method only considers a subset of user visible content - excluding the body of the email - and the hidden unique identifier of the message, if available.
  * (Use case: The same email was sent to a mailbox and one of its aliases, OR addressed to multiple work items on the same connecto.r)

If any of the above methods determines that the email is a duplicate, then the email is considered to be a duplicate.

## Multiple Received Emails for the same Sent Email

In a scenario where a sender includes multiple addresses in the recipient list (To and CC) which are picked up by Enate, the system would normally receive 2 (or more) copies of the email, and the Email routing **outside** of Enate would determine whether it is caught as a duplicate or not. However, the duplication taking place in the Email Server infrastructure cannot be guaranteed.

Whether multiple emails are created or not in this scenario is outside the control of Enate and should be investigated with your Email Server provider or Email administration team. In our experience factors which may affect this include (but are not limited to):

* If the email is sent by internal or external senders
* If the recipients are real mailboxes or aliases
* If transport rules are used (Exchange/Office 365)
* If 3rd party antispam/antivirus products are involved in email delivery.

{% hint style="warning" %}
**Due to the variability in behavior of external systems with regards to multiple emails and duplicates, we strongly advise business processes and email scenarios are tested thoroughly to ensure the desired behavior in Enate is achieved.**
{% endhint %}

### Enate Routing

A work item will be created following the applicable configured routing within that mailbox - these may obviously be different, resulting in the created Work Items potentially being in different contexts (and Ticket Categories for Tickets).

### BCC Emails

Enate has some support for Emails received via BCC through the use of special Wildcard routes. As the enate mailbox is not listed in the recipient list for the email normal routes cannot work, however you are able to create a route where any recipient is allowed and the sender (from) can be used for routing purposes. See this article on [Wildcard Routes for incoming BCC Emails](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic/wildcard-routes-for-incoming-bcc-emails) for more information on this.

## Example showing these various impacts

Imagine an email sent to <mark style="color:blue;"><joe@enate.net></mark>, <mark style="color:blue;"><tom@enate.net></mark> and <mark style="color:blue;"><joe@enate.io></mark> and BCCd to <mark style="color:blue;"><kevin@enate.net></mark>. Here <mark style="color:blue;"><joe@enate.io></mark> is an alias for <mark style="color:blue;"><joe@enate.net></mark>.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBjq6xmewpCoEf0w4SMFf%2FDedupe1.PNG?alt=media\&token=875866cb-f5d7-4cbc-a8f0-cf1813518681)

### **Likely Email Behaviour: Internal vs External Email**

If the email is sent by a colleague (an internal email) then it is likely, depending on Email Infrastructure, that Joe would receive 1 email, Tom would receive 1 email and Kevin would receive 1 email.

If the email is sent by an external contact (an external email) then it is likely, depending on Email Infrastructure, that Joe would receive 2 emails, Tom would receive 1 email and Kevin would receive 1 email. Joe would see 2 identical emails in his Inbox with no discernible differences; only when viewing the Email headers would differences be identified and even then it is unlikely either email could be attributed to <mark style="color:blue;"><joe@enate.net></mark> vs <mark style="color:blue;"><joe@enate.io></mark>.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fm3rdM46cljTqfIAOTcJF%2FDedupe2.PNG?alt=media\&token=7a731ca1-68cf-49d1-971e-dcec324d0233)

In both examples Kevin would receive the email but wouldn’t really know why – he would not be able to identify himself as a recipient in the To or CC fields and the BCC field is not shown.

### **Behaviour in Enate**

The impact of these 2 examples if received by Enate is that for the first example (sent from *internal*):

* 1 email would be received in the mailbox <mark style="color:blue;"><joe@enate.net>.</mark>
  * 1 email would follow the configured routing rules for <joe@enate.net> and <jo@enate.io> resulting in 2 work items.
* 1 email would be received in the mailbox <mark style="color:blue;"><tom@enate.net></mark> which would follow the configured routing rules resulting in 1 Work Item.
* 1 email would be received in the mailbox <mark style="color:blue;"><kevin@enate.net></mark> but routing rules on this Email Connector wouldn’t match any of the To or CC addresses, so it will be made available in unprocessed view ***unless*** a route had been added to create a work item based on the from address.

In the second example (sent from *external*):

* 2 emails would be received in the mailbox <mark style="color:blue;"><joe@enate.net>.</mark>
  * 1 email would follow the configured routing rules for <mark style="color:blue;"><joe@enate.net></mark> and <mark style="color:blue;"><joe@enate.io></mark> resulting in 2 work items.
  * 1 email would be received in the mailbox  <mark style="color:blue;"><joe@enate.io></mark> which would be treated as a duplicate.
* 1 email would be received in the mailbox <mark style="color:blue;"><tom@enate.net></mark>. Same as for Internal, behaviour would be as above would result in 1 work item.
* 1 email would be received in the mailbox <mark style="color:blue;"><kevin@enate.net>,</mark> but routing rules on this Email Connector wouldn’t match any of the To or CC addresses, so it will be made available in unprocessed view ***unless*** a route had been added to create a work item based on the from address.

Notice how in either case the end result is the same

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeRpRN67J3ql05U7olvIk%2Fimage.png?alt=media&#x26;token=8a2dcac7-2647-42f7-a685-cc3a6da541cf" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCNCGmHVwfa10FO5BCHAM%2Fimage.png?alt=media&#x26;token=91ed5a14-7933-45f8-95da-c3327fc72cc4" alt=""><figcaption></figcaption></figure>
