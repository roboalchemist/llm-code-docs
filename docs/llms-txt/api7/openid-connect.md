# Source: https://docs.api7.ai/hub/openid-connect.md

# Source: https://docs.api7.ai/cloud/guides/traffic-management/authentication/openid-connect.md

# Use OpenID Connect to Protect Your APIs

OpenID Connect is an identity layer based on the OAuth 2.0 framework. It allows third-party Service to authenticate the end-user and obtain their basic information.

API7 Cloud supports the OpenID Connect plugin so that you can authenticate your API consumers with well-known providers like [Google](https://developers.google.com/identity/protocols/oauth2/openid-connect), [Auth0](https://auth0.com/), etc.

This guide will show you how to use the OpenID Connect plugin to integrate the Auth0 service.

## Prepare the Environment[â](#prepare-the-environment "Direct link to Prepare the Environment")

### Deploy Apache APISIX[â](#deploy-apache-apisix "Direct link to Deploy Apache APISIX")

Please refer to [How to Deploy Apache APISIX](https://docs.api7.ai/cloud/guides/product/how-to-deploy-apache-apisix.md) to learn how to deploy Apache APISIX and connect it to API7 Cloud. In this guide, we'll deploy an Apache APISIX instance on Docker.

### Create Service and Route[â](#create-service-and-route "Direct link to Create Service and Route")

We'll create a service with the following details in this guide.

1. The service name is `oidc-app`.
2. The path prefix is `/v1`.
3. The HTTP Host is `oidc.httpbin.org`.
4. The upstream URL is `https://httpbin.org`.

Besides, we'll create a route inside the `oidc-app` Service.

1. The route name is `anything`.
2. The path is `/anything` (prefix match).
3. Accepted HTTP method is `GET`.

tip

If you don't know how to configure a service and route, please refer to the [Getting Started](https://docs.api7.ai/cloud/getting-started/.md) guides first

Then, let's add the OpenID Connect plugin to the `oidc-app` Service.

![Add OpenID Connect Plugin](https://static.api7.ai/2022/12/30/add-oidc-plugin.png)

We create an [Application](https://auth0.com/docs/get-started/applications) on Auth0 before and fill in its `Client ID`, `Client Secret`, and `Identity Server` here. You should replace them according to your actual case. Moreover, we fill the `Redirect URI` to `http://oidc.httpbin.org:9080/v1/anything/callback` so that the redirected API call will also match the `anything` route. You can use any endpoint if you ensure the redirected API call will be handled by the same route where the OIDC authentication starts.

important

Please avoid using any meaningful business API endpoint when you design the `Redirect URI`.

## Test the Authentication[â](#test-the-authentication "Direct link to Test the Authentication")

We'll use the browser to access the `oidc-app` Service. The URL is `https://oidc.httpbin.org:9080/v1/anything` in our case.

Before doing that, please make sure you set the DNS resolution for `odic-app.httpbin.org` to your Apache APISIX instance (e.g., change the `/etc/hosts` file).

![OpenID Connect Login](https://static.api7.ai/2022/12/30/oidc-login.png)

We use a pre-created user account to log in.

![OpenID Connect Anything](https://static.api7.ai/2022/12/30/oidc-anything-api.png)

As you can see, we are authenticated by Auth0, and the user information is encoded into the `X-Userinfo` header. We can see the user information by decoding it.

```
echo 'eyJzdWIiOiJhdXRoMHw2MmUwYTcwYzc2MTQxYzVhYmU2NDNmMTIifQ==' | base64 -d
{"sub":"auth0|62e0a70c76141c5abe643f12"}
```

## See Also[â](#see-also "Direct link to See Also")

* [API7 Cloud OpenID Connect Plugin Reference](https://docs.api7.ai/cloud/references/plugins/traffic-management/authentication.md#openid-connect)
* [Apache APISIX OpenID Connect Plugin](https://apisix.apache.org/docs/apisix/plugins/openid-connect/)
* [How to Integrate Keycloak for Authentication with Apache APISIX](https://www.keycloak.org/2021/12/apisix)
* [Centralize Authentication at the Gateway with Apache APISIX and OpenID Connect](https://developer.okta.com/blog/2021/08/18/apache-apisix-gateway)
