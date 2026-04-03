# Backends/Shimmering

Source: https://python-social-auth.readthedocs.io/en/latest/backends/shimmering.html

Shimmering Verify
¶

Shimmering implemented OAuth2 protocol for their authentication mechanism. To
enable 

python-social_core-auth

 support follow this steps:

Go to 
Shimmering Developer Console
 and create an application.

Fill App Id and Secret in your project settings:

SOCIAL_AUTH_SHIMMERING_KEY

=

&#39;...&#39;

SOCIAL_AUTH_SHIMMERING_SECRET

=

&#39;...&#39;

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.shimmering.ShimmeringOAuth2&#39;

,

...

)