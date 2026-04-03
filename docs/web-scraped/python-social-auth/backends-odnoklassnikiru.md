# Backends/Odnoklassnikiru

Source: https://python-social-auth.readthedocs.io/en/latest/backends/odnoklassnikiru.html

Odnoklassniki.ru
¶

There are two options with Odnoklassniki: either you use OAuth2 workflow to
authenticate odnoklassniki users at external site, or you authenticate users
within your IFrame application.

OAuth2
¶

If you use OAuth2 workflow, you need to:

register a new application with 
OAuth registration form

fill out some settings:

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY

=

&#39;&#39;

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET

=

&#39;&#39;

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME

=

&#39;&#39;

add 

'social_core.backends.odnoklassniki.OdnoklassnikiOAuth2'

 into your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

.

IFrame applications
¶

If you want to authenticate users in your IFrame application,

read 
Rules for application developers

fill out 
Developers registration form

get your personal sandbox

fill out some settings:

SOCIAL_AUTH_ODNOKLASSNIKI_APP_KEY

=

&#39;&#39;

SOCIAL_AUTH_ODNOKLASSNIKI_APP_SECRET

=

&#39;&#39;

SOCIAL_AUTH_ODNOKLASSNIKI_APP_PUBLIC_NAME

=

&#39;&#39;

add 

'social_core.backends.odnoklassniki.OdnoklassnikiApp'

 into your

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

sign a public offer and do some bureaucracy

You may also use:

SOCIAL_AUTH_ODNOKLASSNIKI_APP_EXTRA_USER_DATA_LIST

Defaults to empty tuple, for the list of available fields see 
Documentation on user.getInfo