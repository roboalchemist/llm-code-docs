# Configuration/Django

Source: https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

Django Framework
¶

Django framework has a little more support since this application was derived
from 
django-social-auth
. Here are some details on configuring this
application on Django.

Installing
¶

From 
pypi
:

$ pip install social-auth-app-django

And for 
MongoEngine
 ORM:

$ pip install social-auth-app-django-mongoengine

Quickstart
¶

This quickstart covers the essential configuration to get social authentication working in your Django project.

1. Add to INSTALLED_APPS
:

INSTALLED_APPS

=

(

...

&#39;social_django&#39;

,

)

2. Configure authentication backends
 (example for Google OAuth2):

AUTHENTICATION_BACKENDS

=

(

&#39;social_core.backends.google.GoogleOAuth2&#39;

,

&#39;django.contrib.auth.backends.ModelBackend&#39;

,

# Keep for username/password login

)

3. Add OAuth credentials to settings.py
:

This is where you configure your 

client_id

, 

client_secret

, and 

scope

 for each provider:

# Google OAuth2

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

=

&#39;your-client-id.apps.googleusercontent.com&#39;

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

=

&#39;your-client-secret&#39;

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE

=

[

&#39;https://www.googleapis.com/auth/userinfo.email&#39;

,

&#39;https://www.googleapis.com/auth/userinfo.profile&#39;

,

]

For other providers, the pattern is 

SOCIAL_AUTH_&lt;PROVIDER&gt;_KEY

, 

SOCIAL_AUTH_&lt;PROVIDER&gt;_SECRET

, and 

SOCIAL_AUTH_&lt;PROVIDER&gt;_SCOPE

. See 

Backends

 for provider-specific settings.

Warning

Never commit credentials to version control. Use environment variables instead:

import

os

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

=

os

.

environ

.

get

(

&#39;GOOGLE_OAUTH2_KEY&#39;

)

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

=

os

.

environ

.

get

(

&#39;GOOGLE_OAUTH2_SECRET&#39;

)

4. Add URLs to urls.py
:

urlpatterns

=

[

...

path

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

)),

]

5. Configure redirect URLs
:

LOGIN_URL

=

&#39;/login/&#39;

LOGIN_REDIRECT_URL

=

&#39;/&#39;

LOGOUT_REDIRECT_URL

=

&#39;/&#39;

6. Run migrations
:

python

manage

.

py

migrate

7. Add login link in template
:

&lt;

a

href

=

