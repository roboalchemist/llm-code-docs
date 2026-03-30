# Source: https://ngrok.com/docs/universal-gateway/examples/route-by-oidc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Route to Services Based on OIDC Authentication

> Use the data returned by your OIDC provider to route authenticated requsets to specific upstream services.

export const domain_0 = undefined

With ngrok, you can use OpenID Connect to do more than authenticate requests—you can also use the data returned by your OIDC provider to route requests to specific upstream services.

This pattern allows you to grant credentialed users and remote devices access to services on your internal ngrok network without maintaining a complex routing topology.
Example use cases include internal management UIs or API services.

## 1. Set up your OIDC provider

You can use any provider with the [`oidc` Traffic Policy action](/traffic-policy/actions/oidc/#overview).
You'll need the base URL of your Open ID provider, and, in most cases, a client ID and secret.

These are referred to as `$ISSUER_URL`, `$CLIENT_ID`, and `$CLIENT_SECRET`.

## 2. Start endpoints for your services

Start an internal [Agent Endpoint](/universal-gateway/agent-endpoints/), replacing `$PORT` based on where one of your upstream services listen.
You can also use one of the [SDKs](/agent-sdks) or the [Kubernetes Operator](/k8s).

```bash  theme={null}
ngrok http $PORT --url https://service-one.internal
```

Start a second Agent Endpoint for another service you want to route to, replacing `$OTHER_PORT` with the port for this service.

```bash  theme={null}
ngrok http $OTHER_PORT --url https://service-two.internal
```

Repeat the process for as many services as you need to route to.

## 3. Reserve a domain

Navigate to the [**Domains** section](https://dashboard.ngrok.com/domains) of the ngrok dashboard and click **New +** to reserve a free static domain like {<code>{domain_0}</code> || `https://your-service.ngrok.app`} or a [custom domain](/universal-gateway/custom-domains/) you already own.

We'll refer to this domain as `$NGROK_DOMAIN` from here on out.

## 4. Create a Cloud Endpoint

Navigate to the [**Endpoints** section](https://dashboard.ngrok.com/endpoints?sortBy=updatedAt\&orderBy=desc) of the ngrok dashboard, then click **New +** and **Cloud Endpoint**.

In the **URL** field, enter the domain you just reserved to finish creating your [Cloud Endpoint](/universal-gateway/cloud-endpoints/).

## 5. Enforce OIDC authentication and routing with Traffic Policy

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor, replacing `$ISSUER_URL`, `$CLIENT_ID`, and `$CLIENT_SECRET` with the appropriate values.

```yaml  theme={null}
on_http_request:
  - actions:
      - type: openid-connect
        config:
          issuer_url: "$ISSUER_URL"
          client_id: "$CLIENT_ID"
          client_secret: "$CLIENT_SECRET"
          scopes:
            - openid

  - expressions:
      - actions.ngrok.oidc.identity.name == 'Bob'
    actions:
      - type: forward-internal
        config:
          url: https://service-one.internal
  - expressions:

      - actions.ngrok.oidc.identity.name == 'Alice'
    actions:
      - type: forward-internal
        config:
          url: https://service-two.internal
```

**What's happening here?** This policy first requires OIDC authentication on every request using your issuer URL, client ID, and client secret.

If you authenticate successfully, this policy then filters your request based on the name as returned from your OIDC provider and routes your request to a specific service.

## 6. Try out your endpoints

Visit the domain you reserved either in the browser or in the terminal using a tool like `curl`.
You should see the app or service at the port connected to your internal Agent Endpoint.

## What's next?

* Explore [other authentication methods](/traffic-policy/examples/add-authentication/) like OAuth, Basic Auth, JWT validation, or SAML.
* Learn about [other routing options](/traffic-policy/examples/route-requests/) beyond OIDC identity, like routing by path, header, or geographic location.
* Read the guides on [securing access to remote devices](/guides/device-gateway/agent/) or [site-to-site connectivity](/guides/site-to-site-connectivity/) for more comprehensive setups involving Service Users, scoped auth tokens, and mTLS.
* View your traffic in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector).


Built with [Mintlify](https://mintlify.com).