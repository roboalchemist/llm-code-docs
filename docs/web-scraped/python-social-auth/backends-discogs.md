# Backends/Discogs

Source: https://python-social-auth.readthedocs.io/en/latest/backends/discogs.html

Discogs
¶

Discogs uses OAuth v1 for Authentication.

Register a new application int the 
Discogs API settings
, and

Add the Discogs backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&quot;social_core.backends.discogs.DiscogsOAuth1&quot;

,

...

)

Add the 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_DISCOGS_KEY

=

&#39;&#39;

SOCIAL_AUTH_DISCOGS_SECRET

=

&#39;&#39;

Check 
Discogs API documentation
 for details.