# Backends/Bitbucket_Datacenter_Oauth2

Source: https://python-social-auth.readthedocs.io/en/latest/backends/bitbucket_datacenter_oauth2.html

Bitbucket Data Center OAuth2
¶

Bitbucket Data Center (previously Bitbucket Server) supports the 
OAuth 2.0
 protocol. It supports two types of OAuth 2.0 flows:

Authorization code with 
Proof Key for Code Exchange (PKCE)

Authorization code

Configuration
¶

Register a new 
Application Link
 in your Bitbucket Data Center instance.

Provide the host URL of your Bitbucket Data Center instance:

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_URL

=

&quot;https://my-bitbucket-server.acme.com&quot;

Fill 
Client ID
 in 

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_KEY

 and 
Client Secret
 in 

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_SECRET

 in your project settings:

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_KEY

=

&quot;...&quot;

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_SECRET

=

&quot;...&quot;

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&quot;social_core.backends.bitbucket_datacenter.BitbucketDataCenterOAuth2&quot;

,

...

)

Extra Configuration
¶

You can specify the scope that your application requires:

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_SCOPE

=

[

&quot;PUBLIC_REPOS&quot;

]

You can see all possible values at 
Bitbucket Data Center OAuth 2.0 provider API
. By default, 

PUBLIC_REPOS

 is set.

You can choose to disable PKCE:

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_USE_PKCE

=

False

By default, 
True
 is set.

You can specify PKCE challenge method:

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_PKCE_CODE_CHALLENGE_METHOD

=

&#39;...&#39;

The possible values for this are 

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

You can specify the user’s avatar size:

SOCIAL_AUTH_BITBUCKET_DATACENTER_OAUTH2_USER_AVATAR_SIZE

=

48

This is the size of the user’s avatar requested from the API which is stored in 

EXTRA_DATA[&quot;avatar_url&quot;]

. By default, 

48

 is set.