# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-azure-ad.md

# Set Up SSO with Microsoft Entra ID (Azure AD)

[OpenID Connect (OIDC)](https://openid.net/connect/) is a simple identity layer on top of the [OAuth 2.0 protocol](https://www.rfc-editor.org/rfc/rfc6749). It allows clients to verify the identity of end users based on the authentication performed by the identity provider, as well as to obtain basic profile information about end users in an interoperable and REST-like manner. With APISIX and [Microsoft Entra ID (formerly Azure AD)](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id), you can implement OIDC-based authentication processes to protect your APIs and enable single sign-on (SSO).

[Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) is Microsoft's cloud-based identity and access management service. It allows organizations to securely manage and authenticate users and devices, ensuring that the right individuals have the appropriate access to company resources. Microsoft Entra ID offers features such as single sign-on (SSO), multi-factor authentication (MFA), and integration with various third-party applications.

The guide will show you how to integrate APISIX with Microsoft Entra ID using [authorization code flow](#authenticate-with-user-credentials) and [client credentials flow](#authenticate-with-client-credentials).

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.
* Create an [Azure](https://signup.azure.com/) account that has an active subscription.

## Register an application in Azure[â](#register-an-application-in-azure "Direct link to Register an application in Azure")

Log in to the [Azure portal](https://portal.azure.com/), go to the **App registrations**Â service and register a new application.

![azure-ad-create-an-app](https://static.api7.ai/uploads/2023/09/07/oqdS1Z61_azure-ad-create-an-app-v1.png)

Once the app is registered, click on the **Authentication** tab and click on **Add a platform**. Choose **Web** application type and add a new redirect URI `http://localhost:9080/anything/callback` to the **Redirect URIs** list under the **Web** page. This is the address that the application redirects users to upon a successful authentication with Microsoft Entra ID. Click on **Configure** to save changes.

![azure-ad-app-add-redirect-uri](https://static.api7.ai/uploads/2023/09/02/WpApGXm2_azure-ad-app-add-redirect-uri.png)

To configure Microsoft Entra ID to use [v2.0 tokens](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens#token-formats),Â edit your application **Manifest**, and setÂ `accessTokenAcceptedVersion`Â toÂ `2`.

![azure-ad-update-manifest](https://static.api7.ai/uploads/2023/09/07/r8n7qaai_azure-ad-update-manifest-v1.png)

InÂ **Certificates & Secrets** tab, create a client secret and save the value to a secure location so that you can use it later for APISIX OIDC plugin configuration. You can only view the secret once.

![azure-ad-create-secret](https://static.api7.ai/uploads/2023/09/07/jttBfWaz_azure-ad-create-secret-v1.png)

Navigate back to the **Overview** tab and find **Directory (tenant) ID** and **Application (client) ID**. Save them to environment variables along with the client secret:

```
# replace with your values
export TENANT_ID=dcbd8da3-e0b3-486c-9212-08a199dc3451
export CLIENT_ID=e0951842-d546-4c63-9e9e-d33a527673de 
export CLIENT_SECRET=wSY8Q~x4z2Tn6Rq5lA4NTtZ6GLBMGvZF_R2LEcPx 
```

## Configure APISIX[â](#configure-apisix "Direct link to Configure APISIX")

In this section, you will create a route with OIDC that forwards client requests to [httpbin.org](http://httpbin.org/), a public HTTP request and response service.

The route `/anything/{anything}` of `httpbin.org` returns anything passed in request data in JSON type, such as methods, arguments, and headers.

### Enable OIDC Plugin[â](#enable-oidc-plugin "Direct link to Enable OIDC Plugin")

Create the route and enable the plugin `openid-connect`:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "auth-with-oidc",
  "uri":"/anything/*",
  "plugins": {
    "openid-connect": {
      "client_id": "'"$CLIENT_ID"'",
      "client_secret": "'"$CLIENT_SECRET"'",
      "discovery": "https://login.microsoftonline.com/'"$TENANT_ID"'/v2.0/.well-known/openid-configuration",
      "scope": "openid", 
      "redirect_uri": "http://localhost:9080/anything/callback",
      "bearer_only": false,
      "session": {
        "secret": "f86cf31663a9c9fa0a28c2cc78badef1"
      }
    }
  },
  "upstream":{
    "type":"roundrobin",
    "nodes":{
      "httpbin.org:80":1
    }
  }
}'
```

â¶ `client_id`: Microsoft Entra ID client ID.

â· `client_secret`: Microsoft Entra ID client secret.

â¸ `discovery`: URI to OIDC discovery document of Microsoft Entra ID.

â¹ `redirect_uri`: URI to redirect to after authentication with Microsoft Entra ID.

âº `bearer_only`: Set to `false` for authorization code flow.

â» `session.secret`: Replace with your key used for session encryption and HMAC operation. Required when `bearer_only` is `false`.

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything/*
        name: auth-with-oidc
        plugins:
          openid-connect:
            client_id: 'e0951842-d546-4c63-9e9e-d33a527673de'
            client_secret: 'wSY8Q~x4z2Tn6Rq5lA4NTtZ6GLBMGvZF_R2LEcPx'
            discovery: 'https://login.microsoftonline.com/dcbd8da3-e0b3-486c-9212-08a199dc3451/v2.0/.well-known/openid-configuration'
            scope: 'openid'
            redirect_uri: 'http://localhost:9080/anything/callback'
            bearer_only: false
            session:
              secret: f86cf31663a9c9fa0a28c2cc78badef1
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ `client_id`: Microsoft Entra ID client ID.

â· `client_secret`: Microsoft Entra ID client secret.

â¸ `discovery`: URI to OIDC discovery document of Microsoft Entra ID.

â¹ `redirect_uri`: URI to redirect to after authentication with Microsoft Entra ID.

âº `bearer_only`: Set to `false` for authorization code flow.

â» `session.secret`: Replace with your key used for session encryption and HMAC operation. Required when `bearer_only` is `false`.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Authenticate with User Credentials[â](#authenticate-with-user-credentials "Direct link to Authenticate with User Credentials")

Navigate to `http://localhost:9080/anything/test` in a browser. You should be redirected to the Microsoft Entra ID sign-in page:

![Microsoft Entra ID Authentication Page](https://static.api7.ai/uploads/2023/09/01/caen60yH_azure-ad-successful-authentication.png)

<br />

info

You can customize Microsoft Entra ID sign-in page for your own branding. See how to [configure your company branding](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/customize-branding) on the sign-in page.

Sign in with your Azure credentials. You should see a response similar to the following in the browser:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-us", 
    "Cookie": "session=...", 
    "Host": "localhost", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15", 
    "X-Access-Token": "eyJ...", 
    "X-Amzn-Trace-Id": "Root=1-65698cfb-262bc17d50bca6de3e855301", 
    "X-Forwarded-Host": "localhost", 
    "X-Id-Token": "eyJ...",
    "X-Userinfo": "eyJ..."
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "172.24.0.1, 108.**.**.**", 
  "url": "http://localhost/anything/test"
}
```

## Authenticate with Client Credentials[â](#authenticate-with-client-credentials "Direct link to Authenticate with Client Credentials")

The client credentials flow involves a machine-to-machine (M2M) application exchanging credentials with services where there is no user involved.

In this section, you will update the existing route with additional OIDC configurations and authenticate to Microsoft Entra ID with an access token.

### Update OIDC Plugin[â](#update-oidc-plugin "Direct link to Update OIDC Plugin")

Update the OIDC plugin on the route to use the JWKS endpoint of the identity server to verify the token:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes/auth-with-oidc" -X PATCH -d '
{
  "plugins": {
    "openid-connect": {
      "use_jwks": true
    }
  }
}'
```

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything/*
        name: auth-with-oidc
        plugins:
          openid-connect:
            use_jwks: true
            client_id: 'e0951842-d546-4c63-9e9e-d33a527673de'
            client_secret: 'wSY8Q~x4z2Tn6Rq5lA4NTtZ6GLBMGvZF_R2LEcPx'
            discovery: 'https://login.microsoftonline.com/dcbd8da3-e0b3-486c-9212-08a199dc3451/v2.0/.well-known/openid-configuration'
            scope: 'openid'
            redirect_uri: 'http://localhost:9080/anything/callback'
            bearer_only: false
            session:
              secret: f86cf31663a9c9fa0a28c2cc78badef1
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

### Test Access Token[â](#test-access-token "Direct link to Test Access Token")

Obtain an access token for the registered test application in Azure:

```
curl -i "https://login.microsoftonline.com/$TENANT_ID/oauth2/v2.0/token" -X POST \
  -d 'client_id='$CLIENT_ID'' \
  -d 'client_secret='$CLIENT_SECRET'' \
  -d 'scope='$CLIENT_ID'/.default' \
  -d 'grant_type=client_credentials'
```

The expected response is similar to the following:

```
{
  "token_type": "Bearer",
  "expires_in": 3599,
  "ext_expires_in": 3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJlMDk1MTg0Mi1kNTQ2LTRjNjMtOWU5ZS1kMzNhNTI3NjczZGUiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vZGNiZDhkYTMtZTBiMy00ODZjLTkyMTItMDhhMTk5ZGMzNDUxL3YyLjAiLCJpYXQiOjE2OTQ2MDczMzAsIm5iZiI6MTY5NDYwNzMzMCwiZXhwIjoxNjk0NjExMjMwLCJhaW8iOiJBU1FBMi84VUFBQUFHZXcvTjhPQm1OSEtaK1cydVNnR0NNckhwRlNERmVuNUNBcTVONG1QQ2ZzPSIsImF6cCI6ImUwOTUxODQyLWQ1NDYtNGM2My05ZTllLWQzM2E1Mjc2NzNkZSIsImF6cGFjciI6IjEiLCJvaWQiOiIxODA5NTNiZi1lZDZlLTRjNjUtYmRiZS01Y2JlNmRhMTI4OTYiLCJyaCI6IjAuQVRvQW80MjkzTFBnYkVpU0VnaWhtZHcwVVVJWWxlQkcxV05NbnA3VE9sSjJjOTdoQUFBLiIsInN1YiI6IjE4MDk1M2JmLWVkNmUtNGM2NS1iZGJlLTVjYmU2ZGExMjg5NiIsInRpZCI6ImRjYmQ4ZGEzLWUwYjMtNDg2Yy05MjEyLTA4YTE5OWRjMzQ1MSIsInV0aSI6IlM5anBfWS1qUjBhcm9lS3NVdnNqQUEiLCJ2ZXIiOiIyLjAifQ.bAt8rh56MK7igDZws0mtSqXDhHvwIyKoxOW7uqSD5aWBaXPxINpNTqIW04n4_p14uLhBlxSufV8WHmS5V1Pdv-QENu9VMUs00blOH38TX0S3WfyCkYuecvWnHc4kYi4TFxTVk1nTvhU7LgOYIHLDb04rRxP-D0tFJ7qo2gI2nSvDChEPCID8WkugPbXJyo1gc49UAuv75d2PhFkidIigDq_DGQQoa88ZLW1iDcQYVgTitEg9zhqSlYksOq1xGClB16sSubnKF6dwqXOfUamAMeu41YLDdgOAb3bS3J54OOe5uUliemHxWo4Z-rfBOI8uOKUioVLv2RImaHylhutaeA"
}
```

Save the access token to an environment variable:

```
# replace with your access token
export ACCESS_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikc2elVuYzgtM0JrVlgtZmdnMTdKNSJ9.eyJpc3MiOiJodHRwczovL2Rldi00bGc0aWZzcTRqdnBuN3MyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJlQUM4VVRWUEZpcnVmT2g0YTFEWnRjN0YyMHo3eUd1dkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9jbGllbnRjcmVkZW50aWFscy5jb20iLCJpYXQiOjE2OTMwNDAwMjcsImV4cCI6MTY5MzEyNjQyNywiYXpwIjoiZUFDOFVUVlBGaXJ1Zk9oNGExRFp0YzdGMjB6N3lHdXYiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.aePOiFlW0q0mlrQwKdtP1MGfY2nX7TSnTrEjoJI03aG7lBCHhPX_WwszhYvtM5c_cyQtcI6R4ibPskpTssdEXGCe2wbOhstPWeIb9rCFf_kA_g0p1wDM8j8egRfl7PLmFffaEmU0eNrgmjTgYQ0Erk63XDykPFOFWiQKPfDQ2hf4jz_3J_VKNqwy7yQuxisnD5TysybGmrONoiBjYLGIymk1ii-qKEoNt5_DRv10aSBwyRtxDZbiwhAKcWNO7zLaJVmZZLg1aTiRYxgIOU-_AP4iAR6Y4vK_GxyHqf7G6j6yH8wqCj8Nm2bLEg8Gqb9Fd-xbpbQCiC3X14ja5NTYtw"
```

Send a request to the route with the valid access token authorization header:

```
curl -i "http://127.0.0.1:9080/anything/test" -H "Authorization: Bearer $ACCESS_TOKEN"
```

An `HTTP/1.1 200 OK` response verifies that the client application is able to make authorized calls to the API.

## Next Steps[â](#next-steps "Direct link to Next Steps")

APISIX supports more OIDC identity providers, such as [Okta](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-okta.md), [Keycloak](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-keycloak.md), [Authgear](https://api7.ai/blog/build-full-stack-authetication-app) and [Auth0](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-auth0.md).

In addition, APISIX also supports built-in authentication methods such as [key authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-key-auth.md), [basic authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md), [JWT authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-jwt-auth.md), and [HMAC authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md).
