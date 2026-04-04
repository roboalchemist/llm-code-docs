# Backends/Strava

Source: https://python-social-auth.readthedocs.io/en/latest/backends/strava.html

Strava
¶

Strava uses OAuth v2 for Authentication.

Register a new application at the 
Strava API
, and

fill 

Client

ID

 and 

Client

Secret

 from strava.com values in the settings:

SOCIAL_AUTH_STRAVA_KEY

=

&#39;&#39;

SOCIAL_AUTH_STRAVA_SECRET

=

&#39;&#39;

extra scopes can be defined by using:

SOCIAL_AUTH_STRAVA_SCOPE

=

[

&#39;view_private&#39;

]