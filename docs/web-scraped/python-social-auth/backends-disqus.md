# Backends/Disqus

Source: https://python-social-auth.readthedocs.io/en/latest/backends/disqus.html

Disqus
¶

Disqus uses OAuth v2 for Authentication.

Register a new application at the 
Disqus API
, and

fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_DISQUS_KEY

=

&#39;&#39;

SOCIAL_AUTH_DISQUS_SECRET

=

&#39;&#39;

extra scopes can be defined by using:

SOCIAL_AUTH_DISQUS_AUTH_EXTRA_ARGUMENTS

=

{

&#39;scope&#39;

:

&#39;likes comments relationships&#39;

}

Check 
Disqus Auth API
 for details.