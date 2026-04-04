# Backends/Mixcloud

Source: https://python-social-auth.readthedocs.io/en/latest/backends/mixcloud.html

Mixcloud OAuth2
¶

The 
Mixcloud API
 offers support for authorization. To this backend support:

Register a new application at 
Mixcloud Developers

Add Mixcloud backend to 

AUTHENTICATION_BACKENDS

 in settings:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.mixcloud.MixcloudOAuth2&#39;

,

)

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_MIXCLOUD_KEY

=

&#39;&#39;

SOCIAL_AUTH_MIXCLOUD_SECRET

=

&#39;&#39;

Similar to the other OAuth backends you can define:

SOCIAL_AUTH_MIXCLOUD_EXTRA_DATA

=

[(

&#39;username&#39;

,

&#39;username&#39;

),

(

&#39;name&#39;

,

&#39;name&#39;

),

(

&#39;pictures&#39;

,

&#39;pictures&#39;

),

(

&#39;url&#39;

,

&#39;url&#39;

)]

as a list of tuples 

(response

name,

alias)

 to store user profile data on
the 

UserSocialAuth.extra_data

.