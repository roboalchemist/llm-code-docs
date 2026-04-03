# Backends/Twitter_Oauth2

Source: https://python-social-auth.readthedocs.io/en/latest/backends/twitter_oauth2.html

Twitter API v2
¶

Twitter offers per application keys named 

Client

ID

 and 

Client

Secret

.
To enable Twitter these two keys are needed. Further documentation at

Twitter development resources
:

Register a new application at 
Twitter App Creation
,

Fill 
Client ID
 and 
Client Secret
 values:

SOCIAL_AUTH_TWITTER_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_TWITTER_OAUTH2_SECRET

=

&#39;&#39;

You can specify PKCE challenge method following:

SOCIAL_AUTH_TWITTER_OAUTH2_PKCE_CODE_CHALLENGE_METHOD

=

&#39;&#39;

The possible values for configuration are 

s256

 and 

plain

.
By default, 

s256

 is set.

You can see more information about PKCE at 
RFC7636
.

You need to specify an URL callback or the OAuth will raise a “403 Client Error”.
The callback URL should be something like “
https://example.com/complete/twitter-oauth2
”