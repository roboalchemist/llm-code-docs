# Backends/Battlenet

Source: https://python-social-auth.readthedocs.io/en/latest/backends/battlenet.html

Battle.net
¶

Blizzard implemented OAuth2 protocol for their authentication mechanism. To
enable 

python-social-auth

 support follow this steps:

Go to 
Battlenet Developer Portal
 and create an application.

Fill App Id and Secret in your project settings:

SOCIAL_AUTH_BATTLENET_OAUTH2_KEY

=

&#39;...&#39;

SOCIAL_AUTH_BATTLENET_OAUTH2_SECRET

=

&#39;...&#39;

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.battlenet.BattleNetOAuth2&#39;

,

...

)

Note: If you want to allow the user to choose a username from their own
characters, some further steps are required, see the use cases part of the
documentation. To get the account id and battletag use the user_data function, as

account id is no longer passed inherently
.

Another note: If you get a 500 response “Internal Server Error” the API now requires 
https on callback endpoints
.

Further documentation at 
Developer Guide
.