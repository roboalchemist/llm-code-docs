# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-okta.md

# Set Up SSO with Okta

[OpenID Connect (OIDC)](https://openid.net/connect/) is a simple identity layer on top of the [OAuth 2.0 protocol](https://www.rfc-editor.org/rfc/rfc6749). It allows clients to verify the identity of end users based on the authentication performed by the identity provider, as well as to obtain basic profile information about end users in an interoperable and REST-like manner.

[Okta](https://www.okta.com) offers a comprehensive suite of identity and access management tools designed to support secure and scalable user authentication, enabling businesses to streamline access control across a variety of applications and devices.

The guide will show you how to integrate APISIX with Okta using authorization code grant and client credentials grant, using the [`openid-connect`](https://docs.api7.ai/hub/openid-connect.md) plugin.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.
* Have an [Okta Workflow Identity Cloud](https://www.okta.com/workforce-identity) account.

## Configure Okta[â](#configure-okta "Direct link to Configure Okta")

In this section, you will create an app integration and configure the needed details.

### Create App Integration[â](#create-app-integration "Direct link to Create App Integration")

In Okta, find the **Applications** dropdown from the left menu, select **Applications**, and click **Create App Integration**:

![create app integration](https://static.api7.ai/uploads/2024/11/06/gWsX077t_create-app-integration.png)

Select **OIDC - OpenID Connect** as the sign-in method and **Web Application** as the application type:

![select app types](https://static.api7.ai/uploads/2024/12/12/ylq46csD_create_new_app_details.png)

<br />

Click **Next**. Continue to fill out the details:

* enter an app integration name
* select **Authorization Code** and **Client Credentials** for the grant type
* add `http://localhost:9080/anything/callback` to the **sign-in redirect URIs**

![fill out details for the app](https://static.api7.ai/uploads/2024/12/12/3DAUKdED_redirect_url.png)

<br />

For **controlled access**, you may **skip group assignment for now**, or adjust the access accordingly:

![configure controlled access](https://static.api7.ai/uploads/2024/12/12/z4kaGyQm_controlled_access_and_save.png)

Click **Save**.

### Locate Client ID, Secret, and Domain[â](#locate-client-id-secret-and-domain "Direct link to Locate Client ID, Secret, and Domain")

Once the app is created, find the client ID and secret under the app's **General** tab:

![find client ID and secret](https://static.api7.ai/uploads/2024/12/12/lHxfdWzp_client_id_Secret.png)

Locate the Okta domain by clicking your username in the upper-right corner:

![find Okta domain](https://static.api7.ai/uploads/2024/11/07/2CBKSMjo_okta-domain-name.png)

Save the client ID, client secret, your Okta domain name, and your authorization server to environment variables for configurations in APISIX:

```
# replace with your values
export OKTA_CLIENT_ID=0oakxd44nbRLmD6JF5d7
export OKTA_CLIENT_SECRET=h4B_dqp_QnIIzZiDG9MSM_tr4QJJkuEj8CF8iw9jGaBak7m60cArKdsHPf
export OKTA_DOMAIN=dev-02223846.okta.com
export OKTA_AUTH_SERVER=default
```

### Assign User to App[â](#assign-user-to-app "Direct link to Assign User to App")

Complete steps in this section only if you are implementing the authorization code flow.

Navigate back to the **Applications** main interface and click **Assign Users to App**:

![assign user to app](https://static.api7.ai/uploads/2024/12/12/O774gMsn_assign_user_to_app.png)

Select the app as well as users to assign, and click **Next**:

![select app and user](https://static.api7.ai/uploads/2024/12/12/L0AXpgMf_step_1.png)

Finish by confirming the assignments:

![confirm assignments](https://static.api7.ai/uploads/2024/12/12/VUIIfsvW_step_2.png)

See [configure for authorization code grant](#configure-for-authorization-code-grant) for the next step.

### Create Custom Scopes[â](#create-custom-scopes "Direct link to Create Custom Scopes")

Complete steps in this section only if you are implementing the client credentials flow.

The client credentials flow does not have a user context, so you cannot request `openid` scopes. Instead, [create a custom scope](https://developer.okta.com/docs/guides/implement-grant-type/clientcreds/main/#create-custom-scopes).

Navigate back to the **Applications** main interface and click **Assign Users to App**:

In the left menu, find the **Security** dropdown from the left menu, select **API**, and click into your authorization server:

![security api authorization server](https://static.api7.ai/uploads/2024/11/07/gLmn5CGJ_security-api.png)

Under the **Scopes** tab, add a new scope:

![add a new scope](https://static.api7.ai/uploads/2024/12/12/a7QJrW5n_add_scope.png)

Fill out the scope name as well as the display phrase, and finish creating the scope:

![fill out scope name and display phrase](https://static.api7.ai/uploads/2024/12/12/PENRVllO_scope_details.png)

Under the **Access Policies** tab, add a new policy:

![add a new policy](https://static.api7.ai/uploads/2024/11/07/ficZuVCM_add-policy.png)

Fill out the policy name, description, as well as the client to assign to, and finish creating the policy:

![fill out the policy details](https://static.api7.ai/uploads/2024/12/12/zWeM4GMR_policy_details.png)

Once created, add a rule for the policy:

![add policy rule](https://static.api7.ai/uploads/2024/12/12/JLVK3CLC_policy_rule.png)

Configure the rule details. Make sure the client credentials grant is checked and finish creating the rule:

![rule details](https://static.api7.ai/uploads/2024/12/12/w8unbEP1_rule_details.png)

See [configure for client credentials grant](#configure-for-client-credentials-grant) for the next step.

## Configure APISIX[â](#configure-apisix "Direct link to Configure APISIX")

In this section, you will create a route with OIDC that forwards client requests toÂ [httpbin.org](http://httpbin.org/), a public HTTP request and response service.

The routeÂ `/anything/{anything}`Â ofÂ `httpbin.org`Â returns anything passed in request data in JSON type, such as methods, arguments, and headers.

### Configure for Authorization Code Grant[â](#configure-for-authorization-code-grant "Direct link to Configure for Authorization Code Grant")

The authorization code grant is used by web and mobile applications. The flow starts by authorization server displaying a login page in browser where users could key in their credentials. During the process, a short-lived authorization code is exchanged for an access token, which APISIX stores in browser session cookies and will be sent with every request visiting the upstream resource server.

Create the route and enable the plugin `openid-connect` as such:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "auth-with-oidc",
  "uri":"/anything/*",
  "plugins": {
    "openid-connect": {
      "client_id": "'"$OKTA_CLIENT_ID"'",
      "client_secret": "'"$OKTA_CLIENT_SECRET"'",
      "discovery": "https://'"$OKTA_DOMAIN"'/.well-known/openid-configuration",
      "scope": "openid profile",
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

â¶ `client_id`: Okta client ID.

â· `client_secret`: Okta client secret.

â¸ `discovery`: URI to Okta discovery document.

â¹ `redirect_uri`: URI to redirect to after authentication with Okta.

âº `bearer_only`: Set to `false` for authorization code grant.

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
            client_id: '0oakxd44nbRLmD6JF5d7'
            client_secret: 'h4B_dqp_QnIIzZiDG9MSM_tr4QJJkuEj8CF8iw9jGaBak7m60cArKdsHPf'
            discovery: 'https://dev-xxxxxxxx.okta.com/.well-known/openid-configuration'
            scope: openid profile
            redirect_uri: 'http://localhost:9080/anything/callback'
            bearer_only: false
            session:
              secret: 'f86cf31663a9c9fa0a28c2cc78badef1'
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ `client_id`: Okta client ID.

â· `client_secret`: Okta client secret.

â¸ `discovery`: URI to Okta discovery document.

â¹ `redirect_uri`: URI to redirect to after authentication with Okta.

âº `bearer_only`: Set to `false` for authorization code grant.

â» `session.secret`: Replace with your key used for session encryption and HMAC operation. Required when `bearer_only` is `false`.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

#### Verify[â](#verify "Direct link to Verify")

Navigate to `http://localhost:9080/anything/test` in a browser. You should be redirected to the Okta's log-in page:

![Okta login page](https://static.api7.ai/uploads/2024/12/12/rNyrL6Y2_okta_signin.png)

<br />

Log in with your credentials. If successful, the request will be forwarded toÂ `httpbin.org` and you should see a response similar to the following:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "text/html..."
    ...
  },
  "json": null,
  "method": "GET",
  "origin": "127.0.0.1, 59.71.xxx.xxx",
  "url": "http://127.0.0.1/anything/test"
}
```

### Configure for Client Credentials Grant[â](#configure-for-client-credentials-grant "Direct link to Configure for Client Credentials Grant")

The client credentials grant involves an machine-to-machine (M2M) application exchanging credentials with services where there is no user involved.

Create the route and enable the plugin `openid-connect` as such:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "auth-with-oidc",
  "uri":"/anything/*",
  "plugins": {
    "openid-connect": {
      "client_id": "'"$OKTA_CLIENT_ID"'",
      "client_secret": "'"$OKTA_CLIENT_SECRET"'",
      "discovery": "https://'"$OKTA_DOMAIN"'/oauth2/'"$OKTA_AUTH_SERVER"'/.well-known/openid-configuration",
      "scope": "openid profile apisix",
      "redirect_uri": "http://localhost:9080/anything/callback",
      "bearer_only": false,
      "session": {
        "secret": "f86cf31663a9c9fa0a28c2cc78badef1"
      },
      "use_jwks": true
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

â¶ `use_jwks`: Use the JWKS endpoint to verify the token.

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
            client_id: '0oakxd44nbRLmD6JF5d7'
            client_secret: 'h4B_dqp_QnIIzZiDG9MSM_tr4QJJkuEj8CF8iw9jGaBak7m60cArKdsHPf'
            discovery: 'https://dev-xxxxxxxx-admin.okta.com/oauth2/default/.well-known/openid-configuration'
            scope: openid profile apisix
            redirect_uri: 'http://localhost:9080/anything/callback'
            bearer_only: false
            session:
              secret: 'f86cf31663a9c9fa0a28c2cc78badef1'
            use_jwks: true
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ `use_jwks`: Use the JWKS endpoint to verify the token.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

#### Obtain Access Token[â](#obtain-access-token "Direct link to Obtain Access Token")

Before proceeding, first prepare a base64-encoded string of the client ID and client secret, in the format of `clientid:clientsecret`, which will be included in the `Authorization` header next for basic authentication.

Obtain an access token for the application:

```
curl "https://dev-02213846-admin.okta.com/oauth2/default/v1/token" -X POST \
  -H 'accept: application/json' \
  -H 'authorization: Basic MG9ha3hkNDRuYlJMbUQ2SkY1ZDc6cTRCX2RxcF9RbklJefwwJTVNNX3RyNFFKSmttdUVqOEhOM2xzQ0Y4aXc5UEdhQmFmN202MGNBcktkc0hQZg==' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  --data 'grant_type=client_credentials&scope=apisix'
```

â¶ Replace with your base64-encoded string containing the client ID and client secret.

â· Adjust the scope accordingly based on your configuration.

You should see a response similar to the following:

```
{
  "token_type":"Bearer",
  "expires_in":3600,
  "access_token":"eyJraWQiOiJTYko2dGFzUmwtOGVZaFBtQmY4TERXcjYtczJwNG9vRXNZSVZzSGNUUHFNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULm1ya1VTd1lyV1VmbHpQcnZoTEV6OXNXMTVSejBvUWtRVjMzSTkzUDVGLWsiLCJpc3MiOiJodHRwczovL2Rldi0wMjIxMzg0Ni5va9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE3MzA5Njc3MTgsImV4Dk3MTMxOCwiY2lkIjoiMG9ha3hkNDRuYlJMbUQ2SkY1ZDciLCJzY3AiOlsiYXBpc2l4Il0sInN1YiI6IjBvYWt4ZDQ0bmJSTG1ENkpGNWQ3In0.PYndg75QRIr4N4kfLXCmlNX3IdzsF-qYYQuYZQPS0QqT21G6AT5eM1idgiEhn6shRKhWkpXLEQTL0mZn6sbgU1S00R5TYHrDzR-tKIhTnoNeJ3aAjduqadoQnQLJk20LQ58NRWb33fN0i9f51NLRs5zQPZbWDNNl1g6s4XE1wirlU_Ol60Gx-cFgbMyrfs4eJW2-q5AS6mtjPz1blS9sOL4KLbWkU0-HkWc-QAv7Dx05Dmat8lT-NvKbIbFq21DlV5BKCL44k55oPrhZSAfkP0494ab8TEsOhCgo8dT0GGYe9219B3rBMDG2aL0jh1OdeZ8coD2haPeA",
  "scope":"apisix"
}
```

Save the access token to an environment variable:

```
# replace with your access token
export ACCESS_TOKEN="eyJraWQiOiJTYko2dGFzUmwtOGVZaFBtQmY4TERXcjYtczJwNG9vRXNZSVZzSGNUUHFNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULm1ya1VTd1lyV1VmbHpQcnZoTEV6OXNXMTVSejBvUWtRVjMzSTkzUDVGLWsiLCJpc3MiOiJodHRwczovL2Rldi0wMjIxMzg0Ni5va9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE3MzA5Njc3MTgsImV4Dk3MTMxOCwiY2lkIjoiMG9ha3hkNDRuYlJMbUQ2SkY1ZDciLCJzY3AiOlsiYXBpc2l4Il0sInN1YiI6IjBvYWt4ZDQ0bmJSTG1ENkpGNWQ3In0.PYndg75QRIr4N4kfLXCmlNX3IdzsF-qYYQuYZQPS0QqT21G6AT5eM1idgiEhn6shRKhWkpXLEQTL0mZn6sbgU1S00R5TYHrDzR-tKIhTnoNeJ3aAjduqadoQnQLJk20LQ58NRWb33fN0i9f51NLRs5zQPZbWDNNl1g6s4XE1wirlU_Ol60Gx-cFgbMyrfs4eJW2-q5AS6mtjPz1blS9sOL4KLbWkU0-HkWc-QAv7Dx05Dmat8lT-NvKbIbFq21DlV5BKCL44k55oPrhZSAfkP0494ab8TEsOhCgo8dT0GGYe9219B3rBMDG2aL0jh1OdeZ8coD2haPeA"
```

#### Verify[â](#verify-1 "Direct link to Verify")

Send a request to the routeÂ with the valid access token:

```
curl -i "http://127.0.0.1:9080/anything/test" -H "Authorization: Bearer $ACCESS_TOKEN"
```

You should receive anÂ `HTTP/1.1 200 OK`Â response.

Send a request to the routeÂ with an invalid access token:

```
curl -i "http://127.0.0.1:9080/anything/test" -H "Authorization: Bearer invalid_token"
```

You should receive anÂ `HTTP/1.1 401 Unauthorized`Â response.

## Next Steps[â](#next-steps "Direct link to Next Steps")

APISIX supports the integration with many other OIDC identity providers, such as [Keycloak](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-keycloak.md), [Authgear](https://api7.ai/blog/build-full-stack-authetication-app), [Microsoft Entra ID (Azure AD)](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-azure-ad.md), and [Google](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-google.md).

In addition, APISIX also supports built-in authentication approaches such as [key authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-key-auth.md), [basic authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md), [JWT authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-jwt-auth.md), and [HMAC authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md).
