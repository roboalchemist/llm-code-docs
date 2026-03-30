# Source: https://ngrok.com/docs/universal-gateway/examples/offload-analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Offload Analytics to a Self-Hosted Service

> With http-request, you can capture observability data from your gateway and send it to a self-hosted analytics service securely and without instrumenting your code.

export const domain_0 = undefined

ngrok and Traffic Policy let you integrate your ["front door" gateway](/universal-gateway/examples/front-door-pattern) with an analytics service you host within your network to capture vital information about your traffic as a part of the request-response lifecycle.

With this gateway setup and the [`http-request` action](/traffic-policy/actions/http-request), you can:

* Host your analytics service in any network, region, or cloud.
* Leave your analytics service completely unexposed to the public internet.
* Simplify your upstream services by removing libraries and code for instrumenting them directly.
* Configure for exactly the timeout and retry conditions your services require.

## 1. Create endpoints for your services

Start an internal [Agent Endpoint](/universal-gateway/agent-endpoints/), replacing `$PORT` based on where your upstream service listens.
You can also use one of the [SDKs](/agent-sdks) or the [Kubernetes Operator](/k8s).

```bash  theme={null}
ngrok http $PORT --url https://service.internal
```

Start a second endpoint for your analytics service.

```bash  theme={null}
ngrok http $PORT --url https://analytics.internal
```

## 2. Reserve a domain

Navigate to the [**Domains** section](https://dashboard.ngrok.com/domains) of the ngrok dashboard and click **New +** to reserve a free static domain like {<code>{domain_0}</code> || `https://your-service.ngrok.app`} or a [custom domain](/universal-gateway/custom-domains/) you already own.

We'll refer to this domain as `$NGROK_DOMAIN` from here on out.

## 3. Create a Cloud Endpoint

Navigate to the [**Endpoints** section](https://dashboard.ngrok.com/endpoints?sortBy=updatedAt\&orderBy=desc) of the ngrok dashboard, then click **New +** and **Cloud Endpoint**.

In the **URL** field, enter the domain you just reserved to finish creating your [Cloud Endpoint](/universal-gateway/cloud-endpoints/).

## 4. Send request data to your analytics service with Traffic Policy

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor.

```yaml  theme={null}
on_http_request:
  - actions:
      - type: forward-internal
        config:
          url: https://service.internal

on_http_response:
  - actions:
      # Send authenticated request to analytics service
      - type: http-request
        config:
          url: https://analytics.internal/api/request
          method: POST
          headers:
            Authorization: "Bearer <ANALYTICS_API_TOKEN>"
            Content-Type: "application/json"
          body: |
            {
              "path": "${req.url.path}",
              "method": "${req.method}",
              "status_code": "${res.status_code}",
              "country_code": "${conn.geo.country_code}",
              "region": "${conn.server_region}",
            }
          timeout: 1s
```

**What's happening here?** This policy sends all requests directly to your upstream service at `https://service.internal`.

As part of the response lifecycle, this policy also sends an authenticated request to your analytics service with a body containing attributes, injected with CEL interpolation, about the user's request and your server's response.
The `http-request` action is purposely given a short timeout and no retry logic to ensure this analytics request doesn't add unnecessarily slow your service's response time.

## 5. Try out your endpoint

Visit the domain you reserved either in the browser or in the terminal using a tool like `curl`.
You should see the app or service at the port connected to your internal Agent Endpoint.

## What's next?

* Explore other examples of using the [`http-request`](/traffic-policy/actions/http-request/#examples) and [`forward-internal`](/traffic-policy/actions/forward-internal/#examples) Traffic Policy actions.
* View your traffic in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector).
* Add even more logging flexibility, plus access to the entire [eventing system](/obs/), with the [`logs` action](/traffic-policy/actions/log/).


Built with [Mintlify](https://mintlify.com).