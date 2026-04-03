# Backends/Twitter

Source: https://python-social-auth.readthedocs.io/en/latest/backends/twitter.html

Twitter
¶

Twitter offers per application keys named 

Consumer

Key

 and 

Consumer

Secret

.
To enable Twitter these two keys are needed. Further documentation at

Twitter development resources
:

Register a new application at 
Twitter App Creation
,

Check the 
Allow this application to be used to Sign in with Twitter

checkbox. If you don’t check this box, Twitter will force your user to login
every time.

Fill 
Consumer Key
 and 
Consumer Secret
 values:

SOCIAL_AUTH_TWITTER_KEY

=

&#39;&#39;

SOCIAL_AUTH_TWITTER_SECRET

=

&#39;&#39;

You need to specify an URL callback or the OAuth will raise a “403 Client Error”.
The callback URL should be something like “
https://example.com/complete/twitter
”

You can request user’s Email address (consult 
Twitter verify
credentials
), the parameter is sent automatically, but the
application needs to be whitelisted in order to get a valid value.

You’ll need to apply for Elevated access via the Developer Portal, see 
Twitter access levels
 for more info.

Twitter usually fails with a 401 error when trying to call the request-token
URL, this is usually caused by server datetime errors (check miscellaneous
section). Installing 

ntp

 and syncing the server date with some pool does
the trick.