# Backends/Google

Source: https://python-social-auth.readthedocs.io/en/latest/backends/google.html

Google
¶

This section describes how to setup the different services provided by Google.

Google OAuth
¶

Attention

Google OAuth deprecation

Important: OAuth 1.0 was officially deprecated on April 20, 2012, and will be
shut down on April 20, 2015. We encourage you to migrate to any of the other
protocols.

Google provides 

Consumer

Key

 and 

Consumer

Secret

 keys to registered
applications, but also allows unregistered application to use their authorization
system with, but beware that this method will display a security banner to the
user telling that the application is not trusted.

Check 
Google OAuth
 and make your choice.

fill 

Consumer

Key

 and 

Consumer

Secret

 values:

SOCIAL_AUTH_GOOGLE_OAUTH_KEY

=

&#39;&#39;

SOCIAL_AUTH_GOOGLE_OAUTH_SECRET

=

&#39;&#39;

anonymous values will be used if not configured as described in their

OAuth reference

setup any needed extra scope in:

SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE

=

[

...

]

Google OAuth2
¶

Recently Google launched OAuth2 support following the definition at 
OAuth2 draft
.
It works in a similar way to plain OAuth mechanism, but developers 
must
 register
an application and apply for a set of keys. Check 
Google OAuth2
 document for details.

IdP Setup
¶

To configure Google OAuth2:

Go to the 
Google Cloud Console

Create a new project or select an existing one

Navigate to 
APIs &amp; Services
 &gt; 
Credentials

Click 
Create Credentials
 &gt; 
OAuth client ID

Configure:

Application type
: Web application

Authorized redirect URIs
: 

https://your-domain.com/complete/google-oauth2/

Note the 
Client ID
 and 
Client Secret

Configure the 
OAuth consent screen
 (

APIs

&amp;

Services

&gt;

OAuth

consent

screen

):

Set the 
PRODUCT NAME
 and other required fields

Add scopes: 

email

, 

profile

, 

openid

Application Configuration
¶

Fill in 

Client

ID

 and 

Client

Secret

 settings with values from Google:

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

=

&#39;&#39;

setup any needed extra scope:

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE

=

[

...

]

Check which applications can be included in their 
Google Data Protocol Directory

To allow user selecting Google account to use, add the 

prompt

 parameter with 

select_account

 value:

SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS

=

{

&#39;prompt&#39;

:

&#39;select_account&#39;

}

To restrict authentication to specific domains (useful for G Suite/Google Workspace organizations), use domain whitelisting. Check the 
whitelists
 settings for details.

Google One Tap
¶

Google One Tap
 is a bit different from the OAuth2 flow as the login process is started
on the client side. Because of this 
start
 url is not available, only a 
complete
 one.

Additional dependencies are needed, these will be automatically installed by the 

google-onetap

 extra, for example: 

uv

pip

install

'social-core[google-onetap]

.

To enable the backend create an application using the 
Google
console
 to retrieve your 
Google Client ID
.
Make sure sure to add your website’s URL to 

Authorized

JavaScript

origins

 and

Authorized

redirect

URIs

(don’t forget to also include the port number if you are using localhost).

Fill in the key setting looking inside the Google console the subsection

Credentials

 inside 

API

&amp;

auth

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.google_onetap.GoogleOneTap&#39;

,

)

SOCIAL_AUTH_GOOGLE_ONETAP_KEY

=

&#39;...&#39;

SOCIAL_AUTH_GOOGLE_ONETAP_IGNORE_MISSING_CSRF_COOKIE

=

True

/

False

SOCIAL_AUTH_GOOGLE_ONETAP_KEY

 corresponds to the variable 

CLIENT

ID

.

SOCIAL_AUTH_GOOGLE_ONETAP_IGNORE_MISSING_CSRF_COOKIE

 disabled the CSRF checks
if the token is missing from the cookies. This is an optional setting
because the cookie is not being set if authentication process started on a different
domain (for more details check out the 
related issue
).

Add the 
One Tap snippet
 to your page:

&lt;

div

id

=

&quot;g_id_onload&quot;

data

-

client_id

=

&quot;YOUR_GOOGLE_CLIENT_ID&quot;

data

-

login_uri

=

&quot;{

% u

rl &#39;social:complete&#39; &#39;google-onetap&#39; %}&quot;

data

-

your_own_param_1_to_login

=

&quot;any_value&quot;

data

-

your_own_param_2_to_login

=

&quot;any_value&quot;

&gt;

&lt;/

div

&gt;

And 
load the client library
:

&lt;

script

src

=

&quot;https://accounts.google.com/gsi/client&quot;

async

&gt;&lt;/

script

&gt;

Google+ Sign-In
¶

Google+ Sign In
 works a lot like OAuth2, but most of the initial work is
done by their Javascript which thens calls a defined handler to complete the
auth process.

To enable the backend create an application using the 
Google
console
 and following the steps from the 
official guide
. Make
sure to enable the Google+ API in the console.

Fill in the key settings looking inside the Google console the subsection

Credentials

 inside 

API

&amp;

auth

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.google.GooglePlusAuth&#39;

,

)

SOCIAL_AUTH_GOOGLE_PLUS_KEY

=

&#39;...&#39;

SOCIAL_AUTH_GOOGLE_PLUS_SECRET

=

&#39;...&#39;

