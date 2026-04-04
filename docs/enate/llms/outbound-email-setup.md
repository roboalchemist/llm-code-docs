# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/setting-up-your-email-infrastucture/outbound-email-setup.md

# Outbound Email Setup

### Protocol Support

Enate currently only supports SMTP/SMTPS for sending email. GraphAPI is currently only available for incoming email.

### Enate Message Handling for Outgoing Email

Internally, Enate matches on the outgoing "From" to determine what email connector configured as either ‘Outgoing’ or ‘Both’ should be used to send a specific message. If no specific email connectors match the "From" address then Enate will fall back to using the System Default Gateway for sending email.

{% hint style="info" %}
Note: This System Default Gateway MUST be configured prior to using Enate.
{% endhint %}

The unmonitored email address which is used as the From address on some automated outgoing emails such as password reset mails (and which you can set in the General Settings section of Builder) functions in the same way as the above configured From addresses. If the System Default Gateway is disabled, you must provide a valid email address for this unmonitored email which has been configured as an outbound email connector.

### Common SMTP Configurations

Outgoing email can be configured in several different ways in Enate depending on the preferences of your mail server teams.

As with incoming email, Enate requires an external DNS name and publicly trusted certificate be configured with SMTP.

The port that Enate connects to SMTP on is configurable within Builder on a per connector basis and so the firewall requirements are dependent on the mail server teams and their configuration of these protocols. Typically, either port 25 for SMTP or ports 465 or 587 for SMTPS are used.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MiufEuqNMAYjHrD2FzB%2F-Miufy0va2zmani43Zeh%2Fimage.png?alt=media\&token=56089e63-16d1-4da4-bdc1-d2f295a10302)

#### Instance-Wide SMTP Gateway

An SMTP gateway can be created with the ability to relay all email sent via it. This can be restricted with a username/password combination to avoid creating an open relay that may be subject to abuse. This can then be configured as the default SMTP/outgoing connector within Enate Builder.

This simplifies ongoing email configurations allowing new incoming email addresses to be added without needing to adjust permissions for sending.

#### Instance-Wide with 'Send As' Permissions

Similar to the above, a gateway can be supplied where a user account with Send As permissions on every account/Email address used within Enate can send email.

For example, an <enate.production@example.com> account could be created with Send As permissions on <enate.sales@example.com>, <enate.finance@example.com> and <enate.accounting@example.com>. This <enate.production@example.com> could then be configured instance-wide within Enate Builder.

This increases the configuration complexity and also requires IT or mail servers to add new addresses on an ongoing basis whenever these are required within Enate.

#### Per-Email Connector SMTP Server Settings

When configuring email connectors in Enate, you can specify either Incoming, Outgoing or Both for the direction.

These settings allow you to configure outgoing email to use connector specific SMTP values. No additional credentials can be specified here and so the POP3/IMAP4 credentials specified on the email connector in Enate must have Send As permissions on the configured SMTP From Address value.

This configuration typically only works where the incoming POP3/IMAP4 address is also the address that will be used to send replies, for example if customers are emailing <enate.sales@example.com> and the reply will also come from <enate.sales@example.com>. If this is not the case then this configuration leads to having to manage multiple sets of permissions across different accounts to allow Send As permissions to cover all addresses used in Enate.
