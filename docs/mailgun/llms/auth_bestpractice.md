# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/auth_bestpractice.md

# Authentication

It is very important that you are using the appropriate authentication
methods with your email. If you are not authenticating your email
properly, ESPs will assume you are spamming and will filter or just drop
your email.

The common types of authentication are:

- [SPF](http://www.openspf.org)
- [DKIM](http://www.dkim.org)
- [DomainKeys](http://domainkeys.sourceforge.net)
- [SenderID](https://docs.microsoft.com/en-us/exchange/antispam-and-antimalware/antispam-protection/sender-id?view=exchserver-2019)


Mailgun uses all of these types of authentication. When you sign up for
Mailgun, we provide the appropriate records for you to include at your
DNS registrar. We also provide a verification button you can use to make
sure that your records are set up correctly.