SOCIAL_AUTH_GOOGLE_PLUS_KEY

 corresponds to the variable 

CLIENT

ID

.

SOCIAL_AUTH_GOOGLE_PLUS_SECRET

 corresponds to the variable

CLIENT

SECRET

.

Add the sign-in button to your template, you can use the SDK button
or add your own and attach the click handler to it (check 
Google+ Identity Sign-In

documentation about it):

&lt;

div

id

=

&quot;google-plus-button&quot;

&gt;

Google

+

Sign

In

&lt;/

div

&gt;

Add the Javascript snippet in the same template as above:

&lt;script src=&quot;https://apis.google.com/js/api:client.js&quot;&gt;&lt;/script&gt;

&lt;script type=&quot;text/javascript&quot;&gt;
  gapi.load(&#39;auth2&#39;, function () {
    var auth2;

    auth2 = gapi.auth2.init({
      client_id: &quot;&lt;PUT SOCIAL_AUTH_GOOGLE_PLUS_KEY HERE&gt;&quot;,
      scope: &quot;&lt;PUT BACKEND SCOPE HERE&gt;&quot;
    });

    auth2.then(function () {
      var button = document.getElementById(&quot;google-plus-button&quot;);
      console.log(&quot;User is signed-in in Google+ platform?&quot;, auth2.isSignedIn.get() ? &quot;Yes&quot; : &quot;No&quot;);

      auth2.attachClickHandler(button, {}, function (googleUser) {
        // Send access-token to backend to finish the authenticate
        // with your application

        var authResponse = googleUser.getAuthResponse();
        var $form;
        var $input;

        $form = $(&quot;&lt;form&gt;&quot;);
        $form.attr(&quot;action&quot;, &quot;/complete/google-plus&quot;);
        $form.attr(&quot;method&quot;, &quot;post&quot;);
        $input = $(&quot;&lt;input&gt;&quot;);
        $input.attr(&quot;name&quot;, &quot;id_token&quot;);
        $input.attr(&quot;value&quot;, authResponse.id_token);
        $form.append($input);
        // Add csrf-token if needed
        $(document.body).append($form);
        $form.submit();
      });
    });
  });
&lt;/script&gt;

Logging out

Logging-out can be tricky when using the the platform SDK because it
can trigger an automatic sign-in when listening to the user status
change. With the method show above, that won’t happen, but if the UI
depends more in the SDK values than the backend, then things can get
out of sync easily. To prevent this, the user should be logged-out
from Google+ platform too. This can be accomplished by doing:

&lt;script type=&quot;text/javascript&quot;&gt;
  gapi.load(&#39;auth2&#39;, function () {
    var auth2;

    auth2 = gapi.auth2.init({
      client_id: &quot;{{ plus_id }}&quot;,
      scope: &quot;{{ plus_scope }}&quot;
    });

    auth2.then(function () {
      if (auth2.isSignedIn.get()) {
        $(&#39;#logout&#39;).on(&#39;click&#39;, function (event) {
          event.preventDefault();
          auth2.signOut().then(function () {
            console.log(&quot;Logged out from Google+ platform&quot;);
            document.location = &quot;/logout&quot;;
          });
        });
      }
    });
  });
&lt;/script&gt;

Google OpenID
¶

Google OpenID works straightforward, no settings are needed. Domains or emails
whitelists can be applied too, check the 
whitelists
 settings for details.

Orkut
¶

As of September 30, 2014, Orkut has been 
shut down
.

User identification
¶

Optional support for static and unique Google Profile ID identifiers instead of
using the e-mail address for account association can be enabled with:

SOCIAL_AUTH_GOOGLE_OAUTH_USE_UNIQUE_USER_ID

=

True

or:

SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID

=

True

depending on the backends in use.

Refresh Tokens
¶

To get an OAuth2 refresh token along with the access token, you must pass an extra argument: 

access_type=offline

.
To do this with Google+ sign-in:

SOCIAL_AUTH_GOOGLE_PLUS_AUTH_EXTRA_ARGUMENTS

=

{

&#39;access_type&#39;

:

&#39;offline&#39;

}

Scopes deprecation
¶

Google is deprecating the full-url scopes from 
Sept 1, 2014
 in favor of

Google+

API

 and the recently introduced shorter scopes names. But

python-social-auth

 already introduced the scopes change at 
e3525187
 which
was released at 

v0.1.24

.

But, to enable the new scopes the application requires 

Google+

API

 to be
enabled in the 
Google console
 dashboard, the change is quick and quite
simple, but if any developer desires to keep using the old scopes, it’s
possible with the following settings:

# Google OAuth2 (google-oauth2)

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE

=

True

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE

=

[

&#39;https://www.googleapis.com/auth/userinfo.email&#39;

,

&#39;https://www.googleapis.com/auth/userinfo.profile&#39;

]

# Google+ SignIn (google-plus)

SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE

=

True

SOCIAL_AUTH_GOOGLE_PLUS_SCOPE

=

[

&#39;https://www.googleapis.com/auth/plus.login&#39;

,

&#39;https://www.googleapis.com/auth/userinfo.email&#39;

,

&#39;https://www.googleapis.com/auth/userinfo.profile&#39;

]

To ease the change, the old API and scopes is still supported by the
application, the new values are the default option but if having troubles
supporting them you can default to the old values by defining this setting:

SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API

=

True

SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API

=

True