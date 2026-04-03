# Backends/Apple

Source: https://python-social-auth.readthedocs.io/en/latest/backends/apple.html

AppleID
¶

Apple ID implemented OAuth2 and OpenID Connect protocols for their authentication mechanism. To
enable 

python-social-auth

 support follow this steps:

Go to 
Apple Developer Portal
 and

Create or select an existing App ID

Create a Sign Certificate

Create a Services ID
, activate “Sign In with Apple” and grant your “return URLs”

Fill App Id and Secret in your project settings:

SOCIAL_AUTH_APPLE_ID_CLIENT

=

&#39;...&#39;

# Your client_id com.application.your, aka &quot;Service ID&quot;

SOCIAL_AUTH_APPLE_ID_TEAM

=

&#39;...&#39;

# Your Team ID, ie K2232113

SOCIAL_AUTH_APPLE_ID_KEY

=

&#39;...&#39;

# Your Key ID, ie Y2P99J3N81K

SOCIAL_AUTH_APPLE_ID_SECRET

=

&quot;&quot;&quot;

-----BEGIN PRIVATE KEY-----

MIGTAgE.....

-----END PRIVATE KEY-----&quot;&quot;&quot;

SOCIAL_AUTH_APPLE_ID_SCOPE

=

[

&#39;email&#39;

,

&#39;name&#39;

]

SOCIAL_AUTH_APPLE_ID_EMAIL_AS_USERNAME

=

True

# If you want to use email as username

Enable the backend:

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.apple.AppleIdAuth&#39;

,

...

)

Further documentation at 
Website Developer Guide
 and 
Getting Started
.