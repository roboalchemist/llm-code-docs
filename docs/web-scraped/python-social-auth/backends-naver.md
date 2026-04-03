# Backends/Naver

Source: https://python-social-auth.readthedocs.io/en/latest/backends/naver.html

Naver
¶

Naver uses OAuth v2 for Authentication.

Register a new application at the 
Naver API
, and

add naver oauth backend to your settings page:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.naver.NaverOAuth2&#39;

,

...

)

fill 

Client

ID

 and 

Client

Secret

 from developer.naver.com
values in the settings:

SOCIAL_AUTH_NAVER_KEY

=

&#39;&#39;

SOCIAL_AUTH_NAVER_SECRET

=

&#39;&#39;

you can get EXTRA_DATA:

SOCIAL_AUTH_NAVER_EXTRA_DATA

=

[

&#39;nickname&#39;

,

&#39;gender&#39;

,

&#39;age&#39;

,

&#39;birthday&#39;

,

&#39;profile_image&#39;

]