# Source: https://documentation.mailgun.com/docs/mailgun/faq/faqs.md

# FAQ: Getting Started/ Settings

### Why not just use Sendmail + Postfix + Courier IMAP?

You can but you should be aware that there is a constant battle raging
between good and evil (i.e., spam) in the email universe. In order to be
on the 'good' side of that battle and get your email delivered, there
are numerous things you need to do. You need to have the right
authentication infrastructure and register your IP and Domain
appropriately. Also, you need to have a history of email sending that
complies with ESPs rules in order to build a good reputation.

Moreover, if you are going to receive, store and host emails, you better
be prepared for maintaining this orchestra of software, take care of
backups, hardware failures, security patches and monitoring. Stop
kidding yourself, it's not 1998 anymore. :-)

Here's a classic post, [So You'd Like to Send Some Email (Through
Code)](http://blog.codinghorror.com/so-youd-like-to-send-some-email-through-code/),
from Jeff Atwood about all of the hurdles in order to properly send
email, and that's just sending.

### Can I get multiple Domains and IP Addresses?

By default we give you one shared IP address. If you would like a
dedicated IP address, simply click on the "Add Dedicated IP" button in
the **IP Management** section of the Control Panel. You will need to add
a credit card to your account first, though, if you have not already
done so. If you want multiple IPs, you can [contact our Support
Team](https://app.mailgun.com/app/support).

You can create up to 1,000 domains on a paid plan in the Control Panel
or through the `Domains API <api-domains>`{.interpreted-text
role="ref"}(Free accounts do not include the ability to create a custom
domain).

### Do I need a dedicated IP address?

It depends on various factors.

If you are sending a lot of email (greater than 50k per week), it is a
good idea to have a dedicated IP in order to isolate your reputation. If
you are sharing your IP, you are sharing your reputation with those
other senders. In addition, ESPs limit the total volume per IP, per
hour. If you are a high volume sender you should consider a pool of IPs.
However, you will have trouble establishing your reputation if you are
not sending enough volume consistently from an IP - in this case, a
shared IP is preferred.

If your email sending is volatile with large spikes of volume, ESPs may
assume those large spikes are spam. Also, if your overall volume is too
low, they won't acknowledge your reputation. Generally, if you are
sending less than 5,000 emails per day, a shared IP may be the right
solution.

The other thing to consider is using separate IPs for your bulk and
transactional mail. There are a couple reasons for this:

- Delivery of time-sensitive transactional emails may get queued
behind a large batch of bulk/marketing emails.
- Your transactional mail will be affected by the reputation created
by your bulk/marketing mail.


Mailgun's infrastructure mitigates some of the arguments for a
dedicated IP address. First of all, we are constantly monitoring our
shared IP addresses for any reputation issues. We also allow you to
schedule delivery of your emails by using the `o:deliverytime`
parameter. This allows you to delay the delivery by using a time in the
future and also allows you to jump other messages in your queue (say
from a large bulk mailing) by using a delivery time of now.

### How do I pick a domain name for my Mailgun account?

The name of an email domain matters most for receiving messages: If your
domain name is `mycompany.com` it means you can receive messages sent to
`xxx@mycompany.com`

Domain names do not matter as much if you're only sending. You can send
messages from `sales@mycompany.com` even if your domain name is called
`anothercompany.org`. Although, it is best for deliverability if you are
using the same domain in the From field that the actual sender is using.

There are two types of domains you can configure with Mailgun:

- A sandbox subdomain of mailgun.org. Example:
`sandboxXX.mailgun.org`. This option allows for quick testing,
without having to setup DNS entries. This domain is provisioned
automatically with every new account. But you can send only to
[authorized
recipients](https://help.mailgun.com/hc/en-us/articles/217531258).
- Your own domain like `mycompany.com`. This requires you to configure
some records at your DNS provider. We provide you with those records
and instructions in your Control Panel.


If your company's primary domain is `mycompany.com`, we recommend the
following domain names for mailgun:

> - `mycompany.com`, unless you're already using this name for your
corporate email;
- `m.mycompany.com` or `mail.mycompany.com`;
- `mycompany.net` or `mycompany.org`.



Sometimes, it is a good idea to separate the domains for the type of
messages you are sending. For example, some companies will use a
different domains or subdomains for bulk marketing mailings and
transactional or corporate mail in order to keep the reputations
separate.

It is recommended for all domains to use MX records, as they're a verification step that is commonly used by ISPs.
MX Records are also required if you want to receive email at the same subdomain you added to Mailgun.

Finally, if you want multiple addresses and you want to direct certain
emails to certain IP addresses, you will need to have a unique domain or
subdomain for each IP address. In this situation, it's best to [contact
our Support Team](https://app.mailgun.com/app/support) to discuss your
infrastructure.

### Can I use the same domain name for Mailgun and for Google Apps (or another email server)?

Yes, for sending. No, for receiving. Only one email server can receive
messages for a given domain name. It could be either Mailgun or Google
servers, but not both. However, you can use the same domain for sending
at multiple servers. If you'd like to register your Domain at multiple
servers for sending but you don't want to receive email at Mailgun,
just don't configure your MX records to point to Mailgun.

If you are receiving emails elsewhere with your domain, we recommend
using a subdomain at Mailgun so you can also receive emails at Mailgun.
This helps improve deliverability and allows us to more easily deal with
any issues that arise with recipient email servers.

### Can I rename a domain?

No, you need to create a new one and delete the old one. It's a good
idea to create the new one first.

### What if I need multiple SPF records?

If you are using multiple email servers and you want an SPF record for
each of them, you should NOT set up a separate TXT record for each. You
need to include the different servers in the same record. Below is
sample syntax:

'v=spf1 include:myemailserver.com include:mailgun.org ~all'

### How do I know if my DNS records are set up correctly

We have a "Check DNS Records Now" button when you click on a domain in
the `Domains` tab that will confirm that they are set up correctly and,
if not, show the incorrect records in red.

You could also use
[dig](http://en.wikipedia.org/wiki/Domain_Information_Groper) in your
command line interface.

### Do you support SSL/TLS?

Only TLS is supported. Support for SSL has been dropped due to the
[POODLE security
vulnerability](http://status.mailgun.com/incidents/9g4kmgh00y5x).

### Ok, everything is set up, how do I start using Mailgun?

Mailgun is primarily a developer's tool so the best way use Mailgun is
through our APIs. They are quite
[RESTful](http://en.wikipedia.org/wiki/REST) and we've tried to make
them as intuitive as possible. Our [Quickstart
Guide](https://documentation.mailgun.com/docs/mailgun/quickstart/) is a good place
to start and you can also use the [API
Reference](https://documentation.mailgun.com/docs/mailgun/api-reference/intro/) for more
detail. We also expose a lot of the features through the Control Panel.
The [User Manual](https://documentation.mailgun.com/docs/mailgun/user-manual/get-started/) is
a good place to get a full overview of all of the capabilities of
Mailgun.