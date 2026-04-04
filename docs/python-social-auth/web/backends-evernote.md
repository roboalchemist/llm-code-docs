# Backends/Evernote

Source: https://python-social-auth.readthedocs.io/en/latest/backends/evernote.html

Evernote OAuth
¶

Evernote OAuth 1.0 for its authentication workflow.

Register a new application at 
Evernote API Key form
.

Fill 

Consumer

Key

 and 

Consumer

Secret

 values in the settings:

SOCIAL_AUTH_EVERNOTE_KEY

=

&#39;&#39;

SOCIAL_AUTH_EVERNOTE_SECRET

=

&#39;&#39;

Sandbox
¶

Evernote supports a sandbox mode for testing, there’s a custom backend for it
which name is 

evernote-sandbox

 instead of 

evernote

. Same settings apply
but use these instead:

SOCIAL_AUTH_EVERNOTE_SANDBOX_KEY

=

&#39;&#39;

SOCIAL_AUTH_EVERNOTE_SANDBOX_SECRET

=

&#39;&#39;