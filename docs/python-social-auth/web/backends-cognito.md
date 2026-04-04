# Backends/Cognito

Source: https://python-social-auth.readthedocs.io/en/latest/backends/cognito.html

Cognito
¶

Cognito implemented OAuth2 protocol for their authentication mechanism. To
enable 

python-social-auth

 support follow this steps:

Go to 
AWS Cognito Console
 and select 

Manage

User

Pools

.

Choose an existing pool or create a new one following the 
Cognito Pool
Tutorial
.

Create an app (make sure to generate a client secret) and configure a pool
domain (
Cognito App Configuration
):

SOCIAL_AUTH_COGNITO_KEY

=

&#39;...&#39;

SOCIAL_AUTH_COGNITO_SECRET

=

&#39;...&#39;

SOCIAL_AUTH_COGNITO_POOL_DOMAIN

=

&#39;...&#39;

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.cognito.CognitoOAuth2&#39;

,

...

)