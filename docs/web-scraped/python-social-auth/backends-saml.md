# Backends/Saml

Source: https://python-social-auth.readthedocs.io/en/latest/backends/saml.html

SAML
¶

The SAML backend allows users to authenticate with any provider that supports
the SAML 2.0 protocol (commonly used for corporate or academic single sign on).

The SAML backend for python-social-auth allows your web app to act as a SAML
Service Provider. You can configure one or more SAML Identity Providers that
users can use for authentication. For example, if your users are students, you
could enable Harvard and MIT as identity providers, so that students of either
of those two universities can use their campus login to access your app.

Required Dependency
¶

You need to install 
python3-saml
, this is included in the 

saml

 extra when
installing 

social-core

.

In case you run into 

lxml

&amp;

xmlsec

libxml2

library

version

mismatch

 error,
it is caused by 

lxml

 being built against a different version of 

libxml2

than 

xmlsec

. To avoid this, please install both packages from the source
and build them against system libraries:

# Install system dependencies

sudo

apt

install

libxmlsec1-dev

# Install Python packages from the source

pip

install

--no-binary

lxml

--no-binary

xmlsec

-e

&#39;social-core[saml]&#39;

Required Configuration
¶

At a minimum, you must add the following to your project’s settings:

SOCIAL_AUTH_SAML_SP_ENTITY_ID

: The SAML Entity ID for your app. This
should be a URL that includes a domain name you own. It doesn’t matter what
the URL points to. Example: 

http://saml.yoursite.com

SOCIAL_AUTH_SAML_SP_PUBLIC_CERT

: The X.509 certificate string for the
key pair that your app will use. You can generate a new self-signed key pair
with:

openssl

req

-

new

-

x509

-

days

3652

-

nodes

-

out

saml

.

crt

-

keyout

saml

.

key

The contents of 

saml.crt

 should then be used as the value of this setting
(you can omit the first and last lines, which aren’t required).

SOCIAL_AUTH_SAML_SP_PRIVATE_KEY

: The private key to be used by your app.
If you used the example openssl command given above, set this to the contents
of 

saml.key

 (again, you can omit the first and last lines).

SOCIAL_AUTH_SAML_ORG_INFO

: A dictionary that contains information about
your app. You must specify values for English at a minimum. Each language’s
entry should specify a 

name

 (not shown to the user), a 

displayname

(shown to the user), and a URL. See the following
example:

{

&quot;en-US&quot;

:

{

&quot;name&quot;

:

&quot;example&quot;

,

&quot;displayname&quot;

:

&quot;Example Inc.&quot;

,

&quot;url&quot;

:

&quot;http://example.com&quot;

,

}

}

SOCIAL_AUTH_SAML_TECHNICAL_CONTACT

: A dictionary with two values,

givenName

 and 

emailAddress

, describing the name and email of a
technical contact responsible for your app. Example:

{

&quot;givenName&quot;

:

&quot;Tech Gal&quot;

,

&quot;emailAddress&quot;

:

&quot;technical@example.com&quot;

}

SOCIAL_AUTH_SAML_SUPPORT_CONTACT

: A dictionary with two values,

givenName

 and 

emailAddress

, describing the name and email of a
support contact for your app. Example:

{

&quot;givenName&quot;

:

&quot;Support Guy&quot;

,

&quot;emailAddress&quot;

:

&quot;support@example.com&quot;

,

}

SOCIAL_AUTH_SAML_ENABLED_IDPS

: The most important setting. List the Entity
ID, SSO URL, and x.509 public key certificate for each provider that your app
wants to support. The SSO URL must support the 

HTTP-Redirect

 binding.
You can get these values from the provider’s XML metadata. Here’s an example,
for 
TestShib
 (the values come from TestShib’s 
metadata
):

{

&quot;testshib&quot;

:

{

&quot;entity_id&quot;

:

&quot;https://idp.testshib.org/idp/shibboleth&quot;

,

&quot;url&quot;

:

&quot;https://idp.testshib.org/idp/profile/SAML2/Redirect/SSO&quot;

,

&quot;x509cert&quot;

:

&quot;MIIEDjCCAvagAwIBAgIBADA ... 8Bbnl+ev0peYzxFyF5sQA==&quot;

,

}

}

Each IDP can define configuration keys to avoid having to use uniform resource
name’s (ie: 

urn:oid:0.9.2342.19200300.100.1.3

 for email address) as
attributes to map user details required to complete account creation. The
values associated with the attr_* keys correspond to the keys specified as
attributes in the IDP.

Important

Version 4.8.0+ Behavior Change:

When you explicitly configure an attribute (e.g., 

attr_first_name

), that
attribute 
must
 be present in the SAML response from the IdP. If it is
