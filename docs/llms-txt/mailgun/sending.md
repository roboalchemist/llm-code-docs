# Source: https://documentation.mailgun.com/docs/mailgun/faq/sending.md

# FAQ: Sending

### Should I use SMTP or the HTTP API?

It's really up to you. Whatever you find easier is fine with us. The
HTTP API has some advantages, however. First of all, it's faster.
Second, we think it's easier to use - you don't have to deal with MIME
because we will assemble it on our side. Just use a request library
available for your language of choice.

### Email clients say "sent via mailgun.us" with messages I send. How do I get rid of this?

Check the following:

- You have a custom domain defined in the `Domains` tab of the Control
Panel.
- You've setup the DKIM DNS record (provided in the Control Panel,
`Domains` tab).
- You're authenticating (SMTP) or posting (API) against the custom
domain.


If you're still seeing "via mailgun.org", please [contact our Support
Team](https://app.mailgun.com/app/support) and we'll investigate.

### What is the difference between the "From" and "Sender"

Each message you send out has both the sender and from address. Simply
put, the sender domain is what the receiving email server sees when
initiating the session, and the from address is what your recipients
will see. For better deliverability it is recommended to use the same
from domain as the sender, but it is not required.

You can technically set the from field to be whatever you like. The
sender must always be one of your Mailgun domains.

### Where do I specify BCC recipients?

BCC functionality works like this: specify a BCC recipient in the
recipients list when sending, but do not include their address in the
"To" or "CC" fields. You could also use the API, which has a
specific BCC parameter.

### How do I send the same message to multiple users using Mailgun?

Mailgun supports the ability send to a group of recipients through a
single API call or SMTP session. This is achieved by either:

- Using Batch Sending by specifying multiple recipient email addresses
as to parameters and using Recipient Variables.
- Using Mailing Lists with Template Variables.


See the `batch-sending`{.interpreted-text role="ref"} section of the
`user-manual`{.interpreted-text role="ref"} for more information.

### I am getting timeouts when connecting via SMTP. Why?

Most often, this is caused by internet service providers ("ISP")
blocking port #25. This tends to happen if you are using a residential
ISP.

To check this, try running telnet in command line:

telnet smtp.mailgun.org 25

If port 25 is not blocked, you should see something like this:

Trying 174.37.214.195...
Connected to mxa.mailgun.org.
Escape character is '^]'.
220 mxa.mailgun.org (Mailgun)

If you don't see this, then you are being blocked. There are a couple workarounds:

- Send using our HTTP API
- Try using port #587 or #2525


### I have multiple domains at Mailgun. How do I tell Mailgun which domain to send mail from?

For SMTP, you have an SMTP username and password for each domain you
have registered at Mailgun. To send mail from a particular domain, just
use the appropriate credentials. For the API, the domain is one of the
parameters in the URI.

### I just submitted a lot of messages. Why is delivery happening so slowly?

There are many factors that can affect the speed of delivery.

1. Your established reputation for the domain and IPs on your account.
2. The total number of IPs allocated to your account.
3. The content quality for the emails being sent.


For newly allocated IPs, Mailgun protects and improves the reputation by
gradually increasing sending rates. This means, as time passes, with
high quality traffic, being sent from your IPs, your sending rates will
increase automatically. If you're seeing slow delivery, please contact
us. We'll evaluate your account configuration to ensure it is
configured for handling the volume you require.