# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-google.md

# Set Up SSO with Google

[OpenID Connect (OIDC)](https://openid.net/connect/) is a simple identity layer on top of the [OAuth 2.0 protocol](https://www.rfc-editor.org/rfc/rfc6749). It allows clients to verify the identity of end users based on the authentication performed by the identity provider, as well as to obtain basic profile information about end users in an interoperable and REST-like manner.

[Google Identity](https://developers.google.com/identity) offers a suite of identity and access management tools, enabling secure user authentication and access control. With APISIX and Google, you can implement OIDC-based authentication processes to protect your APIs and enable single sign-on (SSO).

The guide will show you how to integrate APISIX with Google's OAuth 2.0 APIs to implement SSO, using the authorization code flow.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.
* Have a [Google](https://myaccount.google.com) account.

## Configure Google Credentials[â](#configure-google-credentials "Direct link to Configure Google Credentials")

Go to the [Credentials](https://console.developers.google.com/apis/credentials) page in Google API console and create a new credential of type **OAuth client ID**:

![Google OAuth create OAuth client ID](https://static.api7.ai/uploads/2024/11/04/WolygcOw_google-oauth-create.jpeg)

Configure the details for the client:

* Select the **Web application** as the **Application type**.
* Enter the name of the client, for example, `apisix`.
* Enter the callback URL `http://localhost:9080/anything/callback`.

![Enter client details](https://static.api7.ai/uploads/2024/11/04/WGHSnODc_create-details.jpeg)

Finish the creation.

Copy the generated client ID and secret:

![The generated client ID and secret](https://static.api7.ai/uploads/2024/11/04/HCiZLufr_copy-secret-masked.png)

Save the client ID and secret to environment variables:

```
# replace with your values
export OIDC_CLIENT_ID=590838497384-v1v8tta846d4iki47kuaa5mompqio.apps.googleusercontent.com
export OIDC_CLIENT_SECRET=bSaINfMk1YknmtXvo8lKkfeY0iwpr9c0
```

## Create a Route in APISIX[â](#create-a-route-in-apisix "Direct link to Create a Route in APISIX")

Create a route with `openid-connect` plugin as such:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "auth-with-oidc",
  "uri":"/anything/*",
  "plugins": {
    "openid-connect": {
      "bearer_only": false,
      "session": {
        "secret": "f86cf31663a9c9fa0a28c2cc78badef1"
      },
      "client_id": "'"$OIDC_CLIENT_ID"'",
      "client_secret": "'"$OIDC_CLIENT_SECRET"'",
      "discovery": "https://accounts.google.com/.well-known/openid-configuration",
      "scope": "openid profile",
      "redirect_uri": "http://localhost:9080/anything/callback"
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

â¶ `bearer_only`: Set to `false` for authorization code grant.

â· `session.secret`: Replace with your key used for session encryption and HMAC operation. Required when `bearer_only` is `false`.

â¸ `client_id`: Google OAuth client ID.

â¹ `client_secret`: Google OAuth client secret.

âº `discovery`: URI to [Google discovery document](https://developers.google.com/identity/openid-connect/openid-connect#discovery).

â» `redirect_uri`: URI to redirect to after authentication with Google OAuth.

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
            bearer_only: false
            session:
              secret: "f86cf31663a9c9fa0a28c2cc78badef1"
            client_id: "590838497384-v1v8tta846d4iki47kuaa5mompqio.apps.googleusercontent.com"
            client_secret: "bSaINfMk1YknmtXvo8lKkfeY0iwpr9c0"
            discovery: "https://accounts.google.com/.well-known/openid-configuration"
            scope: openid profile
            redirect_uri: "http://localhost:9080/anything/callback"
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ `bearer_only`: Set to `false` for authorization code grant.

â· `session.secret`: Replace with your key used for session encryption and HMAC operation. Required when `bearer_only` is `false`.

â¸ `client_id`: Google OAuth client ID.

â¹ `client_secret`: Google OAuth client secret.

âº `discovery`: URI to [Google discovery document](https://developers.google.com/identity/openid-connect/openid-connect#discovery).

â» `redirect_uri`: URI to redirect to after authentication with Google OAuth.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Verify[â](#verify "Direct link to Verify")

Navigate to `http://localhost:9080/anything/test` in browser. You should be redirected to Google's log-in page:

![log in with Google](https://static.api7.ai/uploads/2024/11/04/s0xWElW8_google-log-in.jpeg)

<br />

Once logged in, the request will be forwarded to `httpbin.org` and you should see a response similar to the following in browser:

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
  "origin": "127.0.0.1, 122.71.24.81",
  "url": "http://127.0.0.1/anything/test"
}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

APISIX supports the integration with more OIDC identity providers, such as [Keycloak](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-keycloak.md), [Authgear](https://api7.ai/blog/build-full-stack-authetication-app), [Microsoft Entra ID](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-azure-ad.md), and [Auth0](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-auth0.md).

In addition, APISIX also supports built-in authentication approaches such as [key authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-key-auth.md), [basic authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md), [JWT authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-jwt-auth.md), and [HMAC authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md).
