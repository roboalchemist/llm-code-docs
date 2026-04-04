# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/hosting.md

# Hosting

Mailgun is mostly hosted on dedicated servers, however we use cloud servers for
some of the infrastructure (where it makes sense).

Mailgun uses dedicated IP addresses in large subnets. We also do background checks and extensive testing on our IP addresses; Because they are in large continuous blocks, they are less likely to be affected by other, external IP addresses. MBPs (Mailbox Providers) and blacklists occasionally block entire subnets if any of the IPs have questionable reputations; This means that if your IP is clean, it might be blocked because of surrounding IPs. Larger subnets mitigate this risk.

Large, virtual cloud environments are generally not the best environments for email for a few
reasons:

- The IP address should be static so that your domain(s) & IP
address(es) build a reputation together. Also, some more strict
recipients MBPs may require whitelisting your IP address.
Unfortunately, these should be IPv4.
- The IP address and surrounding IP addresses should have a good
reputation. This is rarely the case at large cloud environments due
to their ease of use and lax monitoring (which is inviting to
spammers).
- Mail Transfer Agents should ideally be on real (non-virtual)
machines, optimized for I/O.