# Backends/Salesforce

Source: https://python-social-auth.readthedocs.io/en/latest/backends/salesforce.html

Salesforce
¶

Salesforce uses OAuth v2 for Authentication, check the 
official docs
.

Create an app following the steps in the 
Defining Connected Apps
 docs.

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_SALESFORCE_OAUTH2_KEY

=

&#39;&lt;App UID&gt;&#39;

SOCIAL_AUTH_SALESFORCE_OAUTH2_SECRET

=

&#39;&lt;App secret&gt;&#39;

Add the backend to the 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.salesforce.SalesforceOAuth2&#39;

,

...

)

Then you can start using 

{%

url

social:begin

'salesforce-oauth2'

%}

 in
your templates

If using the sandbox mode:

Fill these settings instead:

SOCIAL_AUTH_SALESFORCE_OAUTH2_SANDBOX_KEY

=

&#39;&lt;App UID&gt;&#39;

SOCIAL_AUTH_SALESFORCE_OAUTH2_SANDBOX_SECRET

=

&#39;&lt;App secret&gt;&#39;

And this backend:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.salesforce.SalesforceOAuth2Sandbox&#39;

,

...

)

Then you can start using 

{%

url

social:begin

'salesforce-oauth2-sandbox'

%}

in your templates