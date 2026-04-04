# Backends/Implementation

Source: https://python-social-auth.readthedocs.io/en/latest/backends/implementation.html

Adding a new backend
¶

Adding new backends is quite easy.  Usually just all that’s required is to add
a 

class

 with a couple of settings and method overrides to retrieve user data
from a services API. Follow the details below:

Common attributes
¶

First, let’s check the common attributes for all backend types.

name

=

''

Any backend needs a name, usually the popular name of the service is used,
like 

facebook

, 

twitter

, etc. It must be unique, otherwise another
backend can take precedence if it’s listed before in the

AUTHENTICATION_BACKENDS

 setting.

ID_KEY

=

None

Defines the attribute in the service response that identifies the user as
unique to the service, the value is later stored in the 

uid

 attribute
in the 

UserSocialAuth

 instance. This can be overridden per-backend
via the 

SOCIAL_AUTH_&lt;BACKEND_NAME&gt;_ID_KEY

 setting (see

Configurable User ID Key
).

REQUIRES_EMAIL_VALIDATION

=

False

Flags the backend to enforce email validation during the pipeline (if the
corresponding pipeline 

social_core.pipeline.mail.mail_validation

 was
enabled).

EXTRA_DATA

=

None

During the auth process some basic user data is returned by the provider or
retrieved by the 

user_data()

 method which usually is used to call some API
on the provider to retrieve it. This data will be stored in the

UserSocialAuth.extra_data

 attribute, but to make it accessible under
some common names on different providers, this attribute defines a list of
tuples in the form 

(name,

alias)

 where 

name

 is the key in the user
data (which should be a 

dict

 instance) and 

alias

 is the name to
store it on 

extra_data

.

ACCESS_TOKEN_METHOD

=

'GET'

Specifying the method type required to retrieve your access token if it’s not
the default GET request.

OAuth
¶

OAuth1 and OAuth2 provide some common definitions based on the shared
behavior during the auth process.  For example, a successful API response from

AUTHORIZATION_URL

 usually returns some basic user data like a user Id.

Shared attributes
¶

name

This defines the backend name and identifies it during the auth process.
The name is used in the URLs 

/login/&lt;backend

name&gt;

 and

/complete/&lt;backend

name&gt;

.

ID_KEY

=

'id'

The default key name where the user identification field is defined, it’s used
in the auth process when some basic user data is returned. This Id is stored
in the 

UserSocialAuth.uid

 field and this, together with the

UserSocialAuth.provider

 field, is used to uniquely identify a user
association.

SCOPE_PARAMETER_NAME

=

'scope'

The scope argument is used to tell the provider the API endpoints you want to
call later, it’s a permissions request granted over the 

access_token

later retrieved. The default value is 

scope

 since that’s usually the name
used in the URL parameter, but can be overridden if needed.

DEFAULT_SCOPE

=

None

Some providers give nothing about the user but some basic data like the user
Id or an email address. The default scope attribute is used to specify a
default value for the 

scope

 argument to request those extra bits.

SCOPE_SEPARATOR

=

'

'

The 

scope

 argument is usually a list of permissions to request, the
list is joined with a separator, usually just a blank space, but this can differ
from provider to provider.  Override the default value with this attribute
if it differs.

OAuth2
¶

OAuth2 backends are fairly simple to implement; just a few settings, a method
override and it’s mostly ready to go.

The key points on these backends are:

AUTHORIZATION_URL

This is the entry point for the authorization mechanism, users must be
redirected to this URL, used on 

auth_url

 method which builds the
redirect address with 

AUTHORIZATION_URL

 plus some arguments
(

client_id

, 

redirect_uri

, 

response_type

, and 

state

).

ACCESS_TOKEN_URL

Must point to the API endpoint that provides an 

access_token

 needed to
authenticate in users behalf on future API calls.

REFRESH_TOKEN_URL

Some providers give the option to renew the 

access_token

 since they are
usually limited in time, once that time runs out, the token is invalidated
and cannot be used anymore. This attribute should point to that API
endpoint.

RESPONSE_TYPE

The response type expected on the auth process, default value is 

code

as dictated by OAuth2 definition. Override it if default value doesn’t fit
the provider implementation.

STATE_PARAMETER

OAuth2 defines that a 

state

 parameter can be passed in order to
validate the process, it’s kind of a CSRF check to avoid man in the middle
attacks. Some don’t recognise it or don’t return it which will make the
auth process invalid. Set this attribute to 

False

 in that case.

REDIRECT_STATE

For those providers that don’t recognise the 

state

 parameter, the app
can add a 

redirect_state

 argument to the 

redirect_uri

 to mimic it.
Set this value to 

False

 if the provider likes to verify the

redirect_uri

 value and this parameter invalidates that check.

Example code:

from

social_core.backends.oauth

import

BaseOAuth2

class

GitHubOAuth2

(

BaseOAuth2

):

&quot;&quot;&quot;GitHub OAuth authentication backend&quot;&quot;&quot;

name

=

&#39;github&#39;

AUTHORIZATION_URL

=

&#39;https://github.com/login/oauth/authorize&#39;

ACCESS_TOKEN_URL

=

