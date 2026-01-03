# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/dns.md

# DNS

Your email reputation is not only tied to your IP, but your domain name as well. You should keep this in mind as you set up your email infrastructure. For the same reasons, it is a good idea to have separate domains or subdomains for your marketing, transactional and corporate mail. We suggest that you use your top level domain for your corporate mail and using different domains or subdomains for your marketing and transactional mail.

While it is not required to use the same domain in the From field of the message as the actual domain sending the message, it is highly recommended. Outlook/Hotmail is especially finicky about this requirement and has a higher propensity to filter your messages to junk if the two domains do not match.

You should also make sure that you are using a well regarded DNS provider and that you publish all of your contact information in the WHOIS record. If you are hiding your contact information through a proxy, MBPs (Mailbox Providers) may take that as a signal that you are spamming.

Also, make sure you include the appropriate records from your DNS provider for authentication. While it's not required to point mx records to the same domain as you are sending from, it is recommended. There are mailbox providers (albeit, a minority) that will check if mx records for the domain are valid before accepting email.

Mailgun gives you the ability to create multiple domains or subdomains very easily. You are free to create multiple domains and subdomains for each of your transactional, marketing and corporate email. Each domain has an isolated queue, so your transactional emails won't get held up by your bulk mailings.