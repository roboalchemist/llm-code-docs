# Backends/Eveonline

Source: https://python-social-auth.readthedocs.io/en/latest/backends/eveonline.html

EVE Online Single Sign-On (SSO)
¶

The EVE Single Sign-On (SSO) works similar to GitHub (OAuth2).

Register a new application at 
EVE Developers
, set the callback URL to

http://example.com/complete/eveonline/

 replacing 

example.com

 with your
domain.

Fill the 

Client

ID

 and 

Secret

Key

 values from EVE Developers in the settings:

SOCIAL_AUTH_EVEONLINE_KEY

=

&#39;&#39;

SOCIAL_AUTH_EVEONLINE_SECRET

=

&#39;&#39;

If you want to use EVE Character names as user names, use this setting:

SOCIAL_AUTH_CLEAN_USERNAMES

=

False

If you want to access EVE Online’s CREST API, use:

SOCIAL_AUTH_EVEONLINE_SCOPE

=

[

&#39;publicData&#39;

]