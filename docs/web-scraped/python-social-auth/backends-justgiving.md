# Backends/Justgiving

Source: https://python-social-auth.readthedocs.io/en/latest/backends/justgiving.html

Just Giving
¶

OAuth2
¶

Follow the steps at 
Just Giving API Docs
 to register your
application and get the needed keys.

Add the Just Giving OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.justgiving.JustGivingOAuth2&#39;

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

SOCIAL_AUTH_JUSTGIVING_KEY

=

&#39;&#39;

SOCIAL_AUTH_JUSTGIVING_SECRET

=

&#39;&#39;