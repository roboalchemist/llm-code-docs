# Backends/Quizlet

Source: https://python-social-auth.readthedocs.io/en/latest/backends/quizlet.html

Quizlet
¶

Quizlet uses OAuth v2 for Authentication.

Register a new application at the 
Quizlet API
, and

Add the Quizlet backend to 

AUTHENTICATION_SETTINGS

:

AUTHENTICATION_SETTINGS

=

(

...

&#39;social_core.backends.quizlet.QuizletOAuth2&#39;

,

...

)

fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_QUIZLET_KEY

=

&#39;&#39;

SOCIAL_AUTH_QUIZLET_SECRET

=

&#39;&#39;

SOCIAL_AUTH_QUIZLET_SCOPE

=

[

&#39;read&#39;

,

&#39;write_set&#39;

]

# &#39;write_group&#39; is also available