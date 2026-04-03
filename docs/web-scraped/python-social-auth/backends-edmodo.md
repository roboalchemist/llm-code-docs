# Backends/Edmodo

Source: https://python-social-auth.readthedocs.io/en/latest/backends/edmodo.html

Edmodo
¶

Edmodo supports OAuth 2.

Register a new application at 
Edmodo Connect API
, and follow the
instructions below.

Add the Edmodo OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.edmodo.EdmodoOAuth2&#39;

,

...

)

Fill 

App

Key

, 

App

Secret

 and 

App

Scope

 values in the settings:

SOCIAL_AUTH_EDMODO_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_EDMODO_OAUTH2_SECRET

=

&#39;&#39;

SOCIAL_AUTH_EDMODO_SCOPE

=

[

&#39;basic&#39;

]