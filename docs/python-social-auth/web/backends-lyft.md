# Backends/Lyft

Source: https://python-social-auth.readthedocs.io/en/latest/backends/lyft.html

Lyft
¶

Lyft implements OAuth2 as its authorization service. To setup a Lyft backend:

Register a new application via the 
Lyft Developer Portal
.

Add the Lyft OAuth2 backend as an option in your settings:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.lyft.LyftOAuth2&#39;

,

...

)

Use the 

Client

Id

 and 

Client

Secret

 from the Developer Portal into your settings:

SOCIAL_AUTH_LYFT_KEY

=

&#39;&#39;

SOCIAL_AUTH_LYFT_SECRET

=

&#39;&#39;

Specify the scope that your app should have access to:

SOCIAL_AUTH_LYFT_SCOPE

=

[

&#39;public&#39;

,

&#39;profile&#39;

,

&#39;rides.read&#39;

,

&#39;rides.request&#39;

]

To learn more about the API and the calls that are available, read the 
Lyft API Documentation
.