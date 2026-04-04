# Pipeline

Source: https://python-social-auth.readthedocs.io/en/latest/pipeline.html

Pipeline
¶

python-social-auth
 uses an extendible pipeline mechanism where developers can
introduce their functions during the authentication, association and
disconnection flows.

Pipeline Overview
¶

The pipeline is a sequence of functions that are executed in order during the
authentication process. Each function receives data from the previous steps and
can pass data to the next steps.

Key Concepts:

Pipeline functions
 are called sequentially in the order they are defined

Each function
 receives arguments from the authentication process and previous pipeline steps

Functions can pass data forward
 by returning a dictionary

Functions can interrupt the flow
 by returning an HTTP response (e.g., redirect)

All functions should accept

**kwargs

 to handle unexpected arguments gracefully

Understanding Return Values
¶

Pipeline functions can return three types of values, each with different behavior:

Return

None

or nothing
: The pipeline continues to the next function. This is
equivalent to returning an empty dict 

{}

.

Return a

dict

: The values in the dictionary are merged into the 

kwargs

 for
all subsequent pipeline functions. This is how you pass data forward in the pipeline.

Example:

def

my_pipeline_function

(

backend

,

user

,

**

kwargs

):

# Calculate something

custom_value

=

&quot;some data&quot;

# Pass it to next functions

return

{

&#39;custom_value&#39;

:

custom_value

}

Return any other value
 (HTTP response, redirect, etc.): The pipeline is interrupted
and the value is returned directly to the client. This is useful for partial pipelines
where you need user input.

Example:

def

my_pipeline_function

(

backend

,

user

,

**

kwargs

):

if

some_condition

:

# Interrupt pipeline and redirect user

return

redirect

(

&#39;/some-form/&#39;

)

Common Function Parameters
¶

The functions will receive a variable set of arguments related to the current
process. Common arguments include:

strategy

 - The current strategy instance (provides access to storage, settings, and request)

backend

 - The current backend instance (the social authentication provider)

user

 - The user instance (

None

 if not yet created or retrieved)

request

 - The current HTTP request object

social

 - The 

UserSocialAuth

 instance (

None

 until created)

uid

 - The unique user ID from the provider

response

 - The raw response from the authentication provider

details

 - Processed user details (username, email, etc.)

is_new

 - Boolean indicating if a user was just created

Any values returned as dicts by previous pipeline functions

Important:
 Always include 

**kwargs

 in your function signature to handle additional
arguments that may be passed from other pipeline functions or future versions:

def

my_custom_pipeline

(

strategy

,

backend

,

user

,

**

kwargs

):

# Your code here

pass

Authentication Pipeline
¶

The authentication workflow is handled by a pipeline where custom functions can
be added or default items can be removed to provide custom behavior. The default
pipeline creates user instances and gathers basic data from providers.

Understanding the Default Pipeline
¶

The pipeline executes in order, with each step depending on data from previous steps.
Here’s what happens at each stage:

The default pipeline is composed by:

(

# Get the information we can about the user and return it in a simple

# format to create the user instance later. In some cases the details are

# already part of the auth response from the provider, but sometimes this

# could hit a provider API.

&#39;social_core.pipeline.social_auth.social_details&#39;

,

# Get the social uid from whichever service we&#39;re authing thru. The uid is

# the unique identifier of the given user in the provider.

&#39;social_core.pipeline.social_auth.social_uid&#39;

,

# Verifies that the current auth process is valid within the current

# project, this is where emails and domains whitelists are applied (if

# defined).

&#39;social_core.pipeline.social_auth.auth_allowed&#39;

,

# Checks if the current social-account is already associated in the site.

&#39;social_core.pipeline.social_auth.social_user&#39;

,

# Make up a username for this person, appends a random string at the end if

# there&#39;s any collision.

&#39;social_core.pipeline.user.get_username&#39;

,

# Send a validation email to the user to verify its email address.

# Disabled by default.

# &#39;social_core.pipeline.mail.mail_validation&#39;,

# Associates the current social details with another user account with

# a similar email address. Disabled by default.

# &#39;social_core.pipeline.social_auth.associate_by_email&#39;,

# Create a user account if we haven&#39;t found one yet.

&#39;social_core.pipeline.user.create_user&#39;

,

# Create the record that associates the social account with the user.

&#39;social_core.pipeline.social_auth.associate_user&#39;

,

# Populate the extra_data field in the social record with the values

# specified by settings (and the default ones like access_token, etc).

&#39;social_core.pipeline.social_auth.load_extra_data&#39;

,

# Update the user record with any changed info from the auth service.

&#39;social_core.pipeline.user.user_details&#39;

,

)

