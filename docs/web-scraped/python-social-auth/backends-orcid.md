# Backends/Orcid

Source: https://python-social-auth.readthedocs.io/en/latest/backends/orcid.html

ORCID
¶

ORCID
 uses OAuth 2 for authentication.

Register an ORCID account, go to 
Developer tools
, enable the public API,
create a new application, set the redirect URI to

http://example.com/complete/orcid/

 replacing 

example.com

 with your
domain.

Fill the 

Client

ID

 and 

Client

secret

 values from the app details in

Developer tools
 (you might need to press “Show details”) in the settings:

SOCIAL_AUTH_ORCID_KEY

=

&#39;&#39;

SOCIAL_AUTH_ORCID_SECRET

=

&#39;&#39;

Member API
¶

You can subscribe to gain access to an 
API with extended capabilities
.
Use 

'social_core.backends.orcid.ORCIDMemberOAuth2'

 class in your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.

Sandbox
¶

ORCID supports a sandbox mode for testing, there’s a custom backend for it
which name is 

orcid-sandbox

 instead of 

orcid

. Same settings apply
but use these instead:

SOCIAL_AUTH_ORCID_SANDBOX_KEY

=

&#39;&#39;

SOCIAL_AUTH_ORCID_SANDBOX_SECRET

=

&#39;&#39;

Sandbox is also available for Member API. You will have to register for with
ORCID it 
separately
.