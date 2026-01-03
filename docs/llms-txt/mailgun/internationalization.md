# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/internationalization/internationalization.md

# Internationalization

Internationalization Domain Names (IDN)

Mailgun's Messages API supports sending to addresses that use internationalized domain names in the `to` and `from` fields. When necessary, Mailgun will automatically convert the domains to the ADCII equivalent using [Punycode](https://en.wikipedia.org/wiki/Punycode).

Note:
Currently, sending domains cannot be created using non-ASCII characters.

Internationalized Email Addresses (SMTPUTF8)
Mailgun supports internationalized email addresses though the use of the SMTPYTF8 extension. An Internationalized email address will contain a non-ASCII character in the local-part portion of the email address and may also use an internationalized domain name.

Mailgun supports internationalized email addresses in the following portions of our product:

- Outgoing Messages (HTTP API)
- Email Verification
- Suppressions Lists


Note:
Match\recipient and forward action are supported for domains using international characters / punycode. However, sending to a punycode domain is not supported.

To send messages to an internationalized email address, the receiving mailbox provider must support the SMTPUTF8 extension