What Data is Available When?

Understanding which data is available at each stage is crucial for placing your
custom functions correctly:

After

social_details

: 

details

 dict is populated with user info

After

social_uid

: 

uid

 contains the provider’s user ID

After

social_user

: 

social

 may contain the UserSocialAuth instance (if user was previously authenticated)

After

get_username

: 

username

 is available

After

create_user

: 

user

 contains the User instance (new or existing)

After

associate_user

: 

social

 contains the UserSocialAuth instance

After

load_extra_data

: 

social.extra_data

 contains access tokens and additional provider data

Customizing the Pipeline
¶

You can override the default pipeline by defining the setting 

SOCIAL_AUTH_PIPELINE

.

Example 1: Preventing New User Creation

A pipeline that won’t create users, just accepts already registered ones would look like this:

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

&#39;social_core.pipeline.social_auth.associate_user&#39;

,

&#39;social_core.pipeline.social_auth.load_extra_data&#39;

,

&#39;social_core.pipeline.user.user_details&#39;

,

)

Note

This example removes 

get_username

 and 

create_user

 steps, so only
users who have previously authenticated can log in.

Example 2: Custom User Loading

When authentication is purely external, you need a custom pipeline function that
populates the 

user

 key. This function should load or identify the user before
the 

social_user

 step:

SOCIAL_AUTH_PIPELINE

=

(

&#39;social_core.pipeline.social_auth.social_details&#39;

,

&#39;social_core.pipeline.social_auth.social_uid&#39;

,

&#39;social_core.pipeline.social_auth.auth_allowed&#39;

,

&#39;myapp.pipeline.load_user&#39;

,

# Custom function to load the user

&#39;social_core.pipeline.social_auth.social_user&#39;

,

&#39;social_core.pipeline.social_auth.associate_user&#39;

,

&#39;social_core.pipeline.social_auth.load_extra_data&#39;

,

&#39;social_core.pipeline.user.user_details&#39;

,

)

Your 

load_user

 function might look like:

def

load_user

(

strategy

,

backend

,

uid

,

user

=

None

,

**

kwargs

):

if

user

:

return

{

&#39;user&#39;

:

user

}

# Load user from your custom authentication system

user

=

MyUserModel

.

get_by_external_id

(

uid

)

return

{

&#39;user&#39;

:

user

}

Per-Backend Pipelines
¶

It is also possible to define pipelines on a per backend basis by defining a setting
such as 

SOCIAL_AUTH_TWITTER_PIPELINE

. Backend-specific pipelines will override
the default and 

SOCIAL_AUTH_PIPELINE

 settings.

Disconnection Pipeline
¶

Like the authentication pipeline, it’s possible to define a disconnection
pipeline if needed.

For example, this can be useful on sites where a user that disconnects all the
related social account is required to fill a password to ensure the
authentication process in the future. This can be accomplished by overriding
the default disconnection pipeline and setup a function that checks if the user
has a password, in case it doesn’t a redirect to a fill-your-password form can
be returned and later continue the disconnection process, take into account
that disconnection ensures the POST method by default, a simple method to
ensure this, is to make your form POST to 

