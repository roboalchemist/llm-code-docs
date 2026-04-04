# Backends/Patreon

Source: https://python-social-auth.readthedocs.io/en/latest/backends/patreon.html

Patreon
¶

Patreon supports OAuth 2.0

Register a new application at 
Patreon Developer Portal
.

Use the 

social.backends.patreon.PatreonOAuth2

, either by adding it to
your 

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

 or instantiating it directly.

Fill in the the 

Client

ID

 and 

Client

Secret

:

SOCIAL_AUTH_PATREON_KEY

=

&#39;&lt;your client ID&gt;&#39;

SOCIAL_AUTH_PATREON_SECRET

=

&#39;&lt;your client secret&gt;&#39;

Checkout the 
Patreon API Docs
 for more information.