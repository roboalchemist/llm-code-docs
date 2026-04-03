# Configuration/Porting_From_Dsa

Source: https://python-social-auth.readthedocs.io/en/latest/configuration/porting_from_dsa.html

Porting from django-social-auth
¶

Being a derivative work from 
django-social-auth
, porting from it to

python-social-auth
 should be an easy task. Porting to others libraries usually
is a pain, I’m trying to make this as easy as possible.

Installed apps
¶

On 
django-social-auth
 there was a single application to add into

INSTALLED_APPS

 plus a setting to define which ORM to be used (default or
MongoEngine). Now the apps are split and there’s not need for that extra
setting.

When using the default ORM:

INSTALLED_APPS

=

(

...

&#39;social_django&#39;

,

...

)

And when using MongoEngine:

INSTALLED_APPS

=

(

...

&#39;social_django_mongoengine&#39;

,

...

)

The models table names were defined to be compatible with those used on

django-social-auth
, so data is not needed to be migrated.

URLs
¶

The URLs are namespaced, you can chose your namespace, the 
example app
 uses
the 

social

 namespace. Replace the old include with:

urlpatterns

=

patterns

(

&#39;&#39;

,

...

url

(

&#39;&#39;

,

include

(

&#39;social_django.urls&#39;

,

namespace

=

&#39;social&#39;

))

...

)

On templates use a namespaced URL:

{

%

url

&#39;social:begin&#39;

&quot;google-oauth2&quot;

%

}

Account disconnection URL would be:

{

%

url

&#39;social:disconnect_individual&#39;

provider

,

id

%

}

Porting settings
¶

All 
python-social-auth
 settings are prefixed with 

SOCIAL_AUTH_

, except for
some exception on Django framework, 

AUTHENTICATION_BACKENDS

 remains the
same for obvious reasons.

All backends settings have the backend name included in the name, all uppercase
and with dashes replaced with underscores. For example, the Google OAuth2
backend is named 

google-oauth2

, so setting names related to that backend
should start with 

SOCIAL_AUTH_GOOGLE_OAUTH2_

.

Keys and secrets are some mandatory settings needed for OAuth providers; to
keep consistency the names follow the same naming convention: 

*_KEY

 for the
application key, and 

*_SECRET

 for the secret. OAuth1 backends used to have

CONSUMER

 in the setting name but not anymore. Following with the Google
OAuth2 example:

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

=

&#39;...&#39;

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

=

&#39;...&#39;

Remember that the name of the backend is needed in the settings, and names
differ a little from backend to backend; for instance the

Facebook OAuth2 backend
 name is 

facebook

. So the settings should be:

SOCIAL_AUTH_FACEBOOK_KEY

=

&#39;...&#39;

SOCIAL_AUTH_FACEBOOK_SECRET

=

&#39;...&#39;

Authentication backends
¶

Import path for authentication backends changed a little, there’s no more

contrib

 module, there’s no need for it. Some backends changed the names to
have some consistency. Check the backends, it should be easy to track the names
changes. Examples of the new import paths:

AUTHENTICATION_BACKENDS

=

(

&#39;social_core.backends.open_id.OpenIdAuth&#39;

,

&#39;social_core.backends.google.GoogleOpenId&#39;

,

&#39;social_core.backends.google.GoogleOAuth2&#39;

,

&#39;social_core.backends.google.GoogleOAuth&#39;

,

&#39;social_core.backends.twitter.TwitterOAuth&#39;

,

&#39;social_core.backends.facebook.FacebookOAuth2&#39;

,

)

Session
¶

Django stores the last authentication backend used in the user session as an
import path; this can cause import troubles when porting since the old import
paths aren’t valid anymore. Some solutions to this problem are:

Clean the session and force the users to login again in your site

Run a migration script that will update the authentication backend session
value for each session in your database. This implies figuring out the new
import path for each backend you have configured, which is the value used in

AUTHENTICATION_BACKENDS

 setting.

&#64;tomgruner
 created a Gist 
here
 that updates the value just for Facebook
backend. A 

template

 for this script would look like this:

from

django.contrib.sessions.models

import

Session

BACKENDS

=

{

&#39;social_auth.backends.facebook.FacebookBackend&#39;

:

&#39;social_core.backends.facebook.FacebookOAuth2&#39;

}

for

sess

in

Session

.

objects

.

iterator

():

session_dict

=

sess

.

get_decoded

()

if

&#39;_auth_user_backend&#39;

in

session_dict

.

keys

():

# Change old backend import path from new backend import path

if

session_dict

[

&#39;_auth_user_backend&#39;

]

.

startswith

(

&#39;social_auth&#39;

):

session_dict

[

&#39;_auth_user_backend&#39;

]

=

BACKENDS

[

session_dict

[

&#39;_auth_user_backend&#39;

]]

new_sess

=

Session

.

objects

.

save

(

sess

.

session_key

,

session_dict

,

sess

.

expire_date

)

print

(

&#39;New session saved 

{}

&#39;

.

format

(

new_sess

.

pk

))