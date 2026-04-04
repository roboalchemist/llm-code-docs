# Backends/Vault

Source: https://python-social-auth.readthedocs.io/en/latest/backends/vault.html

Hashicorp Vault
¶

The 
Vault
 backend allows authentication against the OIDC 
provider
 in
Hashicorp 
Vault
 version 1.9 and later.

The backend class is 
VaultOpenIdConnect
 with name 
vault
.  A minimum
configuration is:

SOCIAL_AUTH_VAULT_OIDC_ENDPOINT

=

&#39;https://vault.example.net:8200/v1/identity/oidc/provider/default&#39;

SOCIAL_AUTH_VAULT_KEY

=

&#39;&lt;client_id&gt;&#39;

SOCIAL_AUTH_VAULT_SECRET

=

&#39;&lt;client_secret&gt;&#39;

The remaining configuration will be auto-detected, by fetching:

&lt;

SOCIAL_AUTH_VAULT_OIDC_ENDPOINT

&gt;/.

well

-

known

/

openid

-

configuration

You may need to set 

SOCIAL_AUTH_VAULT_VERIFY_SSL

=

False

 if your Vault
server does not have its certificate signed by a trusted CA (e.g.  with
LetsEncrypt), although this should only be used for testing and not in
production.

Vault OIDC configuration
¶

Vault 1.10 onwards includes a pre-defined provider “default”, key “default”
and assignment “allow_all”.  With Vault 1.9 you will need to create these
objects explicitly.

You can then create an OIDC client, and read it back to get the auto-generated
client ID and secret:

vault

write

identity

/

oidc

/

client

/

my

-

app
 \

redirect_uris

=

&quot;https://www.example.com/callback&quot;
 \

assignments

=

&quot;allow_all&quot;
 \

key

=

&quot;default&quot;
 \

id_token_ttl

=

&quot;30m&quot;
 \

access_token_ttl

=

&quot;1h&quot;

vault

read

identity

/

oidc

/

client

/

my

-

app

Scopes
¶

Vault is very flexible with regard to configuring claims and scopes,
so it’s up to you how you map entity and/or alias metadata to OIDC claims.
Here is a suggestion, which exposes the entity name as “preferred_username”
and takes the other claims from entity metadata:

vault

write

identity

/

oidc

/

scope

/

profile
 \

description

=

&quot;Provides user info&quot;
 \

template

=

&#39;{

&quot;preferred_username&quot;

:

{{

identity

.

entity

.

name

}},

&quot;name&quot;

:

{{

identity

.

entity

.

metadata

.

name

}},

&quot;given_name&quot;

:

{{

identity

.

entity

.

metadata

.

given_name

}},

&quot;family_name&quot;

:

{{

identity

.

entity

.

metadata

.

family_name

}}

}

&#39;

vault

write

identity

/

oidc

/

scope

/

email
 \

description

=

&quot;Provides email address&quot;
 \

template

=

&#39;{

&quot;email&quot;

:

{{

identity

.

entity

.

metadata

.

email

}}

}

&#39;

vault

write

identity

/

oidc

/

scope

/

groups
 \

description

=

&quot;Provides a list of group names&quot;
 \

template

=

&#39;{

&quot;groups&quot;

:

{{

identity

.

entity

.

groups

.

names

}}

}

&#39;

The Vault backend inherits defaults from 

open_id_connect.py

.  In
particular, it looks for the username in the 

preferred_username

 claim.
If you need to choose a different claim then you can do so:

SOCIAL_AUTH_VAULT_USERNAME_KEY

=

&#39;nickname&#39;

The default set of scopes requested are “openid”, “profile” and “email”.
You can request additional claims like this:

SOCIAL_AUTH_VAULT_SCOPE

=

[

&#39;groups&#39;

]

and you can remove the default scopes using:

SOCIAL_AUTH_VAULT_IGNORE_DEFAULT_SCOPE

=

True