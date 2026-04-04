# Backends/Qiita

Source: https://python-social-auth.readthedocs.io/en/latest/backends/qiita.html

Qiita
¶

Qiita

Register a new application at 
Qiita
, set the callback URL to

http://example.com/complete/qiita/

 replacing 

example.com

 with your
domain.

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_QIITA_KEY

=

&#39;&#39;

SOCIAL_AUTH_QIITA_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_QIITA_SCOPE

=

[

...

]

See auth scopes at 
Qiita Scopes docs
.

Default behavior is to identify users by their 
id
. However, this can be changed by renaming accounts, etc.

If you want to identify each user with a unique 
permanent_id
, set the following:

SOCIAL_AUTH_QIITA_IDENTIFIED_BY_PERMANENT_ID

=

True