&quot;{

% u

rl &#39;social:begin&#39; &#39;google-oauth2&#39; %}&quot;

&gt;

Login

with

Google

&lt;/

a

&gt;

Note

Database considerations
: SQLite has field length limitations that can cause issues. For production, use PostgreSQL or MySQL. If using MySQL InnoDB or SQLite, add:

SOCIAL_AUTH_UID_LENGTH

=

223

For additional configuration options, see 

Configuration

.

Register the application
¶

The 
Django built-in app
 comes with two ORMs, one for default Django ORM and
another for 
MongoEngine
 ORM.

Add the application to 

INSTALLED_APPS

 setting, for default ORM:

INSTALLED_APPS

=

(

...

&#39;social_django&#39;

,

...

)

And for 
MongoEngine
 ORM:

INSTALLED_APPS

=

(

...

&#39;social_django_mongoengine&#39;

,

...

)

Also ensure to define the 
MongoEngine
 storage setting:

SOCIAL_AUTH_STORAGE

=

&#39;social_django_mongoengine.models.DjangoStorage&#39;

Database
¶

When using PostgreSQL, it’s recommended to use the built-in 
JSONB

field to store the extracted 

extra_data

. To enable it define the setting:

SOCIAL_AUTH_JSONFIELD_ENABLED

=

True

(For Django 1.7 and higher) you need to sync the database to create needed
models once you added 

social_django

 to your installed apps:

./

manage

.

py

migrate

Authentication backends
¶

Add desired authentication backends to Django’s 
AUTHENTICATION_BACKENDS

setting:

AUTHENTICATION_BACKENDS

=

(

&#39;social_core.backends.open_id.OpenIdAuth&#39;

,

&#39;social_core.backends.google.GoogleOAuth2&#39;

,

&#39;social_core.backends.twitter.TwitterOAuth&#39;

,

...

&#39;django.contrib.auth.backends.ModelBackend&#39;

,

)

Take into account that backends 
must
 be defined in 
AUTHENTICATION_BACKENDS

or Django won’t pick them when trying to authenticate the user.

Don’t miss 

django.contrib.auth.backends.ModelBackend

 if using 

django.contrib.auth

application or users won’t be able to login by username / password method.

For more documentation about setting backends to specific social applications, please see the 

Backends

.

URLs entries
¶

Add URLs entries:

urlpatterns

=

patterns

(

&#39;&#39;

,

...

path

(

&quot;&quot;

,

include

(

&#39;social_django.urls&#39;

,

namespace

=

&quot;social&quot;

)),

...

)

In case you need a custom namespace, this setting is also needed:

SOCIAL_AUTH_URL_NAMESPACE

=

&#39;social&#39;

Hint

In case you include the namespace from another namespace, you need to adjust
the configuration accordingly to include the parent namespace:

SOCIAL_AUTH_URL_NAMESPACE

=

&#39;accounts:social&#39;

Requiring POST only login
¶

By default login url 

social:begin

 uses 

GET

 request if you would like to require 

POST

 only (for example to comply with SOC audits) logging in then please use:

SOCIAL_AUTH_REQUIRE_POST

=

True

Templates
¶

Example of google-oauth2 backend usage in template:

&lt;

a

href

=

&quot;{

% u

rl &quot;

social

:

begin

&quot; &quot;

google

-

oauth2

&quot; %}&quot;

&gt;

Google

&lt;/

a

&gt;

Template Context Processors
¶

There’s a context processor that will add backends and associations data to
template context:

TEMPLATES

=

[

{

...

&#39;OPTIONS&#39;

:

{

...

&#39;context_processors&#39;

:

[

...

&#39;social_django.context_processors.backends&#39;

,

&#39;social_django.context_processors.login_redirect&#39;

,

...

]

}

}

]

backends

 context processor will load a 

backends

 key in the context with
three entries on it:

associated

It’s a list of 

UserSocialAuth

 instances related with the currently
logged in user. Will be empty if there’s no current user.

not_associated

A list of available backend names not associated with the current user yet.
If there’s no user logged in, it will be a list of all available backends.

backends

A list of all available backend names.

Personalized Configuration
¶

You can add (or remove) several features on the social auth pipeline.

By default there are some pipelines on social_django:

social_details

 - Get the information we can about the user and return it in a simple
format to create the user instance later. On some cases the details are
already part of the auth response from the provider, but sometimes this
could hit a provider API.

social_uid

 - Get the social uid from whichever service we’re authing thru. The uid is
the unique identifier of the given user in the provider.

auth_allowed

 - Verifies that the current auth process is valid within the current
project, this is where emails and domains whitelists are applied (if
defined).

social_user

 - Checks if the current social-account is already associated in the site.

get_username

- Make up a username for this person, appends a random string at the end if
there’s any collision.

create_user

 - Create a user account if we haven’t found one yet.

associate_user

 - Create the record that associated the social account with this user.

extra_data

 - Populate the extra_data field in the social record with the values
specified by settings (and the default ones like access_token, etc).

user_details

 - Update the user record with any changed info from the auth service.

Some other pipelines are available for use as well, but are not included by default:

associate_by_email

 - Associate current auth with a user with the same email address in the DB.
Obs: This pipeline entry is not 100% secure unless you know that the providers
enabled enforce email verification on their side, otherwise a user can
attempt to take over another user account by using the same (not validated)
email address on some provider.

Usage example:

SOCIAL_AUTH_PIPELINE

=

(

&#39;social_core.pipeline.social_auth.social_details&#39;

,

&#39;social_core.pipeline.social_auth.social_uid&#39;

,

&#39;social_core.pipeline.social_auth.social_user&#39;

,

&#39;social_core.pipeline.user.get_username&#39;

,

&#39;social_core.pipeline.social_auth.associate_by_email&#39;

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

ORMs
¶

As detailed above the built-in Django application supports default ORM and

MongoEngine
 ORM.

When using 
MongoEngine
 make sure you’ve followed the instructions for

MongoEngine Django integration
, as you’re now utilizing that user model. The

MongoEngine_
 backend was developed and tested with version 0.6.10 of

MongoEngine_
.

Alternate storage models implementations currently follow a tight pattern of
models that behave near or identical to Django ORM models. It is currently
not decoupled from this pattern by any abstraction layer. If you would like
to implement your own alternate, please see the 

social_django.models

 and

social_django_mongoengine.models

 modules for guidance.

Active users filtering
¶

By default the model allows only active users to authenticate. This can be
customised by 

SOCIAL_AUTH_ACTIVE_USERS_FILTER

 setting which is passed as
kwargs to the query set filter method.

Disable filtering for active users

¶

SOCIAL_AUTH_ACTIVE_USERS_FILTER

=

{}

Use custom field to filter active users

¶

SOCIAL_AUTH_ACTIVE_USERS_FILTER

=

{

&quot;deleted_account&quot;

:

False

}

JSON field support
¶

Django 3.1 introduces 
JSONField
 support for all backends and adds a
deprecation warning.

These are the related settings to enabling this integration:

SOCIAL_AUTH_JSONFIELD_ENABLED
 (boolean)

Same behavior, setting name updated to match 
JSONField
 being supported by
all systems:

SOCIAL_AUTH_POSTGRES_JSONFIELD

=

True

# Before

SOCIAL_AUTH_JSONFIELD_ENABLED

=

True

# After

SOCIAL_AUTH_JSONFIELD_CUSTOM
 (import path)
Allows specifying an import string. This gives better control to setting a
custom JSONField.

For django systems &lt; 3.1 (technically &lt;4), you can set the old 
JSONField

to maintain behavior with earlier social-app-django releases:

SOCIAL_AUTH_JSONFIELD_CUSTOM

=

&#39;django.contrib.postgres.fields.JSONField&#39;

For sites running or upgrading to django 3.1+, then can set this so the new
value:

SOCIAL_AUTH_JSONFIELD_CUSTOM

=

&#39;django.db.models.JSONField&#39;

Deprecating setting: 
SOCIAL_AUTH_POSTGRES_JSONFIELD
 (bool)
Rename this to 
SOCIAL_AUTH_JSONFIELD_ENABLED
. The setting will be deprecated
in a future release.

Exceptions Middleware
¶

A base middleware is provided that handles 

SocialAuthBaseException

 by
providing a message to the user via the Django messages framework, and then
responding with a redirect to a URL defined in one of the middleware methods.

The middleware is at 

social_django.middleware.SocialAuthExceptionMiddleware

.
Any method can be overridden, but for simplicity these two are recommended:

get_message

(

request

,

exception

)

get_redirect_uri

(

request

,

exception

)

By default, the message is the exception message and the URL for the redirect
is the location specified by the 

LOGIN_ERROR_URL

 setting.

If a valid backend was detected by 

strategy()

 decorator, it will be
available at 

request.strategy.backend

 and 

process_exception()

 will
use it to build a backend-dependent redirect URL but fallback to default if not
defined.

Backend-specific settings
¶

Both the 

LOGIN_ERROR_URL

 and 

RAISE_EXCEPTIONS

 settings can be configured
on a per-backend basis. This allows you to customize error handling behavior for
specific authentication backends.

To define backend-specific error URLs, use the backend name in the setting:

SOCIAL_AUTH_LOGIN_ERROR_URL

=

&#39;/login-error/&#39;

# Default for all backends

SOCIAL_AUTH_FACEBOOK_LOGIN_ERROR_URL

=

&#39;/facebook-error/&#39;

# Specific to Facebook

SOCIAL_AUTH_GOOGLE_OAUTH2_LOGIN_ERROR_URL

=

&#39;/google-error/&#39;

# Specific to Google OAuth2

Similarly, you can control exception raising on a per-backend basis:

SOCIAL_AUTH_RAISE_EXCEPTIONS

=

False

# Default for all backends

SOCIAL_AUTH_FACEBOOK_RAISE_EXCEPTIONS

=

True

# Raise exceptions only for Facebook

This is particularly useful when you want different error handling strategies for
different authentication providers, such as showing a custom error page for certain
providers or raising exceptions for debugging specific backends while keeping
others in production mode.

Exception processing is disabled if any of this settings is defined with a

True

 value:

&lt;

backend

name

&gt;

_SOCIAL_AUTH_RAISE_EXCEPTIONS

=

True

SOCIAL_AUTH_RAISE_EXCEPTIONS

=

True

RAISE_EXCEPTIONS

=

True

DEBUG

=

True

The redirect destination will get two 

GET

 parameters:

message

=

''

Message from the exception raised, in some cases it’s the message returned
by the provider during the auth process.

backend

=

''

Backend name that was used, if it was a valid backend.

The middleware will attempt to use the Django built-in 
messages

application to store the exception message, and tag it with

social-auth
 and the backend name. If the application is not enabled,
or a 
MessageFailure
 error happens, the app will default to the URL
format described above.

Django Admin
¶

The default application (not the 
MongoEngine
 one) contains an 

admin.py

module that will be auto-discovered by the usual mechanism.

But, by the nature of the application which depends on the existence of a user
model, it’s easy to fall in a recursive import ordering making the application
fail to load. This happens because the admin module will build a set of fields
to populate the 

search_fields

 property to search for related users in the
administration UI, but this requires the user model to be retrieved which might
not be defined at that time.

To avoid this issue define the following setting to circumvent the import
error:

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS

=

[

&#39;field1&#39;

,

&#39;field2&#39;

]

For example:

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS

=

[

&#39;username&#39;

,

&#39;first_name&#39;

,

&#39;email&#39;

]

The fields listed 
must
 be user models fields.

It’s also possible to define more search fields, not directly related
to the user model by definig the following setting:

SOCIAL_AUTH_ADMIN_SEARCH_FIELDS

=

[

&#39;field1&#39;

,

&#39;field2&#39;

]