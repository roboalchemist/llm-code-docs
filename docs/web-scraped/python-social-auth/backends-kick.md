# Backends/Kick

Source: https://python-social-auth.readthedocs.io/en/latest/backends/kick.html

Kick
¶

Kick works similar to Facebook (OAuth) but with Oauth2.1.

Register a new application in the 
developer tab
 of your Kick settings
page, set the callback URL to 

http://example.com/complete/kick/

replacing 

example.com

 with your domain.

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_KICK_KEY

=

&#39;&#39;

SOCIAL_AUTH_KICK_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_KICK_SCOPE

=

[

...

]

Further documentation at 
Developer Guide
.