# Backends/Nationbuilder

Source: https://python-social-auth.readthedocs.io/en/latest/backends/nationbuilder.html

NationBuilder
¶

NationBuilder supports OAuth2
 as their authentication mechanism. Follow these
steps in order to use it:

Register a new application at your 
Nation Admin panel
 (define the 
Callback
URL
 to 

http://example.com/complete/nationbuilder/

 where 

example.com

is your domain).

Fill the 

Client

ID

 and 

Client

Secret

 values from the newly created
application:

SOCIAL_AUTH_NATIONBUILDER_KEY

=

&#39;&#39;

SOCIAL_AUTH_NATIONBUILDER_SECRET

=

&#39;&#39;

Also define your NationBuilder slug:

SOCIAL_AUTH_NATIONBUILDER_SLUG

=

&#39;your-nationbuilder-slug&#39;

Enable the backend in 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.nationbuilder.NationBuilderOAuth2&#39;

...

)