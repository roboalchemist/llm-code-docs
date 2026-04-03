# Backends/Lastfm

Source: https://python-social-auth.readthedocs.io/en/latest/backends/lastfm.html

Last.fm
¶

Last.fm uses a similar authentication process than OAuth2 but it’s not. In
order to enable the support for it just:

Register an application at 
Get an API Account
, set the Last.fm callback to
something sensible like 
http://your.site/complete/lastfm

Fill in the 
API Key
 and 
API Secret
 values in your settings:

SOCIAL_AUTH_LASTFM_KEY

=

&#39;&#39;

SOCIAL_AUTH_LASTFM_SECRET

=

&#39;&#39;

Enable the backend in 

AUTHENTICATION_BACKENDS

 setting.