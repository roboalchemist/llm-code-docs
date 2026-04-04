# Backends/Untappd

Source: https://python-social-auth.readthedocs.io/en/latest/backends/untappd.html

Untappd
¶

Untappd uses OAuth v2 for Authentication, check the 
official docs
.

Create an app by filling out the form here: 
Add App

Apps are approved on a one-by-one basis, so you’ll need to wait a
few days to get your client ID and secret.

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_UNTAPPD_KEY

=

&#39;&lt;App UID&gt;&#39;

SOCIAL_AUTH_UNTAPPD_SECRET

=

&#39;&lt;App secret&gt;&#39;

Optionally include a 

User

Agent

 to identify your calls to Untappd (this
may become required in the future):

SOCIAL_AUTH_UNTAPPD_USER_AGENT

=

&#39;My Custom User Agent or App Name&#39;

Add the backend to the 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.untappd.UntappdOAuth2&#39;

,

...

)

Then you can start using 

{%

url

social:begin

'untappd'

%}

 in
your templates