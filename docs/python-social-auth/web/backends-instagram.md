# Backends/Instagram

Source: https://python-social-auth.readthedocs.io/en/latest/backends/instagram.html

Instagram
¶

Instagram uses OAuth v2 for Authentication.

Register a new application at the 
Instagram API
, and

Add instagram backend to 

AUTHENTICATION_SETTINGS

:

AUTHENTICATION_SETTINGS

=

(

...

&#39;social_core.backends.instagram.InstagramOAuth2&#39;

,

...

)

fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_INSTAGRAM_KEY

=

&#39;&#39;

SOCIAL_AUTH_INSTAGRAM_SECRET

=

&#39;&#39;

extra scopes can be defined by using:

SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS

=

{

&#39;scope&#39;

:

&#39;likes comments relationships&#39;

}