# Backends/Lifescience

Source: https://python-social-auth.readthedocs.io/en/latest/backends/lifescience.html

Lifescience AAI
¶

Lifescience’s OpenID Connect (OIDC) backend requires the following minimum
configuration:

SOCIAL_AUTH_LIFESCIENCE_OIDC_KEY

=

&#39;&lt;client_id&gt;&#39;

SOCIAL_AUTH_LIFESCIENCE_OIDC_SECRET

=

&#39;&lt;client_secret&gt;&#39;

Scopes
¶

The default scopes will include the user’s email.
You can request additional claims, for example:

SOCIAL_AUTH_LIFESCIENCE_OIDC_SCOPE

=

[

&#39;eduperson_entitlement&#39;

]

and you can prevent the inclusion of the default scopes using:

SOCIAL_AUTH_LIFESCIENCE_OIDC_IGNORE_DEFAULT_SCOPE

=

True