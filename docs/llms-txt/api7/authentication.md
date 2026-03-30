# Source: https://docs.api7.ai/enterprise-whitepaper/features/authentication.md

# Source: https://docs.api7.ai/enterprise-whitepaper/tags/authentication.md

# Source: https://docs.api7.ai/enterprise/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/authentication.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/authentication.md

# Source: https://docs.api7.ai/cloud/references/plugins/traffic-management/authentication.md

# Source: https://docs.api7.ai/cloud/guides/traffic-management/authentication.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/authentication.md

# Source: https://docs.api7.ai/cloud/references/plugins/traffic-management/authentication.md

# Source: https://docs.api7.ai/cloud/guides/traffic-management/authentication.md

# Authentication

Besides the original Apache APISIX authentication plugins, API7 Cloud also provides another authentication plugin, which integrates five auth methods and provides a well-designed UI form.

You can visit the following docs to learn how to use each auth method in this plugin.

* [Basic Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/basic-auth.md)
* [Key Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/key-auth.md)
* [HMAC Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/hmac-auth.md)
* [JWT Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/jwt-auth.md)
* [OpenID Connect Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/openid-connect.md)

tip

Note that you can simultaneously use this authentication plugin with the original Apache APISIX authentication plugins. In such a case, your API requests must pass all verifications of these plugins, or the gateway will reject them.
