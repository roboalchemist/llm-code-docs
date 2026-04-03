# Backends/Azuread

Source: https://python-social-auth.readthedocs.io/en/latest/backends/azuread.html

Microsoft Azure Active Directory
¶

IdP Setup
¶

To configure Azure AD:

Log into the Azure Portal

Navigate to 
Azure Active Directory
 &gt; 
App registrations
 &gt; 
New registration

Configure:

Name
: Your application name

Redirect URI
: Select 
Web
 and enter 

https://your-domain.com/complete/azuread-oauth2/

After registration, note the 
Application (client) ID
 and 
Directory (tenant) ID

Create a client secret:

Go to 
Certificates &amp; secrets
 &gt; 
New client secret

Copy the secret value immediately (you won’t be able to see it again)

Configure API Permissions:

Go to 
API permissions
 &gt; 
Add a permission
 &gt; 
Microsoft Graph

Add delegated permissions: 

User.Read

, 

email

, 

openid

, 

profile

Click 
Grant admin consent
 if required

Application Configuration
¶

Fill in 

Client

ID

 and 

Client

Secret

 settings with values from Azure AD:

SOCIAL_AUTH_AZUREAD_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_AZUREAD_OAUTH2_RESOURCE

=

&#39;&#39;

This is the resource you would like to access after authentication succeeds.
Some of the possible values are: 

https://graph.windows.net

 or

https://&lt;your

Sharepoint

site

name&gt;-my.sharepoint.com

.

When using Microsoft Graph, the resource needed is:

SOCIAL_AUTH_AZUREAD_OAUTH2_RESOURCE

=

&#39;https://graph.microsoft.com/&#39;

Add the backend to the authentication backends setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.azuread.AzureADOAuth2&#39;

,

...

)

If you are using an authority host other than the default 

AZURE_PUBLIC_CLOUD

 (

'login.microsoftonline.com'

)
then you can override the default with the  

AUTHORITY_HOST

 setting. A list of Azure authority hosts can be found
in the 
Azure Authority Hosts
 doc:

SOCIAL_AUTH_AZUREAD_OAUTH2_AUTHORITY_HOST

=

&#39;&#39;

Federated identity credentials (client assertions) are supported when you do not want to use a client secret. After
adding a federated credential to your Entra ID app, point the backend at the OIDC token that your workload issues
(for example, Kubernetes service account tokens issued via Azure Workload Identity, or other OIDC tokens where you manage
writing the token to a file). Precedence: if 

SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET

 is set, the backend uses the client
secret and does not send a client assertion; otherwise it prefers an explicit 

SOCIAL_AUTH_AZUREAD_OAUTH2_CLIENT_ASSERTION

;
if no assertion is provided, it reads a token file from 

AZURE_FEDERATED_TOKEN_FILE

 (or 

OAUTH2_FIC_TOKEN_FILE

) or

SOCIAL_AUTH_AZUREAD_OAUTH2_FEDERATED_TOKEN_FILE

. The backend will automatically use a client assertion instead of

CLIENT_SECRET

 when the secret is omitted.

Default path used by Azure Workload Identity on Kubernetes:

AZURE_FEDERATED_TOKEN_FILE

=/

var

/

run

/

secrets

/

azure

/

tokens

/

azure

-

identity

-

token

Or configure explicitly via the backend setting:

SOCIAL_AUTH_AZUREAD_OAUTH2_FEDERATED_TOKEN_FILE

=

&#39;/path/to/oidc/token&#39;

You can also provide a pre-built client assertion JWT (preferred when you already create the assertion yourself):

SOCIAL_AUTH_AZUREAD_OAUTH2_CLIENT_ASSERTION

=

&#39;eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...&#39;

# Optional: defaults to the standard JWT bearer URN shown here

SOCIAL_AUTH_AZUREAD_OAUTH2_CLIENT_ASSERTION_TYPE

=

&#39;urn:ietf:params:oauth:client-assertion-type:jwt-bearer&#39;

Minimal configs by approach:

Token file (workload-issued OIDC token): leave 

SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET

 unset; set either

AZURE_FEDERATED_TOKEN_FILE

 (or 

OAUTH2_FIC_TOKEN_FILE

) or 

SOCIAL_AUTH_AZUREAD_OAUTH2_FEDERATED_TOKEN_FILE

