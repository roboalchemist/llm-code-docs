# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/outbox-view.md

# Outbox View

## Overview

The Outbox Page is where you can find emails belonging to yourself or to your team that are scheduled be to sent at a later date, or have failed to send.

You can access the Outbox Page from the Emails section in the navigation link. The total number of emails in your Outbox will also be shown in the navigation link.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6zBPgzDCBQ7DugKl91bf%2Fimage.png?alt=media\&token=ac110c95-a933-425c-bd7f-26a0fe54da9a)

You can select how many emails will be shown from the option on the right.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FypvBw33Z3mOSWcawFlqm%2F8-Outbox-Page-Number-of-rows.gif?alt=media\&token=abe4fae4-3a3f-45a3-aadb-a22e6886b6aa)

## Outbox Grid Views

The first time a Team Leader logs in, they will land on the 'My Team Emails' view. The first time a Team Member logs in, they will land on the 'My Emails' view. You are able to change your view of the outbox page to show just your outbox emails, your team's, the system's or all outbox emails. This will be saved when you log out and log back in.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK48xnoeWvjpoA9cgRbX0%2F8-outbox-page-filters.gif?alt=media\&token=7a54f2b6-516c-4ba8-89ab-5e0fe50e3270)

Selecting '**My Emails**' lets you see emails sent by you that are in your outbox.

'**My Team Emails**' shows you emails sent by your team that are in the outbox, as well as emails relating to work items that your team members are working on that are in the outbox.

Selecting '**System Emails**' lets you see emails that are sent automatically by the system e.g. because a Ticket has been split or merged.

'**All**' lets you see emails sent by you, your team, as well as emails from outside of your team for which you have access.

## Retry and Cancel Options

You are able to manually retry sending an email by clicking on the Retry icon. The email will now be in a state of **'**&#x50;ending Retry'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJkOzke4SSq4rYPj5bw54%2F8-retry-sending-email-from-outbo.gif?alt=media\&token=7c26d189-032c-4cd2-a5c8-75ce04c1454a)

You can also retry sending an email from the timeline of the work item itself.

Additionally, the system can automatically retry sending emails if your system has been set with an Automated Failure Retry Pattern ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern)). Once the system has retried sending an email the maximum number of times specified, it will no longer retry sending it automatically, but you can still retry sending the email manually, i.e. by clicking the 'Retry' icon.

You are also able to cancel sending an email by clicking on the Cancel icon. This will remove the email from the Outbox.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_RA0uUPIci_XLqD9Fs%2F-M_REKnN58uonsLTRux6%2Fimage.png?alt=media\&token=261065a7-6f73-4cad-83a7-4def7b4d7b23)

You are also able to retry or cancel sending emails in bulk.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNIX3WDn8E0lxUGCeZUAI%2F8-outbox-page-bulk-options.gif?alt=media\&token=9ae7e2e4-e9eb-4132-87e4-04efb3ceaeae)

{% hint style="info" %}
Please note that the system will not automatically retry sending emails that have been migrated from an older version (2020.1 or older). These can only be sent by retrying manually, i.e. clicking the 'Retry' icon.
{% endhint %}

## Viewing an Email

Double clicking on an email will open the email's details in a popup in read only form. You can see who the email is from, who it is to, etc. You are also able to retry and cancel sending the email from the popup.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fp0vnOV3tG7uXuFtATaxP%2F8-opening-email-in-outbox-page.gif?alt=media\&token=ab58437e-71c2-4016-b001-177289693b7a)

## Adjusting Grid Columns

You can adjust the grid columns by clicking on the settings cog. These will be saved when you log out and log back in. The 'To' and 'Subject' columns are mandatory.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY4Ng==>" %}

* **Email Connector** - the name of the email connector through which your system sends emails. This is configured in Builder, [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-connectors-detail).
* **Importance** - the importance setting of the email i.e. high, normal, low.
* **System Generated** - if the email was automatically generated by the system (e.g. to notify a user when a Ticket has been split).
* **Last Attempt To Send** - when the last attempt to send the email was (automatically by the system or manually by a user)
* **Last Send Failure Message** - a message displaying the reason why the last attempt to send the email failure e.g. The Email connector is disabled. Please enable it and try again.
* **Logged** - the date and time recorded when the email first failed to send.&#x20;
* **Next Attempt To Send** - when the system will next try to send the email
* **Packet** - the work item reference that the email is from. Clicking on this will take you to the work item screen.
* **Packet Type** - if the email is related to a Ticket, Case or Action
* **Send Retry Count** - this will show the number of times the system has tried to send the email. You can set this number in Builder, [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern).
* **Send Status** - this shows what status emails in the outbox are in in terms of sending. There are 4 states:
  * **Failed** - an email with this Send Status has failed to send. In order to send it, it must be manually 'retried'.&#x20;
  * **Connector Disabled** - if an email has this Send Status, it means that the Email Connector has been disabled in Builder. [Click here for more information about how to switch it on](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-connectors-detail).
  * **Pending Retry** - an email with this Send Status is awaiting automatic retry by the system.
  * **Queued** - an email with this Send Status is already scheduled to be sent. Emails send when an Undo Send option has been set will have this status too ([see here for more information about the Undo Send option](https://docs.enate.net/enate-help/work-manager/user-settings#undo-send)). When these emails will be sent depends on the Automated Failure Retry Pattern option which is set in Builder, [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern).
* **Attachment Count** - how many (if any) files are attached to the email
