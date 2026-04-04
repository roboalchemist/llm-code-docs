# Backends/Udata

Source: https://python-social-auth.readthedocs.io/en/latest/backends/udata.html

Udata
¶

Datagouvfr OAuth2
¶

Datagouvfr
 supports OAuth2 for their API. In order to set it up:

Go get your 
your API key
 (previous account creation is required).

Fill 
Consumer Key
 and 
Consumer Secret
 values in settings:

SOCIAL_AUTH_DATAGOUVFR_KEY

=

&#39;&#39;

SOCIAL_AUTH_DATAGOUVFR_SECRET

=

&#39;&#39;

Add 

'social_core.backends.udata.DatagouvfrOAuth2'

 into your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.