# Backends/Sketchfab

Source: https://python-social-auth.readthedocs.io/en/latest/backends/sketchfab.html

Sketchfab
¶

Sketchfab uses OAuth 2 for authentication.

To use:

Follow the steps at 
Sketchfab Oauth
, and ask for an

Authorization

code

 grant type.

Fill the 

Client

id/key

 and 

Client

Secret

 values you received
in your django settings:

SOCIAL_AUTH_SKETCHFAB_KEY

=

&#39;&#39;

SOCIAL_AUTH_SKETCHFAB_SECRET

=

&#39;&#39;