# Backends/Mediawiki

Source: https://python-social-auth.readthedocs.io/en/latest/backends/mediawiki.html

MediaWiki OAuth1 backend
¶

Usage
¶

In addition to the general setup you need to define the
following settings:

SOCIAL_AUTH_MEDIAWIKI_KEY

=

&lt;

consumer_key

&gt;

SOCIAL_AUTH_MEDIAWIKI_SECRET

=

&lt;

consumer_secret

&gt;

SOCIAL_AUTH_MEDIAWIKI_URL

=

&#39;https://meta.wikimedia.org/w/index.php&#39;

In the OAuth consumer registration you can choose the option to:

Allow consumer to specify a callback in requests
and use “callback” URL above as a required prefix

This is preferable. If your URL is 
https://myurl.org/
 use
the following option:

SOCIAL_AUTH_MEDIAWIKI_CALLBACK

=
 \

&#39;https://myurl.org/oauth/complete/mediawiki&#39;

But it is also possible to use:

SOCIAL_AUTH_MEDIAWIKI_CALLBACK

=

&#39;oob&#39;

General documentation
¶

https://www.mediawiki.org/wiki/Extension:OAuth

Developer documentation
¶

https://www.mediawiki.org/wiki/OAuth/For_Developers

Code based on
¶

https://github.com/mediawiki-utilities/python-mwoauth