/disconnect/

 and set the needed
password in your pipeline function. Check 
Partial Pipeline
 below.

In order to override the disconnection pipeline, just define the setting:

SOCIAL_AUTH_DISCONNECT_PIPELINE

=

(

# Verifies that the social association can be disconnected from the current

# user (ensure that the user login mechanism is not compromised by this

# disconnection).

&#39;social_core.pipeline.disconnect.allowed_to_disconnect&#39;

,

# Collects the social associations to disconnect.

&#39;social_core.pipeline.disconnect.get_entries&#39;

,

# Revoke any access_token when possible.

&#39;social_core.pipeline.disconnect.revoke_tokens&#39;

,

# Removes the social associations.

&#39;social_core.pipeline.disconnect.disconnect&#39;

,

)

Backend specific disconnection pipelines can also be defined with a setting such as

SOCIAL_AUTH_TWITTER_DISCONNECT_PIPELINE

.

Partial Pipeline
¶

The partial pipeline feature allows you to pause the authentication process to
request additional information from the user, then resume where you left off.

How Partial Pipelines Work
¶

Pause the pipeline
: Use the 

&#64;partial

 decorator on your function

Return an HTTP response
: Redirect the user to a form or page

User completes the action
: User fills out a form and submits it

Resume the pipeline
: User is redirected back to 

/complete/&lt;backend&gt;/

 and
the pipeline resumes from the same function

Basic Example
¶

Here’s a simple example of collecting additional user information:

from

social_core.pipeline.partial

import

partial

@partial

def

require_email

(

strategy

,

backend

,

details

,

user

=

None

,

**

kwargs

):

if

user

and

user

.

email

:

# User already has email, continue

return

# Check if email was submitted in this request

email

=

strategy

.

request_data

()

.

get

(

&#39;email&#39;

)

if

email

:

# Email was provided, pass it forward

return

{

&#39;details&#39;

:

{

&#39;email&#39;

:

email

}}

# No email yet - interrupt pipeline and show form

return

strategy

.

render_html

(

&#39;email_form.html&#39;

)

In your template, the form should POST to 

/complete/&lt;backend&gt;/

.

Django example
:

&lt;

form

method

=

&quot;post&quot;

action

=

