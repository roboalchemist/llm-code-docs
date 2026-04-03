# Backends/Reddit

Source: https://python-social-auth.readthedocs.io/en/latest/backends/reddit.html

Reddit
¶

Reddit implements 
OAuth2 authentication workflow
. To enable it, just follow:

Register an application at 
Reddit Preferences Apps

Fill the 
Consumer Key
 and 
Consumer Secret
 values in your settings:

SOCIAL_AUTH_REDDIT_KEY

=

&#39;&#39;

SOCIAL_AUTH_REDDIT_SECRET

=

&#39;&#39;

By default the token is not permanent, it will last an hour. To get
a refresh token just define:

SOCIAL_AUTH_REDDIT_AUTH_EXTRA_ARGUMENTS

=

{

&#39;duration&#39;

:

&#39;permanent&#39;

}

This will store the 

refresh_token

 in 

UserSocialAuth.extra_data

attribute, to refresh the access token just do:

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

&#39;reddit&#39;

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

&#39;reddit&#39;

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

,

redirect_uri

=

&#39;http://localhost:8000/complete/reddit/&#39;

)

Reddit requires 

redirect_uri

 when refreshing the token and it must be the
same value used during the auth process.