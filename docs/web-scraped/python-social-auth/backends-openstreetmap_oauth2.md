# Backends/Openstreetmap_Oauth2

Source: https://python-social-auth.readthedocs.io/en/latest/backends/openstreetmap_oauth2.html

OpenStreetMap OAuth 2
¶

OpenStreetMap supports the OAuth 2.0 protocol. It supports two types of OAuth 2.0 flows:

Authorization code with 
Proof Key for Code Exchange (PKCE)

Authorization code

Configuration
¶

Login to your account

Register your application as OAuth 2 application on the 
My Client Applications page

Set the redirect URIs to 
https://example.com/complete/openstreetmap-oauth2/

PKCE can be enabled/disabled using the “Confidential application?” flag.

Select all required Permissions.

Scopes names are shown next to each permission after saving.

Fill 
Client ID
 in 

SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_KEY

 and

Client Secret
 in 

SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_SECRET

SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_KEY = ‘…’
SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_SECRET = ‘…’

Note: 
Client Secret
 isn’t required for PKCE.

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.openstreetmap_oauth2.OpenStreetMapOAuth2&#39;

,

...

)

Access tokens currently do not expire automatically.

More documentation at 
OpenStreetMap Wiki
:

Extra Configuration
¶

You can specify the scopes that your application requires:

SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_SCOPE

=

[

&#39;read_prefs&#39;

]

You can choose to disable PKCE:

SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_USE_PKCE

=

False

By default, 
True
 is set.