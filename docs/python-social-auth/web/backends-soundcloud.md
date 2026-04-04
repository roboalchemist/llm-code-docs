# Backends/Soundcloud

Source: https://python-social-auth.readthedocs.io/en/latest/backends/soundcloud.html

SoundCloud
¶

SoundCloud uses OAuth2 for its auth mechanism.

Register a new application at 
SoundCloud App Registration
, set your
application name, website and redirect URI.

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_SOUNDCLOUD_KEY

=

&#39;&#39;

SOCIAL_AUTH_SOUNDCLOUD_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_SOUNDCLOUD_SCOPE

=

[

...

]

Possible scope values are 
*
 or 
non-expiring
 according to their 
/connect
documentation
.

Check the rest of their doc at 
SoundCloud Developer Documentation
.