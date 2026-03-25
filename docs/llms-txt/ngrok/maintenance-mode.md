# Source: https://ngrok.com/docs/universal-gateway/examples/maintenance-mode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy a Consistent Maintenance Message with Traffic Policy

> Learn how to use Traffic Policy to immediately deploy a consistent maintenance message without needing to spin up a new backend service or change DNS records.

export const domain_0 = undefined

Whenever you're making infrastructure changes, a major upgrade to your services during planned downtime, or experiencing an incident, you still want to maintain a public-facing presence on your endpoints to tell customers what's going on.

With ngrok, you can use Traffic Policy and the [`custom-response`](/traffic-policy/actions/custom-response/) action to immediately deploy a consistent maintenance message without needing to spin up a new backend service or change DNS records to point to a third-party app.

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

## 4. Create a maintenance page on your Cloud Endpoint with Traffic Policy

While viewing your new Cloud Endpoint in the dashboard, copy the policy below and paste it into the Traffic Policy editor.

```yaml  theme={null}
on_http_request:
  - actions:
      - type: custom-response
        config:
          body: "We're currently undergoing maintenance. Please check back later!"
      - type: forward-internal
        config:
          url: https://service.internal
```

**What's happening here?** This policy "interrupts" every request by providing a custom response containing your maintenance message.

When your maintenance window is over and you're ready to route traffic to your upstream service, you can remove or comment out the `custom-response` action.

```yaml  theme={null}
on_http_request:
  - actions:
  #    - type: custom-response
  #      config:
  #        body: "We're currently undergoing maintenance. Please check back later!"
      - type: forward-internal
        config:
          url: https://service.internal
```

## 5. Try out your endpoint

Visit the domain you reserved either in the browser or in the terminal using a tool like `curl`.
You should see the app or service at the port connected to your internal Agent Endpoint.

## What's next?

* Learn more about using Traffic Policy to return custom responses by [trying out the examples](/traffic-policy/actions/custom-response/#examples).
* View your traffic in [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector).


Built with [Mintlify](https://mintlify.com).