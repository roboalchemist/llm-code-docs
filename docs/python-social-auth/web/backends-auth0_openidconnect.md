# Backends/Auth0_Openidconnect

Source: https://python-social-auth.readthedocs.io/en/latest/backends/auth0_openidconnect.html

Auth0 OpenID Connect
¶

Auth0 OpenID Connect (OIDC) implementation. Separate from
the previous 

Auth0OAuth2

 backend, as it builds on the base
OIDC backend.

IdP Setup
¶

To configure Auth0:

Log into your Auth0 Dashboard

Navigate to 
Applications
 &gt; 
Create Application

Select 
Regular Web Applications

In the application settings, configure:

Allowed Callback URLs
: 

https://your-domain.com/complete/auth0-openidconnect/

Allowed Logout URLs
: 

https://your-domain.com/logout/

 (if using logout)

Allowed Web Origins
: 

https://your-domain.com

Note the 
Domain
 (e.g., 

mytenant.auth0.com

), 
Client ID
, and 
Client Secret

Application Configuration
¶

Use the values from your Auth0 application:

SOCIAL_AUTH_AUTH0_OPENIDCONNECT_DOMAIN

=

&#39;mytenant.auth0.com&#39;

SOCIAL_AUTH_AUTH0_OPENIDCONNECT_KEY

=

&#39;&lt;client_id&gt;&#39;

SOCIAL_AUTH_AUTH0_OPENIDCONNECT_SECRET

=

&#39;&lt;client_secret&gt;&#39;

Scopes
¶

The default scope is 

[&quot;openid&quot;,

&quot;profile&quot;,

&quot;email&quot;]

. In order to support
refresh tokens/long-lived logins, you may want to add the 

offline_access

 scope:

SOCIAL_AUTH_AUTH0_OPENIDCONNECT_SCOPE

=

&#39;openid profile email offline_access&#39;