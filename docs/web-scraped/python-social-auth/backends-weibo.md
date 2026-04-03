# Backends/Weibo

Source: https://python-social-auth.readthedocs.io/en/latest/backends/weibo.html

Weibo OAuth
¶

Weibo OAuth 2.0 workflow.

Register a new application at 
Weibo
.

Fill 

Consumer

Key

 and 

Consumer

Secret

 values in the settings:

SOCIAL_AUTH_WEIBO_KEY

=

&#39;&#39;

SOCIAL_AUTH_WEIBO_SECRET

=

&#39;&#39;

By default 

account

id

, 

profile_image_url

 and 

gender

 are stored in
extra_data field.

The user name is used by default to build the user instance 

username

,
sometimes this contains non-ASCII characters which might not be desirable for
the website. To avoid this issue it’s possible to use the Weibo 

domain

which will be inside the ASCII range by defining this setting:

SOCIAL_AUTH_WEIBO_DOMAIN_AS_USERNAME

=

True