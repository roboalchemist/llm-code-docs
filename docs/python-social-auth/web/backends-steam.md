# Backends/Steam

Source: https://python-social-auth.readthedocs.io/en/latest/backends/steam.html

Steam OpenID
¶

Steam OpenID works quite straightforward, but to retrieve some user data (known
as 

player

 on Steam API) a Steam API Key is needed.

Configurable settings:

Supply a Steam API Key from 
Steam Dev

Fill key in your project settings:

SOCIAL_AUTH_STEAM_API_KEY

=

&#39;...&#39;

To save 

player

 data provided by Steam into 

extra_data

:

SOCIAL_AUTH_STEAM_EXTRA_DATA

=

[

&#39;player&#39;

]

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.steam.SteamOpenId&#39;

,

...

)