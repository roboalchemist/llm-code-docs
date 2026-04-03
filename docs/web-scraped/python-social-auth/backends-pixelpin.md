# Backends/Pixelpin

Source: https://python-social-auth.readthedocs.io/en/latest/backends/pixelpin.html

PixelPin
¶

PixelPin only supports OAuth2.

PixelPin OAuth2
¶

Developer documentation for PixelPin can be found at

http://developer.pixelpin.co.uk/
. To setup OAuth2 do the following:

Register a new developer account at 
PixelPin Developers
.

You require a PixelPin account to create developer accounts. Sign up at

PixelPin Account Page
 For the value of redirect uri, use whatever path you
need to return to on your web application. The example code provided with the
plugin uses 

http://&lt;yoursite&gt;/complete/pixelpin-oauth2/

.

Once verified by email, record the values of client id and secret for the
next step.

Fill 
Consumer Key
 and 
Consumer Secret
 values in your settings.py
file:

SOCIAL_AUTH_PIXELPIN_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_PIXELPIN_OAUTH2_SECRET

=

&#39;&#39;

Add 

'social_core.backends.pixelpin.PixelPinOAuth2'

 into your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.