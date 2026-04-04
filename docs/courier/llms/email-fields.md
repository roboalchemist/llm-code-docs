# Source: https://www.courier.com/docs/platform/content/template-settings/email-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customizing Email Address Fields

> Customize the ‘From’, ‘Reply-To’, ‘CC’, and ‘BCC’ fields per notification or globally via integration settings. Channel settings override defaults and support dynamic variables for personalized address handling.

> How to set the sender name and email address for your email notification's 'From', 'Reply To', 'CC' and 'BCC' fields.

Courier allows you to define the From name and email by default or per notification.

The `Reply to`, `CC`, and `BCC` addresses are set per notification within the channel settings.

## Setting the 'From' Name and Email Address

You can set the 'From' name and email address for email notifications in two ways:

1. The default provider integration settings
2. On a per-channel basis using the email channel settings.

<Note>
  **INFO**

  The channel settings will *always* override the default provider integration settings on the channel and notification where they are set.
</Note>

## Setting Default Address Fields in the Integration Settings

By default, email notifications will use the `from` name and `email` address you set in your provider integration settings.

Some providers allow us to provide you a `From Email Address` field alongside a `From Name` field.

<Frame caption="Email From Field">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/email-from.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=068afb929516c85946a7958e69694263" alt="Email From Field" width="728" height="148" data-path="assets/platform/content/email-from.png" />
</Frame>

When the provider integration settings don't allow a Sender Name field use the `Sender Name <example@youremailprovider.com>` format to define the `from` name that will display in your recipient's email client.

<Frame caption="Email API">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/email-api.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=a04101012547836eb27249181106fbae" alt="Email From Field" width="731" height="143" data-path="assets/platform/content/email-api.png" />
</Frame>

### Overriding the Default From Name and Email Via Channel Settings

To override the integration default and define your sender name for a specific channel within a single notification, open the [channel settings](/platform/sending/channel-settings).

<Frame caption="Channel Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/email-channel-settings.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=16232087111b6e764d25ea01ec10bf6b" alt="Channel Settings" width="438" height="275" data-path="assets/platform/content/email-channel-settings.png" />
</Frame>

Once you open the channel settings you'll see the email configuration fields for setting the `From` email.

Use the `Sender Name <example@youremailprovider.com>` format to define a name.

## Setting the 'Reply To', 'CC' and 'BCC' Addresses

To set the `Reply To`, `CC` and `BCC` addresses, open the email channel settings and add your email addresses into the corresponding fields.

<Info>
  You can use [variables](/platform/content/variables/inserting-variables) to dynamically set any of these email addresses.
</Info>

<Frame caption="General Template Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/email-general.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=40ca66c186d7a2500fa50aba31683a79" alt="General Template Settings" width="1224" height="811" data-path="assets/platform/content/email-general.png" />
</Frame>
