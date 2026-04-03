# Backends/Flickr

Source: https://python-social-auth.readthedocs.io/en/latest/backends/flickr.html

Flickr
¶

Flickr uses OAuth v1.0 for authentication.

Register a new application at the 
Flickr App Garden
, and

fill 

Key

 and 

Secret

 values in the settings:

SOCIAL_AUTH_FLICKR_KEY

=

&#39;&#39;

SOCIAL_AUTH_FLICKR_SECRET

=

&#39;&#39;

Flickr might show a messages saying “Oops! Flickr doesn’t recognise the
permission set.”, if encountered with this error, just define this setting:

SOCIAL_AUTH_FLICKR_AUTH_EXTRA_ARGUMENTS

=

{

&#39;perms&#39;

:

&#39;read&#39;

}