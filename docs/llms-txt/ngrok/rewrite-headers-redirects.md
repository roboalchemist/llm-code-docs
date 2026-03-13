# Source: https://ngrok.com/docs/universal-gateway/examples/rewrite-headers-redirects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Intercept and Rewrite Headers in HTTP Redirect Responses

> By routing to internal services and editing headers, you can manipulate traffic in ways that allow you to seamlessly access customer networks and upstream services despite their network topology.

export const domain_0 = "https://service-01.customer-abc.ngrok.app"

Many customers use ngrok for [site-to-site connectivity](/guides/site-to-site-connectivity/).
This is usually pretty straightforward, but occasionally a service requires a specific `Host` header or uses internal DNS names or redirect flows that break in an outbound tunneled environment (for example, `302` redirects to `internal.corp.local`).

With ngrok, you can use the [`url-rewrite` action](/traffic-policy/actions/url-rewrite) in a Traffic Policy to intercept `302` redirect headers coming from customer apps to preserve UX and agent behavior.

## 1. Create an endpoint for the customer's upstream service

Start an internal [Agent Endpoint](/universal-gateway/agent-endpoints/), replacing `$PORT` based on where the upstream service listens and using a URL namespacing scheme that logically separates individual services and customers.
You can also use one of the [SDKs](/agent-sdks) or the [Kubernetes Operator](/k8s).

Depending on how you work with your customer, you may be creating this endpoint or instructing them how to do it themselves.

```bash  theme={null}
ngrok http $PORT --url https://service-01.customer-abc.internal
```

## 2. Reserve a domain

Navigate to the [**Domains** section](https://dashboard.ngrok.com/domains) of the ngrok dashboard and click **New +** to reserve a free static domain like {<code>{domain_0}</code> || `https://your-service.ngrok.app`} or a [custom domain](/universal-gateway/custom-domains/) you already own.

We'll refer to this domain as `$NGROK_DOMAIN` from here on out.

## 3. Create a Cloud Endpoint

Navigate to the [**Endpoints** section](https://dashboard.ngrok.com/endpoints?sortBy=updatedAt\&orderBy=desc) of the ngrok dashboard, then click **New +** and **Cloud Endpoint**.

In the **URL** field, enter the domain you just reserved to finish creating your [Cloud Endpoint](/universal-gateway/cloud-endpoints/).

## 4. Use Traffic Policy to route traffic and edit headers

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor, then replace `$NGROK_DOMAIN`.

```yaml  theme={null}
on_http_request:
  - actions:
      - type: add-headers
        config:
          headers:
            host: 127.0.0.1
      - type: forward-internal
        config:
          url: https://service-01.customer-abc.internal

on_http_response:
  - expressions:
      - "res.status_code == 302"
    actions:
      - type: set-vars
        config:
          vars:
            orig: "${url.parse(res.location).path}"
      - type: remove-headers
        config:
          headers:
            - Location
      - type: add-headers
        config:
          headers:
            Location: "$NGROK_DOMAIN/${vars.orig}"
```

**What's happening here?** First, this policy rewrites the `Host` header on all requests to `127.0.0.1` so that your customer's upstream service recognizes the request as coming from the same local network, not through ngrok, then forwards the request to the internal Agent Endpoint you created in the first step.

During the HTTP response, the policy then checks whether the status code is `302`, which indicates content has moved.
If the status code is `302`, then the policy saves the existing path to a variable, removes the `Location` header, and writes a new `Location` header by building a new URL based on `$NGROK_URL` and the original path.

## What's next?

* Follow along with the [comprehensive site-to-site guide](/guides/site-to-site-connectivity/) for ways to make your setup more production-ready, like creating Service Users to isolate agents and white-labeling ngrok with a custom connect URL.
* Read more about [Traffic Policy](/traffic-policy), [core concepts](/traffic-policy/concepts), and [actions](/traffic-policy/actions) you might want to implement next.
* View your site-to-site traffic in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector).


Built with [Mintlify](https://mintlify.com).