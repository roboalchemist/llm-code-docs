# Backends/Arcgis

Source: https://python-social-auth.readthedocs.io/en/latest/backends/arcgis.html

ArcGIS
¶

ArcGIS uses OAuth2 for authentication.

Register a new application at 
ArcGIS Developer Center
.

OAuth2
¶

Add the OAuth2 backend to your settings page:

AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.arcgis.ArcGISOAuth2&#39;

,

...

)

Fill 

Client

Id

 and 

Client

Secret

 values in the settings:

SOCIAL_AUTH_ARCGIS_KEY

=

&#39;&#39;

SOCIAL_AUTH_ARCGIS_SECRET

=

&#39;&#39;