missing, authentication will fail with an error like:

Missing

needed

parameter

first_name

(configured

by

attr_first_name)

.

Options:

Remove the configuration
 if the attribute is not provided by your IdP.
The backend will automatically try to map using built-in attribute names.

Ensure your IdP provides the attribute
 with the exact name you configured.

Use the correct attribute name
 from your IdP’s SAML response (check
the actual attribute names sent by your IdP).

Extending on the “testshib” example:

{

&quot;testshib&quot;

:

{

&quot;entity_id&quot;

:

&quot;https://idp.testshib.org/idp/shibboleth&quot;

,

&quot;url&quot;

:

&quot;https://idp.testshib.org/idp/profile/SAML2/Redirect/SSO&quot;

,

&quot;x509cert&quot;

:

&quot;MIIEDjCCAvagAwIBAgIBADA ... 8Bbnl+ev0peYzxFyF5sQA==&quot;

,

&quot;attr_user_permanent_id&quot;

:

&quot;email&quot;

,

&quot;attr_first_name&quot;

:

&quot;first_name&quot;

,

&quot;attr_last_name&quot;

:

&quot;last_name&quot;

,

&quot;attr_username&quot;

:

&quot;email&quot;

,

&quot;attr_email&quot;

:

&quot;email&quot;

,

}

}

In this example, the attr_user_permanent_id and attr_email are both set to the
email address passed back in the attribute key ‘email’.

Note: testshib does not provide email as an attribute. This was tested using
Okta and G Suite (formerly Google Apps for Business).

Built-in Attribute Mappings:

If you omit the 

attr_*

 configuration keys, the backend will automatically
try to extract user details using a list of commonly used attribute names,
including both namespaced URN variants (like

http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname

) and
simple names (like 

first_name

, 

firstName

, 

given_name

). Missing
attributes will be silently ignored when using the built-in mappings.

Basic Usage
¶

Set all of the required configuration variables described above.

Generate the SAML XML metadata for your app. The best way to do this is to
create a new view/page/URL in your app that will call the backend’s

generate_metadata_xml()

 method. Here’s an example of how to do this in
Django:

def

saml_metadata_view

(

request

):

complete_url

=

reverse

(

&#39;social:complete&#39;

,

args

=

(

&quot;saml&quot;

,

))

saml_backend

=

load_backend

(

load_strategy

(

request

),

&quot;saml&quot;

,

redirect_uri

=

complete_url

,

)

metadata

,

errors

=

saml_backend

.

generate_metadata_xml

()

if

not

errors

:

return

HttpResponse

(

content

=

metadata

,

content_type

=

&#39;text/xml&#39;

)

Download the metadata for your app that was generated by the above method,
and send it to each Identity Provider (IdP) that you wish to use. Each IdP
must install and configure your metadata on their system before it will work.

Now everything is set! To allow users to login with any given IdP, you need to
give them a link to the python-social-auth “begin”/”auth” URL and include an

idp

 query parameter that specifies the name of the IdP to use. This is
needed since the backend supports multiple IdPs. The names of the IdPs are the
keys used in the 

SOCIAL_AUTH_SAML_ENABLED_IDPS

 setting.

Django example:

# In view:

context

[

&#39;testshib_url&#39;

]

=

u

&quot;

{base}

?

{params}

&quot;

.

format

(

base

=

reverse

(

&#39;social:begin&#39;

,

kwargs

=

{

&#39;backend&#39;

:

&#39;saml&#39;

}),

params

=

urllib

.

urlencode

({

&#39;next&#39;

:

&#39;/home&#39;

,

&#39;idp&#39;

:

&#39;testshib&#39;

})

)

# In template:

&lt;

a

href

=

&quot;{{ testshib_url }}&quot;

&gt;

TestShib

Login

&lt;/

a

&gt;

# Result:

&lt;

a

href

=

&quot;/login/saml/?next=

%2F

home&amp;amp;idp=testshib&quot;

&gt;

TestShib

Login

&lt;/

a

&gt;

Testing with the 
TestShib
 provider is recommended, as it is known to work
well.

Advanced Settings
¶

SOCIAL_AUTH_SAML_SP_EXTRA

: This can be set to a dict, and any key/value
pairs specified here will be passed to the underlying 

python-saml

 library
configuration’s 

sp

 setting. Refer to the 

python-saml

 documentation for
details.

To publish a rollover certificate in advance of changing, use

SOCIAL_AUTH_SAML_SP_EXTRA

 to set 

['sp']['x509certNew']

 of 

python-saml

:

{

&quot;x509certNew&quot;

:

&quot;MIIEDjCCAvagAwIBAgIBADA ... 8Bbnl+ev0peYzxFyF5sQA==&quot;

,

}

