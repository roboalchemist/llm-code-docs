# Backends/Digitalocean

Source: https://python-social-auth.readthedocs.io/en/latest/backends/digitalocean.html

DigitalOcean
¶

DigitalOcean uses OAuth2 for its auth process. See the full 
DigitalOcean
developer’s documentation
 for more information.

Register a new application in the 
Apps &amp; API page
 in the DigitalOcean
control panel, setting the callback URL to 

http://example.com/complete/digitalocean/

replacing 

example.com

 with your domain.

Fill the 

Client

ID

 and 

Client

Secret

 values from GitHub in the settings:

SOCIAL_AUTH_DIGITALOCEAN_KEY

=

&#39;&#39;

SOCIAL_AUTH_DIGITALOCEAN_SECRET

=

&#39;&#39;

By default, only 

read

 permissions are granted. In order to create,
destroy, and take other actions on the user’s resources, you must request

read

write

 permissions like so:

SOCIAL_AUTH_DIGITALOCEAN_AUTH_EXTRA_ARGUMENTS

=

{

&#39;scope&#39;

:

&#39;read write&#39;

}