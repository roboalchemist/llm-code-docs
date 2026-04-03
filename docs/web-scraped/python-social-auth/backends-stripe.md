# Backends/Stripe

Source: https://python-social-auth.readthedocs.io/en/latest/backends/stripe.html

Stripe
¶

Stripe uses OAuth2 for its authorization service. To setup Stripe backend:

Register a new application at 
Stripe App Creation
, and

Grab the 

client_id

 value in 

Applications

 tab and fill the 

App

Id

setting:

SOCIAL_AUTH_STRIPE_KEY

=

&#39;ca_...&#39;

Grab the 

Test

Secret

Key

 in the 

API

Keys

 tab and fill the 

App

Secret

 setting:

SOCIAL_AUTH_STRIPE_SECRET

=

&#39;...&#39;

Define 

SOCIAL_AUTH_STRIPE_SCOPE

 with the desired scope (options are

read_only

 and 

read_write

):

SOCIAL_AUTH_STRIPE_SCOPE

=

[

&#39;read_only&#39;

]

Add the needed backend to 

AUTHENTICATION_BACKENDS

:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.stripe.StripeOAuth2&#39;

,

...

)

More info on Stripe OAuth2 at 
Integrating OAuth
.