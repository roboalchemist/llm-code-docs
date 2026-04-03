# Backends/Coursera

Source: https://python-social-auth.readthedocs.io/en/latest/backends/coursera.html

Coursera
¶

Coursera uses a variant of OAuth2 authentication. The details of the API
can be found at 
OAuth2-based APIs - Coursera Technology
.

Take the following steps in order to use the backend:

Create an account at 
Coursera
.

Open 
Developer Console
, create an organisation and application.

3. Set 
Client ID
 as a 

SOCIAL_AUTH_COURSERA_KEY

 and

Secret Key
 as a 

SOCIAL_AUTH_COURSERA_SECRET

 in your local settings.

Add the backend to 

AUTHENTICATION_BACKENDS

 setting:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.coursera.CourseraOAuth2&#39;

,

...

)