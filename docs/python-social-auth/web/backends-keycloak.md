# Backends/Keycloak

Source: https://python-social-auth.readthedocs.io/en/latest/backends/keycloak.html

Keycloak - Open Source Red Hat SSO
¶

Keycloak is an open source IAM and SSO system.

IdP Setup
¶

To configure Keycloak:

Log into your Keycloak Admin Console and select your Realm

Navigate to 
Clients
 &gt; 
Create

Configure the client:

Client ID
: Choose a meaningful name (e.g., 

django-app

)

Client Protocol
: 

openid-connect

Access Type
: 

confidential

Valid Redirect URIs
: 

https://your-domain.com/complete/keycloak/

Save and go to the 
Credentials
 tab to get the 
Client Secret

Under 
Fine Grain OpenID Connect Configuration
 (found in the client’s Settings or Advanced Settings tab; location may vary depending on Keycloak version), set:

User Info Signed Response Algorithm
: 

RS256

Request Object Signature Algorithm
: 

RS256

Get the public key from 
Realm Settings
 &gt; 
Keys
 &gt; 
RS256

Create an 
Audience Mapper
 (
Mappers
 &gt; 
Create
) to ensure your 

client_id

 is in the JWT’s 

aud

 claim

Note the 
Authorization URL
 and 
Token URL
 from the Realm OpenID Endpoint Configuration

Application Configuration
¶

Add Keycloak to your 

AUTHENTICATION_BACKENDS

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.keycloak.KeycloakOAuth2&#39;

,

&#39;django.contrib.auth.backends.ModelBackend&#39;

,

)

Configure with values from your Keycloak client:

SOCIAL_AUTH_KEYCLOAK_KEY

=

&#39;test-django-oidc&#39;

SOCIAL_AUTH_KEYCLOAK_SECRET

=

&#39;a7a41-245e-...&#39;

SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY

=
 \

&#39;MIIBIjANBxxxdSD&#39;

SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL

=
 \

&#39;https://iam.example.com/auth/realms/voxcloud-staff/protocol/openid-connect/auth&#39;

SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL

=
 \

&#39;https://iam.example.com/auth/realms/voxcloud-staff/protocol/openid-connect/token&#39;

User ID Configuration
¶

The default behavior is to associate users via the 

sub

 (subject) field from the
JWT token. However, you can configure which field to use as the unique user identifier
by setting:

SOCIAL_AUTH_KEYCLOAK_ID_KEY

=

&#39;email&#39;

This can be useful if you want to use email, username, or another field as the unique
identifier instead of the 

sub

 field.

Warning

Changing the ID key after users have already authenticated will prevent them from
logging in, as their stored 

uid

 will not match the new identifier. Configure
this setting before users start authenticating, or perform a data migration.

See the 
Configurable User ID Key
 documentation for more information about this feature.