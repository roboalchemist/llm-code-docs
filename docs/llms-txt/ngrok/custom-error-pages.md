# Source: https://ngrok.com/docs/universal-gateway/examples/custom-error-pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Custom Error Pages

> Instead of a blank page or HTTP error code, ensure your services automatically failover to error pages with clear details and instructions.

export const domain_0 = undefined

When your upstream nodes or services go offline, you don't want your users to see a blank page, a standalone HTTP error code, or an ngrok-branded error page.
A custom error page gives you the chance to communicate clearly and reinforce your brand even during downtime.

With ngrok’s Traffic Policy engine, you can define exactly what your users see when your upstream service fails. This example walks you through how to route requests to your internal service, and then fall back to a branded error page if that service is unavailable.

## 1. Create an endpoint for your service

Start an internal [Agent Endpoint](/universal-gateway/agent-endpoints/), replacing `$PORT` based on where your service listens.
You can also use one of the [SDKs](/agent-sdks) or the [Kubernetes Operator](/k8s).

```bash  theme={null}
ngrok http $PORT --url https://service.internal
```

## 2. Reserve a domain

Navigate to the [**Domains** section](https://dashboard.ngrok.com/domains) of the ngrok dashboard and click **New +** to reserve a free static domain like {<code>{domain_0}</code> || `https://your-service.ngrok.app`} or a [custom domain](/universal-gateway/custom-domains/) you already own.

We'll refer to this domain as `$NGROK_DOMAIN` from here on out.

## 3. Create a Cloud Endpoint

Navigate to the [**Endpoints** section](https://dashboard.ngrok.com/endpoints?sortBy=updatedAt\&orderBy=desc) of the ngrok dashboard, then click **New +** and **Cloud Endpoint**.

In the **URL** field, enter the domain you just reserved to finish creating your [Cloud Endpoint](/universal-gateway/cloud-endpoints/).

## 4. Add routing to your service and error handling with Traffic Policy

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor.

```yaml  theme={null}
on_http_request:
  - actions:
      - type: forward-internal
        config:
          url: https://service.internal
          on_error: continue
      - type: custom-response
        config:
          status_code: 503
          headers:
            content-type: text/html
          body: |
            <!doctype html>
            <html>
            <head>
              <meta charset="UTF-8" />
              <meta name="viewport" content="width=device-width, initial-scale=1" />
              <title>Error at ${req.host}!</title>
              <style>
                body { font-family: system-ui, sans-serif; padding: 2rem; background: #fff; }
                code { font-family: monospace; background: #eee; padding: 0.2em 0.4em; border-radius: 4px; }
                .container { max-width: 600px; margin: 0 auto; }
              </style>
            </head>
            <body>
              <div class="container">
                <h1>Sorry, something went wrong!</h1>
                <p>We're having trouble reaching <strong>${req.host}</strong>.</p>
                <ul>
                  <li>Time: <code>${timestamp(time.now)}</code></li>
                  <li>Path: <code>${req.url.path}</code></li>
                  <li>Method: <code>${req.method}</code></li>
                  <li>Region: <code>${conn.server_region}</code></li>
                </ul>
              </div>
            </body>
            </html>
```

**What's happening here?** This policy forwards all HTTP requests to the internal Agent Endpoint you created at `https://service.internal`.

If forwarding to `https://service.internal` fails, the `on_error: continue` configuration on your `forward-internal` action means that the policy continues to the next rule, which sends a custom `503` error response with the HTML specified in the `body`.

## 5. Try out your endpoint

Visit the domain you reserved either in the browser or in the terminal using a tool like `curl`.
You should see the app or service at the port connected to your internal Agent Endpoint.

If you take down either your upstream service or the internal Agent Endpoint, you'll see your custom error message.

## What's next?

* See other examples of using the [`custom-response`](/traffic-policy/actions/custom-response/#examples) to create error pages or messages, such as a JSON-based response for an API service.
* View your traffic in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector) to see who and when users hit your custom error page.
* Add the [`log` action](/traffic-policy/actions/log) before the `custom-response` to send error events over to your observability platform for enriched debugging.


Built with [Mintlify](https://mintlify.com).