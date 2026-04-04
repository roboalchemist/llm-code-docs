# Backends/Jawbone

Source: https://python-social-auth.readthedocs.io/en/latest/backends/jawbone.html

Jawbone
¶

Jawbone uses OAuth2. In order to enable the backend follow:

Register an application at 
Jawbone Developer Portal
, set the 

OAuth

redirect

URIs

 to 

http://&lt;your

hostname&gt;/complete/jawbone/

Fill in the 
Client Id
 and 
Client Secret
 values in your settings:

SOCIAL_AUTH_JAWBONE_KEY

=

&#39;&#39;

SOCIAL_AUTH_JAWBONE_SECRET

=

&#39;&#39;

Specify scopes with:

SOCIAL_AUTH_JAWBONE_SCOPE

=

[

...

]

Available scopes are listed in the 
Jawbone Authentication Reference
,
“socpes” section.