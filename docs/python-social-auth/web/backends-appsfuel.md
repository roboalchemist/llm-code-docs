# Backends/Appsfuel

Source: https://python-social-auth.readthedocs.io/en/latest/backends/appsfuel.html

Appsfuel
¶

Appsfuel uses OAuth v2 for Authentication check the 
official docs
 too.

Sign up at the 
Appsfuel Developer Program

Create and verify a new app

On the dashboard click on 
Show API keys

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_APPSFUEL_KEY

=

&#39;&lt;App UID&gt;&#39;

SOCIAL_AUTH_APPSFUEL_SECRET

=

&#39;&lt;App secret&gt;&#39;

Appsfuel gives you the chance to integrate with 
Live
 or 
Sandbox
 env.

Appsfuel Live
¶

Add ‘social_core.backends.contrib.appsfuel.AppsfuelBackend’ into your

AUTHENTICATION_BACKENDS

.

Then you can start using 

{%

url

social:begin

'appsfuel'

%}

 in your
templates

Appsfuel Sandbox
¶

Add 

'social_core.backends.appsfuel.AppsfuelOAuth2Sandbox'

 into your

AUTHENTICATION_BACKENDS

.

Then you can start using 

{%

url

social:begin

'appsfuel-sandbox'

%}

 in
your templates

Define the settings:

SOCIAL_AUTH_APPSFUEL_SANDBOX_KEY

=

&#39;&lt;App UID&gt;&#39;

SOCIAL_AUTH_APPSFUEL_SANDBOX_SECRET

=

&#39;&lt;App secret&gt;&#39;