# Backends/Upwork

Source: https://python-social-auth.readthedocs.io/en/latest/backends/upwork.html

Upwork
¶

Upwork supports only OAuth 1.

Register a new application at 
Upwork Developers
.

OAuth1
¶

Add the Upwork OAuth backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.upwork.UpworkOAuth&#39;

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

SOCIAL_AUTH_UPWORK_KEY

=

&#39;&#39;

SOCIAL_AUTH_UPWORK_SECRET

=

&#39;&#39;

Note:
 For more information please go to 
Upwork API Reference
.