# Backends/Pinterest

Source: https://python-social-auth.readthedocs.io/en/latest/backends/pinterest.html

Pinterest
¶

Pinterest implemented OAuth2 protocol for their authentication mechanism.
To enable 

python-social-auth

 support follow this steps:

Go to 
Pinterest developers zone
 and create an application.

Fill App Id and Secret in your project settings:

SOCIAL_AUTH_PINTEREST_KEY

=

&#39;...&#39;

SOCIAL_AUTH_PINTEREST_SECRET

=

&#39;...&#39;

SOCIAL_AUTH_PINTEREST_SCOPE

=

[

&#39;read_public&#39;

,

&#39;write_public&#39;

,

&#39;read_relationships&#39;

,

&#39;write_relationships&#39;

]

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.pinterest.PinterestOAuth2&#39;

,

...

)