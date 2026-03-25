# Source: https://docs.iredmail.org/performance.tuning.html

Title: Performance tuning

URL Source: https://docs.iredmail.org/performance.tuning.html

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

*   [Performance tuning](https://docs.iredmail.org/performance.tuning.html#performance-tuning)
    *   [Setup a DNS server in LAN or localhost to cache DNS queries](https://docs.iredmail.org/performance.tuning.html#setup-a-dns-server-in-lan-or-localhost-to-cache-dns-queries)
    *   [Enable postscreen service to help reduce spam](https://docs.iredmail.org/performance.tuning.html#enable-postscreen-service-to-help-reduce-spam)
    *   [Update Amavisd + Postfix config files to process more emails concurrently](https://docs.iredmail.org/performance.tuning.html#update-amavisd-postfix-config-files-to-process-more-emails-concurrently)

If you're running a busy mail server (many inbound/outbound emails every day), you can follow below suggestions for better performance.

### Setup a DNS server in LAN or localhost to cache DNS queries

Mail services **heavily** rely on DNS service and perform many many DNS queries, a cache DNS server in LAN or localhost helps **A LOT**:

*   It speeds up DNS queries. This helps a lot to speed up mail flow.
*   It reduces DNS queries to DNSBL servers, so that you can continue using their excellent service without exceeding the max query limit.

### Enable postscreen service to help reduce spam

*   [Enable postscreen service](https://docs.iredmail.org/enable.postscreen.html)

If you don't want to use postscreen service, you can [enable DNSBL service](https://docs.iredmail.org/enable.dnsbl.html) instead, it helps a lot too. Although both `postscreen` and pure DNSBL services uses the same DNSBL servers, but `postscreen` offers additional solutions to reduce spam, so postscreen is better.

postscreen and DNSBL service help catch a lot spam before putting the spams in local mail queue, so they save much system resource.

### Update Amavisd + Postfix config files to process more emails concurrently

*   [Process more emails concurrently](https://docs.iredmail.org/concurrent.processing.html)
