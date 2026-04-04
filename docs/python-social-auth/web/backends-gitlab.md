# Backends/Gitlab

Source: https://python-social-auth.readthedocs.io/en/latest/backends/gitlab.html

GitLab
¶

GitLab supports OAuth2 protocol.

Register a new application at 
GitLab Applications
.

Set the callback URL to 

http://example.com/complete/gitlab/

replacing 

example.com

 with your domain. Drop the trailing slash
if the project doesn’t use it, the URL 
must
 match the value sent.

Ensure to mark the 

read_user

 scope. If marking 

api

 scope too, define:

SOCIAL_AUTH_GITLAB_SCOPE

=

[

&#39;api&#39;

]

Fill the 

Client

ID

 and 

Client

Secret

 values from GitLab in the settings:

SOCIAL_AUTH_GITLAB_KEY

=

&#39;&#39;

SOCIAL_AUTH_GITLAB_SECRET

=

&#39;&#39;

If your GitLab setup resides in another domain, then add the following setting:

SOCIAL_AUTH_GITLAB_API_URL

=

&#39;https://example.com&#39;

it must be the 
full url
 to your GitLab setup.