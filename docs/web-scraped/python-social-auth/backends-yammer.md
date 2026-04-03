# Backends/Yammer

Source: https://python-social-auth.readthedocs.io/en/latest/backends/yammer.html

Yammer
¶

Yammer users OAuth2 for their auth mechanism, this application supports Yammer
OAuth2 in production and staging modes.

Production Mode
¶

In order to enable the backend, follow:

Register an application at 
Client Applications
,
set the 

Redirect

URI

 to 

http://&lt;your

hostname&gt;/complete/yammer/

Fill 
Client Key
 and 
Client Secret
 settings:

SOCIAL_AUTH_YAMMER_KEY

=

&#39;...&#39;

SOCIAL_AUTH_YAMMER_SECRET

=

&#39;...&#39;

Staging Mode
¶

Staging mode is configured the same as 

Production

Mode

, but settings are
prefixed with:

SOCIAL_AUTH_YAMMER_STAGING_

*