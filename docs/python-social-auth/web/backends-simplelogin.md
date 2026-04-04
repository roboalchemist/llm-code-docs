# Backends/Simplelogin

Source: https://python-social-auth.readthedocs.io/en/latest/backends/simplelogin.html

SimpleLogin
¶

SimpleLogin uses OAuth 2.0 for Authentication.

On your project settings, you should add SimpleLogin on your

AUTHENTICATION_BACKENDS

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.simplelogin.SimpleLoginOAuth2&#39;

,

)

Register a new app at 
SimpleLogin App
. By default, SimpleLogin whitelists

localhost

 so your app should work locally.
Please set the callback URL to 

http://example.com/complete/simplelogin/

replacing 

example.com

 with your domain when you deploy your web app to
production.

Add these values of 

Client

ID

 and 

Client

Secret

 from SimpleLogin in
your project settings file.

The 

Client

ID

 should be added on 

SOCIAL_AUTH_SIMPLELOGIN_KEY

 and the

Client

Secret

 should be added on 

SOCIAL_AUTH_SIMPLELOGIN_SECRET

:

SOCIAL_AUTH_SIMPLELOGIN_KEY

=

&#39;client-id&#39;

SOCIAL_AUTH_SIMPLELOGIN_SECRET

=

&#39;very-secret&#39;