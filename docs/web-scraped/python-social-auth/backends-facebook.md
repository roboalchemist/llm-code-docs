# Backends/Facebook

Source: https://python-social-auth.readthedocs.io/en/latest/backends/facebook.html

Facebook
¶

Python Social Auth provides multiple backends for Facebook authentication:

FacebookOAuth2
 (

social_core.backends.facebook.FacebookOAuth2

) - Standard Facebook OAuth2 authentication

FacebookAppOAuth2
 (

social_core.backends.facebook.FacebookAppOAuth2

) - For Facebook Canvas Applications

FacebookLimitedLogin
 (

social_core.backends.facebook_limited.FacebookLimitedLogin

) - For Facebook Limited Login (iOS SDK)

OAuth2
¶

Facebook uses OAuth2 for its auth process. Further documentation at 
Facebook
development resources
:

Register a new application at 
Facebook App Creation
, don’t use

localhost

 as 

App

Domains

 and 

Site

URL

 since Facebook won’t allow
them. Use a placeholder like 

myapp.com

 and define that domain in your

/etc/hosts

 or similar file.

Add the Facebook OAuth2 backend to your 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.facebook.FacebookOAuth2&#39;

,

...

)

fill 

App

Id

 and 

App

Secret

 values in values:

SOCIAL_AUTH_FACEBOOK_KEY

=

&#39;&#39;

SOCIAL_AUTH_FACEBOOK_SECRET

=

&#39;&#39;

Define 

SOCIAL_AUTH_FACEBOOK_SCOPE

 to get extra permissions
from facebook. Email is not sent by default, to get it, you must request the

email

 permission:

SOCIAL_AUTH_FACEBOOK_SCOPE

=

[

&#39;email&#39;

]

Define 

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS

 to pass extra parameters
to 
https://graph.facebook.com/me
 when gathering the user profile data (you need
to explicitly ask for fields like 

email

 using 

fields

 key):

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS

=

{

&#39;locale&#39;

:

&#39;ru_RU&#39;

,

&#39;fields&#39;

:

&#39;id, name, email, age_range&#39;

}

If you define a redirect URL in Facebook setup page, be sure to not define

http://127.0.0.1:8000
 or 
http://localhost:8000
 because it won’t work when
testing. Instead I define 
http://myapp.com
 and setup a mapping on 

/etc/hosts

.

Currently the backend uses Facebook API version 
18.0
 by default, but this can
be overridden by the following setting:

SOCIAL_AUTH_FACEBOOK_API_VERSION

=

&#39;19.0&#39;

Note

If you’re using Facebook Graph API v3.0 or later, be aware that several
parameters have been deprecated:

The 

display

 parameter (e.g., 

{'display':

'touch'}

) is no longer
supported. Facebook now automatically detects mobile devices based on
the user agent.

Make sure to check Facebook’s 
Graph API Changelog
 for other deprecated
features when upgrading to newer API versions.

Canvas Application
¶

If you need to perform authentication from Facebook Canvas application:

Create your canvas application at 
http://developers.facebook.com/apps

In Facebook application settings specify your canvas URL 

mysite.com/fb

(current default)

Add the Facebook Canvas Application backend to your 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.facebook.FacebookAppOAuth2&#39;

,

...

)

Setup your Python Social Auth settings and your application namespace:

SOCIAL_AUTH_FACEBOOK_APP_KEY

=

&#39;&#39;

SOCIAL_AUTH_FACEBOOK_APP_SECRET

=

&#39;&#39;

SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE

=

&#39;&#39;

Launch your testing server on port 80 (use sudo or nginx or apache) for
browser to be able to load it when Facebook calls canvas URL

Open your Facebook page via 
http://apps.facebook.com/app_namespace
 or
better via 
http://www.facebook.com/pages/user-name/user-id?sk=app_app-id

After that you will see this page in a right way and will able to connect
to application and login automatically after connection

Provide a template to be rendered, it must have this JavaScript snippet (or
similar) in it:

&lt;

script

type

=

&quot;text/javascript&quot;

&gt;

var

domain

=

&#39;https://apps.facebook.com/&#39;

,

redirectURI

=

domain

+

{{

FACEBOOK_APP_NAMESPACE

}}

+

&#39;/&#39;

;

window

.

top

.

location

=

&#39;https://www.facebook.com/dialog/oauth/&#39;

+

&#39;?client_id={{ FACEBOOK_KEY }}&#39;

+

&#39;&amp;redirect_uri=&#39;

+

encodeURIComponent

(

redirectURI

)

+

&#39;&amp;scope={{ FACEBOOK_EXTENDED_PERMISSIONS }}&#39;

;

&lt;/

script

&gt;

More info on the topic at 
Facebook Canvas Application Authentication
.