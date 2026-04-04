# Backends/Changetip

Source: https://python-social-auth.readthedocs.io/en/latest/backends/changetip.html

ChangeTip
¶

ChangeTip

Register a new application at 
ChangeTip
, set the callback URL to

http://example.com/complete/changetip/

 replacing 

example.com

 with your
domain.

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_CHANGETIP_KEY

=

&#39;&#39;

SOCIAL_AUTH_CHANGETIP_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_CHANGETIP_SCOPE

=

[

...

]

See auth scopes at 
ChangeTip OAuth docs
.