SOCIAL_AUTH_SAML_SECURITY_CONFIG

: This can be set to a dict, and any
key/value pairs specified here will be passed to the underlying

python-saml

 library configuration’s 

security

 setting. Two useful keys
that you can set are 

metadataCacheDuration

 and 

metadataValidUntil

,
which control the expiry time of your XML metadata. By default, a cache
duration of 10 days will be used, which means that IdPs are allowed to cache
your metadata for up to 10 days, but no longer. 

metadataCacheDuration

 must
be specified as an ISO 8601 duration string (e.g. 
P1D
 for one day).

SOCIAL_AUTH_SAML_EXTRA_DATA

: This can be set to a list of tuples similar
to the OAuth backend setting. It maps IDP attributes to extra_data attributes.
Each attribute will be a list of values (even if only 1 value) per how

python3-saml
 processes attributes:

SOCIAL_AUTH_SAML_EXTRA_DATA

=

[(

&#39;attribute_name&#39;

,

&#39;extra_data_name_for_attribute&#39;

),

(

&#39;department&#39;

,

&#39;department&#39;

),

(

&#39;manager_full_name&#39;

,

&#39;manager_full_name&#39;

)]

In 

SOCIAL_AUTH_SAML_ENABLED_IDPS

: 

x509certMulti[&quot;signing&quot;]

 is a list
that can be used instead of 

x509cert

. For example, when the IdP
certificate is rotated, use:

SOCIAL_AUTH_SAML_ENABLED_IDPS

=

{

&quot;my_idp&quot;

:

{

&quot;entity_id&quot;

:

&quot;https://...&quot;

,

&quot;url&quot;

:

&quot;https://...&quot;

,

&quot;x509certMulti&quot;

:

{

&quot;signing&quot;

:

[

# Old certificate

&quot;&quot;&quot;

  -----BEGIN CERTIFICATE-----

  MIIEDjCCAvagAwIBAgIBADA ...

  -----END CERTIFICATE-----

               &quot;&quot;&quot;

,

# New certificate

&quot;&quot;&quot;

  -----BEGIN CERTIFICATE-----

  8Bbnl+ev0peYzxFyF5sQA ...

  -----END CERTIFICATE-----

               &quot;&quot;&quot;

]

}

}

}

Advanced Usage
¶

You can subclass the 

SAMLAuth

 backend to provide custom functionality. In
particular, there are two methods that are designed for subclasses to override:

get_idp(self,

idp_name)

: Given the name of an IdP, return an instance of

SAMLIdentityProvider

 with the details of the IdP. Override this method if
you wish to use some other method for configuring the available identity
providers, such as fetching them at runtime from another server, or using a
list of providers from a Shibboleth federation.

_check_entitlements(self,

idp,

attributes)

: This method gets called during
the login process and is where you can decide to accept or reject a user based
on the user’s SAML attributes. For example, you can restrict access to your
application to only accept users who belong to a certain department. After
inspecting the passed attributes parameter, do nothing to allow the user to
login, or raise 

social_core.exceptions.AuthForbidden

 to reject the user.

Troubleshooting
¶

Error: “Missing needed parameter first_name (configured by attr_first_name)”

This error occurs when you have explicitly configured an attribute mapping (like

attr_first_name

) but your IdP is not providing that attribute in the SAML
response.

Solution:

Check what attributes your IdP actually provides.
 Inspect the SAML
response from your IdP to see the exact attribute names being sent.

Remove unused attribute configurations.
 If your IdP doesn’t provide

first_name

, simply remove 

&quot;attr_first_name&quot;:

&quot;first_name&quot;

 from your
configuration. The backend will try to use built-in mappings instead.

Use the correct attribute name.
 If your IdP provides the attribute with
a different name (e.g., 

givenName

 or a namespaced URN like

http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname

), use
that name in your configuration:

&quot;attr_first_name&quot;

:

&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname&quot;

,

Configure your IdP
 to include the attribute in the SAML response if you
need it.

Example:
 For Google G Suite SSO, if you’re not receiving 

first_name

 and

last_name

 attributes, remove those configurations and let the backend use
its built-in mappings:

SOCIAL_AUTH_SAML_ENABLED_IDPS

=

{

&quot;gsuite&quot;

:

{

&quot;entity_id&quot;

:

&quot;...&quot;

,

&quot;url&quot;

:

&quot;...&quot;

,

&quot;x509cert&quot;

:

&quot;...&quot;

,

&quot;attr_user_permanent_id&quot;

:

&quot;email&quot;

,

&quot;attr_username&quot;

:

&quot;email&quot;

,

&quot;attr_email&quot;

:

&quot;email&quot;

,

# Remove attr_first_name and attr_last_name if not provided by IdP

}

}