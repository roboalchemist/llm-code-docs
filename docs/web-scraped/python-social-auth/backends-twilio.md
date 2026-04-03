# Backends/Twilio

Source: https://python-social-auth.readthedocs.io/en/latest/backends/twilio.html

Twilio
¶

Register a new application at 
Twilio Connect Api

Fill 

SOCIAL_AUTH_TWILIO_KEY

 and 

SOCIAL_AUTH_TWILIO_SECRET

 values in
the settings:

SOCIAL_AUTH_TWILIO_KEY

=

&#39;&#39;

SOCIAL_AUTH_TWILIO_SECRET

=

&#39;&#39;

Add desired authentication backends to Django’s 

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

setting:

&#39;social_core.backends.twilio.TwilioAuth&#39;

,

Usage example:

&lt;

a

href

=

&quot;/login/twilio&quot;

&gt;

Enter

using

Twilio

&lt;/

a

&gt;