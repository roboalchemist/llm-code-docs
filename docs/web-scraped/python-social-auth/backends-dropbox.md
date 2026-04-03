# Backends/Dropbox

Source: https://python-social-auth.readthedocs.io/en/latest/backends/dropbox.html

Dropbox
¶

Dropbox supports both OAuth 1 and 2.

Register a new application at 
Dropbox Developers
, and follow the
instructions below for the version of OAuth for which you are adding
support.

OAuth2 Api V2
¶

Add the Dropbox OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social.backends.dropbox.DropboxOAuth2V2&#39;

,

...

)

Fill 

App

Key

 and 

App

Secret

 values in the settings:

SOCIAL_AUTH_DROPBOX_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET

=

&#39;&#39;

OAuth1
¶

Deprecated since version V1: 
api is deprecated. 
https://blogs.dropbox.com/developers/2016/06/api-v1-deprecated/

Add the Dropbox OAuth backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.dropbox.DropboxOAuth&#39;

,

...

)

Fill 

App

Key

 and 

App

Secret

 values in the settings:

SOCIAL_AUTH_DROPBOX_KEY

=

&#39;&#39;

SOCIAL_AUTH_DROPBOX_SECRET

=

&#39;&#39;

OAuth2
¶

Deprecated since version V1: 
api is deprecated. 
https://blogs.dropbox.com/developers/2016/06/api-v1-deprecated/

Add the Dropbox OAuth2 backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.dropbox.DropboxOAuth2&#39;

,

...

)

Fill 

App

Key

 and 

App

Secret

 values in the settings:

SOCIAL_AUTH_DROPBOX_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET

=

&#39;&#39;