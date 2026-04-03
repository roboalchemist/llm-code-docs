# Backends/Dribbble

Source: https://python-social-auth.readthedocs.io/en/latest/backends/dribbble.html

Dribbble
¶

Dribbble

Register a new application at 
Dribbble
, set the callback URL
to 

http://example.com/complete/dribbble/

 replacing

example.com

 with your domain.

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_DRIBBBLE_KEY

=

&#39;&#39;

SOCIAL_AUTH_DRIBBBLE_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_DRIBBBLE_SCOPE

=

[

...

]

See auth scopes at 
Dribbble Developer docs
.