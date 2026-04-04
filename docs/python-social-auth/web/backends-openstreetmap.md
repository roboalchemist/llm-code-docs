# Backends/Openstreetmap

Source: https://python-social-auth.readthedocs.io/en/latest/backends/openstreetmap.html

OpenStreetMap (Legacy OAuth 1.0a)
¶

Note: OAuth 1.0(a) support will be sunset in Summer 2024. Please use OAuth 2.0 instead.

OpenStreetMap supports OAuth 1.0 and 1.0a but 1.0a should be used for the new
applications, as 1.0 is for support of legacy clients only.

Access tokens currently do not expire automatically.

More documentation at 
OpenStreetMap Wiki
:

Login to your account

Register your application as OAuth consumer on your 
OpenStreetMap user settings page
, and

Set 

App

Key

 and 

App

Secret

 values in the settings:

SOCIAL_AUTH_OPENSTREETMAP_KEY

=

&#39;&#39;

SOCIAL_AUTH_OPENSTREETMAP_SECRET

=

&#39;&#39;