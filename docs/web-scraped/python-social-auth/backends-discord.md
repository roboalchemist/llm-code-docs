# Backends/Discord

Source: https://python-social-auth.readthedocs.io/en/latest/backends/discord.html

Discord
¶

Discord uses OAuth2 for authentication.

Register a new application at the 
Discord Developer Portal
, set the
callback URL to 

http://example.com/complete/discord/

 replacing

example.com

 with your domain.

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_DISCORD_KEY

=

&#39;&#39;

SOCIAL_AUTH_DISCORD_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_DISCORD_SCOPE

=

[

...

]

See available scopes at 
Discord OAuth2 Scopes
.