# Configuration/Pyramid

Source: https://python-social-auth.readthedocs.io/en/latest/configuration/pyramid.html

Pyramid Framework
¶

Pyramid
 reusable applications are tricky (or I’m not capable enough). Here are
details on how to enable this application on Pyramid.

Dependencies
¶

The 
Pyramid app
 depends on 
sqlalchemy
, there’s no support for others
ORMs yet but pull-requests are welcome.

Installing
¶

From 
pypi
:

$ pip install social-auth-app-pyramid

Enabling the application
¶

The application can be scanned by 

Configurator.scan()

, also it defines an

includeme()

 in the 

__init__.py

 file which will add the needed routes to
your application configuration. To scan it just add:

config

.

include

(

&#39;social_pyramid&#39;

)

config

.

scan

(

&#39;social_pyramid&#39;

)

Models Setup
¶

At the moment the models for 
python-social-auth
 are defined inside a function
because they need the reference to the current DB instance and the User model
used on your project (check 
User model reference
 below). Once the Pyramid
application configuration and database are defined, call 

init_social

 to
register the models:

from

social_pyramid.models

import

init_social

init_social

(

config

,

Base

,

DBSession

)

So far I wasn’t able to find another way to define the models on another way
rather than making it as a side-effect of calling this function since the
database is not available and 

current_app

 cannot be used on initialization
time, just run time.

User model reference
¶

The application keeps a reference to the User model used by your project,
define it by using this setting:

SOCIAL_AUTH_USER_MODEL

=

&#39;foobar.models.User&#39;

The value must be the import path to the User model.

Global user
¶

The application expects the current logged in user accessible at 

request.user

,
the example application ensures that with this handler:

def

get_user

(

request

):

user_id

=

request

.

session

.

get

(

&#39;user_id&#39;

)

if

user_id

:

user

=

DBSession

.

query

(

User

)
\

.

filter

(

User

.

id

==

user_id

)
\

.

first

()

else

:

user

=

None

return

user

The handler is added to the configuration doing:

config

.

add_request_method

(

&#39;example.auth.get_user&#39;

,

&#39;user&#39;

,

reify

=

True

)

This is just a simple example, probably your project does it in a better way.

User login
¶

Since the application doesn’t make any assumption on how you are going to login
the users, you need to specify it. In order to do that, define these settings:

SOCIAL_AUTH_LOGIN_FUNCTION

=

&#39;example.auth.login_user&#39;

SOCIAL_AUTH_LOGGEDIN_FUNCTION

=

&#39;example.auth.login_required&#39;

The first one must accept the strategy used and the user instance that was
created or retrieved from the database, there you can set the user id in the
session or cookies or whatever place used later to retrieve the id again and
load the user from the database (check the snippet above in 
Global User
).

The second one is used to ensure that there’s a user logged in when calling the
disconnect view. It must accept a 

User

 instance and return 

True

 or

False

.

Check the 
auth.py
 in the example application for details on how it’s done
there.

Social auth in templates context
¶

To access the social instances related to a user in the template context, you
can do so by accessing the 

social_auth

 attribute in the user instance:

&lt;li tal:repeat=&quot;social request.user.social_auth&quot;&gt;${social.provider}&lt;/li&gt;

Also you can add the backends (associated and not associated to a user) by
enabling this context function in your project:

from

pyramid.events

import

subscriber

,

BeforeRender

from

social_pyramid.utils

import

backends

@subscriber

(

BeforeRender

)

def

add_social

(

event

):

request

=

event

[

&#39;request&#39;

]

event

.

update

(

backends

(

request

,

request

.

user

))

That will load a dict with entries:

{

&#39;associated&#39;

:

[

...

],

&#39;not_associated&#39;

:

[

...

],

&#39;backends&#39;

:

[

...

]

}

The 

associated

 key will have all the associated 

UserSocialAuth

instances related to the given user. 

not_associated

 will have the backends
names not associated and backends will have all the enabled backends names.