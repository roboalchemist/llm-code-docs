# Backends/Osso

Source: https://python-social-auth.readthedocs.io/en/latest/backends/osso.html

Osso - Open Source SAML SSO
¶

Osso is an open source service that handles SAML tenant onboarding, documentation and authentication.

Your application can then consume normalized user profile resources as part of an OAuth 2.0 authorization code grant flow.

Learn more about Osso at 
https://ossoapp.com
 or continue below to start consuming your Osso instance from your application via Python Social Auth.

To enable Osso as a backend:

On your project settings, add Osso on your 

AUTHENTICATION_BACKENDS

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.osso.OssoOAuth2&#39;

,

)

Create or update an OAuth Client in your Osso instance, adding a redirect URI to your allow

http://example.com/complete/osso/

 replacing 

http://example.com

 with your application’s domain.
Grab the 

Client

ID

 and 

Client

Secret

 to use in your application.

Add these values of 

Client

ID

 and 

Client

Secret

 from Osso in your project settings file.

The 

Client

ID

 should be added on 

SOCIAL_AUTH_OSSO_KEY

 and the 

Client

Secret

 should be
added on 

SOCIAL_AUTH_OSSO_SECRET

. You also need to add your Osso instance base URL as 

SOCIAL_AUTH_OSSO_BASE_URL

:

SOCIAL_AUTH_OSSO_KEY

=

os

.

getenv

(

&#39;SOCIAL_AUTH_OSSO_KEY&#39;

)

SOCIAL_AUTH_OSSO_SECRET

=

os

.

getenv

(

&#39;SOCIAL_AUTH_OSSO_SECRET&#39;

)

SOCIAL_AUTH_OSSO_BASE_URL

=

&#39;https://demo.ossoapp.com&#39;

When constructing your sign in flow, Osso supports passing an 

email

 or 

domain

 parameter in order to route
the user to the correct IDP. If you don’t include one of these parameters, and instead implement a button, Osso
will display a hosted login page. Here’s an example login form with 

email

:

&lt;

form

action

=

&quot;

{%

url

&#39;social:begin&#39;

&#39;osso&#39;

%}

&quot;

method

=

&quot;post&quot;

class

=

&quot;login-form&quot;

&gt;

&lt;

label

&gt;
Email
&lt;/

label

&gt;

&lt;

input

type

=

&quot;email&quot;

name

=

&quot;email&quot;

/&gt;

{%

csrf_token

%}

&lt;

button

type

=

&quot;submit&quot;

&gt;
Sign in with SSO
&lt;/

button

&gt;

&lt;/

form

&gt;