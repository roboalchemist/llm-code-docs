# Backends/Gitea

Source: https://python-social-auth.readthedocs.io/en/latest/backends/gitea.html

Gitea
¶

Gitea supports OAuth2 protocol.

Register a new application at 
Gitea Applications
.

Set the callback URL to 

http://example.com/complete/gitea/

replacing 

example.com

 with your domain. Drop the trailing slash
if the project doesn’t use it, the URL 
must
 match the value sent.

Fill the 

Client

ID

 and 

Client

Secret

 values from Gitea in the settings:

SOCIAL_AUTH_GITEA_KEY

=

&#39;&#39;

SOCIAL_AUTH_GITEA_SECRET

=

&#39;&#39;

If your Gitea setup resides in another domain, then add the following setting:

SOCIAL_AUTH_GITEA_API_URL

=

&#39;https://example.com&#39;

it must be the 
full url
 to your Gitea setup.