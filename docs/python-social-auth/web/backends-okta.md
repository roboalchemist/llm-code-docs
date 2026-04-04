# Backends/Okta

Source: https://python-social-auth.readthedocs.io/en/latest/backends/okta.html

Okta
¶

This section describes how to setup the different services provided by Okta.

Okta OAuth2
¶

IdP Setup
¶

To configure Okta for OAuth2:

Log into your Okta Admin Console

Navigate to 
Applications
 &gt; 
Create App Integration

Select 
OIDC - OpenID Connect
 and 
Web Application

Set the 
Sign-in redirect URI
 to:

https

:

//

your

-

domain

.

com

/

complete

/

okta

-

oauth2

/

Save and note the 
Client ID
, 
Client Secret
, and 
Okta domain
 (e.g., 

https://dev-123456.okta.com

)

Important

Do NOT use the 

/oauth2/default

 endpoint for Okta authentication.

Application Configuration
¶

Fill 

Client

ID

, 

Client

Secret

 and 

API

URL

(e.g.

https://dev-123456.okta.com/oauth2)

 settings with the values from the IdP setup above:

SOCIAL_AUTH_OKTA_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_OKTA_OAUTH2_SECRET

=

&#39;&#39;

SOCIAL_AUTH_OKTA_OAUTH2_API_URL

=

&#39;&#39;

Okta OpenID Connect
¶

IdP Setup
¶

Follow the same steps as OAuth2 above, but use the redirect URI:

https

:

//

your

-

domain

.

com

/

complete

/

okta

-

openidconnect

/

Application Configuration
¶

Fill 

Client

ID

, 

Client

Secret

 and 

API

URL

(e.g.

https://dev-123456.okta.com/oauth2)

 settings with the values from the IdP setup:

SOCIAL_AUTH_OKTA_OPENIDCONNECT_KEY

=

&#39;&#39;

SOCIAL_AUTH_OKTA_OPENIDCONNECT_SECRET

=

&#39;&#39;

SOCIAL_AUTH_OKTA_OPENIDCONNECT_API_URL

=

&#39;&#39;