# Backends/Spotify

Source: https://python-social-auth.readthedocs.io/en/latest/backends/spotify.html

Spotify
¶

Spotify supports OAuth 2.

Register a new application at 
Spotify Web API
, and follow the
instructions below.

OAuth2
¶

Add the Spotify OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.spotify.SpotifyOAuth2&#39;

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

SOCIAL_AUTH_SPOTIFY_KEY

=

&#39;&#39;

SOCIAL_AUTH_SPOTIFY_SECRET

=

&#39;&#39;