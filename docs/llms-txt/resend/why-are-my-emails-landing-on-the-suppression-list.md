# Source: https://resend.com/docs/knowledge-base/why-are-my-emails-landing-on-the-suppression-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Why are my emails landing on the Suppression List?

> Learn why your emails land on the Suppression List and how to remove them.

When sending to an email address results in a hard bounce, Resend places this address on the Suppression List. Emails placed on the list cannot be sent to until they are removed.

<Info>
  We place emails on the Suppression List to protect domain reputation, both
  yours and ours. Sending an email to a known hard bounce recipient can damage
  domain reputation and affect email deliverability.
</Info>

## Reasons emails are placed on the Suppression List

Here are some possible reasons an email address is placed on the Suppression List:

* The recipient's email address **contains a typo**.
* The recipient's email address **doesn't exist**.
* The recipient's email server has **permanently blocked delivery**.
* The recipient has marked the delivery as spam.

## View email bounce details

You can view the reason an email bounced on the [Emails](https://resend.com/emails) page:

1. Open the [Emails](https://resend.com/emails) page and search for the recipient's email address in question.
2. Click on the email to view its details.
3. Hover over the `Bounced` status indicator to see a summary of the bounce reason.

<img alt="Email Bounce Notification" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-bounce-details-1.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=f0f99293137b8de4a9862b05cfd87d74" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/email-bounce-details-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-bounce-details-1.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=0fd440475bc204251169761afee247d4 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-bounce-details-1.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5d0c2fa42b7e8173818e5ed4f27dabc0 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-bounce-details-1.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=a7777878ad51806c9c2368069a663cf7 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-bounce-details-1.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=ed292d9d5aef5c9ef159b7d026e89d77 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-bounce-details-1.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=85dec0cbae94dae7a300487c6748af36 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-bounce-details-1.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=060e633e0c298de6faaddae8c77d927f 2500w" />

For more technical details and suggested next steps, click the **See details** button. The drawer will open on the right side of your screen with the bounce type, subtype, and suggestions on how to proceed.

## What happens if you try sending to a recipient on the suppression list?

Whenever you send an email with Resend, we check if the recipient is on the suppression list. If they are, we'll [suppress](/dashboard/emails/email-suppressions.mdx) the delivery to prevent damaging your sender reputation and our infrastructure.

## Removing an email address from the Suppression List

You may be able to send a message to the same recipient in the future if the issue that caused the message to bounce is resolved and the email address is removed from the Suppression List.

<Warning>
  Remember, if you do not address the issue that caused the email to bounce, the
  email address will return to the Suppression List the next time you attempt to
  send to it.
</Warning>

To remove your recipient from the Suppression List, click on the email in the [emails dashboard](https://resend.com/emails), and click **Remove from suppression list**.

<img alt="Email Bounced button" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-suppression-list-2.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=baf9f0a40313b856be978b728fb1d01c" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/email-suppression-list-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-suppression-list-2.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=5cd771fb178129ea877cb7a8c4ae7232 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-suppression-list-2.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1afcefe9521079a01a864660d4cadb3f 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-suppression-list-2.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=754178c89bd180234e114b26931ad834 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-suppression-list-2.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=ba26e1577b0f049e9d52b087004ed564 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-suppression-list-2.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=0e3a00dfb4ff6af14ab63702bb457fba 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/email-suppression-list-2.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e08834d9cda300da7cb0473c4d100b10 2500w" />