to the token path. 

CLIENT_ASSERTION_TYPE

 is not needed for this mode.

Pre-built client assertion: leave 

SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET

 unset; set

SOCIAL_AUTH_AZUREAD_OAUTH2_CLIENT_ASSERTION

 (and optionally 

SOCIAL_AUTH_AZUREAD_OAUTH2_CLIENT_ASSERTION_TYPE

if you use a non-standard type). 

FEDERATED_TOKEN_FILE

 is not read in this mode because the explicit assertion wins.

Kubernetes projected service account token volume example:

apiVersion

:

v1

kind

:

Pod

metadata

:

name

:

mypod

spec

:

serviceAccountName

:

myserviceaccount

containers

:

-

name

:

mycontainer

image

:

myimage

env

:

-

name

:

AZURE_FEDERATED_TOKEN_FILE

value

:

/

var

/

run

/

secrets

/

azure

/

tokens

/

azure

-

identity

-

token

volumeMounts

:

-

name

:

azure

-

identity

-

token

mountPath

:

/

var

/

run

/

secrets

/

azure

/

tokens

readOnly

:

true

volumes

:

-

name

:

azure

-

identity

-

token

projected

:

sources

:

-

serviceAccountToken

:

path

:

azure

-

identity

-

token

audience

:

api

:

//

AzureADTokenExchange

expirationSeconds

:

3600

These settings apply to Azure AD/Entra ID scenarios. For more information on workload identity, see 
Workload Identity Federation
 and 
Federated identity credentials (Workload Identity)
.

Tenant Support
¶

If the app is linked to a specific tenant (vs the common tenant) it’s
possible to use a version of the backend with tenant support.

Note: The backends are split because of the needed cryptography dependencies which must be installed manually.

IdP Setup for Tenant
¶

Follow the same IdP setup steps from the ‘IdP Setup’ section above, but use redirect URI:

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

azuread

-

tenant

-

oauth2

/

Application Configuration for Tenant
¶

Fill in 

Client

ID

, 

Client

Secret

, and 

Tenant

ID

 settings:

SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_SECRET

=

&#39;&#39;

SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_TENANT_ID

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_RESOURCE

=

&#39;&#39;

This is the resource you would like to access after authentication succeeds.
Some of the possible values are: 

https://graph.windows.net

 or

https://&lt;your

Sharepoint

site

name&gt;-my.sharepoint.com

.

When using Microsoft Graph, the resource needed is:

SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_RESOURCE

=

&#39;https://graph.microsoft.com/&#39;

Add the backend to the authentication backends setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.azuread_tenant.AzureADTenantOAuth2&#39;

,

...

)

If you are using an authority host other than the default 

AZURE_PUBLIC_CLOUD

 (‘login.microsoftonline.com’)
then you can override the default with the  

AUTHORITY_HOST

 setting. The Azure authority hosts are listed
in the 
Azure Authority Hosts
 doc:

SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_AUTHORITY_HOST

=

&#39;&#39;

B2C Tenant
¶

If the app needs custom business logic for authentication then use the Azure AD B2C tenant.

To enable OAuth2 B2C Tenant support:

Fill in 

Client

ID

 and 

Client

Secret

 settings. These values can be
obtained easily as described in 
Azure AD Application Registration
 doc:

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_SECRET

=

&#39;&#39;

Fill in the tenant id:

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_TENANT_NAME

=

&#39;&#39;

Fill in the B2C policy:

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_POLICY

=

&#39;&#39;

The policy should start with 
b2c_
. For more information see 
Azure AD B2C User flows and custom policies overview
 doc.

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_RESOURCE

=

&#39;&#39;

This is the resource you would like to access after authentication succeeds.
Some of the possible values are: 

https://graph.windows.net

 or

https://&lt;your

Sharepoint

site

name&gt;-my.sharepoint.com

.

When using Microsoft Graph, the resource needed is:

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_RESOURCE

=

&#39;https://graph.microsoft.com/&#39;

Add the backend to the authentication backends setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.azuread_b2c.AzureADB2COAuth2&#39;

,

...

)

If you are using an authority host other than the default 

AZURE_PUBLIC_CLOUD

 (‘b2clogin.com’)
then you can override the default with the  

AUTHORITY_HOST

 setting.

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_AUTHORITY_HOST = ‘’