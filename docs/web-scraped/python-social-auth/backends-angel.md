# Backends/Angel

Source: https://python-social-auth.readthedocs.io/en/latest/backends/angel.html

Angel List
¶

Angel uses OAuth v2 for Authentication.

Register a new application at the 
Angel List API
, and

fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_ANGEL_KEY

=

&#39;&#39;

SOCIAL_AUTH_ANGEL_SECRET

=

&#39;&#39;

extra scopes can be defined by using:

SOCIAL_AUTH_ANGEL_AUTH_EXTRA_ARGUMENTS

=

{

&#39;scope&#39;

:

&#39;email messages&#39;

}

Note:

Angel List does not currently support returning 

state

 parameter used to
validate the auth process.