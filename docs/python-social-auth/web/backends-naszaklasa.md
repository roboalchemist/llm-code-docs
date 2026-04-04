# Backends/Naszaklasa

Source: https://python-social-auth.readthedocs.io/en/latest/backends/naszaklasa.html

NationBuilder
¶

NaszaKlasa supports OAuth2
 as their authentication mechanism. Follow these
steps in order to use it:

Register a new application at your 
NK Developers
 (define the 
Callback
URL
 to 

http://example.com/complete/nk/

 where 

example.com

is your domain).

Fill the 

Client

ID

 and 

Client

Secret

 values from the newly created
application:

SOCIAL_AUTH_NK_KEY

=

&#39;&#39;

SOCIAL_AUTH_NK_SECRET

=

&#39;&#39;

Enable the backend in 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.nk.NKOAuth2&#39;

,

...

)