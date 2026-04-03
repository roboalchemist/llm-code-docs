# Backends/Oidc

Source: https://python-social-auth.readthedocs.io/en/latest/backends/oidc.html

OIDC (OpenID Connect)
¶

The 
OIDC
 backend allows authentication against a generic OIDC provider.
The backend class is 
OpenIdConnectAuth
 with name 
oidc
.  A minimum
configuration is:

SOCIAL_AUTH_OIDC_OIDC_ENDPOINT

=

&#39;https://.....&#39;

SOCIAL_AUTH_OIDC_KEY

=

&#39;&lt;client_id&gt;&#39;

SOCIAL_AUTH_OIDC_SECRET

=

&#39;&lt;client_secret&gt;&#39;

The remaining configuration will be auto-detected, by fetching:

&lt;

SOCIAL_AUTH_OIDC_OIDC_ENDPOINT

&gt;/.

well

-

known

/

openid

-

configuration

This class can be used standalone, but is also the base class for some other
backends.

IdP Setup
¶

To configure your OIDC Identity Provider for use with this backend:

Create a new application/client in your IdP with type “Web Application”

Set the 
Redirect URI
 (also called Callback URL) to:

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

oidc

/

Replace 

your-domain.com

 with your actual application domain.

Configure scopes to include at minimum: 

openid

, 

profile

, 

email

Note the generated 
Client ID
 and 
Client Secret
 for use in your Django settings

Ensure your IdP exposes the OpenID Connect discovery endpoint at: 

https://your-idp-domain/.well-known/openid-configuration

Note

For development, you can use 

http://localhost:8000/complete/oidc/

 as the redirect URI.

Authentication Request Parameters
¶

All this parameters are optional and they might not be supported by the OIDC provider.

Prompt
¶

This informs the OIDC provider whether the OIDC provider prompts the user for reauthentication and consent.

SOCIAL_AUTH_OIDC_PROMPT

=

&#39;&lt;prompt&gt; ...&#39;

Defined values are

none

login

consent

select_account

Username
¶

The 
OIDC
 backend will check for a 

preferred_username

 key in the values
returned by the server.  If the username is under a different key, this can
be overridden:

SOCIAL_AUTH_OIDC_USERNAME_KEY

=

&#39;nickname&#39;

This setting indicates that the username should be populated by the

nickname

 claim instead.

Scopes
¶

The default set of scopes requested are “openid”, “profile” and “email”.
You can request additional claims, for example:

SOCIAL_AUTH_OIDC_SCOPE

=

[

&#39;groups&#39;

]

and you can prevent the inclusion of the default scopes using:

SOCIAL_AUTH_OIDC_IGNORE_DEFAULT_SCOPE

=

True