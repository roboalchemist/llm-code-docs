# Source: https://ngrok.com/docs/universal-gateway/examples/route-by-geography.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Route to Endpoints by Geography

> Show users content based on their region, comply with regulations, or ensure traffic hits the nearest endpoint for the best latency.

export const domain_0 = undefined

To route traffic to specific regions, you can use ngrok's Cloud Endpoints, internal Agent Endpoints, and Traffic Policy engine to match incoming traffic based on the [client's IP geolocation data](/traffic-policy/variables/connection/#conngeocountry-code) using [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html), then forward requests to the appropriate regional endpoints.

With this setup, you can:

* Showcase user content tailored to their region, like country-specific pricing.
* Comply with regulations like GDPR.
* Ensure your customers' traffic is routed to the nearest possible endpoint for the best latency.

This also implements the ['front door' pattern](/universal-gateway/examples/front-door-pattern), which creates a loose coupling between the traffic management logic at your gateway and your services.

## 1. Start endpoints for your services

On a server designated for U.S. traffic, start an internal [Agent Endpoint](/universal-gateway/agent-endpoints/), replacing `$PORT` based on where your service listens.
You can also use one of the [SDKs](/agent-sdks) or the [Kubernetes Operator](/k8s).

```bash  theme={null}
ngrok http $PORT --url https://us-service.internal
```

On a server designated for Canadian traffic, start a second endpoint.

```bash  theme={null}
ngrok http $PORT --url https://ca-service.internal
```

## 2. Reserve a domain

Navigate to the [**Domains** section](https://dashboard.ngrok.com/domains) of the ngrok dashboard and click **New +** to reserve a free static domain like {<code>{domain_0}</code> || `https://your-service.ngrok.app`} or a [custom domain](/universal-gateway/custom-domains/) you already own.

We'll refer to this domain as `$NGROK_DOMAIN` from here on out.

## 3. Create a Cloud Endpoint

Navigate to the [**Endpoints** section](https://dashboard.ngrok.com/endpoints?sortBy=updatedAt\&orderBy=desc) of the ngrok dashboard, then click **New +** and **Cloud Endpoint**.

In the **URL** field, enter the domain you just reserved to finish creating your [Cloud Endpoint](/universal-gateway/cloud-endpoints/).

## 4. Add routing to your services with Traffic Policy

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor.

```yaml  theme={null}
on_http_request:
  - expressions:
      # Check if the client is from the U.S.
      - "conn.geo.country_code == 'US'"
    actions:
      # Forward the request to the U.S. internal service
      - type: forward-internal
        config:
          url: http://us-service.internal

  - expressions:
      # Check if the client is from Canada
      - "conn.geo.country_code == 'CA'"
    actions:
      # Forward the request to the CA internal service
      - type: forward-internal
        config:
          url: http://ca-service.internal

  - actions:
      # Forward all other requests to a "default" service of your choosing
      - type: forward-internal
        config:
          url: http://us-service.internal
```

**What's happening here?** This policy checks every HTTP request to see where it originated from.
If that's the U.S. or Canada, ngrok forwards the traffic to its respective endpoint.
If the traffic comes from any other country, ngrok forwards it to a "default" service of your choosing.

## 5. Try out your endpoint

Visit the domain you reserved either in the browser or in the terminal using a tool like `curl`.
You should see the app or service at the port connected to your internal Agent Endpoint.

## What's next?

* Explore [other routing methods](/traffic-policy/examples/route-requests/), like routing by path, header, cookie, or IP intelligence.
* [Add authentication](/traffic-policy/examples/add-authentication/) to your regional endpoints with OAuth, OIDC, or JWT validation.
* View your traffic in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector).
* Check out [Endpoint Pools](/universal-gateway/endpoint-pooling/) for dead-simple load balancing.


Built with [Mintlify](https://mintlify.com).