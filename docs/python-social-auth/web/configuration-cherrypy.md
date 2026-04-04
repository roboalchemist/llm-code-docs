# Configuration/Cherrypy

Source: https://python-social-auth.readthedocs.io/en/latest/configuration/cherrypy.html

CherryPy Framework
¶

CherryPy framework is supported, it works but I’m sure there’s room for
improvements. The implementation uses SQLAlchemy as ORM and expects some values
accessible on 

cherrypy.request

 for it to work.

At the moment the configuration is expected on 

cherrypy.config

 but ideally
it should be an application configuration instead.

Expected values are:

cherrypy.request.user

Current logged in user, load it in your application on a 

before_handler

handler.

cherrypy.request.db

Current database session, again, load it in your application on
a 

before_handler

.

Dependencies
¶

The 
CherryPy application
 depends on 
sqlalchemy
, there’s no support for
others ORMs yet.

Installing
¶

From 
pypi
:

$ pip install social-auth-app-cherrypy

Enabling the application
¶

The application is defined on 

social_cherrypy.views.CherryPyPSAViews

,
register it in the preferred way for your project.

Check the rest of the docs for the other settings like enabling authentication
backends and backends keys.

Models Setup
¶

The models are located in 

social_cherrypy.models

. A reference to
your 

User

 model is required to be defined in the project settings, it
should be an import path, for example:

cherrypy

.

config

.

update

({

&#39;SOCIAL_AUTH_USER_MODEL&#39;

:

&#39;models.User&#39;

})

Login mechanism
¶

By default the application sets the session value 

user_id

, this is a simple
solution and it should be improved, if you want to provider your own login
mechanism you can do it by defining the 

SOCIAL_AUTH_LOGIN_METHOD

 setting,
it should be an import path to a callable, like this:

SOCIAL_AUTH_USER_MODEL

=

&#39;app.login_user&#39;

And an example of this function:

def

login_user

(

strategy

,

user

):

strategy

.

session_set

(

&#39;user_id&#39;

,

user

.

id

)

Then, ensure to load the user in your application at 

cherrypy.request.user

,
for example:

def

load_user

():

user_id

=

cherrypy

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

cherrypy

.

request

.

user

=

cherrypy

.

request

.

db

.

query

(

User

)

.

get

(

user_id

)

else

:

cherrypy

.

request

.

user

=

None

cherrypy

.

tools

.

authenticate

=

cherrypy

.

Tool

(

&#39;before_handler&#39;

,

load_user

)