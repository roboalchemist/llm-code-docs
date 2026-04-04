# Backends/Behance

Source: https://python-social-auth.readthedocs.io/en/latest/backends/behance.html

Behance
¶

DEPRECATED NOTICE
¶

NOTE:
 IT SEEMS THAT BEHANCE HAS DROPPED THEIR OAUTH2 SUPPORT WITHOUT MUCH
NOTICE BESIDE A 
BLOG POST
 ON SEPTEMBER 2014 MENTIONING THAT IT WILL BE
INTRODUCED “SOON”. THIS BACKEND IS IN DEPRECATED STATE FOR NOW.

Behance uses OAuth2 for its auth mechanism.

Register a new application at 
Behance App Registration
, set your
application name, website and redirect URI.

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_BEHANCE_KEY

=

&#39;&#39;

SOCIAL_AUTH_BEHANCE_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_BEHANCE_SCOPE

=

[

...

]

Check available permissions at 
Possible Scopes
. Also check the rest of their
doc at 
Behance Developer Documentation
.