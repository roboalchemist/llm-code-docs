# Backends/Seznam

Source: https://python-social-auth.readthedocs.io/en/latest/backends/seznam.html

Seznam
¶

Seznam supports OAuth2 for developers to authenticate users for their apps.
The documentation for the API can be found at 
Seznam OAuth documentation
.
This backend also provides additional configuration options to support
slightly different enterprise versions.

Register a new application at 
Application management
, set the

redirect_uri

 to 

http://example.com/complete/seznam-oauth2/

,
replacing 

example.com

 with your domain.

Fill 

client_id

 and 

client_secret

 values in the settings:

SOCIAL_AUTH_SEZNAM_OAUTH2_KEY

=

&#39;&lt;client_id&gt;&#39;

SOCIAL_AUTH_SEZNAM_OAUTH2_SECRET

=

&#39;&lt;client_secret&gt;&#39;

If you would like to access some additional information from the user,
you can set the 

SOCIAL_AUTH_SEZNAM_OAUTH2_SCOPE

 setting to a list of
extra scopes that are supported according to the 
scope documentation
.  For
example, to request access to the user’s phone number and avatar:

SOCIAL_AUTH_SEZNAM_OAUTH2_SCOPE

=

[

&#39;contact-phone&#39;

,

&#39;avatar&#39;

]

User ID
¶

Seznam recommends the use of 

oauth_user_id

 as the user identifier instead
of mutable data such as 

username

 or 

email

 because using mutable identifiers
can pose security risks if the user changes them.

For that reason 

oauth_user_id

 is used by default, but for compatibility
with enterprise backend versions or other use cases, you can override this behavior
by configuring the ID key via settings:

SOCIAL_AUTH_SEZNAM_OAUTH2_ID_KEY

=

&#39;id&#39;

See the 
Configurable User ID Key
 documentation for more information about this feature.