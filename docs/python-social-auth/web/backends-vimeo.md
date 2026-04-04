# Backends/Vimeo

Source: https://python-social-auth.readthedocs.io/en/latest/backends/vimeo.html

Vimeo
¶

Vimeo uses OAuth1 to grant access to their API. In order to get the backend
running follow:

Register an application at 
Vimeo Developer Portal
 filling the required
settings. Ensure to fill 

App

Callback

URL

 field with

http://&lt;your

hostname&gt;/complete/vimeo/

Fill in the 
Client Id
 and 
Client Secret
 values in your settings:

SOCIAL_AUTH_VIMEO_KEY

=

&#39;&#39;

SOCIAL_AUTH_VIMEO_SECRET

=

&#39;&#39;

Specify scopes with:

SOCIAL_AUTH_VIMEO_SCOPE

=

[

...

]

Add the backend to 

AUTHENTICATION_BACKENDS

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.vimeo.VimeoOAuth1&#39;

,

...

)