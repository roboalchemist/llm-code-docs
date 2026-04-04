# Backends/Kakao

Source: https://python-social-auth.readthedocs.io/en/latest/backends/kakao.html

Kakao
¶

Kakao uses OAuth v2 for Authentication.

Register a new applicationat the 
Kakao API
, and

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_KAKAO_KEY

=

&#39;&#39;

SOCIAL_AUTH_KAKAO_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_KAKAO_SCOPE

=

[

...

]