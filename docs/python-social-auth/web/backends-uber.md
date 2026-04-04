# Backends/Uber

Source: https://python-social-auth.readthedocs.io/en/latest/backends/uber.html

Uber
¶

Uber uses OAuth v2 for Authentication.

Register a new application at the 
Uber API
, and follow the instructions below

OAuth2
¶

Add the Uber OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.uber.UberOAuth2&#39;

,

...

)

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_UBER_KEY

=

&#39;&#39;

SOCIAL_AUTH_UBER_SECRET

=

&#39;&#39;

Scope should be defined by using:

SOCIAL_AUTH_UBER_SCOPE

=

[

&#39;profile&#39;

,

&#39;request&#39;

]