&#39;https://github.com/login/oauth/access_token&#39;

ACCESS_TOKEN_METHOD

=

&#39;POST&#39;

SCOPE_SEPARATOR

=

&#39;,&#39;

EXTRA_DATA

=

[

(

&#39;id&#39;

,

&#39;id&#39;

),

(

&#39;expires&#39;

,

&#39;expires&#39;

)

]

def

get_user_details

(

self

,

response

):

&quot;&quot;&quot;Return user details from GitHub account&quot;&quot;&quot;

return

{

&#39;username&#39;

:

response

.

get

(

&#39;login&#39;

),

&#39;email&#39;

:

response

.

get

(

&#39;email&#39;

)

or

&#39;&#39;

,

&#39;first_name&#39;

:

response

.

get

(

&#39;name&#39;

)}

def

user_data

(

self

,

access_token

,

*

args

,

**

kwargs

):

&quot;&quot;&quot;Loads user data from service&quot;&quot;&quot;

url

=

&#39;https://api.github.com/user?&#39;

+

urlencode

({

&#39;access_token&#39;

:

access_token

})

return

self

.

get_json

(

url

)

OAuth2 with PKCE
¶

This is simply an extension of OAuth2 adding 
Proof Key for Code Exchange (PKCE)
 which provides security against authorization code interception attack.

Use the 

BaseOAuth2PKCE

 class as a drop-in replacement for 

BaseOAuth2

 for implementing backends that support PKCE. For reference, you may refer to 
Bitbucket Data Center OAuth2
 and 
Twitter OAuth2
 as example implementations.

Only a single key attribute is needed on these backends:

PKCE_DEFAULT_CODE_CHALLENGE_METHOD

Depends on which code challenge method is supported by the provider.
The possible values for this are 

s256

 and 

plain

.
By default, 

s256

 is set.

OAuth1
¶

OAuth1 process is a bit more trickier, 
Twitter Docs
 explains it quite well.
Besides the 

AUTHORIZATION_URL

 and 

ACCESS_TOKEN_URL

 attributes, a third
one is needed used when starting the process.

REQUEST_TOKEN_URL

=

''

During the auth process an unauthorized token is needed to start the
process, later this token is exchanged for an 

access_token

. This
setting points to the API endpoint where that unauthorized token can be
retrieved.

Example code:

from

xml.dom

import

minidom

from

social_core.backends.oauth

import

ConsumerBasedOAuth

class

TripItOAuth

(

ConsumerBasedOAuth

):

&quot;&quot;&quot;TripIt OAuth authentication backend&quot;&quot;&quot;

name

=

&#39;tripit&#39;

AUTHORIZATION_URL

=

&#39;https://www.tripit.com/oauth/authorize&#39;

REQUEST_TOKEN_URL

=

&#39;https://api.tripit.com/oauth/request_token&#39;

ACCESS_TOKEN_URL

=

&#39;https://api.tripit.com/oauth/access_token&#39;

EXTRA_DATA

=

[(

&#39;screen_name&#39;

,

&#39;screen_name&#39;

)]

def

get_user_details

(

self

,

response

):

&quot;&quot;&quot;Return user details from TripIt account&quot;&quot;&quot;

try

:

first_name

,

last_name

=

response

[

&#39;name&#39;

]

.

split

(

&#39; &#39;

,

1

)

except

ValueError

:

first_name

=

response

[

&#39;name&#39;

]

last_name

=

&#39;&#39;

return

{

&#39;username&#39;

:

response

[

&#39;screen_name&#39;

],

&#39;email&#39;

:

response

[

&#39;email&#39;

],

&#39;fullname&#39;

:

response

[

&#39;name&#39;

],

&#39;first_name&#39;

:

first_name

,

&#39;last_name&#39;

:

last_name

}

def

user_data

(

self

,

access_token

,

*

args

,

**

kwargs

):

&quot;&quot;&quot;Return user data provided&quot;&quot;&quot;

url

=

&#39;https://api.tripit.com/v1/get/profile&#39;

request

=

self

.

oauth_request

(

access_token

,

url

)

content

=

self

.

fetch_response

(

request

)

try

:

dom

=

minidom

.

parseString

(

content

)

except

ValueError

:

return

None

return

{

&#39;id&#39;

:

dom

.

getElementsByTagName

(

&#39;Profile&#39;

)[

0

]

.

getAttribute

(

&#39;ref&#39;

),

&#39;name&#39;

:

dom

.

getElementsByTagName

(

&#39;public_display_name&#39;

)[

0

]

.

childNodes

[

0

]

.

data

,

&#39;screen_name&#39;

:

dom

.

getElementsByTagName

(

&#39;screen_name&#39;

)[

0

]

.

childNodes

[

0

]

.

data

,

&#39;email&#39;

:

dom

.

getElementsByTagName

(

&#39;is_primary&#39;

)[

0

]

.

parentNode

.

getElementsByTagName

(

&#39;address&#39;

)[

0

]

.

childNodes

[

0

]

.

data

,

}

OpenID
¶

OpenID is far simpler than OAuth since it’s used for authentication rather
than authorization (regardless it’s used for authorization too).

