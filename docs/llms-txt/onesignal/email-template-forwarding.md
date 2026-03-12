# Source: https://documentation.onesignal.com/docs/en/email-template-forwarding.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email template forwarding

> Forward your email templates to create them quickly!

Add email templates to your app by simply sending any email to a unique address. After creating a new email template in this way you can immediately view it in the dashboard, edit any necessary links and resources, and start using it right away.

This could save you a lot of time migrating email templates to OneSignal. It is a great starting point for creating email templates from examples. You can always login to the dashboard **Messages > Templates** and update the new template to make sure its reusable with the correct images, links and general clean up.

<Warning>
  If you are using an email from an external source it is strongly recommended that you change any existing links and images to point to new resources you host instead.
</Warning>

<Info>
  Only HTML emails are currently accepted.

  Text-only emails should be created manually in the dashboard via copy and paste.
</Info>

Within your OneSignal dashboard, navigate to **Settings > Keys & IDs > Incoming Email Templates**.

Copy the full `@templates.onesignal.email` address.

<Frame caption="Generate and copy email template forwarding address">
    <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b19f9f4-Screenshot_2023-08-18_at_5.23.52_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=9ca2664e391e154f466a3bced4da5bcf" alt="" width="2426" height="788" data-path="images/docs/b19f9f4-Screenshot_2023-08-18_at_5.23.52_PM.png" />
</Frame>

Within your email client, select the email you want to "template-ize".

Send the email to the `@templates.onesignal.email`

Navigate to **Messages > Templates > Email** to see your new template.

***

Built with [Mintlify](https://mintlify.com).
