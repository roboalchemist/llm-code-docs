# Backends/Shopify

Source: https://python-social-auth.readthedocs.io/en/latest/backends/shopify.html

Shopify
¶

Shopify uses OAuth 2 for authentication.

To use this backend, you must:

Install the 
Shopify python library
:

pip

install

--

upgrade

ShopifyAPI

Register a new application at 
Shopify Partners

Configure your Shopify app to use the application URL of 
https://[your domain]/login/shopify/

Configure your Shopify app to use the callback URL of 
https://[your domain]/complete/shopify/

If you’re using Django, add the backend to your AUTHENTICATION_BACKENDS configuration:

AUTHENTICATION_BACKENDS

=

(

...

,

&#39;social_core.backends.shopify.ShopifyOAuth2&#39;

,

...

,

)

fill 

API

Key

 and 

Shared

Secret

 values in your django settings:

SOCIAL_AUTH_SHOPIFY_KEY

=

&#39;&#39;

SOCIAL_AUTH_SHOPIFY_SECRET

=

&#39;&#39;

fill the scope permissions that you require into the settings 
Shopify API
:

SOCIAL_AUTH_SHOPIFY_SCOPE

=

[

&#39;write_script_tags&#39;

,

&#39;read_orders&#39;

,

&#39;write_customers&#39;

,

&#39;read_products&#39;

]

If you’d like to, you can set your desired Shopify API version in your settings:

SOCIAL_AUTH_SHOPIFY_API_VERSION

=

&#39;2020-10&#39;

ShopifyAPI 5.0.0
 introduced a non backward compatible change in order to
support Shopify API versioning. The backend will default to value 
2019-04
 but
it’s possible to override the default with the following setting:

SOCIAL_AUTH_SHOPIFY_API_VERSION

=

&#39;unstable&#39;