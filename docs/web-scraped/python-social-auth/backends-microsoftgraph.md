# Backends/Microsoftgraph

Source: https://python-social-auth.readthedocs.io/en/latest/backends/microsoftgraph.html

Microsoft Graph
¶

Go to 
Azure portal
 and create an application.

Fill App Id and Secret in your project settings:

SOCIAL_AUTH_MICROSOFT_GRAPH_KEY

=

&#39;...&#39;

SOCIAL_AUTH_MICROSOFT_GRAPH_SECRET

=

&#39;...&#39;

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.microsoft.MicrosoftOAuth2&#39;

,

...

)

Register an application with the Microsoft identity platform
.