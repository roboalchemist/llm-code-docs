# Backends/Stackoverflow

Source: https://python-social-auth.readthedocs.io/en/latest/backends/stackoverflow.html

Stackoverflow
¶

Stackoverflow uses OAuth 2.0

“Register For An App Key” at the 
Stack Exchange API
 site. Set your OAuth
domain and application website settings.

Add the 

Client

Id

, 

Client

Secret

 and 

API

Key

 values in settings:

SOCIAL_AUTH_STACKOVERFLOW_KEY

=

&#39;&#39;

SOCIAL_AUTH_STACKOVERFLOW_SECRET

=

&#39;&#39;

SOCIAL_AUTH_STACKOVERFLOW_API_KEY

=

&#39;&#39;

You can ask for extra permissions with:

SOCIAL_AUTH_STACKOVERFLOW_SCOPE

=

[

...

]