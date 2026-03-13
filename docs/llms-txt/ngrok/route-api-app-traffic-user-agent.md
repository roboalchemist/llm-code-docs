# Source: https://ngrok.com/docs/universal-gateway/examples/route-api-app-traffic-user-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Route API and App Traffic by User Agent

> Automatically enforce the right type of AuthN and route requests to the appropriate upstream service from the same hostname and path.

export const domain_0 = undefined

If you're serving both web app and API services from the same hostname, you can use ngrok and the Traffic Policy engine to:

1. Automatically enforce OAuth or JWT validation on browser or curl/machine-to-machine traffic, respectively.
2. Route only authenticated requests to your upstream app and API services.

This way, your users can hit the same hostname, authenticate themselves, and get the response they expect, while you know that all your services are protected.

## 1. Set up your JWT provider

You can use any provider/issuer, but there is a guide for defining an API and [generating tokens with Auth0](/integrations/jwt-validation/auth0).

## 2. Start internal endpoints for your services

Start an internal [Agent Endpoint](/universal-gateway/agent-endpoints/), replacing `$PORT` based on where your app service listens.
You can also use one of the [SDKs](/agent-sdks) or the [Kubernetes Operator](/k8s).

```bash  theme={null}
ngrok http 8080 --url https://web-service.internal
```

Start a second endpoint for your API service.

```bash  theme={null}
ngrok http 8081 --url https://api-service.internal
```

## 3. Reserve a domain

Navigate to the [**Domains** section](https://dashboard.ngrok.com/domains) of the ngrok dashboard and click **New +** to reserve a free static domain like {<code>{domain_0}</code> || `https://your-service.ngrok.app`} or a [custom domain](/universal-gateway/custom-domains/) you already own.

We'll refer to this domain as `$NGROK_DOMAIN` from here on out.

## 4. Create a Cloud Endpoint

Navigate to the [**Endpoints** section](https://dashboard.ngrok.com/endpoints?sortBy=updatedAt\&orderBy=desc) of the ngrok dashboard, then click **New +** and **Cloud Endpoint**.

In the **URL** field, enter the domain you just reserved to finish creating your [Cloud Endpoint](/universal-gateway/cloud-endpoints/).

## 5. Add JWT validation, OAuth, and routing with Traffic Policy

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor.
You may need to change:

* `$YOUR_JWT_DOMAIN`: The domain name for your tenant at your JWT provider—for example, with Auth0, it looks something like `https://example.us.auth0`.
* `$YOUR_EMAIL_DOMAIN`: The domain name associated with your organization's Google accounts for OAuth checks.

```yaml  theme={null}
on_http_request:
  - expressions:
      # Check if the client's user agent does not contain 'Mozilla', which means they are an API user
      - "!(req.user_agent.contains('Mozilla'))"
    actions:
      # If true, apply the `jwt-validation` action
      - type: "jwt-validation"
        config:
          issuer:
            allow_list:
              - value: "https://$YOUR_JWT_DOMAIN"
          http:
            tokens:
              - type: "jwt"
                method: "header"
                name: "Authorization"
                prefix: "Bearer "
          jws:
            allowed_algorithms:
              - "RS256"
            keys:
              sources:
                additional_jkus:
                  - "https://$YOUR_JWT_DOMAIN/.well-known/jwks.json"
      - type: "forward-internal"
        config:
          url: https://api-service.internal

  - expressions:
      # Check if the client's user agent contains 'Mozilla', which means they are a browser user
      - "req.user_agent.contains('Mozilla')"
    actions:
      # If true, apply the oauth action
      - type: oauth
        config:
          provider: google

  - expressions:
      # Check again whether the client's user agent contains 'Mozilla,' then also check whether the email they used in the OAuth flow matches $YOUR_DOMAIN, and if both are `true`, then forward to your
      - "req.user_agent.contains('Mozilla')"
      - "actions.ngrok.oauth.identity != null && actions.ngrok.oauth.identity.email.endsWith('@$YOUR_EMAIL_DOMAIN')"
    actions:
      - type: "forward-internal"
        config:
          url: https://web-service.internal

  - expressions:
      # In all other situations, use `custom-response` to respond with a generaic unauthorized error
      - type: "custom-response"
        config:
          status_code: 403
```

**What's happening here?** In the first section, this policy checks whether the request's user agent comes from an API user, then applies the `jwt-validation` action.
If the request has the appropriate `Authorization: Bearer …` header, then ngrok forwards it to your API service.

In the second section, it then checks whether the user agent is from a human/browser, then asks them to authenticate with Google's OAuth.
If the account they sign in to matches `$YOUR_EMAIL_DOMAIN`, then ngrok forwards it to your web app service.

In all other cases, the policy returns a `403 Forbidden` response because the request was not properly authenticated.

## 6. Try out your endpoint

Visit the domain you reserved either in the browser or in the terminal using a tool like `curl`.
You should see the app or service at the port connected to your internal Agent Endpoint.

In your terminal, make sure you add your JWT as a header:

```bash  theme={null}
curl https://your-service.ngrok.app \
	--header 'Authorization: Bearer $JWT_FROM_PROVIDER'
```

## What's next?

* Explore [other authentication methods](/traffic-policy/examples/add-authentication/) like Basic Auth, OIDC, or SAML.
* Learn about [more routing options](/traffic-policy/examples/route-requests/) beyond user agent, like routing by path, header, cookie, or geographic location.
* Explore all the configuration options in the [`jwt-validation`](/traffic-policy/actions/jwt-validation) and [`oauth`](/traffic-policy/actions/oauth) actions.
* View your traffic in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector).


Built with [Mintlify](https://mintlify.com).