# Backends/Slack

Source: https://python-social-auth.readthedocs.io/en/latest/backends/slack.html

Slack
¶

Slack

Register a new application at 
Slack
, set the callback URL to

http://example.com/complete/slack/

 replacing 

example.com

 with your
domain.

Fill 

Client

ID

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_SLACK_KEY

=

&#39;&#39;

SOCIAL_AUTH_SLACK_SECRET

=

&#39;&#39;

Also it’s possible to define extra permissions with:

SOCIAL_AUTH_SLACK_SCOPE

=

[

...

]

See auth scopes at 
Slack OAuth docs
.

Limiting by team is possible by:

SOCIAL_AUTH_SLACK_TEAM

=

&#39;&#39;