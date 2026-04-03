# Backends/Nfdi

Source: https://python-social-auth.readthedocs.io/en/latest/backends/nfdi.html

NFDI (OpenID Connect)
¶

The 
NFDI
 backend allows authentication against all OIDC providers of 
NFDI

(German National Research Data Infrastructure) and also for the Helmholtz
AAI. These backends provides their endpoints, as well as the
default scopes.

The provided backends are:

`

XcsOpenIdConnect

TextplusOpenIdConnect

MardiOpenIdConnect

ObjectsOpenIdConnect

CultureOpenIdConnect

CatOpenIdConnect

ChemOpenIdConnect

DatascienceOpenIdConnect

EnergyOpenIdConnect

IngOpenIdConnect

MatWerkOpenIdConnect

DaphneOpenIdConnect

FairmatOpenIdConnect

ImmunoOpenIdConnect

PunchOpenIdConnect

HelmholtzOpenIdConnect

InfraproxyStagingOpenIdConnect

InfraproxyOpenIdConnect

EduidOpenIdConnect

EduidStagingOpenIdConnect

`

A minimum configuration is:

SOCIAL_AUTH_OIDC_KEY

=

&#39;&lt;client_id&gt;&#39;

SOCIAL_AUTH_OIDC_SECRET

=

&#39;&lt;client_secret&gt;&#39;

The remaining configuration will be auto-detected, by fetching:

&lt;

OIDC_ENDPOINT

&gt;/.

well

-

known

/

openid

-

configuration

This class can be used standalone, but may also be used as the base class for some other
backends. Find more information at the 
NFDI_AAI_WEBSITE

Username
¶

The 
NFDI
 backend will check for a 

preferred_username

 key in the values
returned by the server.  If the username is under a different key, this can
be overridden:

SOCIAL_AUTH_OIDC_USERNAME_KEY

=

&#39;nickname&#39;

This setting indicates that the username should be populated by the

nickname

 claim instead.

Scopes
¶

The default set of scopes requested are those configured by default in the
cleass. You can request additional claims, for example:

SOCIAL_AUTH_OIDC_SCOPE

=

[

&#39;groups&#39;

]