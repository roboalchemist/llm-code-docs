# Configuration/Webpy

Source: https://python-social-auth.readthedocs.io/en/latest/configuration/webpy.html

Webpy Framework
¶

Webpy
 framework is easy to setup, once that 
python-social-auth
 is installed
or accessible in the 

PYTHONPATH

, just add the needed configurations to make
it run.

Dependencies
¶

The 
Webpy app
 depends on 
sqlalchemy
, there’s no support for others
ORMs yet but pull-requests are welcome.

Installing
¶

From 
pypi
:

$ pip install social-auth-app-webpy

Configuration
¶

Add the needed settings into 

web.config

 store. Settings are prefixed with

SOCIAL_AUTH_

 but there’s a helper for it:

from

social_core.utils

import

setting_name

web

.

config

[

setting_name

(

&#39;USER_MODEL&#39;

)]

=

&#39;models.User&#39;

web

.

config

[

setting_name

(

&#39;LOGIN_REDIRECT_URL&#39;

)]

=

&#39;/done/&#39;

web

.

config

[

setting_name

(

&#39;AUTHENTICATION_BACKENDS&#39;

)]

=

(

&#39;social_core.backends.google.GoogleOAuth2&#39;

,

...

)

Add all the settings needed for the app (check 
Configuration
 section for
details).

URLs
¶

Add the social application into URLs:

from

social_webpy

import

app

as

social_app

urls

=

(

...

&#39;&#39;

,

social_app

.

app_social

...

)

Session
¶

python-social-auth
 depends on sessions storage to keep some essential values,
usually redirects and 

state

 parameters used to validate authentication
process on OAuth providers.

The 
Webpy built-in app
 expects the session reference to be available under

web.web_session

 so ensure it’s available there.

User model
¶

Like the other apps, the User model must be defined on settings since
a reference to it is kept on 

UserSocialAuth

 instance. Define like this:

web

.

config

[

setting_name

(

&#39;USER_MODEL&#39;

)]

=

&#39;models.User&#39;

Where the value is the import path to the User model used on your project.