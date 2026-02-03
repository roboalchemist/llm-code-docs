# Source: https://resend.com/docs/dashboard/emails/email-suppressions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Suppressions

> Understanding and resolving delivery issues.

## What does it mean that the email was `suppressed`?

A suppression happens when you try sending an email to a recipient that previously [bounced](/dashboard/emails/email-bounces) or marked your email as spam.

To protect your sender reputation and our sending infrastructure, we proactively stop that delivery from happening.

## What caused the suppression?

The suppression is caused by:

* `Bounced` when the recipient's mail server rejects the email and the response indicates a permanent failure to deliver. There could be [multiple reasons why an email `bounced`](/dashboard/emails/email-bounces#bounce-types-and-subtypes).
* `Complained` when the recipient marked your email as spam.

<Tip>
  Not all Inbox Service Providers return a `complained` event. Most notably,
  Gmail/Google Workspace doesn't.
</Tip>

## Viewing Suppression Details in Resend

You can see the suppressed details by clicking on the email, and hovering over the `Suppressed` label.

<img alt="Email Suppression Notification" src="https://mintcdn.com/resend/03eaUBXyB1UIHhJ_/images/email-suppression-visibility-1.png?fit=max&auto=format&n=03eaUBXyB1UIHhJ_&q=85&s=b7e1336eb062d3fe1aeedde51443db9e" data-og-width="1800" width="1800" data-og-height="1116" height="1116" data-path="images/email-suppression-visibility-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/03eaUBXyB1UIHhJ_/images/email-suppression-visibility-1.png?w=280&fit=max&auto=format&n=03eaUBXyB1UIHhJ_&q=85&s=6d6d36d109607f7c4a462e57152d4d20 280w, https://mintcdn.com/resend/03eaUBXyB1UIHhJ_/images/email-suppression-visibility-1.png?w=560&fit=max&auto=format&n=03eaUBXyB1UIHhJ_&q=85&s=b7db066204a09e900e87302222c8fa6a 560w, https://mintcdn.com/resend/03eaUBXyB1UIHhJ_/images/email-suppression-visibility-1.png?w=840&fit=max&auto=format&n=03eaUBXyB1UIHhJ_&q=85&s=8ad1631633664127bc1b3dcf8ddad8e6 840w, https://mintcdn.com/resend/03eaUBXyB1UIHhJ_/images/email-suppression-visibility-1.png?w=1100&fit=max&auto=format&n=03eaUBXyB1UIHhJ_&q=85&s=36a42b12ae4e64d47f91ea6dee68d153 1100w, https://mintcdn.com/resend/03eaUBXyB1UIHhJ_/images/email-suppression-visibility-1.png?w=1650&fit=max&auto=format&n=03eaUBXyB1UIHhJ_&q=85&s=a83e31dc7b892e475adb3d020286701e 1650w, https://mintcdn.com/resend/03eaUBXyB1UIHhJ_/images/email-suppression-visibility-1.png?w=2500&fit=max&auto=format&n=03eaUBXyB1UIHhJ_&q=85&s=2a0353e7c405efcff0eedaa1794c02f3 2500w" />

Once you click **See Details**, the drawer will open on the right side of your screen with the suppression reason along with suggestions on how to proceed.

You can also click **Remove from Suppression List** to prevent the address from being suppressed. Do note that if it bounces or is marked as spam again, it'll be suppressed again. Multiple or repeated bounces will negatively impact your sender reputation.
