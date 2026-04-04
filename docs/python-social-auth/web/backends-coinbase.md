# Backends/Coinbase

Source: https://python-social-auth.readthedocs.io/en/latest/backends/coinbase.html

Coinbase
¶

Coinbase uses OAuth2.

Register an application at 
Coinbase

Fill in the 
Client Id
 and 
Client Secret
 values in your settings:

SOCIAL_AUTH_COINBASE_KEY

=

&#39;&#39;

SOCIAL_AUTH_COINBASE_SECRET

=

&#39;&#39;

Set the 

redirect_url

 on coinbase. Make sure to include the trailing
slash, eg. 

http://hostname/complete/coinbase/

Specify scopes with:

SOCIAL_AUTH_COINBASE_SCOPE

=

[

...

]

By default the scope is set to 

balance

.

extra scopes can be defined by using:

SOCIAL_AUTH_COINBASE_AUTH_EXTRA_ARGUMENTS

=

{

&#39;account&#39;

:

&#39;all&#39;

}