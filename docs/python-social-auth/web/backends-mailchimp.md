# Backends/Mailchimp

Source: https://python-social-auth.readthedocs.io/en/latest/backends/mailchimp.html

MailChimp
¶

MailChimp uses OAuth v2 for Authentication, check the 
official docs
.

Create an app by filling out the form here: 
Add App

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_MAILCHIMP_KEY

=

&#39;&lt;App UID&gt;&#39;

SOCIAL_AUTH_MAILCHIMP_SECRET

=

&#39;&lt;App secret&gt;&#39;

Add the backend to the 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.mailchimp.MailChimpOAuth2&#39;

,

...

)

Then you can start using 

{%

url

social_core:begin

'mailchimp'

%}

 in
your templates