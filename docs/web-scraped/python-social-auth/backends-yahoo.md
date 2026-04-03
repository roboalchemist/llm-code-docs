# Backends/Yahoo

Source: https://python-social-auth.readthedocs.io/en/latest/backends/yahoo.html

Yahoo
¶

Yahoo supports OpenID and OAuth2 for their auth flow.

Yahoo OpenID
¶

OpenID doesn’t require any particular configuration beside enabling the backend
in the 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.yahoo.YahooOAuth2&#39;

,

...

)

Yahoo OAuth2
¶

OAuth 2.0 workflow, useful if you are planning to use Yahoo’s API.

Register a new application at 
Yahoo Developer Center
, set your app domain
and configure scopes (they can’t be overridden by application).

Fill 

Consumer

Key

 and 

Consumer

Secret

 values in the settings:

SOCIAL_AUTH_YAHOO_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_YAHOO_OAUTH2_SECRET

=

&#39;&#39;