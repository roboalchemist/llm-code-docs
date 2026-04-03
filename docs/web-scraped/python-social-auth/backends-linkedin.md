# Backends/Linkedin

Source: https://python-social-auth.readthedocs.io/en/latest/backends/linkedin.html

LinkedIn
¶

Sign In with LinkedIn only support OpenID Connect since August 1, 2023. The previous
OAuth2 has been deprecated. See 
LinkedIn OpenID Connect
 for more details.

LinkedIn previously supported OAuth2. Migration between each type is fairly
simple since the same Key / Secret pair is used for both authentication types.

LinkedIn OAuth2 setup is similar to any other OAuth2 service. The auth flow is
explained on 
LinkedIn Developers
 docs. First you will need to register an
app att 
LinkedIn Developer Network
.

OpenID Connect
¶

Fill the application key and secret in your settings:

SOCIAL_AUTH_LINKEDIN_OPENIDCONNECT_KEY

=

&#39;&#39;

SOCIAL_AUTH_LINKEDIN_OPENIDCONNECT_SECRET

=

&#39;&#39;

OAuth2
¶

Fill the application key and secret in your settings:

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET

=

&#39;&#39;

Application scopes can be specified by:

SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE

=

[

...

]

Check the available options at 
LinkedIn Scopes
 (also called as permissions
by LinkedIn). If you want to request a user’s email address, you’ll need
specify that your application needs access to the email address use the

r_emailaddress

 scope.

To request extra fields using 
LinkedIn fields selectors
 just define this
setting:

SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS

=

[

...

]

with the needed fields selectors, also define

SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA

 properly, that way the values will
be stored in 

UserSocialAuth.extra_data

 field. By default 

id

,

firstName

 and 

lastName

 are requested and stored.

For example, to request a user’s email from the Linkedin API and store the
information in 

UserSocialAuth.extra_data

, you would add these settings:

# Add email to requested authorizations.

SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE

=

[

&#39;r_liteprofile&#39;

,

&#39;r_emailaddress&#39;

]

# Add the fields so they will be requested from linkedin.

SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS

=

[

&#39;emailAddress&#39;

]

# Arrange to add the fields to UserSocialAuth.extra_data

SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA

=

[(

&#39;id&#39;

,

&#39;id&#39;

),

(

&#39;firstName&#39;

,

&#39;first_name&#39;

),

(

&#39;lastName&#39;

,

&#39;last_name&#39;

),

(

&#39;emailAddress&#39;

,

&#39;email_address&#39;

)]

Looks like LinkedIn is forcing the definition of the callback URL in the
application when OAuth2 is used. Follow the setup 1 carefully as per 
Linkedin
App Setup
 to add a redirect url/callback url. Be sure to set the proper
values, otherwise a 

(400)

Client

Error:

Bad

Request

 might be returned by
their service.