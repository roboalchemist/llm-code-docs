# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tls-connection-settings/require-tls.md

# Require tls

TLS sending connection settings ensure your emails are securely transmitted by encrypting the connection between your email server and recipients, protecting your messages from interception during delivery.

If set to *True*, messages can only be sent over a TLS connection. If the TLS connection cannot be established, Mailgun will not deliver the message. If set to *False*, Mailgun will try to upgrade the connection. If Mailgun cannot upgrade the connection, the message will be delivered over a plaintext SMTP connection. The default is False.