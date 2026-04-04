# Backends/Flat

Source: https://python-social-auth.readthedocs.io/en/latest/backends/flat.html

Flat
¶

Flat
 uses OAuth2. In order to enable the backend follow:

On your project settings, you should add Flat on your

AUTHENTICATION_BACKENDS

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.flat.FlatOAuth2&#39;

,

)

Register an application at 
Flat Developer Portal

Fill in the 
Client Id
 and 
Client Secret
 values in your settings:

SOCIAL_AUTH_FLAT_KEY

=

&#39;&#39;

SOCIAL_AUTH_FLAT_SECRET

=

&#39;&#39;

Set the 

Callback

URL

 to 

http://&lt;your

hostname&gt;/complete/flat/

Specify 
scopes
 with:

SOCIAL_AUTH_FLAT_SCOPE

=

[

...

]