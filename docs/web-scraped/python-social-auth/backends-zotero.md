# Backends/Zotero

Source: https://python-social-auth.readthedocs.io/en/latest/backends/zotero.html

Zotero
¶

Zotero implements OAuth1 as their authentication mechanism for their Web API v3.

Go to the 
Zotero app registration page
 to register your application.

Fill the 
Client ID
 and 
Client Secret
 in your project settings:

SOCIAL_AUTH_ZOTERO_KEY

=

&#39;...&#39;

SOCIAL_AUTH_ZOTERO_SECRET

=

&#39;...&#39;

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.zotero.ZoteroOAuth&#39;

,

...

)

Further documentation at 
Zotero Web API v3 page
.