# Backends/Trello

Source: https://python-social-auth.readthedocs.io/en/latest/backends/trello.html

Trello
¶

Trello provides OAuth1 support for their authentication process.

In order to enable it, follow:

Generate an Application Key pair at 
Trello Developers API Keys

Fill 
Consumer Key
 and 
Consumer Secret
 settings:

SOCIAL_AUTH_TRELLO_KEY

=

&#39;...&#39;

SOCIAL_AUTH_TRELLO_SECRET

=

&#39;...&#39;

There are also two optional settings:

your app name, otherwise the authorization page will say “Let An unknown application use your account?”:

SOCIAL_AUTH_TRELLO_APP_NAME

=

&#39;My App&#39;

the expiration period, social auth defaults to ‘never’, but you can change it:

SOCIAL_AUTH_TRELLO_EXPIRATION

=

&#39;30days&#39;