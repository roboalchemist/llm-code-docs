# Backends/Bungie

Source: https://python-social-auth.readthedocs.io/en/latest/backends/bungie.html

Bungie
¶

Bungie uses OAuth 2.0 for authentication.

Bungie does not return username, email or name information. They
return a short form membership id (bungie site account) that is then
stored as the uid for social auth. To get the username,
_GetBungieNetUser_ is called which returns the bungie.net profile,
including user name as the _displayName_ field. You may super the

get_user_details

 function to change behavior or redirect your
users to a partial pipeline flow that gathers missing user data such
as email, password (local to your site), first name, last name
etc. The pipeline flow is best interrupted at the 6th step in the
sample pipeline below:

SOCIAL_AUTH_PIPELINE

=

(

# Get the information we can about the user and return it in a simple

# format to create the user instance later. On some cases the details are

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

# Super&#39;ed in bungie.py

&#39;social_core.pipeline.social_auth.auth_allowed&#39;

,

# Checks if the current social-account is already associated in the site.

&#39;social_core.pipeline.social_auth.social_user&#39;

,

# Make up a username for this person, appends a random string at the end if

# there&#39;s any collision.

&#39;social_core.pipeline.user.get_username&#39;

,

# Redirect to an @partial view to get missing user information here.

# If you wish to validate or associate by email, this is required.

# &#39;&lt;my_app&gt;.pipeline.required_user_information&#39;,

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

Register a new application at 
https://www.bungie.net/en/Application/

Set the 

Callback

URL

 in the Bungie.net Application Registration
page to 

https://&lt;your

domain&gt;/complete/bungie

 This 
must
 be

https

. During development you can use stunnel to proxy the request
or you can install sslserver from pip.

Set the 

Authentication

Backend

, 

Client

ID

(aka

OAuth

Key)

,

OAuth

Secret

, and 

X-API-KEY

 values in your Django settings:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.bungie.BungieBaseAuth&#39;

,

...

)

SOCIAL_AUTH_BUNGIE_API_KEY

=

&#39;...&#39;

SOCIAL_AUTH_BUNGIE_KEY

=

&#39;&lt;client_id&gt;&#39;

SOCIAL_AUTH_BUNGIE_SECRET

=

&#39;...&#39;

SOCIAL_AUTH_BUNGIE_ORIGIN

=

&#39;...&#39;

Bungie allows whitespace in usernames, modify these if needed:

SOCIAL_AUTH_SLUGIFY_USERNAMES

=

False

SOCIAL_AUTH_CLEAN_USERNAMES

=

False

SOCIAL_AUTH_USER_MODEL

=

&#39;auth.User&#39;