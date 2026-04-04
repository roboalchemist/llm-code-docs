# Backends/Beats

Source: https://python-social-auth.readthedocs.io/en/latest/backends/beats.html

Beats
¶

Beats supports OAuth 2.

Register a new application at 
Beats Music API
, and follow the
instructions below.

OAuth2
¶

Add the Beats OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.beats.BeatsOAuth2&#39;

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

SOCIAL_AUTH_BEATS_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_BEATS_OAUTH2_SECRET

=

&#39;&#39;