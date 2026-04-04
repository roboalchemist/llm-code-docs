# Backends/Docker

Source: https://python-social-auth.readthedocs.io/en/latest/backends/docker.html

Docker
¶

Docker.io OAuth2
¶

Docker.io now supports OAuth2 for their API. In order to set it up:

Register a new application by following the instructions in their website:

Register Your Application

Fill 
Consumer Key
 and 
Consumer Secret
 values in settings:

SOCIAL_AUTH_DOCKER_KEY

=

&#39;&#39;

SOCIAL_AUTH_DOCKER_SECRET

=

&#39;&#39;

Add 

'social_core.backends.docker.DockerOAuth2'

 into your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.