A single attribute is usually needed, the authentication URL endpoint.

URL

=

''

OpenID endpoint where to redirect the user.

Sometimes the URL is user dependent, like in 
myOpenID
 where the URL is

https://&lt;user

handler&gt;.myopenid.com

. For those cases where the user must
input it’s handle (or full URL). The backend must override the 

openid_url()

method to retrieve it and return a full URL to where the user will be
redirected.

Example code:

from

social_core.backends.open_id

import

OpenIdAuth

from

social_core.exceptions

import

AuthMissingParameter

class

LiveJournalOpenId

(

OpenIdAuth

):

&quot;&quot;&quot;LiveJournal OpenID authentication backend&quot;&quot;&quot;

name

=

&#39;livejournal&#39;

def

get_user_details

(

self

,

response

):

&quot;&quot;&quot;Generate username from identity url&quot;&quot;&quot;

values

=

super

(

LiveJournalOpenId

,

self

)

.

get_user_details

(

response

)

values

[

&#39;username&#39;

]

=

values

.

get

(

&#39;username&#39;

)

or
 \

urlparse

.

urlsplit

(

response

.

identity_url

)
\

.

netloc

.

split

(

&#39;.&#39;

,

1

)[

0

]

return

values

def

openid_url

(

self

):

&quot;&quot;&quot;Returns LiveJournal authentication URL&quot;&quot;&quot;

if

not

self

.

data

.

get

(

&#39;openid_lj_user&#39;

):

raise

AuthMissingParameter

(

self

,

&#39;openid_lj_user&#39;

)

return

&#39;http://

%s

.livejournal.com&#39;

%

self

.

data

[

&#39;openid_lj_user&#39;

]

Auth APIs
¶

For others authentication types, a 

BaseAuth

 class is defined to help. Those
custom auth methods must override the 

auth_url()

 and 

auth_complete()

methods.

Example code:

from

google.appengine.api

import

users

from

social_core.backends.base

import

BaseAuth

from

social_core.exceptions

import

AuthException

class

GoogleAppEngineAuth

(

BaseAuth

):

&quot;&quot;&quot;GoogleAppengine authentication backend&quot;&quot;&quot;

name

=

&#39;google-appengine&#39;

def

get_user_id

(

self

,

details

,

response

):

&quot;&quot;&quot;Return current user id.&quot;&quot;&quot;

user

=

users

.

get_current_user

()

if

user

:

return

user

.

user_id

()

def

get_user_details

(

self

,

response

):

&quot;&quot;&quot;Return user basic information (id and email only).&quot;&quot;&quot;

user

=

users

.

get_current_user

()

return

{

&#39;username&#39;

:

user

.

user_id

(),

&#39;email&#39;

:

user

.

email

(),

&#39;fullname&#39;

:

&#39;&#39;

,

&#39;first_name&#39;

:

&#39;&#39;

,

&#39;last_name&#39;

:

&#39;&#39;

}

def

auth_url

(

self

):

&quot;&quot;&quot;Build and return complete URL.&quot;&quot;&quot;

return

users

.

create_login_url

(

self

.

redirect_uri

)

def

auth_complete

(

self

,

*

args

,

**

kwargs

):

&quot;&quot;&quot;Completes login process, must return user instance.&quot;&quot;&quot;

if

not

users

.

get_current_user

():

raise

AuthException

(

&#39;Authentication error&#39;

)

kwargs

.

update

({

&#39;response&#39;

:

&#39;&#39;

,

&#39;backend&#39;

:

self

})

return

self

.

strategy

.

authenticate

(

*

args

,

**

kwargs

)

Common backend methods
¶

All backends inherit from 

BaseAuth

 which provides several methods that can be
overridden to customize behavior. Here are some key methods:

id_key()

Returns the ID key to use for this backend. By default, this method checks
if the 

ID_KEY

 has been configured via settings (using

SOCIAL_AUTH_&lt;BACKEND_NAME&gt;_ID_KEY

) and returns that value if present,
otherwise it falls back to the 

ID_KEY

 class attribute.

Most backends should not need to override this method unless they have
special logic for determining the ID key. Instead, use the

SOCIAL_AUTH_&lt;BACKEND_NAME&gt;_ID_KEY

 setting to configure it.

get_user_id(details,

response)

Returns a unique ID for the current user from the provider’s response or
from the details dict. This method uses 

id_key()

 to determine which
field to extract from the response. The default implementation checks
both 

details

 and 

response

 dicts for the configured ID key.

Override this method if you need custom logic for extracting the user ID,
such as combining multiple fields or performing transformations.

Example of custom user ID retrieval:

def

get_user_id

(

self

,

details

,

response

):

&quot;&quot;&quot;Custom user ID retrieval&quot;&quot;&quot;

id_key

=

self

.

id_key

()

# Gets configured or default ID_KEY

if

self

.

setting

(

&quot;USERNAME_AS_ID&quot;

,

False

):

id_key

=

&quot;username&quot;

return

response

.

get

(

id_key

)

get_user_details(response)

Extracts user details (username, email, first_name, last_name, fullname)
from the provider’s API response. This method should return a dictionary
with the extracted values.