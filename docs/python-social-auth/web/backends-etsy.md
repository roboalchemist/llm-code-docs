# Backends/Etsy

Source: https://python-social-auth.readthedocs.io/en/latest/backends/etsy.html

Etsy OAuth2
¶

Etsy supports the 
OAuth 2.0
 protocol using Authorization code with 
Proof Key for Code Exchange (PKCE)
 flow.

Configuration
¶

Register a new 
Application Link
 in your Etsy Account.

Fill 
Client ID
 in 

SOCIAL_AUTH_ETSY_OAUTH2_KEY

 in your project settings:

SOCIAL_AUTH_ETSY_OAUTH2_KEY

=

&quot;...&quot;

Note: 
Client Secret
 isn’t required via this flow.

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&quot;social_core.backends.etsy.EtsyOAuth2&quot;

,

...

)

Extra Configuration
¶

You can specify the scope that your application requires:

SOCIAL_AUTH_ETSY_OAUTH2_SCOPE

=

[

&quot;shops_r&quot;

,

&quot;shops_w&quot;

,

...

]

You can see all possible values at 
Etsy OAuth 2.0 provider API Scopes
.

You can specify PKCE challenge method:

SOCIAL_AUTH_ETSY_OAUTH2_PKCE_CODE_CHALLENGE_METHOD

=

&#39;...&#39;

The possible value for this is only 

S256

 which is set by default.

You can see more information about PKCE at 
RFC7636
.