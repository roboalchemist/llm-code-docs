# Backends/Twitch

Source: https://python-social-auth.readthedocs.io/en/latest/backends/twitch.html

Twitch
¶

Twitch works similar to Facebook (OAuth).

Register a new application in the 
connections tab
 of your Twitch settings
page, set the callback URL to 

http://example.com/complete/twitch/

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

SOCIAL_AUTH_TWITCH_KEY

=

&#39;&#39;

SOCIAL_AUTH_TWITCH_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_TWITCH_SCOPE

=

[

...

]