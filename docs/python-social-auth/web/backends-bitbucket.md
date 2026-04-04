# Backends/Bitbucket

Source: https://python-social-auth.readthedocs.io/en/latest/backends/bitbucket.html

Bitbucket
¶

Bitbucket supports both OAuth2 and OAuth1 logins.

Register a new OAuth Consumer by following the instructions in the
Bitbucket documentation: 
OAuth on Bitbucket

Note: For OAuth2, your consumer MUST have the “account” scope otherwise
the user profile information (username, name, etc.) won’t be accessible.

Configure the appropriate settings for OAuth2 or OAuth1 (see below).

OAuth2
¶

Fill 

Consumer

Key

 and 

Consumer

Secret

 values in the settings:

SOCIAL_AUTH_BITBUCKET_OAUTH2_KEY

=

&#39;&lt;your-consumer-key&gt;&#39;

SOCIAL_AUTH_BITBUCKET_OAUTH2_SECRET

=

&#39;&lt;your-consumer-secret&gt;&#39;

If you would like to restrict access to only users with verified e-mail
addresses, set 

SOCIAL_AUTH_BITBUCKET_OAUTH2_VERIFIED_EMAILS_ONLY

=

True

By default the setting is set to 

False

 since it’s possible for a
project to gather this information by other methods.

OAuth1
¶

OAuth1 works similarly to OAuth2, but you must fill in the following settings
instead:

SOCIAL_AUTH_BITBUCKET_KEY

=

&#39;&lt;your-consumer-key&gt;&#39;

SOCIAL_AUTH_BITBUCKET_SECRET

=

&#39;&lt;your-consumer-secret&gt;&#39;

If you would like to restrict access to only users with verified e-mail
addresses, set 

SOCIAL_AUTH_BITBUCKET_VERIFIED_EMAILS_ONLY

=

True

.
By default the setting is set to 

False

 since it’s possible for a
project to gather this information by other methods.

User ID
¶

Bitbucket recommends the use of 
UUID
 as the user identifier instead
of 

username

 since they can change and impose a security risk. For
that reason 

UUID

 is used by default, but for backward
compatibility reasons, it’s possible to get the old behavior again by
defining this setting:

SOCIAL_AUTH_BITBUCKET_USERNAME_AS_ID

=

True