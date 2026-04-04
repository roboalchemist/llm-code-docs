# Backends/Mendeley

Source: https://python-social-auth.readthedocs.io/en/latest/backends/mendeley.html

Mendeley
¶

Mendeley supports OAuth1 and OAuth2, they are in the process of deprecating
OAuth1 API (which should be fully deprecated on April 2014, check their

announcement
).

OAuth1
¶

In order to support OAuth1 (not recommended, use OAuth2 instead):

Register a new application at 
Mendeley Application Registration

Fill 
Consumer Key
 and 
Consumer Secret
 values:

SOCIAL_AUTH_MENDELEY_KEY

=

&#39;&#39;

SOCIAL_AUTH_MENDELEY_SECRET

=

&#39;&#39;

OAuth2
¶

In order to support OAuth2:

Register a new application at 
Mendeley Application Registration
, or
migrate your OAuth1 application, check their 
migration steps here
.

Fill 
Application ID
 and 
Application Secret
 values:

SOCIAL_AUTH_MENDELEY_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_MENDELEY_OAUTH2_SECRET

=

&#39;&#39;