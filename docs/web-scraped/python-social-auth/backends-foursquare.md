# Backends/Foursquare

Source: https://python-social-auth.readthedocs.io/en/latest/backends/foursquare.html

Foursquare
¶

Foursquare uses OAuth2. In order to enable the backend follow:

Register an application at 
Foursquare Developers Portal
,
set the 

Redirect

URI

 to 

http://&lt;your

hostname&gt;/complete/foursquare/

Fill in the 
Client Id
 and 
Client Secret
 values in your settings:

SOCIAL_AUTH_FOURSQUARE_KEY

=

&#39;&#39;

SOCIAL_AUTH_FOURSQUARE_SECRET

=

&#39;&#39;