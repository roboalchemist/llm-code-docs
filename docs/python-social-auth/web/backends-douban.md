# Backends/Douban

Source: https://python-social-auth.readthedocs.io/en/latest/backends/douban.html

Douban
¶

Douban supports OAuth 1 and 2.

Douban OAuth1
¶

Douban OAuth 1 works similar to Twitter OAuth.

Douban offers per application keys named 

Consumer

Key

 and 

Consumer

Secret

. To enable Douban OAuth these two keys are needed. Further
documentation at 
Douban Services &amp; API
:

Register a new application at 
Douban API Key
, make sure to mark the 
web
application
 checkbox.

Fill 
Consumer Key
 and 
Consumer Secret
 values in settings:

SOCIAL_AUTH_DOUBAN_KEY

=

&#39;&#39;

SOCIAL_AUTH_DOUBAN_SECRET

=

&#39;&#39;

Add 

'social_core.backends.douban.DoubanOAuth'

 into your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.

Douban OAuth2
¶

Recently Douban launched their OAuth2 support and the new developer site, you
can find documentation at 
Douban Developers
. To setup OAuth2 follow:

Register a new application at 
Create A Douban App
, make sure to mark the

web application
 checkbox.

Fill 
Consumer Key
 and 
Consumer Secret
 values in settings:

SOCIAL_AUTH_DOUBAN_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_DOUBAN_OAUTH2_SECRET

=

&#39;&#39;

Add 

'social_core.backends.douban.DoubanOAuth2'

 into your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.