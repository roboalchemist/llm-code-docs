# Backends/Auth0

Source: https://python-social-auth.readthedocs.io/en/latest/backends/auth0.html

Auth0
¶

Auth0 OAuth2
¶

Auth0 provides OAuth2 authentication. This is the original 

Auth0OAuth2

 backend.

For a newer OpenID Connect implementation, see 

Auth0 OpenID Connect

.

Setup
¶

To enable Auth0 OAuth2 support:

Register your application at 
Auth0 Dashboard
 to get your Auth0 domain,
Client ID, and Client Secret.

Fill in the settings with your Auth0 domain, Client ID, and Client Secret:

SOCIAL_AUTH_AUTH0_KEY

=

&#39;&#39;

SOCIAL_AUTH_AUTH0_SECRET

=

&#39;&#39;

SOCIAL_AUTH_AUTH0_DOMAIN

=

&#39;yourdomain.auth0.com&#39;

Replace 

yourdomain

 with your Auth0 tenant domain.

Add the backend to your authentication backends:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.auth0.Auth0OAuth2&#39;

,

...

)

Scopes
¶

You can define custom scopes using the 

SOCIAL_AUTH_AUTH0_SCOPE

 setting:

SOCIAL_AUTH_AUTH0_SCOPE

=

[

&#39;openid&#39;

,

&#39;profile&#39;

,

&#39;email&#39;

]

The backend will handle JWT token validation and extract user details including
username, email, full name, and profile picture.