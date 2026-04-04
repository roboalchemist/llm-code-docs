# Backends/Fitbit

Source: https://python-social-auth.readthedocs.io/en/latest/backends/fitbit.html

Fitbit
¶

Fitbit supports both OAuth 2.0 and OAuth 1.0a logins. OAuth 2 is
preferred for new integrations, as OAuth 1.0a does not support getting
heartrate or location and will be deprecated in the future.

Register a new OAuth Consumer 
here

Configure the appropriate settings for OAuth 2.0 or OAuth 1.0a (see
below).

OAuth 2.0 or OAuth 1.0a
¶

Fill 

Consumer

Key

 and 

Consumer

Secret

 values in the
settings:

SOCIAL_AUTH_FITBIT_KEY

=

&#39;&lt;your-consumer-key&gt;&#39;

SOCIAL_AUTH_FITBIT_SECRET

=

&#39;&lt;your-consumer-secret&gt;&#39;

OAuth 2.0 specific settings
¶

By default, only the 

profile

 scope is requested. To request more
scopes, set SOCIAL_AUTH_FITBIT_SCOPE:

SOCIAL_AUTH_FITBIT_SCOPE

=

[

&#39;activity&#39;

,

&#39;heartrate&#39;

,

&#39;location&#39;

,

&#39;nutrition&#39;

,

&#39;profile&#39;

,

&#39;settings&#39;

,

&#39;sleep&#39;

,

&#39;social&#39;

,

&#39;weight&#39;

]

The above will request all permissions from the user.