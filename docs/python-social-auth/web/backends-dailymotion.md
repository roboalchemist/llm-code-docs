# Backends/Dailymotion

Source: https://python-social-auth.readthedocs.io/en/latest/backends/dailymotion.html

DailyMotion
¶

DailyMotion uses OAuth2. In order to enable the backend follow:

Register an application at 
DailyMotion Developer Portal

Fill in the 
Client Id
 and 
Client Secret
 values in your settings:

SOCIAL_AUTH_DAILYMOTION_KEY

=

&#39;&#39;

SOCIAL_AUTH_DAILYMOTION_SECRET

=

&#39;&#39;

Set the 

Callback

URL

 to 

http://&lt;your

hostname&gt;/complete/dailymotion/

Specify scopes with:

SOCIAL_AUTH_DAILYMOTION_SCOPE

=

[

...

]

Available scopes are listed in the 
Requesting Extended Permissions

section.