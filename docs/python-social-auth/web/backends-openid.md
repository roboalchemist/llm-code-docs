# Backends/Openid

Source: https://python-social-auth.readthedocs.io/en/latest/backends/openid.html

OpenID
¶

OpenID
 support is simpler to implement than 
OAuth
. Google and Yahoo
providers are supported by default, others are supported by POST method
providing endpoint URL.

OpenID
 backends can store extra data in 

UserSocialAuth.extra_data

 field
by defining a set of values names to retrieve from any of the used schemas,
AttributeExchange and SimpleRegistration. As their keywords differ we need
two settings.

Settings is per backend, so we have two possible values for each one. Name
is dynamically checked using uppercase backend name as prefix:

SOCIAL_AUTH_

&lt;

uppercase

backend

name

&gt;

_SREG_EXTRA_DATA

SOCIAL_AUTH_

&lt;

uppercase

backend

name

&gt;

_AX_EXTRA_DATA

Example:

SOCIAL_AUTH_GOOGLE_SREG_EXTRA_DATA

=

[(

...

,

...

)]

SOCIAL_AUTH_GOOGLE_AX_EXTRA_DATA

=

[(

...

,

...

)]

Settings must be a list of tuples mapping value name in response and value
alias used to store. A third value (boolean) is supported to, it’s purpose is
to signal if the value should be discarded if it evaluates to 

False

, this
is to avoid replacing old (needed) values when they don’t form part of current
response. If not present, then this check is avoided and the value will replace
any data.

Username
¶

The 
OpenID
 backend will check for a 

username

 key in the values returned by
the server, but default to 

first-name

 + 

last-name

 if that key is
missing. It’s possible to indicate the username key in the values If the
username is under a different key with a setting, but backends should have
defined a default value. For example:

SOCIAL_AUTH_FEDORA_USERNAME_KEY

=

&#39;nickname&#39;

This setting indicates that the username should be populated by the

nickname

 value in the Fedora 
OpenID
 provider.