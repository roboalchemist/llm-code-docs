# Use_Cases

Source: https://python-social-auth.readthedocs.io/en/latest/use_cases.html

Use Cases
¶

Some miscellaneous options and use cases for 
python-social-auth
.

Return the user to the original page
¶

There’s a common scenario to return the user back to the original page from
where they requested to login. For that purpose, the usual 

next

 query-string
argument is used. The value of this parameter will be stored in the session and
later used to redirect the user when login was successful.

In order to use it, just define it with your link. For instance, when using
Django:

&lt;

a

href

=

&quot;{

% u

rl &#39;social:begin&#39; &#39;facebook&#39; %}?next={{ request.path }}&quot;

&gt;

Login

with

Facebook

&lt;/

a

&gt;

Pass custom GET/POST parameters and retrieve them on authentication
¶

In some cases, you might need to send data over the URL, and retrieve it while
processing the after-effect. For example, for conditionally executing code in
custom pipelines.

In such cases, add it to 

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION

.

In your settings:

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION

=

[

&#39;key&#39;

]

In template:

&lt;

a

href

=

&quot;{

% u

rl &#39;social:begin&#39; &#39;facebook&#39; %}?key={{ value }}&quot;

&gt;

Login

with

Facebook

&lt;/

a

&gt;

In your custom pipeline, retrieve it using:

strategy

.

session_get

(

&#39;key&#39;

)

Retrieve Google+ Friends
¶

Google provides a 
People API endpoint
 to retrieve the people in your circles
on Google+. In order to access that API first we need to define the needed
scope:

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE

=

[

&#39;https://www.googleapis.com/auth/plus.login&#39;

]

Once we have the 

access

token

 we can call the API like this:

import

requests

user

=

User

.

objects

.

get

(

...

)

social

=

user

.

social_auth

.

get

(

provider

=

&#39;google-oauth2&#39;

)

response

=

requests

.

get

(

&#39;https://www.googleapis.com/plus/v1/people/me/people/visible&#39;

,

params

=

{

&#39;access_token&#39;

:

social

.

extra_data

[

&#39;access_token&#39;

]}

)

friends

=

response

.

json

()[

&#39;items&#39;

]

Associate users by email
¶

Sometimes it’s desirable that social accounts are automatically associated if
the email already matches a user account.

For example, if a user signed up with their Facebook account, then logged out and
next time tries to use Google OAuth2 to login, it could be nice (if both social
sites have the same email address configured) that the user gets into their
initial account created by Facebook backend.

This scenario is possible by enabling the 

associate_by_email

 pipeline
function, like this:

SOCIAL_AUTH_PIPELINE

=

(

&#39;social_core.pipeline.social_auth.social_details&#39;

,

&#39;social_core.pipeline.social_auth.social_uid&#39;

,

&#39;social_core.pipeline.social_auth.auth_allowed&#39;

,

&#39;social_core.pipeline.social_auth.social_user&#39;

,

&#39;social_core.pipeline.user.get_username&#39;

,

&#39;social_core.pipeline.social_auth.associate_by_email&#39;

,

# &lt;--- enable this one

&#39;social_core.pipeline.user.create_user&#39;

,

&#39;social_core.pipeline.social_auth.associate_user&#39;

,

&#39;social_core.pipeline.social_auth.load_extra_data&#39;

,

&#39;social_core.pipeline.user.user_details&#39;

,

)

This feature is disabled by default because it’s not 100% secure to automate
this process with all the backends. Not all the providers will validate your
email account and others users could take advantage of that.

Take for instance User A registered in your site with the email

foo&#64;bar.com

. Then a malicious user registers into another provider that
doesn’t validate their email with that same account. Finally this user will turn
to your site (which supports that provider) and sign up to it, since the email
is the same, the malicious user will take control over the User A account.

Signup by OAuth access_token
¶

It’s a common scenario that mobile applications will use an SDK to signup
a user within the app, but that signup won’t be reflected by

python-social-auth
 unless the corresponding database entries are created. In
order to do so, it’s possible to create a view / route that creates those
entries by a given 

access_token

. Take the following code for instance (the
code follows Django conventions, but versions for others frameworks can be
implemented easily):

from

django.contrib.auth

import

login

from

social_django.utils

import

psa

# Define an URL entry to point to this view, call it passing the

# access_token parameter like ?access_token=&lt;token&gt;. The URL entry must

# contain the backend, like this:

#

#   url(r&#39;^register-by-token/(?P&lt;backend&gt;[^/]+)/$&#39;,

#       &#39;register_by_access_token&#39;)

@psa

(

&#39;social:complete&#39;

)

def

register_by_access_token

(

request

,

backend

):

# This view expects an access_token GET parameter, if it&#39;s needed,

# request.backend and request.strategy will be loaded with the current

# backend and strategy.

token

=

request

.

GET

.

get

(

&#39;access_token&#39;

)

user

=

request

.

backend

.

do_auth

(

token

)

if

user

:

login

(

request

,

user

)

return

&#39;OK&#39;

else

:

return

&#39;ERROR&#39;

The snippet above is quite simple, it doesn’t return JSON and usually this call
will be done by AJAX. It doesn’t return the user information, but that’s
something that can be extended and filled to suit the project where it’s going
to be used.

Note
: when dealing with 

OAuth1

, the 

access_token

 is

actually a query-string composed by 

oauth_token

 and

oauth_token_secret

, 
python-social-auth
 expects this to be a

dict

 with those keys, but if an string is detected, it will treat
it as a query string in the form 

oauth_token=123&amp;oauth_token_secret=456

.

Multiple scopes per provider
¶

At the moment 
python-social-auth
 doesn’t provide a method to define multiple
scopes for single backend, this is usually desired since it’s recommended to
ask the user for the minimum scope possible and increase the access when it’s
really needed. It’s possible to add a new backend extending the original one to
accomplish that behavior. There are two ways to do it.

Overriding 

get_scope()

 method:

from

social_core.backends.facebook

import

FacebookOAuth2

class

CustomFacebookOAuth2

(

FacebookOauth2

):

def

get_scope

(

self

):

scope

=

super

(

CustomFacebookOAuth2

,

self

)

.

get_scope

()

if

self

.

data

.

get

(

&#39;extrascope&#39;

):

scope

=

scope

+

[(

&#39;foo&#39;

,

&#39;bar&#39;

)]

return

scope

This method is quite simple, it overrides the method that returns the scope
value in a backend (

get_scope()

) and adds extra values to the list if it
was indicated by a parameter in the 

GET

 or 

POST

 data
(

self.data

).

Put this new backend in some place in your project and replace the original

FacebookOAuth2

 in 

AUTHENTICATION_BACKENDS

 with this new version.

When overriding this method, take into account that the default output the
base class for 

get_scope()

 is the raw value from the settings (whatever
they are defined), doing this will actually update the value in your
settings for all the users:

scope

=

super

(

CustomFacebookOAuth2

,

self

)

.

get_scope

()

scope

+=

[

&#39;foo&#39;

,

&#39;bar&#39;

]

Instead do it like this:

scope

=

super

(

CustomFacebookOAuth2

,

self

)

.

get_scope

()

scope

=

scope

+

[

&#39;foo&#39;

,

&#39;bar&#39;

]

It’s possible to do the same by defining a second backend which extends from
the original but overrides the name, this will imply new URLs and also new
settings for the new backend (since the name is used to build the settings
names), it also implies a new application in the provider since not all
providers give you the option of defining multiple redirect URLs. To do it
just add a backend like:

from

social_core.backends.facebook

import

FacebookOAuth2

class

CustomFacebookOAuth2

(

FacebookOauth2

):

name

=

&#39;facebook-custom&#39;

Put this new backend in some place in your project keeping the original

FacebookOAuth2

 in 

AUTHENTICATION_BACKENDS

. Now a new set of URLs
will be functional:

/

login

/

facebook

-

custom

/

complete

/

facebook

-

custom

/

disconnect

/

facebook

-

custom

And also a new set of settings:

SOCIAL_AUTH_FACEBOOK_CUSTOM_KEY

=

&#39;...&#39;

SOCIAL_AUTH_FACEBOOK_CUSTOM_SECRET

=

&#39;...&#39;

SOCIAL_AUTH_FACEBOOK_CUSTOM_SCOPE

=

[

...

]

When the extra permissions are needed, just redirect the user to

/login/facebook-custom

 and then get the social auth entry for this new
backend with 

user.social_auth.get(provider='facebook-custom')

 and use
the 

access_token

 in it.

Enable a user to choose a username from their World of Warcraft characters
¶

If you want to register new users on your site via battle.net, you can enable
these users to choose a username from their own World-of-Warcraft characters.
To do this, use the 

battlenet-oauth2

 backend along with a small form to
choose the username.

The form is rendered via a partial pipeline item like this:

@partial

def

pick_character_name

(

backend

,

details

,

response

,

is_new

=

False

,

*

args

,

**

kwargs

):

if

backend

.

name

==

&#39;battlenet-oauth2&#39;

and

is_new

:

data

=

backend

.

strategy

.

request_data

()

if

data

.

get

(

&#39;character_name&#39;

)

is

None

:

# New user and didn&#39;t pick a character name yet, so we render

# and send a form to pick one. The form must do a POST/GET

# request to the same URL (/complete/battlenet-oauth2/). In this

# example we expect the user option under the key:

#   character_name

# you have to filter the result list according to your needs.

# In this example, only guild members are allowed to sign up.

char_list

=

[

c

[

&#39;name&#39;

]

for

c

in

backend

.

get_characters

(

response

.

get

(

&#39;access_token&#39;

))

if

&#39;guild&#39;

in

c

and

c

[

&#39;guild&#39;

]

==

&#39;&lt;guild name&gt;&#39;

]

return

render_to_response

(

&#39;pick_character_form.html&#39;

,

{

&#39;charlist&#39;

:

char_list

,

})

else

:

# The user selected a character name

return

{

&#39;username&#39;

:

data

.

get

(

&#39;character_name&#39;

)}

Don’t forget to add the partial to the pipeline:

SOCIAL_AUTH_PIPELINE

=

(

&#39;social_core.pipeline.social_auth.social_details&#39;

,

&#39;social_core.pipeline.social_auth.social_uid&#39;

,

&#39;social_core.pipeline.social_auth.auth_allowed&#39;

,

&#39;social_core.pipeline.social_auth.social_user&#39;

,

&#39;social_core.pipeline.user.get_username&#39;

,

&#39;path.to.pick_character_name&#39;

,

&#39;social_core.pipeline.user.create_user&#39;

,

&#39;social_core.pipeline.social_auth.associate_user&#39;

,

&#39;social_core.pipeline.social_auth.load_extra_data&#39;

,

&#39;social_core.pipeline.user.user_details&#39;

,

)

It needs to be somewhere before create_user because the partial will change the
username according to the users choice.

Re-prompt Google OAuth2 users to refresh the 

refresh_token

¶

A 

refresh_token

 also expire, a 

refresh_token

 can be lost, but they can
also be refreshed (or re-fetched) if you ask to Google the right way. In order
to do so, set this setting:

SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS

=

{

&#39;access_type&#39;

:

&#39;offline&#39;

,

&#39;approval_prompt&#39;

:

&#39;auto&#39;

}

Then link the users to 

/login/google-oauth2?approval_prompt=force

. If you
want to refresh the 

refresh_token

 only on those users that don’t  have it,
do it with a pipeline function:

def

redirect_if_no_refresh_token

(

backend

,

response

,

social

,

*

args

,

**

kwargs

):

if

backend

.

name

==

&#39;google-oauth2&#39;

and

social

and
 \

response

.

get

(

&#39;refresh_token&#39;

)

is

None

and
 \

social

.

extra_data

.

get

(

&#39;refresh_token&#39;

)

is

None

:

return

redirect

(

&#39;/login/google-oauth2?approval_prompt=force&#39;

)

Set this pipeline after 

social_user

:

SOCIAL_AUTH_PIPELINE

=

(

&#39;social_core.pipeline.social_auth.social_details&#39;

,

&#39;social_core.pipeline.social_auth.social_uid&#39;

,

&#39;social_core.pipeline.social_auth.auth_allowed&#39;

,

&#39;social_core.pipeline.social_auth.social_user&#39;

,

&#39;path.to.redirect_if_no_refresh_token&#39;

,

&#39;social_core.pipeline.user.get_username&#39;

,

&#39;social_core.pipeline.user.create_user&#39;

,

&#39;social_core.pipeline.social_auth.associate_user&#39;

,

&#39;social_core.pipeline.social_auth.load_extra_data&#39;

,

&#39;social_core.pipeline.user.user_details&#39;

,

)

Improve unicode cleanup from usernames
¶

It’s possible to improve the username cleanup by using an external library like

Unidecode
 or 
Text-Unicode
. You can integrate these by using the

SOCIAL_AUTH_CLEAN_USERNAME_FUNCTION
 documented at 
Username Generation

section. For instance, this will do the work:

SOCIAL_AUTH_CLEAN_USERNAME_FUNCTION

=

&#39;unidecode.unidecode&#39;