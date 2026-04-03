# Backends/Khanacademy

Source: https://python-social-auth.readthedocs.io/en/latest/backends/khanacademy.html

Khan Academy
¶

Khan Academy uses a variant of OAuth1 authentication flow. Check the API
details at 
Khan Academy API Authentication
.

Follow this steps in order to use the backend:

Register a new application at 
Khan Academy API Apps
,

Fill 
Consumer Key
 and 
Consumer Secret
 values:

SOCIAL_AUTH_KHANACADEMY_OAUTH1_KEY

=

&#39;&#39;

SOCIAL_AUTH_KHANACADEMY_OAUTH1_SECRET

=

&#39;&#39;

Add the backend to 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.khanacademy.KhanAcademyOAuth1&#39;

,

...

)