# Backends/Mineid

Source: https://python-social-auth.readthedocs.io/en/latest/backends/mineid.html

MineID
¶

MineID works similar to Facebook (OAuth).

Register a new application at 
MineID.org
, set the callback URL to

http://example.com/complete/mineid/

 replacing 

example.com

 with your
domain.

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_MINEID_KEY

=

&#39;&#39;

SOCIAL_AUTH_MINEID_SECRET

=

&#39;&#39;

Self-hosted MineID
¶

Since MineID is an Open Source software and can be self-hosted, you can
change settings to point to your instance:

SOCIAL_AUTH_MINEID_HOST

=

&#39;www.your-mineid-instance.com&#39;

SOCIAL_AUTH_MINEID_SCHEME

=

&#39;https&#39;

# or &#39;http&#39;