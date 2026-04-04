# Backends/Mailru

Source: https://python-social-auth.readthedocs.io/en/latest/backends/mailru.html

Mail.ru OAuth
¶

Mail.ru uses OAuth2 workflow. 
Register new application
 to use it and fill in settings:

SOCIAL_AUTH_MAILRU_KEY

=

&#39;&#39;

SOCIAL_AUTH_MAILRU_SECRET

=

&#39;&#39;

Add 

social_core.backends.mailru.MRGOAuth2

 to 

AUTHENTICATION_BACKENDS

 to activate Mail.ru authorization.

Legacy OAuth2 authorization
¶

Also available 

social_core.backends.mailru.MailruOAuth2

 for authorization with 

connect.mail.ru

 server.

Create an app
 and set following settings:

SOCIAL_AUTH_MAILRU_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_MAILRU_OAUTH2_SECRET

=

&#39;&#39;