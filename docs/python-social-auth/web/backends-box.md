# Backends/Box

Source: https://python-social-auth.readthedocs.io/en/latest/backends/box.html

Box.net
¶

Box works similar to Facebook (OAuth2).

Register an application at 
Manage Box Applications

Fill the 
Consumer Key
 and 
Consumer Secret
 values in your settings:

SOCIAL_AUTH_BOX_KEY

=

&#39;&#39;

SOCIAL_AUTH_BOX_SECRET

=

&#39;&#39;

By default the token is not permanent, it will last an hour. To refresh the
access token just do:

from

social_django.utils

import

load_strategy

strategy

=

load_strategy

(

backend

=

&#39;box&#39;

)

user

=

User

.

objects

.

get

(

pk

=

foo

)

social

=

user

.

social_auth

.

filter

(

provider

=

&#39;box&#39;

)[

0

]

social

.

refresh_token

(

strategy

=

strategy

)