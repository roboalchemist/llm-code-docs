# Sending e-mail

Although Python makes sending e-mails relatively easy via the `smtplib` [https://docs.python.org/3/library/smtplib.html#module-smtplib]
library, Scrapy provides its own facility for sending e-mails which is very
easy to use and it’s implemented using Twisted non-blocking IO [https://docs.twisted.org/en/stable/core/howto/defer-intro.html], to avoid interfering with the non-blocking
IO of the crawler. It also provides a simple API for sending attachments and
it’s very easy to configure, with a few settings.

## Quick example

There are two ways to instantiate the mail sender. You can instantiate it using
the standard `__init__` method:

```
from scrapy.mail import MailSender

mailer = MailSender()

```