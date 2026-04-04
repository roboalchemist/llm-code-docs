# Backends/Amazon

Source: https://python-social-auth.readthedocs.io/en/latest/backends/amazon.html

Amazon
¶

Amazon implemented OAuth2 protocol for their authentication mechanism. To
enable 

python-social-auth

 support follow this steps:

Go to 
Amazon App Console
 and create an application.

Fill App Id and Secret in your project settings:

SOCIAL_AUTH_AMAZON_KEY

=

&#39;...&#39;

SOCIAL_AUTH_AMAZON_SECRET

=

&#39;...&#39;

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.amazon.AmazonOAuth2&#39;

,

...

)

Further documentation at 
Website Developer Guide
 and 
Getting Started for Web
.

Note:
 This backend supports TLSv1 protocol since SSL will be deprecated

from May 25, 2015