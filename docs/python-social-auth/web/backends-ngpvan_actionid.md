# Backends/Ngpvan_Actionid

Source: https://python-social-auth.readthedocs.io/en/latest/backends/ngpvan_actionid.html

NGP VAN ActionID
¶

NGP VAN
’s 
ActionID
 service provides an OpenID 1.1 endpoint, which provides
first name, last name, email address, and phone number.

ActionID doesn’t require major settings beside being defined on

AUTHENTICATION_BACKENDS

SOCIAL_AUTH_AUTHENTICATION_BACKENDS

=

(

...

&#39;social_core.backends.ngpvan.ActionIDOpenID&#39;

,

...

)

If you want to be able to access the “phone” attribute offered by NGP VAN
within 

extra_data

 you can add the following to your settings:

SOCIAL_AUTH_ACTIONID_OPENID_AX_EXTRA_DATA

=

[

(

&#39;http://openid.net/schema/contact/phone/business&#39;

,

&#39;phone&#39;

)

]

NGP VAN offers the ability to have your domain whitelisted, which will disable
the “{domain} is requesting a link to your ActionID” warning when your app
attempts to login using an ActionID account. Contact

NGP VAN Developer Support
 for more information