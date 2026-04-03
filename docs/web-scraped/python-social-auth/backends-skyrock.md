# Backends/Skyrock

Source: https://python-social-auth.readthedocs.io/en/latest/backends/skyrock.html

Skyrock
¶

OAuth based Skyrock Connect.

Skyrock offers per application keys named 

Consumer

Key

 and 

Consumer

Secret

. To enable Skyrock these two keys are needed. Further documentation
at 
Skyrock developer resources
:

Register a new application at 
Skyrock App Creation
,

Your callback domain should match your application URL in your application
configuration.

Fill 
Consumer Key
 and 
Consumer Secret
 values:

SOCIAL_AUTH_SKYROCK_KEY

=

&#39;&#39;

SOCIAL_AUTH_SKYROCK_SECRET

=

&#39;&#39;