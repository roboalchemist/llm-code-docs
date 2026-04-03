# Backends/Moves

Source: https://python-social-auth.readthedocs.io/en/latest/backends/moves.html

Moves
¶

Moves
 provides an OAuth2 authentication flow. In order to enable it:

Register an application at 
Manage Your Apps
, remember to fill the

Redirect

URI

 once the application was created.

Fill 
Client ID
 and 
Client secret
 in the settings:

SOCIAL_AUTH_MOVES_KEY

=

&#39;&#39;

SOCIAL_AUTH_MOVES_SECRET

=

&#39;&#39;

Define the mandatory scope for your application:

SOCIAL_AUTH_MOVES_SCOPE

=

[

&#39;activity&#39;

,

&#39;location&#39;

]

The scope parameter is required by 
Moves
 but the backend doesn’t set
a default one to minimize the application permissions request, so it’s
mandatory for the developer to define this setting.

Add the backend to the 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.moves.MovesOAuth2&#39;

,

...

)