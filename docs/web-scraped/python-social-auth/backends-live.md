# Backends/Live

Source: https://python-social-auth.readthedocs.io/en/latest/backends/live.html

MSN Live Connect
¶

Live uses OAuth2 for its connect workflow, notice that it isn’t OAuth WRAP.

Register a new application at 
Live Connect Developer Center
, set your site
domain as redirect domain,

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_LIVE_KEY

=

&#39;&#39;

SOCIAL_AUTH_LIVE_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_LIVE_SCOPE

=

[

...

]

Defaults are 

wl.basic

 and 

wl.emails

. Latter one is necessary to
retrieve user email.

Ensure to have a valid 

Redirect

URL

 (

http://your-domain/complete/live

)
defined in the application if 

Enhanced

security

redirection

 is enabled.