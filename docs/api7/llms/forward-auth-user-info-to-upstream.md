# Source: https://docs.api7.ai/enterprise/best-practices/forward-auth-user-info-to-upstream.md

# Forward User Information from External Authentication to Upstream

When using authentication plugins such as [OpenID Connect](https://docs.api7.ai/hub/openid-connect.md) or [SAML Auth](https://docs.api7.ai/hub/saml-auth.md), you may need to pass authenticated user information to upstream services. This enables upstream applications to implement additional business logic based on user identity, such as personalization, auditing, and access control.

This guide uses Azure AD (Microsoft Entra ID) as the example identity provider.

This guide covers two solutions:

1. **Associate consumer name with external authentication**: Set a resolved user identifier (for example, `sub` or `name_id`) as the `consumer_name` for the current request.
2. **Forward user information headers to upstream**: Pass the resolved user information to upstream services via custom request headers.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/getting-started/launch-your-first-api.md).

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route in API7 Dashboard for the upstream service you want to protect.

![Create a route](https://static.api7.ai/uploads/2026/01/27/yK5yfSik_0-create-routes.png)

## Associate Consumer Name with External Authentication[â](#associate-consumer-name-with-external-authentication "Direct link to Associate Consumer Name with External Authentication")

After successful authentication, both `openid-connect` and `saml-auth` store user information in `ctx.external_user`. Configure `serverless-post-function` to run in the `rewrite` phase, and place it after the authentication plugin on the route so `ctx.external_user` is already populated.

### Using OpenID Connect[â](#using-openid-connect "Direct link to Using OpenID Connect")

#### Configure the OpenID Connect Plugin[â](#configure-the-openid-connect-plugin "Direct link to Configure the OpenID Connect Plugin")

Log in to the [Azure portal](https://portal.azure.com/), go to the **App registrations**Â service and register a new application.

![azure-ad-create-an-app](https://static.api7.ai/uploads/2026/01/28/f8O4bjzB_register-new-app.png)

Configure the redirect URI in the IdP and the plugin:

![Configure the OpenID Connect redirect URL](https://static.api7.ai/uploads/2026/01/27/ZTTI6dd6_1-plugin-openid-connect-config-redirect-url.png)

Set the token version to v2:

![Set token version to v2](https://static.api7.ai/uploads/2026/01/27/n8OWJjPz_2-plugin-openid-connect-set-token-version.png)

Copy the client information (such as `client_id` and `client_secret`) from the IdP:

![Copy OpenID Connect client information](https://static.api7.ai/uploads/2026/01/27/R1ZlLYbp_2-plugin-openid-connect-copy-info.png)

![Copy OpenID Connect client secret](https://static.api7.ai/uploads/2026/01/28/uSAxQffr_oidc-client-secret.png)

Configure the `openid-connect` plugin on the route. Replace the highlighted configuration with your values:

openid-connect

```
bearer_only: false
client_id: de90e86d-d632-4861-99cf-4a97fb2482fe
client_secret: Jex8Q~O.EwzJUQrwL.ji4eK4zCSgpmc4LZtLBbR1
discovery: https://login.microsoftonline.com/a7a70f5e-0b17-4a67-90ab-9e85ff6d9f59/v2.0/.well-known/openid-configuration
redirect_uri: https://your-gateway.com/anything/callback
required_scopes:
  - openid
scope: openid email profile
session:
  secret: f86cf31663a9c9fa0a28c2cc78badef1
```

![Configure the OpenID Connect plugin](https://static.api7.ai/uploads/2026/01/27/lH4Nnw5Y_3-plugin-openid-connect-config.png)

#### Set `consumer_name` with `serverless-post-function`[â](#set-consumer_name-with-serverless-post-function "Direct link to set-consumer_name-with-serverless-post-function")

Use the resolved `sub` in `ctx.external_user` to set the request `consumer_name`:

serverless-post-function

```
phase: rewrite
functions:
  - |
    return function(conf, ctx)
        local core = require("apisix.core")
        core.log.warn(
            "ctx.external_user: ",
            core.json.encode(ctx.external_user, true)
        )
        if type(ctx.external_user) == "table" and ctx.external_user.sub then
            ctx.consumer_name = ctx.external_user.sub
            core.log.warn("consumer_name: ", ctx.consumer_name)
        end
    end
```

![Configure serverless-post-function to set consumer\_name](https://static.api7.ai/uploads/2026/01/27/le15bBhB_4-plugin-openid-connect-config-serverless-to-set-consumer-name.png)

#### Verify[â](#verify "Direct link to Verify")

Visit the route in browser to complete OpenID Connect authentication:

![Visit the route for OpenID Connect authentication](https://static.api7.ai/uploads/2026/01/27/95igHnbh_5-plugin-openid-connect-visist.png)

Check the gateway access log to verify that `consumer_name` is set:

![Check access log for consumer\_name](https://static.api7.ai/uploads/2026/01/27/y3o4jeGL_6-plugin-openid-connect-check-log-see-consumer_name.png)

### Using SAML Auth[â](#using-saml-auth "Direct link to Using SAML Auth")

#### Configure the SAML Auth Plugin[â](#configure-the-saml-auth-plugin "Direct link to Configure the SAML Auth Plugin")

Log in to the [Azure portal](https://portal.azure.com/), go to the **Enterprise applications**Â service and create a new SAML application.

![Create a new SAML application](https://static.api7.ai/uploads/2026/01/28/eaeVaOZZ_create-application-to-prepare-saml.png)

Configure the SAML application in the IdP:

![Set Azure AD app information for SAML](https://static.api7.ai/uploads/2026/01/27/dS6uS38h_1-plugin-saml-set-azure-ad-app-info.png)

Copy the IdP metadata and certificate information:

![Copy SAML IdP information](https://static.api7.ai/uploads/2026/01/27/r6XMwJPC_2-plugin-saml-copy-info.png)

Configure the `saml-auth` plugin on the route. Replace the highlighted configuration with your values:

saml-auth

```
auth_protocol_binding_method: HTTP-POST
idp_cert: |-
  -----BEGIN CERTIFICATE-----
  MIIC8DCCAdigAwIBAgIQFP0SV5NUxJxBB6125kRy4zANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQD
  EylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yNjAxMTkwNjQ2
  MDRaFw0yOTAxMTkwNjQ2MDRaMDQxMjAwBgNVBAMTKU1pY3Jvc29mdCBBenVyZSBGZWRlcmF0ZWQg
  U1NPIENlcnRpZmljYXRlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvWTXi5qeU2oH
  ...
  io9oACxmTrSUJWyGQbPZtrwGUQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQCAKT5abG4qxLpEraNU
  -----END CERTIFICATE-----

idp_uri: https://login.microsoftonline.com/a7a70f5e-0b17-4a67-90ab-9e85ff6d9f59/saml2
login_callback_uri: /anything/login_callback
logout_callback_uri: /anything/logout_callback
logout_redirect_uri: /anything/logout_ok
logout_uri: /anything/logout
secret: testsecret
sp_cert: |-
  -----BEGIN CERTIFICATE-----
  MIIDDzCCAfegAwIBAgIUcULAtArasoM/knVgg/RYEaJDq+IwDQYJKoZIhvcNAQEL
  ...
  5V60djI2y+XTkvDCz/o/1YftMw==
  -----END CERTIFICATE-----
sp_issuer: api7
sp_private_key: |-
  -----BEGIN PRIVATE KEY-----
  MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDiVOfSpH5xTz8d
  ...
  IwBDUu3iS4CcCX18UwwiSjE=
  -----END PRIVATE KEY-----
```

![Configure the SAML Auth plugin](https://static.api7.ai/uploads/2026/01/27/9kqIB0oH_3-plugin-saml-config.png)

#### Set `consumer_name` with `serverless-post-function`[â](#set-consumer_name-with-serverless-post-function-1 "Direct link to set-consumer_name-with-serverless-post-function-1")

Use the resolved `name_id` in `ctx.external_user` to set the request `consumer_name`:

serverless-post-function

```
phase: rewrite
functions:
  - |
    return function(conf, ctx)
        local core = require("apisix.core")
        core.log.warn(
            "ctx.external_user: ",
            core.json.encode(ctx.external_user, true)
        )
        if type(ctx.external_user) == "table" and ctx.external_user.name_id then
            ctx.consumer_name = ctx.external_user.name_id
            core.log.warn("consumer_name: ", ctx.consumer_name)
        end
    end
```

![Configure serverless-post-function to set consumer\_name for SAML](https://static.api7.ai/uploads/2026/01/27/IWqygnsS_4-plugin-saml-config-serverless-to-set-consumer-name.png)

#### Verify[â](#verify-1 "Direct link to Verify")

Visit the route in browser to complete SAML authentication:

![Visit the route for SAML authentication](https://static.api7.ai/uploads/2026/01/27/jrhMwiWN_5-plugn-saml-visit.png)

Check the gateway access log to verify that `consumer_name` is set:

![Check access log for consumer\_name in SAML](https://static.api7.ai/uploads/2026/01/27/vc3TuaOm_6-plugin-saml-check-log-see-consumer_name.png)

## Forward User Information Headers to Upstream[â](#forward-user-information-headers-to-upstream "Direct link to Forward User Information Headers to Upstream")

### Using OpenID Connect[â](#using-openid-connect-1 "Direct link to Using OpenID Connect")

The `openid-connect` plugin has built-in support for forwarding user information to upstream services. No additional `serverless-post-function` configuration is needed for OpenID Connect user information forwarding.

![OpenID Connect user info passed to upstream](https://static.api7.ai/uploads/2026/01/28/03LXdk5F_plugin-openid-connect-passed-to-upstream.png)

### Using SAML Auth[â](#using-saml-auth-1 "Direct link to Using SAML Auth")

Use `serverless-post-function` to extract user information from `ctx.external_user` and set custom request headers.

serverless-post-function

```
phase: rewrite
functions:
  - |
    return function(conf, ctx)
        local core = require('apisix.core')
        local user = ctx.external_user
        if user and user.authenticated then
            core.request.set_header('X-SAML-NameID', user.name_id or '')
            -- Set the full user information request header
            -- (Base64 encoded JSON)
            local userinfo = {
                -- user name id
                name_id = user.name_id,
                -- session index
                session_index = user.session_index,
                -- IdP issuer
                issuer = user.issuer,
                -- IdP user attributes
                attrs = user.attrs
            }
            core.request.set_header(
                'X-SAML-Userinfo',
                ngx.encode_base64(core.json.encode(userinfo))
            )
        end
    end
```

![Configure serverless-post-function to pass user info to upstream](https://static.api7.ai/uploads/2026/01/27/oqg8Yh5o_7-plugin-saml-set-serverless-to-pass-to-upstream.png)

#### Verify[â](#verify-2 "Direct link to Verify")

Send a request to the route after authenticating with the SAML identity provider. The upstream service should receive headers similar to:

```
X-SAML-NameID: xxxx
X-SAML-Userinfo: xxxx
```

![Verify SAML user info headers](https://static.api7.ai/uploads/2026/01/27/zv6f3LZr_8-plugin-saml-visit-to-check.png)

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Consumers](https://docs.api7.ai/enterprise/key-concepts/consumers.md)
  * [Authentication](https://docs.api7.ai/enterprise/key-concepts/authentication.md)
  * [Plugins](https://docs.api7.ai/enterprise/key-concepts/plugins.md)

* Best Practices

  <!-- -->

  * [Log Consumer Label in Access Log](https://docs.api7.ai/enterprise/api-observability/log-consumer-label-in-access-log.md)
  * [Configure Dashboard SSO with Azure AD (OIDC)](https://docs.api7.ai/enterprise/best-practices/dashboard-sso/oidc/azure-ad.md)
  * [Configure Dashboard SSO with Azure AD (SAML)](https://docs.api7.ai/enterprise/best-practices/dashboard-sso/saml/azure-ad.md)

* Plugin Hub

  <!-- -->

  * [OpenID Connect](https://docs.api7.ai/hub/openid-connect.md)
  * [SAML Auth](https://docs.api7.ai/hub/saml-auth.md)
