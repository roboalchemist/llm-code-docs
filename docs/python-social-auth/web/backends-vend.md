# Backends/Vend

Source: https://python-social-auth.readthedocs.io/en/latest/backends/vend.html

Vend
¶

Vend supports OAuth 2.

Register a new application at 
Vend Developers Portal

Add the Vend OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.vend.VendOAuth2&#39;

,

...

)

Fill 

App

Key

 and 

App

Secret

 values in the settings:

SOCIAL_AUTH_VEND_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_VEND_OAUTH2_SECRET

=

&#39;&#39;

More details on their 
docs
.