&quot;{

% u

rl &#39;social:complete&#39; backend %}&quot;

&gt;

{

%

csrf_token

%

}

&lt;

input

type

=

&quot;email&quot;

name

=

&quot;email&quot;

required

&gt;

&lt;

button

type

=

&quot;submit&quot;

&gt;

Continue

&lt;/

button

&gt;

&lt;/

form

&gt;

How Partial Data is Stored
¶

&#64;partial

 stores the pipeline state in a database table named 

social_auth_partial

.
This allows:

Cross-browser support
: The process can resume from any browser

No session dependency
: More reliable than session-based approaches

UUID tokens
: Each partial process is identified by a unique token

The partial token is passed via the 

partial_token

 parameter (by default). The library
automatically picks this value from the request to resume the process.

Accessing Partial Data
¶

Pipeline functions receive a 

current_partial

 instance containing:

current_partial.token

 - The unique token for this partial process

current_partial.backend

 - The backend name

Other saved data from the pipeline

Example of using the partial token in a redirect:

from

urllib.parse

import

urlencode

@partial

def

my_partial_function

(

strategy

,

backend

,

current_partial

=

None

,

**

kwargs

):

# Check if user needs to provide additional information

if

not

kwargs

.

get

(

&#39;phone_number&#39;

):

# Include partial_token in the URL

params

=

urlencode

({

&#39;partial_token&#39;

:

current_partial

.

token

})

url

=

f

&#39;/my-form/?

{

params

}

&#39;

return

redirect

(

url

)

Configuration
¶

To override the default parameter name:

SOCIAL_AUTH_PARTIAL_PIPELINE_TOKEN_NAME

=

&#39;my_token_name&#39;

Check the 
example applications
 for more detailed usage examples.

Email validation
¶

There’s a pipeline to validate email addresses, but it relies a lot on your
project.

The pipeline is at 

social_core.pipeline.mail.mail_validation

 and it’s a partial
pipeline, it will return a redirect to the URL defined by the

EMAIL_VALIDATION_URL
 setting. For Django you can use a view name as the value
for this setting. You can use this redirect to tell the users that an email
validation was sent to them. If you want to mention the email address you can
get it from the session under the key 

email_validation_address

.

In order to send the validation 
python-social-auth
 needs a function that will
take care of it, this function is defined by the developer with the setting

SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION

. It should be an import path. This
function should take four arguments 

strategy

, 

backend

, 

code

 and

partial_token

.

partial_token

 is the same token used on other partials functions
that can be used to restart a halted flow.

code

 is a model instance used to validate the email address, it
contains three fields:

code

=

'...'

Holds an 

uuid.uuid4()

 value and it’s the code used to identify the
validation process.

email

=

'...'

Email address trying to be validate.

verified

=

True

/

False

Flag marking if the email was verified or not.

You should use the code in this instance to build the link for email
validation which should go to 

/complete/email?verification_code=&lt;code

here&gt;&amp;partial_token=&lt;token

here&gt;

.
If you are using Django, you can do it with:

from

django.core.urlresolvers

import

reverse

url

=

strategy

.

build_absolute_uri

(

reverse

(

&#39;social:complete&#39;

,

args

=

(

strategy

.

backend_name

,))

)

+

&#39;?verification_code=&#39;

+

code

.

code

+

&#39;&amp;partial_token=&#39;

+

partial_token

On Flask:

from

flask

import

url_for

url

=

url_for

(

&#39;social.complete&#39;

,

backend

=

strategy

.

backend_name

,

_external

=

True

)

+

&#39;?verification_code=&#39;

+

code

.

code

+

&#39;&amp;partial_token=&#39;

+

partial_token

This pipeline can be used globally with any backend if this setting is defined:

SOCIAL_AUTH_FORCE_EMAIL_VALIDATION

=

True

Or individually by defining the setting per backend basis like

SOCIAL_AUTH_TWITTER_FORCE_EMAIL_VALIDATION

=

True

.

Extending the Pipeline
¶

The pipeline system is designed for extensibility. You can add custom functions to:

Modify authentication data

Create or update related model instances

Request additional user information

Implement custom authorization logic

Integrate with external systems

Steps to Add a Custom Pipeline Function
¶

Write your function
 with the appropriate signature

Place it in an importable location
 in your project

Add it to the pipeline
 in your settings at the appropriate position

Important

Function placement matters! The order determines what data is available.
For example, placing your function after 

create_user

 ensures you receive a 

user

instance rather than 

None

.

Writing Custom Pipeline Functions
¶

Function Signature
¶

Your function should accept the common parameters and 

**kwargs

:

def

my_pipeline_function

(

strategy

,

backend

,

user

=

None

,

**

kwargs

):

# Your code here

pass

Tip

Always include 

**kwargs

 to handle additional parameters from other
pipeline functions or future versions.

See 

Common Function Parameters

 for details on the parameters available to pipeline functions.

Practical Example: Saving User Profile Data
¶

This example creates a 

Profile

 instance to store additional user information from Facebook.

Understanding the Facebook Response

The 

response

 parameter from Facebook typically looks like:

{

&#39;username&#39;

:

&#39;foobar&#39;

,

&#39;access_token&#39;

:

&#39;CAAD...&#39;

,

&#39;first_name&#39;

:

&#39;Foo&#39;

,

&#39;last_name&#39;

:

&#39;Bar&#39;

,

&#39;verified&#39;

:

True

,

&#39;name&#39;

:

&#39;Foo Bar&#39;

,

&#39;locale&#39;

:

&#39;en_US&#39;

,

&#39;gender&#39;

:

&#39;male&#39;

,

&#39;expires&#39;

:

&#39;5183999&#39;

,

&#39;email&#39;

:

&#39;foo@bar.com&#39;

,

&#39;updated_time&#39;

:

&#39;2014-01-14T15:58:35+0000&#39;

,

&#39;link&#39;

:

&#39;https://www.facebook.com/foobar&#39;

,

&#39;timezone&#39;

:

-

3

,

&#39;id&#39;

:

&#39;100000126636010&#39;

,

}

Let’s say we are interested in storing the user profile link, the gender and
the timezone in our 

Profile

 model:

def

save_profile

(

backend

,

user

,

response

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

&#39;facebook&#39;

:

profile

=

user

.

get_profile

()

if

profile

is

None

:

profile

=

Profile

(

user_id

=

user

.

id

)

profile

.

gender

=

response

.

get

(

&#39;gender&#39;

)

profile

.

link

=

response

.

get

(

&#39;link&#39;

)

profile

.

timezone

=

response

.

get

(

&#39;timezone&#39;

)

profile

.

save

()

Now all that’s needed is to tell 

python-social-auth

 to use our function in
the pipeline. Since the function uses user instance, we need to put it after

social_core.pipeline.user.create_user

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

&#39;social_core.pipeline.user.get_username&#39;

,

&#39;social_core.pipeline.user.create_user&#39;

,

&#39;path.to.save_profile&#39;

,

# &lt;--- set the path to the function

&#39;social_core.pipeline.social_auth.associate_user&#39;

,

&#39;social_core.pipeline.social_auth.load_extra_data&#39;

,

&#39;social_core.pipeline.user.user_details&#39;

,

)

Passing Data Forward

The function above returns 

None

, which is fine if subsequent functions don’t need
the profile. To make the 

profile

 available to later pipeline functions, return a dict:

def

save_profile

(

backend

,

user

,

response

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

&#39;facebook&#39;

:

profile

=

user

.

get_profile

()

if

profile

is

None

:

profile

=

Profile

(

user_id

=

user

.

id

)

profile

.

gender

=

response

.

get

(

&#39;gender&#39;

)

profile

.

link

=

response

.

get

(

&#39;link&#39;

)

profile

.

timezone

=

response

.

get

(

&#39;timezone&#39;

)

profile

.

save

()

return

{

&#39;profile&#39;

:

profile

}

# Make profile available to next functions

Common Patterns and Tips
¶

Conditional Execution

Check the backend name to run logic for specific providers:

def

my_function

(

backend

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

:

# Google-specific logic

pass

elif

backend

.

name

==

&#39;facebook&#39;

:

# Facebook-specific logic

pass

Accessing Settings

Use the strategy to access settings:

def

my_function

(

strategy

,

**

kwargs

):

custom_setting

=

strategy

.

setting

(

&#39;MY_CUSTOM_SETTING&#39;

)

Making API Calls

Use the access token from 

response

 to call provider APIs:

def

fetch_additional_data

(

backend

,

response

,

**

kwargs

):

access_token

=

response

.

get

(

&#39;access_token&#39;

)

# Make API call using the token

import

requests

api_response

=

requests

.

get

(

&#39;https://provider-api.com/endpoint&#39;

,

headers

=

{

&#39;Authorization&#39;

:

f

&#39;Bearer 

{

access_token

}

&#39;

}

)

return

{

&#39;additional_data&#39;

:

api_response

.

json

()}

Debugging

Log pipeline execution to understand the flow:

import

logging

logger

=

logging

.

getLogger

(

__name__

)

def

my_function

(

user

,

**

kwargs

):

logger

.

debug

(

f

&#39;Pipeline function called for user: 

{

user

}

&#39;

)

logger

.

debug

(

f

&#39;Available kwargs: 

{

kwargs

.

keys

()

}

&#39;

)

# Your logic here