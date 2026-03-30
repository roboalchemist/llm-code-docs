# Source: https://docs.ghost.org/newsletters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Newsletters

> Sites using the Members feature benefit from built-in email newsletters, where all posts can be delivered directly to segments of your audience in just a few clicks.

***

## Overview

Email newsletters in Ghost can be scheduled and delivered to free and paid members, or a segment of free *or* paid members. Newsletters are delivered using a beautiful HTML template that is standardised for most popular email clients.

Ghost sites have a single newsletter by default but additional ones can be created and customised. Multiple newsletters allow you to tailor content for specific audiences and your members to choose which content they receive.

## Bulk email configuration

In order to send email newsletters from a Ghost site, email needs to be configured.

### Ghost(Pro)

When using [Ghost(Pro)](https://ghost.org/pricing/), email delivery is included and the configuration is handled for you automatically.

### Self-hosted

Self-hosted Ghost installs can configure bulk email by entering Mailgun API keys from the **Email newsletter** settings.

Delivering bulk email newsletters can’t be done with basic SMTP. A bulk mail provider is a requirement to reliably deliver bulk mail. At present, Mailgun is the only supported bulk email provider. Mailgun is free for up to 600 emails per month, and has very reasonable pricing beyond that. [More info here](/faq/mailgun-newsletters/)

<Frame>
  <img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/mailgun-form.webp?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=0df4ab16115fb1665a28735c5b02bc0a" width="1400" height="534" data-path="images/mailgun-form.webp" />
</Frame>

### Auth email

The Members feature uses passwordless email-link based logins for your members. These auth emails are not delivered in bulk and are sent using the standard mail configuration in Ghost.

Self-hosted Ghost installs can [configure mail](/config/#mail) using Mailgun or other providers if preferred.


Built with [Mintlify](https://mintlify.com).