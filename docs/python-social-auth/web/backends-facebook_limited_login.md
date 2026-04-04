# Backends/Facebook_Limited_Login

Source: https://python-social-auth.readthedocs.io/en/latest/backends/facebook_limited_login.html

Facebook Limited Login
¶

Facebook Limited Login
 is required by the Facebook iOS SDK.

App creation
¶

Register a new application at 
Facebook App Creation
, don’t use

localhost

 in the 

App

Domains

 and 

Site

URL

 fields as
Facebook does not allow this.

Instead, use a placeholder like 

myapp.com

 and define that
domain in your 

/etc/hosts

 or similar file for your OS. For
more information see the 
hosts file
 article on Wikipedia.

Configuration
¶

Set the 

SOCIAL_AUTH_FACEBOOK_LIMITED_LOGIN_KEY

 to the value
of the 

App

Id

.  This field is required for verifying the
Facebook access token received from the iOS SDK.

Django Configuration
¶

Set the Facebook Limited Login Key in 

settings.py

:

SOCIAL_AUTH_FACEBOOK_LIMITED_LOGIN_KEY

=

&quot;

{app_id}

&quot;

Enable the auth backend:

AUTHENTICATION_BACKENDS

=

(

...

&quot;social_core.backends.facebook_limited.FacebookLimitedLogin&quot;

,

...

)