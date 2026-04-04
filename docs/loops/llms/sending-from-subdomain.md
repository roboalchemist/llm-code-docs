# Source: https://loops.so/docs/deliverability/sending-from-subdomain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subdomains vs root domains

> Most email services (including Loops) prefer sending emails from subdomains (hey.company.com) over root domains (company.com).

Subdomains can often be easier to configure and can sometimes be more effective at preventing email from being marked as spam.

It is important to remember that emails sent from a subdomain will also appear in the “from” field of your emails, so make sure to use an address that is recognizable to your audience. We recommend sending from a subdomain like:

* hey.company.com
* mail.company.com
* updates.company.com

Whichever you choose, you can always update it later in your [Domain Settings](https://app.loops.so/settings?page=domain).
